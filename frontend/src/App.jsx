import Input from "./Input";

/* This is the main file that is being called in the main.jsx file,
 * from main.jsx, the App component is being called and rendered to the DOM.
 * From there, main.jsx will be called in the index.html file
 * and the whole application will be rendered to the browser.
 */

function App() {
  return (
    /* You call your components inside an element, it can not be more than one element
     * That's why I used empty angle brackets, which is a shorthand for React.
     * However, You can call your components many times you want inside the empty angle brackets.
     */

    <>
      <h1>🎓 Student Registration</h1>
      <Input />
    </>
  );
}

// This exports the App component so it can be used in other parts of the application
export default App;
