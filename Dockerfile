# Use official Python 3.10 base image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy all project files to working directory
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 for Django development server
EXPOSE 8000

# Run migrations and start Django development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
