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

// Function to fetch character name from character URL
function fetchCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
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

  // Function to process characters sequentially
  async function processCharacters() {
    try {
      for (const characterUrl of characterUrls) {
        const characterName = await fetchCharacterName(characterUrl);
        console.log(characterName);
      }
    } catch (err) {
      console.error("Error fetching character data:", err);
    }
  }

  // Call the async function
  processCharacters();
});
