const mongoose = require("mongoose");
// const bcrypt = require("bcryptjs");


const userModel = new mongoose.Schema({
    name:{
        type:String,
        required:true,
        trim:true,
        minLength:3,
    },
    email:{
        type:String,
        required:true,
        trim:true,
        unique:true
    },

    proffession:{
        type:String,
    },

    password:{
        type:String,
        required:true,
    },

},{
    timestamps: true,
});

// Password Hashing
// userModel.pre("save", async function(){
//     const saltNumber = 10;
//     try {
//         if(this.isModified("password")){
//             this.password = await bcrypt.hash(this.password, saltNumber);
//         } 
//     } catch (error) {
//         console.log(error)
//     }

// });

const User = new mongoose.model("User",userModel);

module.exports = User;

