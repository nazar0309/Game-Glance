[&lt; Back to README file](/README.md)

# ERD Diagram

- PostgreSQL was used for the database, storing information about the `About`, `CollaborateRequest`, `Game`, and `Review` models, with Cloudinary used to store image fields.

![ERD diagram of database](/static/images/erd_diagram.png)


### CollaborateRequest Model

| Key    | Field Type | Validation                        |
|--------|------------|-----------------------------------|
| name   | CharField  | max_length=200                    |
| email  | EmailField |                                   |
| message | TextField |                                   |
| read   | BooleanField | default=False                   |

- **Note**: `CollaborateRequest` holds collaboration request data, including name, email, message, and a `read` flag to track requests.

### Game Model

| Key            | Field Type         | Validation                                  |
|----------------|--------------------|---------------------------------------------|
| title          | CharField          | max_length=200                              |
| image          | CloudinaryField    | default='placeholder'                       |
| slug           | SlugField          | max_length=2000, unique=True                |
| description    | TextField          |                                             |
| release_date   | DateField          |                                             |
| company        | CharField          | max_length=100                              |
| genre          | CharField          | max_length=50                               |
| platform       | CharField          | max_length=50 (e.g., PC, PlayStation, Xbox) |
| created_on     | DateTimeField      | auto_now_add=True                           |
| updated_on     | DateTimeField      | auto_now=True                               |
| youtube_url    | URLField           | max_length=500, blank=True, null=True       |

- **Note**: The `Game` model includes detailed game information, including a title, description, release date, genre, platform, and an optional YouTube URL.

### Review Model

| Key        | Field Type        | Validation                                       |
|------------|-------------------|--------------------------------------------------|
| game       | ForeignKey        | Game, on_delete=models.CASCADE, related_name="reviews" |
| author     | ForeignKey        | User, on_delete=models.CASCADE, related_name='reviewer' |
| body       | TextField         | max_length=200                                   |
| approved   | BooleanField      | default=False                                    |
| created_on | DateTimeField     | auto_now_add=True                                |

- **Note**: Each `Review` links to a `Game` and `User`, storing review content, an approval status, and a timestamp for when it was created.
