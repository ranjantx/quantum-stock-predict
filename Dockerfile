# Use a slim Python 3.11 image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements to cache dependencies early
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the full application code
COPY ./app ./app

# Expose FastAPI default port
EXPOSE 8000

# Set the working directory for uvicorn
WORKDIR /app/app

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
