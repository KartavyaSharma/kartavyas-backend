var express = require('express');
var router = express.Router();
var mailing = require('../mailing/mailing')

router.post('/', (req, res) => {
    try {
        mailing.sendEmail(req.body);
        res.status(200).json({ message: 'email sent successfully' });
    } catch(error) {
        console.log(error);
        res.status(400).json({ message: 'failed' });
    }
});

module.exports = router;