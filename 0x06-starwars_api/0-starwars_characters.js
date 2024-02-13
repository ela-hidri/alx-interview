#!/usr/bin/node

const argv = process.argv;
const request = require('request');

async function Movies() {
    try {
        const body = await fetchData('https://swapi-api.alx-tools.com/api/films/' + argv[2]);
        const characters = JSON.parse(body).characters;
        await fetchCharacters(characters);
    } catch (error) {
        console.error('Error fetching movies:', error);
    }
}

async function fetchCharacters(characters) {
    try {
        for (const url of characters) {
            const name = await makeRequest(url);
            console.log(name);
        }
    } catch (error) {
        console.error('Error fetching characters:', error);
    }
}

function makeRequest(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else {
                const name = JSON.parse(body).name;
                resolve(name);
            }
        });
    });
}

async function fetchData(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else {
                resolve(body);
            }
        });
    });
}

Movies();
