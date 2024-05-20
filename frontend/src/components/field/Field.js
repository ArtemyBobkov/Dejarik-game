import React from 'react'
import './Field.css';
import Figure from '../figure/Figure';
import { useSelector } from 'react-redux';

export default function Field() {
  const currentState = useSelector(state => state.gameState.currentState);

  return (
    <div className='field'>
      <div className='sector outer-radius'>
        <div className='sector inner-radius'>
          <div className='sector dejarik'>
          {
            currentState.map((item, index) => (
              <Figure key={index} item={item}/>
            ))
          }
          </div>
        </div>
      </div>
    </div>
  )
}
