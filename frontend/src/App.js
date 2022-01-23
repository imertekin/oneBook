import "./App.css";
import Navbar from "./components/Navbar";
import Booklist from "./components/Booklist";

import { useState, useEffect } from "react";
import axios from "./services/axiosService";

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import BookDetail from "./components/BookDetail";
import NotFound from "./components/NotFound";
import LoginPage from "./components/LoginPage";
import RegisterPage from "./components/RegisterPage";
import Profile from "./components/Profile";

function App() {
  const [Books, setBooks] = useState([]);
  const [isLoggin, setIsLoggin] = useState("");
  const [user, setUser] = useState({
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    comments: [],
    mybooks: [],
    likes: [],
  });

  const access = localStorage.getItem("access_token");
  useEffect(() => {
    access ? setIsLoggin(true) : setIsLoggin(false);
  }, [access]);

  useEffect(() => {
    const getBooks = async () => {
      try {
        const res = await axios.get("/books/");
        setBooks(...[res.data]);
      } catch (error) {}
    };
    const profile = async () => {
      try {
        const res = await axios.get("/profile/");
        setUser(...res.data);
      } catch (error) {}
    };
    profile();
    getBooks();
  }, []);

  return (
    <div className="App">
      <Router>
        <Navbar isLoggin={isLoggin} user={user} />
        <Routes>
          <Route path="/" element={<Booklist Books={Books} />} />
          <Route
            path="/login"
            element={<LoginPage setIsLoggin={setIsLoggin} />}
          />
          <Route
            path="/register"
            element={<RegisterPage setIsLoggin={setIsLoggin} />}
          />
          <Route
            path="/my-profile"
            element={<Profile user={user} setUser={setUser} />}
          />
          <Route path="*" element={<Navigate to="/404" />} />
          <Route path="/404" element={<NotFound />} />
          <Route path="/books/:id" element={<BookDetail user={user} />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
