```markdown
# ALX Travel App

A Django-based travel application with REST API support, MySQL database, Swagger documentation, and CORS configuration.

## Repository Structure
- **Repository**: `alx_travel_app`
- **Directory**: `alx_travel_app`
- **Files**:
  - `requirements.txt`: Project dependencies.
  - `alx_travel_app/settings.py`: Django settings with MySQL, REST Framework, CORS, and Swagger.
  - `alx_travel_app/urls.py`: URL routing with Swagger endpoints.
  - `listings/`: App for core functionality (empty URLs for now).
  - `.env`: Environment variables (not committed).
  - `.gitignore`: Excludes sensitive files.
  - `README.md`: This file.

## Prerequisites
- **Python**: 3.8+
- **MySQL**: Running locally (host: `localhost`, user: `root`, password: configurable).
- **RabbitMQ**: Installed locally (for future Celery use).
- **Git**: For version control.
- **Dependencies**:
  ```bash
  pip install -r requirements.txt
  ```

## Setup
1. **Clone Repository**:
   ```bash
   git clone https://github.com/<your-username>/alx_travel_app.git
   cd alx_travel_app
   ```
2. **Create Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure MySQL**:
   - Create database `alx_travel_db`:
     ```sql
     CREATE DATABASE alx_travel_db;
     ```
   - Create `.env` file in `alx_travel_app/`:
     ```text
     SECRET_KEY=your-secret-key-here
     DEBUG=True
     DATABASE_NAME=alx_travel_db
     DATABASE_USER=root
     DATABASE_PASSWORD=
     DATABASE_HOST=localhost
     DATABASE_PORT=3306
     ```
5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```
6. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```
7. **Access Swagger**:
   - Visit `http://localhost:8000/swagger/` for API documentation.

## Usage
- **API**: Add endpoints in `listings/urls.py` and implement views/models as needed.
- **Swagger**: Automatically documents all APIs at `/swagger/`.
- **CORS**: Allows frontend requests from `http://localhost:3000`.
- **Celery**: Configured for future task queuing (requires RabbitMQ).

## Notes
- **Security**: Update `SECRET_KEY` and `DATABASE_PASSWORD` in `.env` for production.
- **CORS**: Adjust `CORS_ALLOWED_ORIGINS` for additional frontend URLs.
- **RabbitMQ**: Install and configure for Celery tasks in future milestones.
- **Database**: Ensure MySQL server is running before migrations.
