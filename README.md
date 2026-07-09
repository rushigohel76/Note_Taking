# 📝 Study Notes — Django Note-Taking Web Application

Study Notes is a Django-based web application that allows users to create an account, log in securely, create personal notes, view their saved notes, and delete notes they no longer need.

The application was developed to gain practical experience with Django backend development, database relationships, password hashing, session-based authentication, CRUD operations, and user-specific data management.

---

## 🚀 Project Overview

Study Notes provides a simple personal note management system where each registered user has their own collection of notes.

After creating an account and logging in, users can:

- Create new notes
- Save notes to the database
- View all their saved notes
- View recently created notes
- Delete their own notes
- Log out securely

Each note is associated with its owner using a database relationship, ensuring that users access and manage their own notes.

---

## ✨ Features

### 👤 User Registration

Users can create an account by providing:

- Username
- Email address
- Password
- Password confirmation

The registration system includes:

- Required field validation
- Password confirmation validation
- Password hashing before database storage
- Unique email validation at the database level

---

### 🔐 Custom Authentication System

The project implements custom session-based authentication.

The authentication system includes:

- User login
- Credential verification
- Secure password hashing
- Password verification
- Session creation
- Session-based route protection
- Secure logout through session clearing

Passwords are not stored as plain text. Django's password hashing utilities are used for password storage and verification.

---

### 📝 Note Creation

Authenticated users can create personal notes containing:

- Note title
- Note content
- Automatic creation timestamp

Notes are stored in the database and connected to the user who created them.

---

### 📚 Stored Notes

Users can view all of their saved notes.

The application:

- Retrieves notes belonging to the logged-in user
- Orders notes from newest to oldest
- Displays note titles and content
- Keeps each user's notes associated with their account

---

### 🕒 Recent Notes

The home page displays the three most recently created notes for the logged-in user.

This provides quick access to recently added content.

---

### 🗑️ Delete Notes

Users can delete their own notes.

The delete operation checks both:

- Note ID
- Logged-in User ID

This prevents one user from deleting another user's note through the delete operation.

---

## 🛠️ Technologies Used

### Backend

- Python
- Django
- Django ORM
- Django Sessions
- Django Password Hashing Utilities

### Frontend

- HTML5
- CSS3
- Django Templates

### Database

- SQLite / Django-supported relational database

### Development Tools

- Git
- GitHub
- Visual Studio Code / PyCharm

---

## 🗄️ Database Design

The application contains two main models:

### NotesUserDetails

Stores registered user information:

- Username
- Email
- Hashed Password
- Account Creation Time

### StoredNote

Stores user-created notes:

- User Reference
- Note Title
- Note Content
- Creation Time

The relationship between users and notes is:

```text
NotesUserDetails
        │
        │  One-to-Many
        ▼
    StoredNote
