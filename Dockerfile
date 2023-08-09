# FROM python:3.10-alpine  –– having too many issues to install MySQL
FROM ubuntu:22.04

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE stock_system.settings

# Set the working directory inside the container
WORKDIR /app

# Install required packages and link python3/python
RUN apt update && \
    apt install -y python3-dev libmariadb-dev-compat build-essential mysql-client python3-pip && \
    ln -sf python3 /usr/bin/python



# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy initializaiton script
COPY ./runserver.sh /app/
RUN chmod +x ./runserver.sh

# Copy the rest of the application code
COPY . /app/

# Expose the port the application runs on
EXPOSE 8000
