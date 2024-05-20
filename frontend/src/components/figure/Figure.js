import React from 'react'
import './Figure.css'

const calculateRadius = (startRad, figureRad) => {
  return (startRad + (75 * figureRad))
}

const calculateSector = (rad, sect, type) => {
  const sectValue = Math.PI/180 * (15 + (sect * 30));
  const angle = (type === 'sin') ? Math.sin(sectValue) : Math.cos(sectValue);
  const sector = Number((rad * angle).toFixed(2));
  return (type === 'sin') ? sector : -sector;
}

const calculatePosition = (params) => {
  const startRad = (params.radius) ? 37.5 : 0;
  const rad = calculateRadius(startRad, params.radius);
  const x = calculateSector(rad, params.sector, 'sin');
  const y = calculateSector(rad, params.sector, 'cos');
  return {
    x,
    y
  }
};

const figureTypes = {
  H: 'Х',
  G: 'С',
  F: 'Б',
  P: 'П'
}

const calculateStyle = (params) => {
  const figureParams = {
    type: params[0],
    player: params[1],
    radius: Number(params[2]),
    sector: Number(params.substring(3, 5))
  }
  const styleTrans = calculatePosition(figureParams);
  return {
    transform: `translateX(${styleTrans.x}px) translateY(${styleTrans.y}px)`,
    player: (figureParams.player === '1') ? 'first' : 'second'
  };
}
 
export default function Figure({item}) {

  return (
    <div
      className={`figure ${calculateStyle(item).player}`}
      style={{
        transform: `${calculateStyle(item).transform}`
      }}
    >
      {figureTypes[item[0]]}
    </div>
  )
}
