FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install gunicorn

# Expose the application port
EXPOSE 80

# Run the app
CMD ["python", "app.py", "--host=0.0.0.0", "--port=80"]
