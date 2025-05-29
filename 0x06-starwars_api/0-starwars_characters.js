#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const mainUrl = 'https://swapi-api.alx-tools.com/api/films/';

const requestUrl = mainUrl + movieId;

async function getCharacterName () {
  try {
    const filmResp = await getRequest(requestUrl);
    const characters = filmResp.characters;
    // loop through each character URL
    for (const characterurl of characters) {
      const character = await getRequest(characterurl);
      // extract the character's name from the character data
      const characterName = character.name;
      console.log(characterName);
    }
  } catch (error) {
    console.log(error);
  }
}

// performs get request and returns a promise
// so we can work asynchronously
function getRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      // If the request is successful, parse the response body as JSON
      // and resolve the promise with the data
      const resp = JSON.parse(body);
      resolve(resp);
    });
  });
}

getCharacterName();
