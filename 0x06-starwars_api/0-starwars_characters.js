#!/usr/bin/node
const argv = process.argv;
const request = require('request');
function Movies(){
    request('https://swapi-api.alx-tools.com/api/films/' + argv[2], function (error, response, body) {
    const ch = JSON.parse(body).characters;
    fetchdata(ch);
    if (error) {
        console.error(error);
    }
    });
}
async function fetchdata(ch){
    for (const url in ch){
        try {
            const data = await makeRequest(url);
            console.log(data); // Do something with the data
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
}
function makeRequest(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else {
                const name = JSON.parse(body).name;
                console.log(name);
                if (error) {
                    console.error(error);
                }
            }
        });
    });
}

Movies()