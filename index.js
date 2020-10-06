const express = require('express')
const {spawn} = require('child_process');
const app = express();
let port = process.env.PORT || 5000;
app.get('/', (req, res) => {
    let dataToSend;
    // spawn new child process to call the python script
    const python = spawn('python', ['bot.py']);
    console.log(python);
    res.send("Bot activated");
})

app.listen(port, function() {
    console.log("Listening on " + port);
});

