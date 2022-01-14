

export default function Profile({user}) {
    

    return (
        <div>
            <h1>{user.username}</h1>
            <h1>{user.email}</h1>
            <h1>{user.first_name}</h1>
            <h1>{user.last_name}</h1>
        </div>
    )
}
