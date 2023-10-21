#!/bin/bash

# Pull the latest changes from the Git repository
echo "Pulling the latest changes from the Git repository..."
git pull

# Define the name of the Docker image
IMAGE_NAME="email-generator"

# Build the Docker container
echo "Building the Docker container..."
docker build -t $IMAGE_NAME .

# Check if the build was successful
if [ $? -eq 0 ]; then
    echo "Docker container built successfully."

    # Run docker-compose up -d
    echo "Running docker-compose up -d..."
    docker-compose up -d --force-recreate

    # Check if docker-compose started successfully
    if [ $? -eq 0 ]; then
        echo "docker-compose up -d completed successfully."

        # Add a sleep delay (5 seconds) before pruning unused Docker images
        echo "Sleeping for 5 seconds..."
        sleep 15

        # Prune unused Docker images
        echo "Removing unused Docker images..."
        docker image prune -f

        echo "Unused Docker images removed."
    else
        echo "Error: docker-compose up -d failed."
    fi
else
    echo "Error: Docker container build failed."
fi
