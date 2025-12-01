import './CategoryCard.css';
import React from 'react';

function CategoryCard({ title, onClick }) {
  return (
    <div className="category-card" onClick={onClick}>
      <h2 className="category-title">{title}</h2>
    </div>
  );
}

export default CategoryCard;

