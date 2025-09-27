// This component handles user input for student information and displays a list of students.
 
import { useState, useEffect } from "react";

// This function defines the Input component
function Input() {
  // state variables for form inputs and student list
  // ex. name is from the input field, setName is the function to update it
  const [name, setName] = useState("");
  const [major, setMajor] = useState("");
  const [year, setYear] = useState("2025");
  const [students, setStudents] = useState([]);

  // fetch students from backend
  useEffect(() => {
    fetch("http://127.0.0.1:8000/students")
      .then((res) => res.json())
      .then((data) => setStudents(data))
      .catch((err) => console.error("Error fetching students:", err));
  }, []);

  // handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault(); 

    // create payload
    const payload = { name, major, year: parseInt(year) };

    // send POST request to backend
    try {
      const res = await fetch("http://127.0.0.1:8000/students", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload), // convert payload to JSON
      });

      // if successful, update student list so we don't need to refresh
      if (res.ok) {
        const newStudent = await res.json();
        setStudents([...students, newStudent]); // update list
        setName("");
        setMajor("");
        setYear("2025");
      } else {
        console.error(" Failed to add student");
      }
    } catch (err) {
      console.error("Error:", err);
    }
  };

  return (
    <div className="form-wrapper">
      <form className="Input" onSubmit={handleSubmit}>
        <label htmlFor="name">What's your name? Tell me right now!</label>
        <input
          type="text"
          placeholder="Enter your name..."
          value={name}
          onChange={(e) => setName(e.target.value)} // Update name state on change
        />
        <br></br>

        <label htmlFor="major">What major? Comp Sci? We cooked bruh</label>
        <input
          type="text"
          placeholder="Enter your major..."
          value={major}
          onChange={(e) => setMajor(e.target.value)}
        />
        <br></br>

        <label htmlFor="myDropdown">Choose what year you will be graduating</label>
        <select
          id="myDropdown"
          name="myDropdown"
          value={year}
          onChange={(e) => setYear(e.target.value)}
        >
          <option value="2025">2025</option>
          <option value="2026">2026</option>
          <option value="2027">2027</option>
          <option value="2028">2028</option>
          <option value="2029">2029</option>
        </select>
        <br></br>

        <div>
          <button type="submit">Submit</button>
        </div>
        <br></br>
      </form>

      <div className="scrollable-list-container">
        <ul>
          {students.map((s) => (
            <li key={s.id}>
              {s.name} — {s.major} ({s.year})
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Input;
