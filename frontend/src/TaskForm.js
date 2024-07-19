// src/TaskForm.js
import React, { useState } from 'react';

function TaskForm() {
  const [taskName, setTaskName] = useState('');
  const [taskDescription, setTaskDescription] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const taskData = {
      title: taskName,
      description: taskDescription
    };
    console.log("HAHHASHHAHSHASHDSKAJDLKJASLDKJSAKLDLSAKJDLASJKDLKASJDL")
    console.log(`${process.env.REACT_APP_API_URL}`)

    try {
    
      const response = await fetch(`${process.env.REACT_APP_API_URL}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(taskData)
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const result = await response.json();
      console.log('Task created:', result);
      // Optionally reset the form or handle the response further
      setTaskName('');
      setTaskDescription('');
    } catch (error) {
      console.error('Error creating task:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Task Name:
        <input
          type="text"
          value={taskName}
          onChange={(e) => setTaskName(e.target.value)}
        />
      </label>
      <br />
      <label>
        Task Description:
        <input
          type="text"
          value={taskDescription}
          onChange={(e) => setTaskDescription(e.target.value)}
        />
      </label>
      <br />
      <button type="submit">Submit</button>
    </form>
  );
}

export default TaskForm;
