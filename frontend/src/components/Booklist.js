import { Link } from "react-router-dom";

export default function Booklist({ Books }) {
  return (
    <>
      <div className="container-list">
        {Books.map((book) => (
          <Link key={book.id} to={`/books/${book.id}`}>
            <div className="flip-card">
              <div className="flip-card-inner">
                <div className="flip-card-front">
                  <img height="400px" width="265px" src={book.image} alt="" />
                </div>
                <div className="flip-card-back">
                  <h1>{book.name}</h1>
                  <p>ISBN: {book.ISBN}</p>
                  <p>Author: {book.Author}</p>
                  <p>Publisher: {book.Publisher}</p>
                  <p>Genres: {book.Genres}</p>
                </div>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </>
  );
}
