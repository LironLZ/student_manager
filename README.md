# 🎓 Student Management System

This is a simple and user-friendly Student Management System built using Django and Bootstrap. The application allows you to manage students, create assignments for each student, and track assignment status (e.g., pending or completed).

## 🚀 Features

- Add, edit, and delete students
- Assign homework or tasks to each student
- Track assignment status and due dates
- Responsive interface using Bootstrap 5
- Secure login and logout functionality 

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, Bootstrap 5, JavaScript
- **Database:** SQLite (default with Django)


## 💻 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/lironlz/student-manager.git
   cd student-manager

2. Create a virtual environment (recommended)
It's highly recommended to use a virtual environment to isolate the project dependencies from your global Python environment.

For Windows:
Create a virtual environment in your project directory:


python -m venv venv

For macOS/Linux:
Create a virtual environment in your project directory:


python3 -m venv venv

3. Activate the virtual environment
After creating the virtual environment, activate it.

For Windows:

venv\Scripts\activate

For macOS/Linux:

source venv/bin/activate
You should now see (venv) in your terminal prompt, indicating that the virtual environment is active.

4. Install the required dependencies
Install all the necessary packages listed in the requirements.txt file:


pip install -r requirements.txt

5. Run the application
With the dependencies installed, you can now run the project locally. To start the Django development server:

6. Make migrations

py manage.py makemigrations

py manage.py migrate



## Creating a Teacher Account

To log in as a teacher, you must first create a teacher user via the django admin panel:

1. Create a superuser (admin account)

py manage.py createsuperuser

start the server(py manage.py runserver) and log into the admin panel at http://127.0.0.1:8000/admin

inside the admin dashboard add a new teacher entry and set their credentials.


Navigate to http://127.0.0.1:8000/ in your browser to see the application.