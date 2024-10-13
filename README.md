# Event Planner DJRest

Event Planner DJRest is a comprehensive event planning application designed to help users organize and manage events efficiently. This project leverages Django and Django REST framework to provide a robust backend for handling event-related data.

## Features

- User authentication and authorization
- Event creation and management
- API endpoints for event data
- Event notifications (Coming Feature)

## Installation

1. Clone the repository:
	```bash
	git clone https://github.com/seyistry/event_planner_djrest.git
	```
2. Navigate to the project directory:
	```bash
	cd event_planner_djrest
	```
3. Create and activate a virtual environment:
	```bash
	python -m venv venv
	source venv/bin/activate  # On Windows use `venv\Scripts\activate`
	```
4. Install the required dependencies:
	```bash
	pip install -r requirements.txt
	```
5. Apply migrations:
	```bash
	python manage.py migrate
	```
6. Run the development server:
	```bash
	python manage.py runserver
	```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Use the provided API endpoints to interact with event data

## API Endpoints

- `GET 'api/v1/events/` - List all user events
- `POST 'api/v1/events/` - Create a new event
- `GET 'api/v1/events/{id}/` - Retrieve event details
- `PUT 'api/v1/events/{id}/` - Update event details
- `DELETE 'api/v1/events/{id}/` - Delete an event
- `GET 'api/v1/events/{id}/register/` - Get registration details
- `POST 'api/v1/events/{id}/register/` - Register for event
- `POST 'api/v1/events/{id}/join-waitlist/` - Join Event wait list
- `POST 'api/v1/users/` - create a new user account
- `GET 'api/v1/users/info/` - Check user info
- `PUT 'api/v1/users/info/` - Update user info
- `DELETE 'api/v1/users/info/` - Delete user info
- `POST 'api/v1/token/` - Generate JWT token for user
- `POST 'api/v1/token/refresh/` - refresh User token

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [seyistry@gmail.com](mailto:seyistry@gmail.com).

## Author

Oluwaseyi Egunjobi

