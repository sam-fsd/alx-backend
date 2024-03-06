import { createQueue } from 'kue';

const queue = createQueue();

const notification = {
  phoneNumber: '235252341',
  message: 'This is the code to verify your account'
};

const job = queue.create('push_notification_code', notification).save(err => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', result => {
  console.log('Notification job completed');
}).on('failed', function (errorMessage) {
  console.log('Notification job failed');
});
