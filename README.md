# Django Rest Tutorial 🌐💻🐍

This repository contains code for a basic Django Rest Framework project.

[Youtube Link](https://www.youtube.com/watch?v=ygw08d3H9gI&list=PLwjQ5gMPDTTBIA8xw3JV-C82BrVMQu6Gu)  🎥🔴

## Getting Started 🚀

To get started with this project, you will need to follow these steps:

1. Clone the repository to your local machine. 🖥️💾
2. Install the necessary packages by running the command `pip install -r requirements.txt`. 📦👨‍💻
3. Run the migrations by running the command `python manage.py migrate`. 🚀🚀🚀
4. Start the server by running the command `python manage.py runserver`. 🏃‍♂️🌐

## First App 📱

The `first_app` directory contains the code for a simple REST API with CRUD functionality for a `Country` model.

### Country Model 🌍

The `Country` model has the following fields:

- `id` (auto-generated) 🔢
- `name` (string) 📛
- `capital` (string) 🏛️
- `population` (integer) 🧑👥
- `currency` (string) 💰💱

### Serializers 🧵

The `CountrySerializer` class in `serializers.py` defines how the `Country` model should be serialized and deserialized for API requests and responses.

### Views 👁️‍🗨️

The `views.py` module contains three different views for the `Country` model: `GenericApiView`, `CountryView`, and `CountryDetailView`.

#### GenericApiView 👥

The `GenericApiView` class is a subclass of several `mixins` classes provided by the Django Rest Framework to create a generic view for the `Country` model. The view supports `GET`, `POST`, `PUT`, and `DELETE` requests for a list of countries or a single country.

- `GET /api/country/`: List all countries 🌍🌎🌏
- `GET /api/country/<pk>/`: Retrieve a single country 🔍
- `POST /api/country/`: Create a new country 🆕🌍
- `PUT /api/country/<pk>/`: Update an existing country 🔄🌍
- `DELETE /api/country/<pk>/`: Delete an existing country 🗑️🌍

#### CountryView 🌍

The `CountryView` class defines a custom view for `GET` and `POST` requests for the `Country` model. It returns a list of all countries or creates a new country.

- `GET /api/country/`: List all countries 🌍🌎🌏
- `POST /api/country/`: Create a new country 🆕🌍

#### CountryDetailView 🔍

The `CountryDetailView` class defines a custom view for `GET`, `PUT`, and `DELETE` requests for a single country. It retrieves, updates, or deletes a single country based on its primary key (`pk`).

- `GET /api/country/<pk>/`: Retrieve a single country 🔍
- `PUT /api/country/<pk>/`: Update an existing country 🔄🌍
- `DELETE /api/country/<pk>/`: Delete an existing country 🗑️🌍

### Authentication and Authorization 🔑🔐

Two custom views are defined for authentication and authorization:

- `login`: Authenticates a user with a username and password and returns a token if successful.
- `logout`: Deletes a user's token to log them out.

Both views are decorated with the `@api_view`, `@authentication_classes`, and `@permission_classes` decorators to configure the authentication and authorization settings.

- `GET /api/login/`: Authenticate a user with a username and password and return a token  🔒
- `DELETE /api/logout/`: Delete a user's token to log them out 🔓
