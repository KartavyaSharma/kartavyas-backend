var express = require('express');
var router = express.Router();
const nodemailer = require('nodemailer');

router.post('/', (req, res) => {
    const { firstName, lastName, email, message } = req.body;
    const mailData = {
        from: "mail.kartavyas@gmail.com",
        to: "mail.kartavyas@gmail.com",
        subject: "New Contact Form Submission on Kartavyas.com",
        html: '<h1>Hey this is my first message</h1>'
    };

    const transporter = nodemailer.createTransport({
        port: 465,
        host: 'smtp.gmail.com',
        auth: {
            user: process.env.EMAIL,
            pass: process.env.PASSWORD
        }
    })

});