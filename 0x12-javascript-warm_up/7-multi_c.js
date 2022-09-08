#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);
if (!firstArg) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  while (i < firstArg) {
    console.log('C is fun');
    i++;
  }
}
