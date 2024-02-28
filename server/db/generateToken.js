const jwt = require('jsonwebtoken');

const key = process.env.SCRECT_KEY;
const generateAuthToken = (id) =>{
    return jwt.sign({id},key,{
        expiresIn:"30d"
    })

}

module.exports = generateAuthToken;