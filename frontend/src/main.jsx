import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

/* This is the entry point of the React application.
 * It imports necessary modules and renders the App component
 */

ReactDOM.createRoot(document.getElementById("root")).render(
  // Render the App component inside React.StrictMode.
  <React.StrictMode>
    <App /> 
  </React.StrictMode>
);
