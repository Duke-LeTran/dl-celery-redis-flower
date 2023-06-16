FROM python:3.9

WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5555

# Set the entry point command to run the Flask app
CMD ["celery", "-A", "app.celery", "--loglevel=info"]