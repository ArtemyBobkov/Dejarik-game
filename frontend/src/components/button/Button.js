import React from 'react'
import './Button.css'

export default function Button({text, clickHandler, isDisable}) {
  return (
    <button className='button' onClick={clickHandler} disabled={isDisable}>{text}</button>
  )
}
