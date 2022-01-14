import { Link } from "react-router-dom";

export default function Booklist({ Books }) {
  return (
    <>

      <div className="container-list">
        {Books.map((book) => (
          <Link key={book.id} to={`/books/${book.id}`}>
          <img height="400px" width="265px" src={book.image} alt="" />
          </Link>
        ))}
      </div>
    </>
  );
}
