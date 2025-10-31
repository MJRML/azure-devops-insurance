# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model and FastAPI app
COPY models/ ./models/
COPY src/deployment/app_fastapi.py ./deployment/

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI server
CMD ["uvicorn", "deployment.app_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
