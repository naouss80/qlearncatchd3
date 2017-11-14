const net = require('net');
const express = require('express');
const app = express();
const server2 = app.listen(80);
const io = require('socket.io').listen(server2);
var path = require('path');
var os = require('os');
__dirname = process.cwd();

// linux and windows support
if (os.type().indexOf("Windows")>=0) {public_folder = '\\public\\';}
else {public_folder = '/public/';} // asuming we are unix based 

var debug = process.argv[2];

app.use(express.static(path.join(__dirname, 'public')));

const server = net.createServer((c) => {
  // 'connection' listener
  console.log('client connected');
  c.on('end', () => {
    debugr('client disconnected', debug);
  });
  c.on('data', (data) => {
    debugr(data.toString(), debug);
    // send to nodejs here
	io.emit('position', data.toString());
  }); 
});

server.on('error', (err) => {
  throw err;
});

server.listen(2814, () => {
  debugr('server bound', debug);
});

app.get('/', function (req, res) {
  res.sendFile( __dirname + public_folder + 'index.html');
});

function debugr(x, debug){
	if (debug) {console.log(x);}
}
