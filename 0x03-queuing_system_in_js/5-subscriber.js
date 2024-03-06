import { createClient } from 'redis';

const client = createClient();

// Handle connection errors
client.on('error', (err) => {
  console.error('Redis Client not connected to the server:', err);
});

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const channelName = 'holberton school channel';
client.subscribe(channelName, (err, count) => {
  if (err) {
    console.error('Error subscribing to channel:', err);
  } else {
    console.log(`Subscribed to channel: ${channelName} (count: ${count})`);
  }
});

client.on('message', (channel, message) => {
  if (channel === channelName) {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe(channelName);
      client.end(true);
    }
  }
});
