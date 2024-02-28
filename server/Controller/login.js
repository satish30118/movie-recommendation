
// const generateAuthToken = require("../db/generateToken");
// const bcrypt = require('bcryptjs');
const User = require("../model/userModel");

const login = async(req, res) => {

 const {email, password} = req.body;
 console.log("hello ji mai aa gya")

try{

 if(!email || !password){
    console.log("Empty field");
    return res.status(422).json({message:"Empty field"})
 }

 let findUser = await User.findOne({email});

 if(findUser){
    // const passwordMatch = await bcrypt.compare(password,findUser.password);

    // if(!passwordMatch){
    //     console.log("Invalid Credential");
    // return res.status(422).json({message:"Invalid Credential"})
    // }

    console.log("User Login Sucess!!");
    return res.status(200).json({
            message:"User Login Success!!",
            userId : findUser._id,
            name : findUser.name,
            email : findUser.email,
            number : findUser.proffession,
            // token : generateAuthToken(findUser._id),
    })
 }else{
    console.log("User have not registered");
    return res.status(420).json({message:"User have not registered"})
 }
}catch(err){
    console.log(err);
    return res.status(400).json(err)
}
}
module.exports = login;