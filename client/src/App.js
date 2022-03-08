import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("/timetable")
      .then((res) => res.json())
      .then((data) => {
        setData(data);

        console.log(data);
      });
  }, []);

  return (
    <div>
      {typeof data.timetable === "undefined" ? (
        <p>Loading ...</p>
      ) : (
        data.timetable.map((position, i) => <p key={i}>{position}</p>)
      )}
    </div>
  );
}

export default App;
