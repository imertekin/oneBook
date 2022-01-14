import React from 'react'

export default function Navbar({isLoggin,user}) {

  const handlerLogout=async()=>{
    localStorage.removeItem("access_token")
    localStorage.removeItem("refresh_token")
  }

    return (
        <div className='navbar'>
          <div className='nav-item-left' >
            <a href="/">My books</a>
          </div>
          <div className='search-bar'>
            <input type="text" placeholder='Search' />
          </div>
          <div className='nav-item-right'>
           {isLoggin ? ( 
           <>
           <span>{user.username}</span> 
           <a href="/my-profile">Hesabım</a> 
           <a onClick={handlerLogout} href="/">Logout</a>
           </>):(<>
            <a href="/login">Login</a>
            <a href="/register">Register</a>
           </>) }
            
          </div>
            
        </div>
    )
}
