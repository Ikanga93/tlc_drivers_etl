# Use the official Python image from the Docker Hub
FROM python:latest

# Set the working directory in the container
WORKDIR /tlc_drivers_etl

# Enable venv
# ENV PATH="/tlc_drivers_etl/sodapy_nv/bin:$PATH"

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt 
# Copy the activate_env.sh script into the container
# COPY activate_env.sh /tlc_drivers_etl/activate_env.sh

# Create and activate the virtual environment in one step
# RUN python -m venv /tlc_drivers_etl/sodapy_env
# RUN echo "source /tlc_drivers_etl/sodapy_env/bin/activate" >> /tlc_drivers_etl/.bashrc
# RUN /tlc_drivers_etl/activate_env.sh  # Activate the virtual environment
# RUN pip install sodapy

# Copy the rest of the application code into the container
COPY . .

# Copy the entrypoint script into the container
COPY entrypoint.sh /tlc_drivers_etl/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /tlc_drivers_etl/entrypoint.sh

# Use the entrypoint script to run the ETL scsripts
ENTRYPOINT [ "/tlc_drivers_etl/entrypoint.sh" ]