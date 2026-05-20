import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState({ time: "", tasks: [] });

  useEffect(() => {
    fetch('http://localhost:5001/tasks')
      .then((res) => res.json())
      .then((data) => setData(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', maxWidth: '600px', margin: '50px auto' }}>
      <h1>Task Manager</h1>
      <h3>Time: {data.time}</h3>
      <ul>
        {data.tasks.map((task) => (
          <li key={task.id}>{task.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
