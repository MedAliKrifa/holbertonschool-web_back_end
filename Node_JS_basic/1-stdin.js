const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function displayMessage(message) {
  console.log(message);
}

function closeProgram() {
  displayMessage("This important software is now closing");
  rl.close();
}

function getName() {
  displayMessage("Welcome to Holberton School, what is your name?");
  rl.on('line', (input) => {
    if (input.trim().toLowerCase() === 'exit') {
      closeProgram();
    } else {
      displayMessage(`Your name is: ${input}`);
    }
  });
}

getName();
