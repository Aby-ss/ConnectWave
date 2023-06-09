const express = require('express');
const http = require('http');
const socketIO = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIO(server);

// Store connected clients
const clients = [];

// Socket.io event handlers
io.on('connection', (socket) => {
  // Add client to the list
  clients.push(socket.id);
  console.log(`New client connected. Total clients: ${clients.length}`);

  // Emit the updated client count to all clients
  io.emit('clientCount', clients.length);

  // Listen for chat messages
  socket.on('chatMessage', (message) => {
    console.log(`Received message from ${socket.id}: ${message}`);
    // Broadcast the message to all clients
    io.emit('chatMessage', { id: socket.id, message });
  });

  // Handle client disconnection
  socket.on('disconnect', () => {
    // Remove the client from the list
    const index = clients.indexOf(socket.id);
    if (index !== -1) {
      clients.splice(index, 1);
    }
    console.log(`Client disconnected. Total clients: ${clients.length}`);
    // Emit the updated client count to all clients
    io.emit('clientCount', clients.length);
  });
});

// Start the server
const port = 3000;
server.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
