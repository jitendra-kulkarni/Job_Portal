import { useState } from "react";
import api from "../api/axios";
import { useNavigate } from "react-router-dom";


function Login() {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const handleLogin = (e) => {
        e.preventDefault();

        api.post("accounts/login/", {
            username,
            password,
        })
            .then((response) => {
                localStorage.setItem("access", response.data.access);
                localStorage.setItem("refresh", response.data.refresh);

                console.log("Login Successful!");

                navigate("/jobs");
                
                console.log(response.data);
            })
            .catch((error) => {
                console.log(error.response.data);
            });
    };

    return (
        <div>

            <h1>Login</h1>

            <form onSubmit={handleLogin}>

                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />

                <br /><br />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <br /><br />

                <button type="submit">
                    Login
                </button>

            </form>

        </div>
    );
}

export default Login;