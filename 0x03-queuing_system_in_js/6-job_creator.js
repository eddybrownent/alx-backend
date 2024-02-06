import { createQueue } from 'kue';

const queue = createQueue();

const jobData = {
  phoneNumber: '0712345678',
  message: 'This is the code to verify your account',
};

const notificationJob = queue.create('push_notification_code', jobData);

notificationJob
  .on('enqueue', () => {
    console.log('Notification job created:', notificationJob.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });

notificationJob.save();
