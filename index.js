const express = require('express')
let {PythonShell} = require('python-shell')
const app = express()
var port = process.env.PORT || 5000;
app.get('/', (req, res) => {
 
    PythonShell.run('bot.py');
    // spawn new child process to call the python script
    res.send("Bot activated");
})

app.listen(port, function() {
    console.log("Listening on " + port);
});

