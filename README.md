# Django Rest Framework Course

This repository contains the source code and documentation for the Django Rest Framework course on YouTube. The course covers the following topics:

- Serializers
- ModalSerializers
- Function-based API views
- Class-based API views
- Token authentication
- Basic authentication
- Session authentication

## Installation

To install the project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/django-rest-framework-course.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## Usage

To use the APIs provided in the course, follow these steps:

1. Open a web browser and go to `http://localhost:8000/`
2. Use the API endpoints provided in the documentation below to interact with the server

## API Reference

### Serializer API

#### `GET /country/list/`

Returns a list of all serializers.

**Parameters:**

None

**Returns:**

``[
    {
        "id": 1,
        "name": "Poland",
        "note": "There are people that have warm hearts",
        "date": "2022-08-09T15:59:42.468053Z"
    },
]``



### Function-based API View API

#### `GET /function-based-api-view/`

Returns a list of all function-based API views.

**Parameters:**

None

**Returns:**

``[
{
"id": 1,
"name": "Function-based API View A"
},
{
"id": 2,
"name": "Function-based API View B"
}
]``


### Class-based API View API

#### `GET /class-based-api-view/`

Returns a list of all class-based API views.

**Parameters:**

None

**Returns:**

``[
{
"id": 1,
"name": "Class-based API View A"
},
{
"id": 2,
"name": "Class-based API View B"
}
]``


### Token Authentication API

#### `POST /token-auth/`

Authenticates a user using a token.

**Parameters:**

``{
"username": "your-username",
"password": "your-password"
}``


**Returns:**

``{
"token": "your-token"
}``


### Basic Authentication API

#### `GET /basic-auth/`

Authenticates a user using basic authentication.

**Parameters:**

None

**Returns:**

``{
"message": "Hello, your-username!"
}``