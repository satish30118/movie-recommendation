
// const generateAuthToken = require("../db/generateToken");
const User = require("../model/userModel");

const register = async(req, res) => {
  try {
    const {name, email,  password} = req.body;

    if(!name || !email|| !password){
        console.log("Empty Filled")
       return res.status(422).json({message:"Empty Filled"}); 
    }

    //Checking user existance;
    const userExist = await User.findOne({email});

    if(userExist){
        console.log("user Exist")
       return res.status(422).send({message:"User Exist"}); 
    }

    // New User creation
      const newUser = await User({name, email, password});
      await newUser.save();
    
      if(newUser){
        console.log("User registration Sucess")
        return res.status(200).json({
            message:"User registration Sucess",
            userId : newUser._id,
            name : newUser.name,
            email : newUser.email,
            number : newUser.proffession,        
            // token : generateAuthToken(newUser._id)
        })
      }
  } catch (error) {
    console.log(error)
    res.status(400).send({message:"GET A ERROR", error:error})
  }

}

module.exports = register;