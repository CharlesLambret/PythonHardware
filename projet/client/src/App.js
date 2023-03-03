import './App.css';
import {useContext, useEffect, useState} from 'react';
import PokemonCard from './components/pokemoncard';

export function App() {
const [AllPokemons, setAllPokemons] = useState([]);

const [loadmore, setLoadmore] = useState('http://localhost:8000/pokemons');
const [selectedPokemon, setSelectedPokemon] = useState(null);

const getPokemons = async () => {
  const response = await fetch(loadmore);
  const data = await response.json();
  setLoadmore(`http://localhost:8000/pokemons?limit=${data.length}`);

  setAllPokemons(currentlist => {
    const newData = data.filter(p => currentlist.filter(c => c.id === p.id).length === 0);
    return [...currentlist, ...newData];
  });
};

useEffect(() => {
  getPokemons();
}, []);

useEffect(() => {
  if (selectedPokemon !== null) {
    window.history.pushState(null, '', `/${selectedPokemon.name}`);
  }
}, [selectedPokemon]);


  return (
    <div className="App">
      <h1> Liste des Pokemons </h1>
      <div className="pokemons">
        {AllPokemons
          .sort((a, b) => a.id - b.id)
          .map(pokemonStats => (
            <div className="pokemon" key={pokemonStats.id}>
              <div className="img-container">
                <img src={pokemonStats.sprites.front_default} alt={pokemonStats.name} />
              </div>
              <div className="info">
                <span className="number">#{pokemonStats.id}</span>
                <h3 className="name">{pokemonStats.name}</h3>
                {pokemonStats.types.map(type => (
                  <span className="type">{type.name}</span>
                ))}
                <button className="btn" onClick={() => {
                      setSelectedPokemon(pokemonStats);
                      fetch('http://localhost:8000/pokemon', {
                          method: 'POST',
                          headers: {
                              'Content-Type': 'application/json'
                          },
                          body: JSON.stringify({pokemon_id: pokemonStats.id})
                      })
                  }}>
                      Sélectionner le Pokémon
                </button>

              </div>
            </div>
          ))}
      </div>
      <button className='loadmore' onClick={loadmore}>Load More</button>
    </div>
  );
}
