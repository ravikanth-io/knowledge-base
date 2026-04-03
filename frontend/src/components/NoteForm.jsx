import axios from "axios";
import { useState } from "react";

const API = "https://knowledge-base-api-ly0h.onrender.com";

export default function NoteForm({ token }) {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const addNote = async () => {
    await axios.post(
      `${API}/notes`,
      { title, content },
      { headers: { Authorization: `Bearer ${token}` } }
    );

    alert("Saved");
  };

  return (
    <div className="mb-4">
      <input onChange={e=>setTitle(e.target.value)} placeholder="Title" />
      <input onChange={e=>setContent(e.target.value)} placeholder="Content" />
      <button onClick={addNote}>Save</button>
    </div>
  );
}
