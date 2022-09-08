#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (num) {
  console.log('My number is: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
