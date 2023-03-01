
import './App.css';
import {useEffect, useState} from 'react';
import PokemonCard from './components/pokemoncard';

export function App() {
  const [AllPokemons, setAllPokemons] = useState([]);

  const [loadmore, setLoadmore] = useState('https://pokeapi.co/api/v2/pokemon?limit=50');
  const getPokemons = async () => {
    const response = await fetch(loadmore);
    const data = await response.json();
    setLoadmore(data.next);
    function createPokemonObject () {
      data.results.forEach(async pokemon => {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon.name}`);
        const data = await response.json();
        setAllPokemons(currentlist => [...currentlist, data])
        AllPokemons.push(data);
      });
    }
    createPokemonObject(data.result);
  };
  useEffect(() => {
    getPokemons();
  }, []);

  return (
    <div className="App">
      <h1> Liste des Pokemons </h1>
      <div className="pokemons">
        {AllPokemons.map(pokemon => (
          <PokemonCard key={pokemon.id} id={pokemon.id} name={pokemon.name} type={pokemon.type} image={pokemon.image}/>
        ))}
      </div>
      <button className='loadmore'>Load More</button>
    </div>
  );
}