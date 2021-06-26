var express = require('express');
var nodemailer = require('nodemailer');
var router = express.Router();

router.post('/', (req, res) => {
    const { username, password } = req.body;
    const mailData = {
        from: `${process.env.EMAIL_ADDRESS}`,
        to: `${process.env.EMAIL_ADDRESS}`,
        subject: "New Contact Form Submission on Kartavyas.com",
        html: '<h1>Hey this is my first message</h1>'
    };

    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: `${process.env.EMAIL_ADDRESS}`,
            pass: `${process.env.EMAIL_PASS}`
        },
        secure: true,
    });

    transporter.sendMail(mailData, (error, info) => {
        if(error) {
            console.log(error);
            res.status(400).send({ success: false });
        }
        res.status(200).send({ success: true });
    })
});

module.exports = router;