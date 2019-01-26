# QuMed

Setup on development environment
Create a virtual environment QuMedRepo with virtualenvwrapper, using python3 as the default python exe: mkvirtualenv --python=/usr/bin/python3 QuMedRepo

Clone the repo: git clone  https://github.com/Petitpapa89/QuMedRepo.git. This uses SSH, read this to setup SSH on your system: https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html

Alternatively you can use HTTPS: git clone https://github.com/Petitpapa89/QuMedRepo.git

Install Docker (https://www.docker.com/get-started)

To start the server, in the src (/QuMedRepo/Dev/QuMedRepo/src) directory (the folder named 'src' that has the files Dockerfile, docker-compose.yml in it), run the command docker-compose up. Go to localhost:8000 or 0.0.0.0:8000 in your browser to view the app.

You may need to run docker-compose up --build first, before running docker-compose up.

To shut down the server, in the root directory either run the command docker-compose down or use the keyboard shortcut CTRL+C

Structure
The Repo has a main branch master. All other branches checkout from it.