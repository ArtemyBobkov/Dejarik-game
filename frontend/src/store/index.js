import { configureStore } from '@reduxjs/toolkit';
import gameStateReducer from './gameStateSlice';

export default configureStore({
  reducer: {
    gameState: gameStateReducer,
  }
});