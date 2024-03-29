# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 80
EXPOSE 8080
EXPOSE 3306

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python3", "hello-world.py"]
