const express = require("express")
const bodyParser = require('body-parser');
const server = express()
const PORT = 9999

server.use(express.static('public'))
server.use(bodyParser.json());

let data= ""

server.get('/get-image', (req, res) => {
    res.status(200).json({image:data})
})

server.post('/post-image', function(req, res) {
    console.log(req.body);      // your JSON
    res.send(req.body);
    data = req.body.image  
});


//Mode of the Matrix
let modedata= ""

server.get('/mode/get', (req, res) => {
    res.status(200).json({mode:modedata})
})

server.post('/mode/post', function(req, res) {
    console.log(req.body);      // your JSON
    res.send(req.body);
    modedata = req.body.image  
});


server.listen(PORT, () => console.log(`Server has been started on port: ${PORT}`))