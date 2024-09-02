# app/Dockerfile

# This Dockerfile uses python:3.9-slim, which is a lightweight implementation of the Python image. This’ll reduce image size.
FROM python:3.9-slim

# Sets the working directory inside the container to `/app`. It’s unlikely that you’ll need to adjust this.
WORKDIR /app

# Installs several packages and cleans up the apt cache. In some cases some of these packages might not be needed to run a Streamlit container.
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copies everything from the project's root directory to the working directory of the container.
# Make sure there's a .dockerignore file in your root folder that lists all files that contains credentials, like a .env file.
COPY . .

# Installs Python packages listed in the requirements.txt.
RUN pip3 install -r requirements.txt

# Exposes port 8501 for external access. This is typical for Streamlit applications.
EXPOSE 8501

# Checks the health of the Streamlit server.
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Defines how to start the application. In this case the Streamlit application’s filename is st.py, so feel free to adjust it to your app’s name.
ENTRYPOINT ["streamlit", "run", "st.py", "--server.port=8501", "--server.address=0.0.0.0"]
