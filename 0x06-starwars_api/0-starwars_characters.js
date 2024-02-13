#!/usr/bin/node
const argv = process.argv;
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + argv[2], function (error, response, body) {
  const ch = JSON.parse(body).characters;
  ch.forEach(c => {
    request(c, function (error, response, body) {
      const name = JSON.parse(body).name;
      console.log(name);
      if (error) {
        console.error(error);
      }
    });
  });
  if (error) {
    console.error(error);
  }
});