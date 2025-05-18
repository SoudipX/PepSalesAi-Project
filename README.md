# PepSalesAi-Project
Backend Notification System
A scalable Notification Service built with Django REST Framework (DRF) and Celery, supporting Email, SMS, and In-App notifications with RabbitMQ for queue management.

Features
API Endpoints:

POST /api/v1/notifications - Send a notification (Email/SMS/In-App)

GET /api/v1/users/{user_id}/notifications - Fetch all notifications for a user

Asynchronous Processing using Celery + RabbitMQ

Retry Mechanism for failed notifications (max 3 retries)

Django Admin Panel for managing notifications

Setup & Installation
Prerequisites
Python 3.9+

RabbitMQ (for task queue)

(Optional) PostgreSQL (default: SQLite)

Clone the Repository:

git clone https://github.com/yourusername/notification-service-django.git
cd notification-service-django
Install Dependencies:

pip install -r requirements.txt
Configure Database (Optional):
By default, Django uses SQLite. To switch to PostgreSQL:

Update notification_service/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Install psycopg2:

pip install psycopg2-binary
Run Migrations:

python manage.py migrate
Start Services:

Start RabbitMQ (in a new terminal):

rabbitmq-server
Start Django Development Server:

python manage.py runserver
API Docs: http://localhost:8000/api/v1/notifications

Admin Panel: http://localhost:8000/admin (Create a superuser with python manage.py createsuperuser)

Start Celery Worker (in a new terminal):

celery -A notification_service worker --loglevel=info
API Usage
Send a Notification:

curl -X POST http://localhost:8000/api/v1/notifications \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user123", "type": "email", "content": "Hello, World!"}'
Response:

{
  "id": 1,
  "status": "queued"
}
Fetch User Notifications:

curl http://localhost:8000/api/v1/users/user123/notifications
Response:

[
  {
    "id": 1,
    "user_id": "user123",
    "type": "email",
    "content": "Hello, World!",
    "status": "sent",
    "created_at": "2023-10-01T12:00:00Z",
    "sent_at": "2023-10-01T12:02:00Z"
  }
]
Configuration
RabbitMQ: Default credentials (guest:guest). Update in settings.py if needed

Email/SMS Providers: Replace mock implementations in:

notifications/services/email.py (e.g., SendGrid)

notifications/services/sms.py (e.g., Twilio)

Project Structure
notification_service_django/
├── notification_service/       # Django project config
├── notifications/              # Main app
│   ├── models.py              # Notification model
│   ├── serializers.py         # DRF request/response schemas
│   ├── views.py               # API endpoints
│   ├── services/              # Email/SMS/RabbitMQ logic
│   ├── consumers.py           # Celery task definitions
├── manage.py                  # Django CLI
Assumptions
RabbitMQ runs locally with default settings

Email/SMS services are mocked (replace with real providers)

SQLite is the default DB (switch to PostgreSQL in production)

Troubleshooting
Celery not processing tasks?

Ensure RabbitMQ is running (rabbitmq-server)

Check Celery logs for errors

Django server not starting?

Run python manage.py check for configuration issues
