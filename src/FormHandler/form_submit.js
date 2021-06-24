var express = require('express');
var router = express.Router();
const axios = require('axios')

async function sendMail(requestBody) {
    try {
        return await axios.post('/send-email', {
            formData: requestBody
        })
    } catch (error) {
        return error;
    }
}

router.post('/', (req, res) => {
    try {
        sendMail(req.body);
    } catch (error) {
        res.status(400);
    }
    res.status(201);
});

module.exports = router;