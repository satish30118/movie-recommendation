const express = require("express");
const db = require("./db/conn")
const authRoute = require('./Router/authRoute');
const movieRoute = require('./Router/movieRoute');
const app = express();

app.use(express.json())

const PORT = 8000;

app.get("/",(req, res)=>{
    res.send("Hello")
})
app.use("/api/auth", authRoute);
app.use("/api/movie", movieRoute)

app.listen(PORT, ()=>{
    console.log(`Port is listening ${PORT}`)
})