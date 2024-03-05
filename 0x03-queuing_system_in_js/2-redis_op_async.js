import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

// Handle connection errors
client.on('error', (err) => {
  console.error('Redis Client not connected to the server:', err);
});

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, print);
}
const get = promisify(client.get).bind(client);

async function displaySchoolValue (schoolName) {
  const result = await get(schoolName).catch((error) => {
    if (error) {
      console.log(error);
      throw error;
    }
  });
  console.log(result);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
