import React from 'react'
import './Header.css'
import { useSelector } from 'react-redux'

export default function Header() {
  const gameState = useSelector(state => state.gameState);

  const generateHeaderText = (obj) => {
    if (!obj.currentMove) {
      return 'Начало игры'
    };
    if (obj.firstPlayer) {
      return 'Ход первого игрока'
    };
    return 'Ход второго игрока'
  }

  return (
    <div className='header'>{generateHeaderText(gameState)}</div>
  )
}
