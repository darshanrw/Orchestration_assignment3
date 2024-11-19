# Using base Python image for optimized performance
FROM python:3.9-alpine

# Install necessary dependencies
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir flask \
    && apk del .build-deps

# Setting the working directory
WORKDIR /app

# Copy application files
COPY app.py config.txt ./

# Installing Flask
RUN pip install Flask

# Expose application's port
EXPOSE 3000

# Command to run the application
CMD ["python", "app.py"]
