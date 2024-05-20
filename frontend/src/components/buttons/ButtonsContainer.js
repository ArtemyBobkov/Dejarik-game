import React from 'react'
import './ButtonsContainer.css'
import Button from '../button/Button'
import { useDispatch, useSelector } from 'react-redux'
import { doBackwardMove, doForwardMove } from '../../store/gameStateSlice';

export default function ButtonsContainer() {
  const dispatch = useDispatch();
  const gameState = useSelector(state => state.gameState);

  const isForwardDisable = () => {
    return !gameState.game.length || (gameState.currentMove === gameState.game.length);
  }

  const isBackwardDisable = () => {
    return !gameState.game.length || !gameState.currentMove;
  }

  return (
    <div className='button-container'>
      <Button clickHandler={() => dispatch(doBackwardMove())} isDisable={isBackwardDisable()} text='←'/>
      <Button clickHandler={() => dispatch(doForwardMove())} isDisable={isForwardDisable()} text='→'/>
    </div>
  )
}
