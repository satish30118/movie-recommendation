const express = require('express');
const register = require('../Controller/register');
const login = require('../Controller/login');
const router = express.Router();


router.route("/register").post(register);
router.route("/login").post(login);

module.exports = router;


