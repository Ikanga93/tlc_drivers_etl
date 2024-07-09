# Use the official Python image from the Docker Hub
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /tlc_drivers_etl

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install sodapy  

# Copy the rest of the application code into the container
COPY . .

# Copy the entrypoint script into the container
COPY entrypoint.sh /tlc_drivers_etl/tlc_drivers_etl/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /tlc_drivers_etl/entrypoint.sh

# Use the entrypoint script to run the ETL scsripts
ENTRYPOINT [ "/tlc_drivers_etl/entrypoint.sh" ]