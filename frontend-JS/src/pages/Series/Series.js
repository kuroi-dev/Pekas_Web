import './Series.css';
import React from 'react';
import { useNavigate } from 'react-router-dom';

function Series() {
  const navigate = useNavigate();

  const handleBackHome = () => {
    navigate('/');
  };

  return (
    <div className="App-nefli">
      <header className="App-header-nefli">
        <h1>Nefli</h1>
        <button onClick={handleBackHome} className="back-button"><b className='flecha'>▶</b>Volver</button>
      </header>
      <main>
        <h2>Catálogo de Series</h2>
        <p>Aquí aparecerán todos los animes disponibles...</p>
        {/* Aquí irán tus componentes de anime más adelante */}
      </main>
      <footer className="App-footer-nefli">
        <p>&copy; 2026 CineLocal. Derechos reservados para 666.</p>
      </footer>
    </div>
  );
}

export default Series;