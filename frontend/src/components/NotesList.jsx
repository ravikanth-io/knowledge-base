import axios from "axios";
import { useState } from "react";

const API = "https://knowledge-base-api-ly0h.onrender.com";

export default function NotesList({ token }) {
  const [notes, setNotes] = useState([]);

  const load = async () => {
    const res = await axios.get(`${API}/notes`);
    setNotes(res.data);
  };

  const deleteNote = async (id) => {
    await axios.delete(`${API}/notes/${id}`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    load();
  };

  return (
    <div>
      <button onClick={load}>Load Notes</button>

      {notes.map(n => (
        <div key={n.id}>
          <h2>{n.title}</h2>
          <button onClick={()=>deleteNote(n.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
}
