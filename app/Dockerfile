FROM public.ecr.aws/docker/library/python:3.12-slim

# Sets the working directory within the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Exposes port 80
EXPOSE 80

# Command to start the application
CMD ["python", "app.py"]
