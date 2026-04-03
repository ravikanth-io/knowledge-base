import { useState } from "react";
import Login from "./components/Login";
import NoteForm from "./components/NoteForm";
import NotesList from "./components/NotesList";

function App() {
  const [token, setToken] = useState("");

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <h1 className="text-3xl mb-4">Knowledge Engine</h1>

      <Login setToken={setToken} />
      <NoteForm token={token} />
      <NotesList token={token} />
    </div>
  );
}

export default App;
