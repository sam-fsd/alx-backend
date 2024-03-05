import { createClient } from 'redis';

const client = createClient();

// Handle connection errors
client.on('error', (err) => {
  console.error('Redis Client not connected to the server:', err);
});

// Handle successful connection
client.on('ready', () => {
  console.log('Redis client connected to the server');
});
