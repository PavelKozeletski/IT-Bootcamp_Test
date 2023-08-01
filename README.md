To run the project, follow these steps:

1) Install the necessary tools:
Install Python 3.9 or a later version on your computer if it's not already installed.
Make sure Django is installed. If not, run the command: pip install django.

2) Clone the project repository:
Clone the repository from GitHub to your computer.

3) Create a virtual environment (recommended):
Navigate to the root directory of the project.
Create a virtual environment using the command: python -m venv venv.
Activate the virtual environment:
On Windows: venv\Scripts\activate.
On macOS and Linux: source venv/bin/activate.

4) Install dependencies:
Make sure you are in the root directory of the project, where the requirements.txt file is located.
Install dependencies with the command: pip install -r requirements.txt.

5) Create the database and apply migrations:
Execute the command to create the database: python manage.py migrate.

6) Start the Django server:
Run the command: python manage.py runserver.
The server will be launched at http://127.0.0.1:8000/.

7) Check the application:
Open your web browser and go to http://127.0.0.1:8000/app/home/ to view the home page.

8) Shutdown:
To stop the Django server, press Ctrl + C in the command prompt where the server was launched.
