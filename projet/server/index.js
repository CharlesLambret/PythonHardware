const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
let id = 0
app.use(express.json());

app.use(cors());
// Route pour récupérer les données des Pokémons
app.get('/pokemons', async (req, res) => {
  const limit = req.query.limit || 50;
  const url = `https://pokeapi.co/api/v2/pokemon?limit=${limit}`;

  try {
    const { data } = await axios.get(url);
    const results = data.results;

    const pokemonData = await Promise.all(results.map(async (result) => {
      const pokemonUrl = result.url;
      const { data } = await axios.get(pokemonUrl);
      return data;
    }));

    res.status(200).send(pokemonData);
  } catch (error) {
    console.log(error);
    res.status(500).send('Server Error');
  }
});

app.listen(8000, () => {
  console.log('Server is running on port 8000');
});

app.get('/id',(req,res)=>{
  res.send({"id":id})
})

app.post('/pokemon', (req, res) => {
    const pokemon_id = req.body.pokemon_id;
    id = pokemon_id
    console.log(pokemon_id)
    res.send('OK');
});
