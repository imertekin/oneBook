import { useParams, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "../services/axiosService";
import { BsHeartFill } from "react-icons/bs";
import { BsHeart } from "react-icons/bs";
import { BiBookAdd } from "react-icons/bi";
import { MdDeleteOutline } from "react-icons/md";
import ReactTimeAgo from 'react-time-ago'


export default function BookDetail({ user }) {
  const [thisBook, setThisBook] = useState({Author: "",Genres: "",ISBN: "",Print_length:"",Publication_date: "",Publisher: "",id: "",image: "",name: "",_comments: [],
  _likes_count:""});
  const [liked, setLiked] = useState("");
  const [content, setContent] = useState("");

  const { id } = useParams();
  const navigate = useNavigate();

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

  useEffect(() => {
    getBook();
  }, [id, navigate, liked]);

  useEffect(() => {
    const like = () => {
      user.liker &&
      user.liker.filter((i) => i.book === thisBook.name).length > 0
        ? setLiked(true)
        : setLiked(false);
    };
    like();
  }, [thisBook.name, user]);

  const handleLike = async () => {
    try {
      if (!liked) {
        await axios.post(`/books/${id}/like/`);
        setLiked(true);
      } else if (liked) {
        await axios.post(`/books/${id}/unlike/`);
        setLiked(false);
      }
    } catch (error) {}
  };

  const handleComment = async () => {
    try {
      const res = await axios.post(`/books/${id}/comment/`, {
        content: content,
      });
      getBook();
      console.log(res);
      setContent("");
    } catch (error) {}
  };

  const handleAddBooklist=()=>{
    console.log("clicked")
  }

  const handleDelete= async(comment)=>{
    const res = await axios.delete(`/comment/${comment.id}/`)
    getBook()
    console.log(res)
  }

  return (
    <div className="detail-container">
      <div className="detail-upper">
        <img height="200px" width="150px" src={thisBook.image} alt="" />
        <div>
          <p>{thisBook.name}</p>
          <p>{thisBook.Author}</p>
          <div className="btn-container">
            <div
            role="button"
            onClick={handleAddBooklist}
            > 
              <BiBookAdd />
              <span>Add booklist </span>

              </div>
            <div className="like-btn" role="button" onClick={handleLike}>
              {liked ? (
                <BsHeartFill color="red" style={{ width: 20, height: 20 }} />
              ) : (
                <BsHeart style={{ width: 20, height: 20 }} />
              )}
            </div>
            <span>{thisBook._likes_count}</span>
          </div>
        </div>
      </div>
      <div className="comment-area">
        <textarea
        placeholder="Tell Something About The Book"
          cols={40}
          rows={5}
          onChange={(e) => {
            setContent(e.target.value);
          }}
          value={content}
        />
        <button onClick={handleComment}>Post</button>
      </div>
      <div className="comments-container"style={thisBook._comments.length ===0 ? {border:"none"}: {}} >
        {thisBook._comments.map((i) => (
            <div key={i.id} className="comments">
             <span className="comment-item">{i.content}</span>
              <div className="comment-info">
                <div>
              <span>{i.user}</span>
              <ReactTimeAgo className="comment-time" date={new Date(i.created_at)}/>
              </div>
              <div role="button" className="delete-btn" onClick={()=>handleDelete(i)}> {i.user===user.username && <MdDeleteOutline style={{ width: 15, height: 15 }} />} </div>
              </div>
              
            </div>
          ))}
      </div>
    </div>
  );
}
