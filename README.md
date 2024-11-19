# INFO8995 - Assignment 3 - 8934575

## Files submitted under assignment 3
- nginx.conf # Contains the configuration for routing requests to the web service. 
- app.py # The main Flask application that serves a message from config.txt.
- config.txt # A text file containing the message served by the web service.
- Dockerfile # Sets up the Python environment for the Flask application and its dependencies. 
- docker-compose.yml # Orchestrates the deployment of the web service and NGINX containers. 
- README.md # Provides documentation and instructions for the project setup and usage.

## Components

- Web Service:
  - A Flask application that responds with a message defined in config.txt.
  - Exposed on port 3000.

- Load Balancer:
  - NGINX server configured to route traffic to the web service.
  - Listens on port 81.

## Prerequisites

- Ensure you have Docker and Docker Compose installed on your machine.

## Setup and Usage

 - Clone the Repository  
   ```bash
   git clone https://github.com/darshanrw/Orchestration_assignment3.git
## Starting the Services

- Run docker-compose up --build

## Accessing the Web Service on below address
- http://localhost:81

## This will display the message from config.txt:
- Assignment 3 is successfully completed with all the best practices implied!!!!!!

## Stopping the Services
- Run docker-compose down


