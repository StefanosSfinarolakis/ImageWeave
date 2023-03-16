
# Makefile for setting up and managing virtual environment, and running a Django application using Docker and Docker Compose

# Set up virtual environment
venv:
	@echo "Creating virtual environment..."
	python3 -m venv venv
	@echo "Virtual environment created."

# Activate virtual environment
activate:
	@echo "Activating virtual environment..."
	. venv/bin/activate
	@echo "Virtual environment activated."

# Install dependencies from requirements.txt
install:
	@echo "Installing dependencies from requirements.txt..."
	venv/bin/pip install -r requirements.txt
	@echo "Dependencies installed."

# Add dependencies to requirements.txt
add:
	@echo "Enter package name (e.g. django==3.2.9) or CTRL+C to exit:"
	@read package; \
	venv/bin/pip install $$package; \
	venv/bin/pip freeze > requirements.txt; \
	@echo "Package added to requirements.txt."

# Update requirements.txt with latest package versions
update:
	@echo "Updating requirements.txt..."
	venv/bin/pip freeze --exclude-editable > requirements.txt
	@echo "Requirements updated."

# Help command
help:
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@echo "  venv          Set up virtual environment"
	@echo "  activate      Activate virtual environment"
	@echo "  install       Install dependencies from requirements.txt"
	@echo "  add           Add a package to requirements.txt"
	@echo "  update        Update requirements.txt with latest package versions"
	@echo "  clean         Delete virtual environment"
	@echo "  build         Build the Docker image for the Django application"
	@echo "  up            Start the Docker containers for the Django application"
	@echo "  down          Stop the Docker containers for the Django application"
	@echo "  restart       Rebuild and start the Docker containers for the Django application"
	@echo "  logs          View the logs for the Docker containers for the Django application"
	@echo "  manage        Run Django management commands inside the Docker container"

# Clean virtual environment
clean:
	@echo "Deleting virtual environment..."
	rm -rf venv
	@echo "Virtual environment deleted."

# Build the Docker image for the Django application
build:
	@echo "Building Docker image for the Django application..."
	docker build -t <image_name> .
	@echo "Docker image built."

# Start the Docker containers for the Django application
up:
	@echo "Starting Docker containers for the Django application..."
	docker-compose up -d
	@echo "Docker containers started."

# Stop the Docker containers for the Django application
down:
	@echo "Stopping Docker containers for the Django application..."
	docker-compose down
	@echo "Docker containers stopped."

# Rebuild and start the Docker containers for the Django application
restart:
	@echo "Rebuilding and starting Docker containers for the Django application..."
	docker-compose down
	docker-compose up -d
	@echo "Docker containers rebuilt and started."

# View the logs for the Docker containers for the Django application
logs:
	@echo "Viewing logs for Docker containers for the Django application..."
	docker-compose logs -f
	@echo "Logs viewed."

# Run Django management commands inside the Docker container
manage:
	@echo "Running Django management command inside Docker container..."
	docker-compose run web python manage.py $(cmd)
	
