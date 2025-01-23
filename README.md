# saho-task

## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Postman](#postman)
* [Fixtures](#fixtures)
* [Superuser Credentials](#superuser-credentials)

---

## Technologies
* Django
* Django REST Framework (DRF)
* Docker
* PostgreSQL

---

## Setup
To run the project:
1. Clone the repository:
    ```
    $ git clone https://github.com/parsarezaee/saho-task
    ```
2. Navigate to the project directory:
    ```
    $ cd saho-task/saho
    ```
3. Start the project with Docker Compose:
    ```
    $ sudo docker compose up --build
    ```
4. Apply migrations to set up the database schema:
    ```
    $ sudo docker compose exec saho_web python manage.py migrate
    ```

---

## Postman
A Postman collection is included in the project to simplify testing the APIs. You can import the collection directly into Postman:
1. Locate the Postman collection file: `saho.postman_collection.json`
2. Import the file into Postman.
3. Use the pre-configured requests to interact with the API.

---

## Fixtures
The project includes three fixture files to load initial data:
1. `users.json`: Contains 15 users.
2. `orders.json`: Contains sample orders.
3. `superuser.json`: Contains the superuser data.

To load these fixtures, use the following commands:
1. Load the users:
    ```
    $ sudo docker compose exec saho_web python manage.py loaddata users.json
    ```
2. Load the superuser:
    ```
    $ sudo docker compose exec saho_web python manage.py loaddata superuser.json
    ```
3. Load the orders:
    ```
    $ sudo docker compose exec saho_web python manage.py loaddata orders.json
    ```

---

## Superuser Credentials
After loading the `superuser.json` fixture, use the following credentials to log in as the superuser:
- **Username:** `parsa`
- **Password:** `parsa1234`

---

## Testing the API
After setting up the project and loading the data:
1. Use the Postman collection to test the APIs.
2. If required, access the Django admin panel at: http://127.0.0.1:8003/admin/
