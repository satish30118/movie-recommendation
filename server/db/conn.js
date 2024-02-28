const mongoose = require('mongoose');
const db = "mongodb://localhost:27017/modive"


const connect = async()=>{
    try {
       await mongoose.connect(db,{
            family:4,
        })
            console.log("Connection Success")

    } catch (error) {
        console.log(error);
    }
}

connect();