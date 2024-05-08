# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the Docker image
WORKDIR /app

# Copy requirements.txt into the image
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application into the image
COPY . .

# Make port 5000 available to the outside of the Docker container
EXPOSE 5000

# Define the command to run the application
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]