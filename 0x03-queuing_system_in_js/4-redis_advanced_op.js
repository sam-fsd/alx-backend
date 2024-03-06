import { createClient, print } from 'redis';

const client = createClient();

// Handle connection errors
client.on('error', (err) => {
  console.error('Redis Client not connected to the server:', err);
});

// Handle successful connection
client.on('ready', () => {
  console.log('Redis client connected to the server');
});

client.hset('HolbertonSchools', 'Portland', '50', print);
client.hset('HolbertonSchools', 'Seattle', '80', print);
client.hset('HolbertonSchools', 'New York', '20', print);
client.hset('HolbertonSchools', 'Bogota', '20', print);
client.hset('HolbertonSchools', 'Cali', '40', print);
client.hset('HolbertonSchools', 'Paris', '2', print);

client.hgetall('HolbertonSchools', (err, result) => {
  if (err) throw err;
  console.log(result);
});
