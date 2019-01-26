FROM python:3.4

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /QuMedRepo

# Set the working directory to /qumed
WORKDIR /QuMedRepo

# Copy and install requirements
COPY requirements.txt /QuMedRepo/
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /qumed
COPY . /QuMedRepo/

# Make port 8000 available to the world outside this container
EXPOSE 8000