# Creaing Vertual Environment
```bash
python -m venv venv
```
 
# Installing Requirements
```bash
pip install -r requirements.txt
```

# Running the Server
```bash
python manage.py runserver
```

# Creating SuperUser
```bash
python manage.py createsuperuser
```

# Already Created SuperUser
- username: `admin`
- password: `admin`

# JSON Web Token Authentication -> access_token, refresh_token
## Must add a Header in request
###  Header Name: Authorization
## Example:
### `Authorization: JWT access_token`

# API Endpoints

## Related to books-category
### http://127.0.0.1:8000/books_categorys/

## Related to books
### http://127.0.0.1:8000/books/
### http://127.0.0.1:8000/books/1
### http://127.0.0.1:8000/books/my_books
## Related to book reviews
### http://127.0.0.1:8000/books/1/reviews
### http://127.0.0.1:8000/books/1/reviews/1
## Related to book ratings
### http://127.0.0.1:8000/books/1/ratings
### http://127.0.0.1:8000/books/1/ratings/1

## Related to questions-category
### http://127.0.0.1:8000/questions_categorys/

## Related to questions
### http://127.0.0.1:8000/questions
### http://127.0.0.1:8000/questions/1
### http://127.0.0.1:8000/questions/my_questions -> login required
## Related to ranks
### http://127.0.0.1:8000/questions/1/ranks -> login required
### http://127.0.0.1:8000/questions/1/ranks/1 -> login required
## Related to comments
### http://127.0.0.1:8000/questions/1/comments -> login required
### http://127.0.0.1:8000/questions/1/comments/1 -> login required
## Related to comments-replies
### http://127.0.0.1:8000/questions/1/comments/1/replies -> login required
### http://127.0.0.1:8000/questions/1/comments/1/replies/1 -> login required

## Related to profiles
### http://127.0.0.1:8000/profiles/  -> login required
### http://127.0.0.1:8000/profiles/1  -> login required(Moderator and Admin Only)
### http://127.0.0.1:8000/profiles/me  -> login required(Current User's Profile Info)
## Related to login
### http://127.0.0.1:8000/auth/jwt/create -> login
### http://127.0.0.1:8000/auth/jwt/refresh -> login
## Related to users
### http://127.0.0.1:8000/auth/users -> signup(Creating a New User)
### http://127.0.0.1:8000/auth/users -> login required(Moderator and Admin Only)
### http://127.0.0.1:8000/auth/users/1 -> login required(Moderator and Admin Only)
### http://127.0.0.1:8000/auth/users/me/ -> login required(Current User Info)