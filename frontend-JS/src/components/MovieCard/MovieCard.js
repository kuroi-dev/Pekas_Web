import './MovieCard.css';
import React from 'react';

function MovieCard({ title, image, onClick }) {
console.log(title, image , onClick);
  return (
    <div className="movie-card" onClick={onClick}>
      <div className="movie-card-image">
        <img src={image} alt={title} />
        <div className="movie-card-overlay">
          <button className="play-button">▶</button>
        </div>
      </div>
      <div className="movie-card-content">
        <h3 className="movie-title">{title}</h3>
        <div className="movie-info">
          <span className="movie-year">2000</span>
          <span className="movie-genre">Test</span>
        </div>
        <p className="movie-description">lorem ipsum dolor sit amet orem ipsum dolor sit amet orem ipsum dolor sit amet</p>
      </div>
    </div>
  );
}

export default MovieCard;