# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable for OpenWeatherMap API key
ENV WEATHER_API_KEY=your_openweathermap_api_key

# Run the Python script when the container launches
CMD ["python", "scripts/collect_data.py"]
