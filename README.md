# Todo List App

This is a simple todo list application with user authentication, support for adding comments to todos, and a PostgreSQL database. The application is currently in development and can be run using Docker Compose.

## Features

- User authentication with login functionality
- Creation of todos with title, description, and completion status
- Ability to add comments to each todo
- PostgreSQL database to store user data, todos, and comments
- Docker Compose for easy development environment setup

## Instructions

To run the application using Docker Compose, follow these steps:

1. Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory.

   ```bash
   cd todo-list-app
   ```

3. Build and run the Docker containers using Docker Compose.

   ```bash
   docker-compose up
   ```

4. Once the containers are up and running, you should be able to access the application at `http://localhost:8000` in your web browser.

## Development

The application is currently in development and may contain bugs or incomplete features. Development work is ongoing, and updates will be made to the repository regularly.

## Technologies Used

- Python
- Django
- PostgreSQL
- Docker
- Docker Compose
- REST framework for API development

## Contributing

If you would like to contribute to the development of the application, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them to your branch.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.
