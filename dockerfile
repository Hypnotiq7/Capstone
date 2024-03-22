# Using an official python runtime as a parent time
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Set the working directory in the container
COPY . /usr/src/app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variables
ENV DJANGO_SETTINGS_MODULE=bandsite.settings

# Run app.py when the container lauches
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]