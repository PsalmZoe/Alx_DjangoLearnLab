# API Endpoint Documentation

### User Endpoints

#### Register User
- **Path:** `/api/accounts/register/`
- **Method:** POST
- **Request Parameters:**
  - `username` (string, required)
  - `email` (string, required)
  - `password` (string, required)
- **Response Example:**
```json
{
    "id": 1,
    "username": "johndoe",
    "email": "johndoe@example.com",
    "bio": "",
    "profile_picture": null
}
```

#### User Profile
- **Path:** `/api/accounts/profile/`
- **Method:** GET/PUT
- **Request Parameters (PUT):**
  - `bio` (string, optional)
  - `profile_picture` (file, optional)
- **Response Example:**
```json
{
    "id": 1,
    "username": "johndoe",
    "email": "johndoe@example.com",
    "bio": "Hello, world!",
    "profile_picture": "http://example.com/media/profile_pictures/user1.png"
}
```

### Post Endpoints

#### List/Create Posts
- **Path:** `/api/posts/`
- **Method:** GET/POST
- **Request Parameters (POST):**
  - `title` (string, required)
  - `content` (string, required)
- **Response Example (GET):**
```json
[
    {
        "id": 1,
        "author": 1,
        "title": "First Post",
        "content": "This is my first post!",
        "created_at": "2025-01-01T12:00:00Z",
        "updated_at": "2025-01-01T12:00:00Z"
    }
]
```

#### Like/Unlike Post
- **Path:** `/api/posts/<pk>/like/`
- **Method:** POST
- **Response Example:**
```json
{
    "message": "Liked"
}
```

### Notification Endpoints

#### List Notifications
- **Path:** `/api/notifications/`
- **Method:** GET
- **Response Example:**
```json
[
    {
        "id": 1,
        "recipient": 1,
        "actor": 2,
        "verb": "liked your post",
        "target": "Post #1",
        "timestamp": "2025-01-01T12:30:00Z"
    }
]
