const core = require('@actions/core');
const github = require('@actions/github');
const nodemailer = require('nodemailer')

async function run() {
  console.log('Inside custom email sender, host=', core.getInput('smtp-server') );

try {
  const transporter = nodemailer.createTransport({
    host: core.getInput('smtp-server') ,
    port: core.getInput('smtp-port'),
    secure: true, 
    auth: {
      user: "shekhar.siwan23@gmail.com",
      pass: "mngtbbgneduztjdq",
    },
  });

  const mailOptions = {
    from: core.getInput('from'),
    to: core.getInput('to'),
    subject: core.getInput('subject'),
    text: core.getInput('body')
  };

  await transporter.sendMail(mailOptions);
  console.log('Email send ho gaya');
} catch (error) {
  console.log('email nahi gaya', error);
  process.exit(1);
}
}
run();
