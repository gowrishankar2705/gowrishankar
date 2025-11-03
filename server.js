const express = require('express');
const nodemailer = require('nodemailer');
const cors = require('cors');
const rateLimit = require('express-rate-limit');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 10000;

// Middleware
app.use(cors());
app.use(express.json());

// Rate limiting to prevent spam
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 5, // Limit each IP to 5 requests per windowMs
    message: 'Too many requests from this IP, please try again later.'
});

app.use('/api/contact', limiter);

// Create nodemailer transporter
const transporter = nodemailer.createTransport({
    service: 'gmail', // You can use other services like 'outlook', 'yahoo', etc.
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS // Use App Password for Gmail
    }
});

// Verify transporter configuration
transporter.verify((error, success) => {
    if (error) {
        console.error('Email transporter error:', error);
    } else {
        console.log('Email server is ready to send messages');
    }
});

// Contact form endpoint
app.post('/api/contact', async (req, res) => {
    const { name, email, message } = req.body;

    // Validation
    if (!name || !email || !message) {
        return res.status(400).json({ 
            error: 'Please provide all required fields: name, email, and message' 
        });
    }

    // Email validation regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        return res.status(400).json({ 
            error: 'Please provide a valid email address' 
        });
    }

    // Email options - Email sent to you
    const mailOptions = {
        from: process.env.EMAIL_USER,
        to: process.env.RECIPIENT_EMAIL, // Your email where you want to receive messages
        subject: `Portfolio Contact: Message from ${name}`,
        html: `
            <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f9f9f9; border-radius: 10px;">
                <h2 style="color: #00ffff; border-bottom: 3px solid #00ffff; padding-bottom: 10px;">New Portfolio Contact Message</h2>
                
                <div style="background-color: white; padding: 20px; border-radius: 8px; margin: 20px 0;">
                    <p style="margin: 10px 0;"><strong style="color: #333;">From:</strong> ${name}</p>
                    <p style="margin: 10px 0;"><strong style="color: #333;">Email:</strong> <a href="mailto:${email}" style="color: #00ffff;">${email}</a></p>
                    
                    <div style="margin-top: 20px; padding: 15px; background-color: #f0f0f0; border-left: 4px solid #00ffff; border-radius: 4px;">
                        <p style="margin: 0; color: #333; line-height: 1.6;"><strong>Message:</strong></p>
                        <p style="margin: 10px 0; color: #555; line-height: 1.6;">${message}</p>
                    </div>
                </div>
                
                <div style="margin-top: 20px; padding: 15px; background-color: #e8f9ff; border-radius: 8px;">
                    <p style="margin: 0; color: #666; font-size: 14px;">
                        <strong>Quick Reply:</strong> Simply reply to this email to respond directly to ${name}.
                    </p>
                </div>
                
                <p style="margin-top: 20px; color: #999; font-size: 12px; text-align: center;">
                    This message was sent from your portfolio website contact form.
                </p>
            </div>
        `,
        replyTo: email // This allows you to reply directly to the sender
    };

    // Auto-reply to sender (optional but professional)
    const autoReplyOptions = {
        from: process.env.EMAIL_USER,
        to: email,
        subject: 'Thank you for contacting me!',
        html: `
            <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; background-color: #0a0a0a; color: #ffffff; border-radius: 10px;">
                <h2 style="color: #00ffff; border-bottom: 3px solid #00ffff; padding-bottom: 10px;">Thank You for Reaching Out!</h2>
                
                <div style="background-color: #111111; padding: 20px; border-radius: 8px; margin: 20px 0; border: 1px solid rgba(0, 255, 255, 0.2);">
                    <p style="margin: 10px 0; line-height: 1.8;">Hi <strong style="color: #00ffff;">${name}</strong>,</p>
                    
                    <p style="margin: 15px 0; line-height: 1.8;">
                        Thank you for your message! I've received your inquiry and will get back to you as soon as possible.
                    </p>
                    
                    <p style="margin: 15px 0; line-height: 1.8;">
                        In the meantime, feel free to check out my latest projects on 
                        <a href="https://github.com/yourusername" style="color: #00ffff; text-decoration: none;">GitHub</a> 
                        or connect with me on 
                        <a href="https://linkedin.com/in/yourprofile" style="color: #00ffff; text-decoration: none;">LinkedIn</a>.
                    </p>
                    
                    <div style="margin-top: 25px; padding: 15px; background-color: rgba(0, 255, 255, 0.05); border-left: 4px solid #00ffff; border-radius: 4px;">
                        <p style="margin: 0; color: #888; font-size: 14px;"><strong>Your Message:</strong></p>
                        <p style="margin: 10px 0; color: #ccc; line-height: 1.6;">${message}</p>
                    </div>
                </div>
                
                <p style="margin-top: 20px; color: #888; font-size: 14px;">
                    Best regards,<br/>
                    <strong style="color: #00ffff;">Gowrishankar</strong><br/>
                    AI & Data Science Engineer
                </p>
                
                <p style="margin-top: 30px; color: #666; font-size: 12px; text-align: center; border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 15px;">
                    This is an automated response to confirm receipt of your message.
                </p>
            </div>
        `
    };

    try {
        // Send email to you
        await transporter.sendMail(mailOptions);
        
        // Send auto-reply to sender
        await transporter.sendMail(autoReplyOptions);
        
        console.log(`Message received from ${name} (${email})`);
        
        res.status(200).json({ 
            success: true, 
            message: 'Message sent successfully!' 
        });
    } catch (error) {
        console.error('Error sending email:', error);
        res.status(500).json({ 
            error: 'Failed to send message. Please try again later.',
            details: error.message 
        });
    }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
    res.status(200).json({ status: 'Server is running', timestamp: new Date() });
});

// Start server
app.listen(PORT, () => {
    console.log(`✅ Server running on http://localhost:${PORT}`);
    console.log(`📧 Email service: ${process.env.EMAIL_USER ? 'Configured' : 'NOT configured - check .env file'}`);
});



// Serve static files
app.use(express.static('public'));

// Root route serves your HTML
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(process.env.PORT || 3000, '0.0.0.0');

const server = app.listen(PORT, '0.0.0.0', () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM received, closing server...');
  server.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});

process.on('SIGINT', () => {
  console.log('SIGINT received, closing server...');
  server.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});
