# docker build -t quickstart .
# docker run -p 5000:5000 quickstart

# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining app files into the container
COPY . .

# Set the environment variable for the OpenAI API key
# ENV OPENAI_API_KEY <your_openai_api_key>

# Expose the port that Flask app listens on
EXPOSE 5000

# Set the entrypoint command to start the Flask app
CMD ["python", "app.py"]