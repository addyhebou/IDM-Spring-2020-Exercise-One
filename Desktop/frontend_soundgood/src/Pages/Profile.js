import React from 'react';
import { IconContext } from 'react-icons';
import { FaPen, FaTimesCircle, FaTrophy } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import Badge from '../Components/Badge.js';

const tracks = [
  {
    name: 'profile1',
    date: '1 day ago',
    song: "You're beautiful",
    likes: 500,
    dislikes: 200,
    comments: 37,
  },
  {
    name: 'profile2',
    date: '2 day ago',
    song: 'I saw your face',
    likes: 400,
    dislikes: 100,
    comments: 27,
  },
  {
    name: 'profile3',
    date: '3 day ago',
    song: 'In a crowded place',
    likes: 300,
    dislikes: 500,
    comments: 17,
  },
];

export default function Profile() {
  return (
    <div>
      <header>
        <div className='navbar'>
          <Link to='/'>
            <IconContext.Provider
              value={{ style: { color: 'rgb(255, 255, 255)' } }}
            >
              <div>
                <FaTimesCircle />
              </div>
            </IconContext.Provider>
          </Link>
          <h1>Kendrick Lamar</h1>
          <FaPen />
        </div>
      </header>
      <main>
        <div className='image-cropper'>
          <img
            className='profilePic'
            src='https://upload.wikimedia.org/wikipedia/commons/3/32/Pulitzer2018-portraits-kendrick-lamar.jpg'
            alt='Profile picture'
          />
        </div>
        <div className='trophies'>
          <FaTrophy />
          <strong>13,459</strong>
        </div>
        <div className='badges'>
          <Badge />
        </div>
      </main>
      <section>
        <div className='dividerHeader'>
          <h2>Discovered Songs</h2>
          <p>View More</p>
        </div>
        {tracks.map((song) => {
          return (
            <div>
              <p>{song.name}</p>
              <p>{song.song}</p>
            </div>
          );
        })}
      </section>
    </div>
  );
}
