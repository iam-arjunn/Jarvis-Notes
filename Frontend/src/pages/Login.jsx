import { useState } from "react";
import API from "../services/api";
import "../css/Login.css";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const handleLogin = async () => {
    setLoading(true);
    setError("");

    try {
      const res = await API.post("/login", {
        email,
        password,
      });

      localStorage.setItem("token", res.data.access_token);

      setTimeout(() => {
        alert("Welcome to J.A.R.V.I.S 🧠");
        setLoading(false);
      }, 800);

    } catch (err) {
      setLoading(false);
      setError("Invalid email or password");
    }
  };

  return (
    <div className="login-container">
      <div className="login-card">

        <h2 className="login-title">J.A.R.V.I.S</h2>

        {/* ERROR MESSAGE */}
        {error && <p className="error-text">{error}</p>}

        <input
          className="login-input"
          type="email"
          placeholder="Enter Email"
          onChange={(e) => setEmail(e.target.value)}
        />

        {/* PASSWORD FIELD */}
        <div className="password-wrapper">
          <input
            className="login-input"
            type={showPassword ? "text" : "password"}
            placeholder="Enter Password"
            onChange={(e) => setPassword(e.target.value)}
          />

          <span
            className="toggle-password"
            onClick={() => setShowPassword(!showPassword)}
          >
            {showPassword ? (
              // 👁‍🗨 hidden icon
              <svg width="20" height="20" fill="#00d9ff" viewBox="0 0 24 24">
                <path d="M12 5c-7 0-10 7-10 7s3 7 10 7 10-7 10-7-3-7-10-7zm0 12a5 5 0 1 1 0-10 5 5 0 0 1 0 10zm0-8a3 3 0 1 0 0 6 3 3 0 0 0 0-6z" />
                <line x1="2" y1="2" x2="22" y2="22" stroke="#00d9ff" strokeWidth="2" />
              </svg>
            ) : (
              // 👁 visible icon
              <svg width="20" height="20" fill="#00d9ff" viewBox="0 0 24 24">
                <path d="M12 5c-7 0-10 7-10 7s3 7 10 7 10-7 10-7-3-7-10-7zm0 12a5 5 0 1 1 0-10 5 5 0 0 1 0 10zm0-8a3 3 0 1 0 0 6 3 3 0 0 0 0-6z" />
              </svg>
            )}
          </span>
        </div>
        {/* BUTTON */}
        <button
          className="login-button"
          onClick={handleLogin}
          disabled={loading}
        >
          {loading ? <div className="loader"></div> : "Initialize System"}
        </button>

      </div>
    </div>
  );
}

export default Login;