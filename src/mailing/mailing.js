var nodemailer = require('nodemailer');
var ejs = require('ejs');

const { google } = require('googleapis');
const { OAuth2 } = google.auth;

const OAUTH_PLAYGROUND='https://developers.google.com/oauthplayground';

const {
    EMAIL_ADDRESS,
    CLIENT_ID,
    CLIENT_SECRET,
    REFRESH_TOKEN
} = process.env;

const mailing = {};

const oauth2Client = new OAuth2(
    CLIENT_ID,
    CLIENT_SECRET,
    OAUTH_PLAYGROUND
);

const TEMPLATES = {
    new_contact: {
        fileName: 'form.ejs',
        subject: 'New form submisssion from kartavyas.com',
    },
};

mailing.sendEmail = data => {
    oauth2Client.setCredentials({
        refresh_token: REFRESH_TOKEN,
    });

    const accessToken = oauth2Client.getAccessToken();

    const smtpTransport = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            type: 'OAuth2',
            user: EMAIL_ADDRESS,
            clientId: CLIENT_ID,
            clientSecret: CLIENT_SECRET,
            refreshToken: REFRESH_TOKEN,
            accessToken,
        },
    });

    const filePath = `${__dirname}/templates/${TEMPLATES.new_contact.fileName}`;

    ejs.renderFile(filePath, data, {}, (err, content) => {
        if(err) return err;
        
        const mailOptions = {
            from: EMAIL_ADDRESS,
            to: EMAIL_ADDRESS,
            subject: TEMPLATES.new_contact.subject,
            html: content,
        }

        smtpTransport.sendMail(mailOptions, (error, info) => {
            if(error) return error;
            return info;
        });
    });
};

module.exports = mailing;