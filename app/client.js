const io = require('socket.io-client');

// Connect to the server
const socket = io('http://localhost:3000');

// Prompt the user to enter their name
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question('Enter your name: ', (name) => {
  console.log(`Welcome, ${name}! You are now connected to the chat server.`);

  // Listen for chat messages from the server
  socket.on('chatMessage', (data) => {
    console.log(`${data.id}: ${data.message}`);
  });

  // Listen for the updated client count from the server
  socket.on('clientCount', (count) => {
    console.log(`Total clients connected: ${count}`);
  });

  // Listen for user input and send chat messages to the server
  rl.on('line', (message) => {
    socket.emit('chatMessage', message);
  });
});

