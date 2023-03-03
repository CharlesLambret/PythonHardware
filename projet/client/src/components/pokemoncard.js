import React from "react";

export default function PokemonCard(id, name, image, types) {
  
    return( 
        <div className="pokemon">
            <div className="img-container">
              <img src={image} alt={name} />
            </div>
            <div className="info">
              <span className="number">#{id.toString().padStart(3, '0')}</span>
              <h3 className="name">{name}</h3>
              {types.map(type => (
                <span className="type">{type.name}</span>
              ))}
            </div>
          </div>
    )
}