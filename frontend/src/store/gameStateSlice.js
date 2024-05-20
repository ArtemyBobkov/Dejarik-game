import { createSlice } from '@reduxjs/toolkit';
import gameData from '../source/gameData.json';

const initialState = {
  start: ["H1200", "G1201", "F1202", "P1204", "H2211", "G2210", "F2209", "P2207"],
  game: gameData,
  currentState: ["H1200", "G1201", "F1202", "P1204", "H2211", "G2210", "F2209", "P2207"],
  currentMove: 0,
  firstPlayer: true
}

const increaseMove = (obj) => {
  obj.currentMove = obj.currentMove + 1;
  obj.currentState = obj.game[obj.currentMove - 1];
}

const decreaseMove = (obj) => {
  obj.currentMove = obj.currentMove - 1;
  if (obj.currentMove) {
    obj.currentState = obj.game[obj.currentMove - 1];
  } else {
    obj.currentState = obj.start;
  }
}

const gameStateSlice = createSlice({
  name: 'gameState',
  initialState,
  reducers: {
    doForwardMove (state) {
      increaseMove(state);
      if (state.currentState.includes('$$$')) {
        state.firstPlayer = !state.firstPlayer;
        increaseMove(state)
      }
      state.currentState = state.currentState.filter(item => !item.includes('-'))
    },
    doBackwardMove (state) {
      decreaseMove(state);
      if (state.currentState.includes('$$$')) {
        state.firstPlayer = !state.firstPlayer;
        decreaseMove(state)
      }
      state.currentState = state.currentState.filter(item => !item.includes('-'))
    }
  }
})

export const {doForwardMove, doBackwardMove} = gameStateSlice.actions;
export default gameStateSlice.reducer;