import React from "react";

export default function PokemonCard(id, name, image, type) {
    return( 
        <div className="pokemon">
            <div className="img-container">
              <img src={image} alt={name} />
            </div>
            <div className="info">
              <span className="number">#{id.toString().padStart(3, '0')}</span>
              <h3 className="name">{name}</h3>
              <small className="type">Type: <span>{type.map(type => type.type.name).join(', ')}</span></small>
            </div>
          </div>
    )
}