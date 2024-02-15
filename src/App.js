import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, Circle } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import * as turf from '@turf/turf';

const App = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const [outlets, setOutlets] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/outlets/')
      .then(response => response.json())
      .then(data => setOutlets(data));
  }, []);

  const handleSearch = () => {
    setIsLoading(true); // Start loading
    setError(null); // Reset error state

    fetch(`http://127.0.0.1:8000/api/outlets/search?query=${encodeURIComponent(searchQuery)}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch.');
        }
        return response.json();
      })
      .then(data => {
        console.log(data)
        setOutlets(data); 
        setIsLoading(false); 
      })
      .catch(error => {
        console.error('Search error:', error);
        setError('Search failed. Please try again.'); // Set error message
        setIsLoading(false); // End loading
      });
  };

  return (
    <div style={{ height: '100vh', width: '100vw' }}>
      <div style={{ position: 'absolute', zIndex: 1000, top: '5%', left: '50%', transform: 'translate(-50%, -50%)', backgroundColor: 'rgba(255, 255, 255, 0.8)', padding: '10px', borderRadius: '8px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <input type="text" value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} style={{ marginRight: '8px', padding: '5px', borderRadius: '4px', border: '1px solid #ccc' }} />
        <button onClick={handleSearch} style={{ padding: '5px 10px', borderRadius: '4px', border: 'none', backgroundColor: '#007bff', color: 'white', cursor: 'pointer' }}>{isLoading ? 'Searching...' : 'Search'}</button>
      </div>
      {error && <div style={{ color: 'red', position: 'absolute', top: '10%', left: '50%', transform: 'translate(-50%, -50%)' }}>{error}</div>}
      <MapContainer center={[3.1390, 101.6869]} zoom={12} style={{ height: '100%', width: '100%' }}>
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {outlets.map(outlet => (
          <React.Fragment key={outlet.id}>
            <Marker position={[outlet.latitude, outlet.longitude]}>
              <Popup>{outlet.name}</Popup>
            </Marker>
            <Circle center={[outlet.latitude, outlet.longitude]} radius={5000} />
          </React.Fragment>
        ))}
      </MapContainer>
    </div>
  );
  
};

export default App;