import { useParams, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "../services/axiosService";

export default function BookDetail() {
  const [thisBook, setThisBook] = useState("");

  const { id } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const getBook = () => {
      axios
        .get(`/books/${id}/`)
        .then((res) => {
          setThisBook(res.data);
        })
        .catch((err) => {
          if (err.response.status === 404) {
            navigate("/404");
          }
        });
    };
    getBook();
  }, [id, navigate]);

  return (
    <div className="container-detail">
      <div className="flip-card">
        <div className="flip-card-inner">
          <div className="flip-card-front">
            <img height="500px" width="365px" src={thisBook.image} alt="" />
          </div>
          <div className="flip-card-back">
            <h1>{thisBook.name}</h1>
            <p>Yazar: {thisBook.Author}</p>
            <p>Yayınevi: {thisBook.Publisher}</p>
            <p>Tür: {thisBook.Genres}</p>
            <p>Alınabilir mi ? {thisBook.is_avaible ? "Evet" : "Hayır"} </p>
          </div>
        </div>
      </div>
    </div>
  );
}
