import axios from "axios";

const API = "https://knowledge-base-api-ly0h.onrender.com";

export default function Login({ setToken }) {
  const login = async () => {
    const res = await axios.post(`${API}/login`, {
      username: "admin",
      password: "1234",
    });

    setToken(res.data.access_token);
    alert("Logged in");
  };

  return (
    <button onClick={login} className="bg-blue-500 p-2 mb-4">
      Login
    </button>
  );
}
