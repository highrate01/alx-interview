#!/usr/bin/node

const request = require('request');

// Get movie ID from the first argument
const movieId = process.argv[2];

// Define the API URL for the specified movie
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make the API request to get the movie data
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body to JSON
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Loop through each character URL to get the name
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
