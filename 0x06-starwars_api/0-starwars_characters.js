#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Check if the movie ID was passed as an argument
if (!movieId) {
  console.log('Please provide a Movie ID.');
  process.exit(1);
}

// Define the base URL for the Star Wars API
const baseUrl = 'https://swapi.dev/api/films/';

// Function to fetch character name
function fetchCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body.name);
      }
    });
  });
}

// Function to fetch and print characters from the movie
function fetchMovieCharacters (movieId) {
  const movieUrl = `${baseUrl}${movieId}/`;

  request(movieUrl, { json: true }, (err, res, body) => {
    if (err) {
      console.error('Error fetching the movie:', err);
      return;
    }
    if (res.statusCode !== 200) {
      console.log('Movie not found or invalid Movie ID.');
      return;
    }

    // Extract the list of character URLs
    const characterUrls = body.characters;

    // Use Promise.all to fetch all characters in parallel
    Promise.all(characterUrls.map(fetchCharacterName))
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(err => {
        console.error('Error fetching characters:', err);
      });
  });
}

// Call the function to fetch movie characters
fetchMovieCharacters(movieId);
