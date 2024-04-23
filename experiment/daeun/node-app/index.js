const http = require('http');

const hostname = '192.168.1.74';
const port = 8000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
});

server.listen(port, hostname, () => {
  console.log(`Node App running at http://${hostname}:${port}/`);
});
