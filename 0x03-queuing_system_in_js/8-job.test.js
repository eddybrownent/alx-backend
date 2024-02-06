import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';
import sinon from 'sinon';
import { expect } from 'chai';


describe('createPushNotificationsJobs', () => {
  const queue = createQueue();

  beforeEach(() => {
    // Create a sandbox for stubs
    queue.testMode.enter(true);

  });

  afterEach(() => {
    // Restore the sandbox and clear the queue
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'This is the code 3564 to verify your account' },
      { phoneNumber: '9876543210', message: 'This is the code 1894 to verify your account' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(jobs.length);
  });

  it('should log job creation', () => {
    const consoleLogSpy = sinon.spy(console, 'log');
    const jobs = [
      { phoneNumber: '1234567890', message: 'This is the code 3564 to verify your account' },
      { phoneNumber: '9876543210', message: 'This is the code 1894 to verify your account' }
    ];

    createPushNotificationsJobs(jobs, queue);
    
    jobs.forEach((job, id) => {
      console.log(`Notification job created: ${id + 1}`);
      expect(consoleLogSpy.calledWith(`Notification job created: ${id + 1}`)).to.be.true;
    });
    consoleLogSpy.restore();
  });
});
