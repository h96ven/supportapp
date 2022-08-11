# supportapp

It's a backend REST API for operating of a support team service. A user creates a topic with his question. The support team member or admin can see it and answer it. The user can see the reply and reply again, the admin can answer again. And so on. The admin can change the status of the topic. When the status changes, the user receives an email notification. In order to see anything or to create a topic a user must by authenticated. The user only sees the list of topics he created and the replies to them. 

## Technologies:
Django Rest Framework, JWT-authorization, Djoser, PostgreSQL, Docker, Celery, Redis etc.

## Code-style: 
flake8, isort.

## Used techniques:
Class-based views, Mixins, Nested routers, Signals etc.

## How to assemble
One can assemble this project using Docker-compose. Python 3.10 was used. If you have problems installing pip and pipenv for Python 3.10 on WSL Ubuntu, you can manually set the version of Python to 3.8 in Dockerfile and Pipfile. If you have problems installing psycopg2, you can replace psycopg2 for psycopg2-binary in Pipfile.

## To install:

Make sure pip and pipenv are installed.
Install all project dependencies by running: pipenv install.

The web server can be accessed via address: localhost:8000

To access any data, one must be authenticated.

## Registering and logging in 

In order to register a user, fill the forms here: http://localhost:8000/auth/users/ 

In order to log in, fill the forms here: http://localhost:8000/auth/jwt/create 

To emulate that the user is logged in, use the access token in ModHeader Chrome extension (for example): select 'Authorization', in the token field please type "JWT [your access token]" (use your token code instead of '[your access token]' words).
  
Now you can access the list of created topics (if it's not empty): http://localhost:8000/support/tickets/

## Using the supportapp API

You can create a topic to ask questions for the support team to answer to. In order to do that, fill the ‘topic’ and ‘message’ fields. Press the POST button.
  
After the support team sends a reply to the topic, you can see it in the nested “replies” field at /support/tickets/ or in a detailed view, for example, /support/tickets/9/ .
  
In order to create a new reply, you must access the list of replies by using a nested url. For example: /support/tickets/9/replies/ . Where 9 is a ticket id. Now you can type a reply message by filling the ‘text’ field below and pressing the POST button.
  
You can also access a specific reply by using a nested url. For example: /support/tickets/9/replies/27 . Where 9 is a ticket id and 27 is a reply id.
  
Note: not all ticket and reply ids are accessible by the current user, because a user only can see the topic he created. He cannot see other people’s topics, ticket and reply ids.
  
You can use an empty database and fill it yourself to try this app’s functionality.
  
Or you can populate it with my database.

## Populating the database
  
For that, you have auth_populate_database.json and support_populate_database.json files in the db_populate directory of this project.
  
To do that, use this command: docker-compose run web python manage.py loaddata [name of the file].json 
  
In order not to get any errors while running the above command, first you have to run migrations for the new database: docker-compose run web python manage.py migrate
  
To remove the rest of errors, you must have the same quantity of users as my database has.
  
To create the admin user, run: docker-compose run web python manage.py createsuperuser
  
Now you can access the admin panel: http://localhost:8000/admin/
  
You can create regular users at: http://localhost:8000/auth/users/
  
## Trying the functionality
  
Now, try the functionality. Create a topic, write a reply for it as the admin. Read the reply as a user and create a new reply. Change the status to Solved or Frozen as the admin. 
  
When you are done, don’t forget to untick Authentication in ModHeader Chrome extension. Otherwise, all your login information on all other websites would be messed up and you won’t be able to login there.

