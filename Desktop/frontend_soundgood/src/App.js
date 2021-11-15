import Home from './Pages/Home';
import Profile from './Pages/Profile';
import Forum from './Pages/Forum';
import SavedSongs from './Pages/SavedSongs';
import Login from './Components/Login.js';
import Register from './Components/Register.js';
import './App.css';
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className='App'>
      {true ? (
        <div>
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/profile' element={<Profile />} />
            <Route path='savedSongs' element={<SavedSongs />} />
            <Route path='forum' element={<Forum />} />
          </Routes>
        </div>
      ) : (
        <div>
          {/* <Login /> */}
          <Register />
        </div>
      )}
    </div>
  );
}

export default App;
