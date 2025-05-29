#!/usr/bin/node

const request = require("request");

// Get movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error("Usage: ./0-starwars_characters.js <movie_id>");
  process.exit(1);
}

// API endpoint for the specific film
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to print characters recursively to maintain order
function printCharacters(characterUrls, index) {
  if (index >= characterUrls.length) {
    return;
  }

  request(characterUrls[index], (error, response, body) => {
    if (error) {
      console.error("Error fetching character data:", error);
      return;
    }

    const character = JSON.parse(body);
    console.log(character.name);

    // Recursively call for the next character
    printCharacters(characterUrls, index + 1);
  });
}

// Main function to fetch film data and characters
request(filmUrl, (error, response, body) => {
  if (error) {
    console.error("Error fetching film data:", error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error("Film not found");
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  // Start printing characters from index 0
  printCharacters(characterUrls, 0);
});
