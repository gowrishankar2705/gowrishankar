const express = require('express');
const cors = require('cors');
const nodemailer = require('nodemailer');
const rateLimit = require('express-rate-limit');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Rate limiting to prevent spam
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // limit each IP to 5 requests per windowMs
  message: 'Too many requests from this IP, please try again later.'
});

// Middleware
app.use(cors({
  origin: process.env.FRONTEND_URL || '*',
  credentials: true,
  methods: ['GET', 'POST']
}));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files (your HTML, CSS, JS)
app.use(express.static('.'));

// Health check endpoint (important for Render)
app.get('/health', (req, res) => {
  res.status(200).json({ 
    status: 'OK',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

// Root route
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Email transporter configuration
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS
  },
  tls: {
    rejectUnauthorized: false
  }
});

// Verify email configuration on startup
transporter.verify((error, success) => {
  if (error) {
    console.error('Email configuration error:', error);
  } else {
    console.log('✅ Email server is ready to send messages');
  }
});

// Email sending endpoint with rate limiting
app.post('/api/send-email', limiter, async (req, res) => {
  const { name, email, message, subject } = req.body;

  // Input validation
  if (!name || !email || !message) {
    return res.status(400).json({ 
      success: false, 
      error: 'Please provide name, email, and message' 
    });
  }

  // Basic email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    return res.status(400).json({ 
      success: false, 
      error: 'Please provide a valid email address' 
    });
  }

  // Mail options
  const mailOptions = {
    from: process.env.EMAIL_USER,
    to: process.env.EMAIL_USER, // Send to yourself
    subject: subject || `Portfolio Contact from ${name}`,
    html: `
      <!DOCTYPE html>
      <html>
      <head>
        <style>
          body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
          .container { max-width: 600px; margin: 0 auto; padding: 20px; }
          .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                   color: white; padding: 20px; border-radius: 5px 5px 0 0; }
          .content { background: #f9f9f9; padding: 20px; border-radius: 0 0 5px 5px; }
          .field { margin-bottom: 15px; }
          .label { font-weight: bold; color: #667eea; }
          .value { margin-top: 5px; padding: 10px; background: white; border-radius: 3px; }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="header">
            <h2>📧 New Portfolio Contact Message</h2>
          </div>
          <div class="content">
            <div class="field">
              <div class="label">👤 Name:</div>
              <div class="value">${name}</div>
            </div>
            <div class="field">
              <div class="label">📧 Email:</div>
              <div class="value">${email}</div>
            </div>
            <div class="field">
              <div class="label">💬 Message:</div>
              <div class="value">${message.replace(/\n/g, '<br>')}</div>
            </div>
            <div style="margin-top: 20px; padding-top: 20px; border-top: 1px solid #ddd; color: #666; font-size: 12px;">
              <p>Sent from your portfolio website</p>
              <p>Time: ${new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })}</p>
            </div>
          </div>
        </div>
      </body>
      </html>
    `,
    replyTo: email // Allows you to reply directly to the sender
  };

  try {
    // Send email
    await transporter.sendMail(mailOptions);
    
    console.log(`✅ Email sent successfully from ${email}`);
    
    res.status(200).json({ 
      success: true, 
      message: 'Email sent successfully! Thank you for reaching out.' 
    });
  } catch (error) {
    console.error('❌ Email sending error:', error);
    
    res.status(500).json({ 
      success: false, 
      error: 'Failed to send email. Please try again later or contact directly.',
      details: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
});

// Test endpoint (optional - remove in production)
app.get('/api/test', (req, res) => {
  res.json({
    message: 'Backend is working!',
    environment: process.env.NODE_ENV || 'development',
    emailConfigured: !!(process.env.EMAIL_USER && process.env.EMAIL_PASS)
  });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({ 
    error: 'Route not found',
    availableRoutes: [
      'GET /',
      'GET /health',
      'GET /api/test',
      'POST /api/send-email'
    ]
  });
});

// Error handler
app.use((err, req, res, next) => {
  console.error('Server error:', err);
  res.status(500).json({ 
    success: false,
    error: 'Internal server error' 
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Server is running on port ${PORT}`);
  console.log(`📧 Email service: ${process.env.EMAIL_USER ? 'Configured' : 'Not configured'}`);
  console.log(`🌍 Environment: ${process.env.NODE_ENV || 'development'}`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM signal received: closing HTTP server');
  server.close(() => {
    console.log('HTTP server closed');
  });
});
