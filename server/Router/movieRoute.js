const express = require('express');
const PyConnect = require('../PyConnect');
const router = express.Router();


router.route("/").post(PyConnect);


module.exports = router;