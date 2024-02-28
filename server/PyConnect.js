


const PyConnect = async(req, res) => {
    const {spawn} = require('child_process');


    try {
        
   
// const childPython = spawn("python", ["--version"]);
// const childPython = spawn('python', ["phython.py"]);

const childPython = spawn('python', ["main.py", "searchText", "Movie"]);



var sendData={};
childPython.stdout.on('data', (data) =>{
    console.log(`stdout:  ${data}`)
    sendData = data.toString();
  
});

childPython.stderr.on("data", (data) =>{
    console.log(`stderr: ${data}`);
})

childPython.on("close", (code) =>{
    console.log(`child process exited with code: ${code}`);
    res.status(200).json({data: sendData})
})

} catch (error) {
        console.log(error)
}

}

module.exports = PyConnect;