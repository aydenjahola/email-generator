# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 4000 available to the world outside this container
EXPOSE 4000

# Run app.py when the container launches
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:4000"]
