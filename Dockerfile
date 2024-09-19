FROM docker:17.12.0-ce as static-docker-source

FROM debian:stretch
ARG CLOUD_SDK_VERSION=232.0.0
ENV CLOUD_SDK_VERSION=$CLOUD_SDK_VERSION

COPY --from=static-docker-source /usr/local/bin/docker /usr/local/bin/docker
RUN apt-get -qqy update && apt-get install -qqy \
        curl \
        gcc \
        python-dev \
        python-setuptools \
        apt-transport-https \
        lsb-release \
        openssh-client \
        git \
        gnupg \
    && easy_install -U pip && \
    pip install -U crcmod   && \
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" > /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && \
    apt-get install -y google-cloud-sdk=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-app-engine-python=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-app-engine-python-extras=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-app-engine-java=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-app-engine-go=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-datalab=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-datastore-emulator=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-pubsub-emulator=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-bigtable-emulator=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-cbt=${CLOUD_SDK_VERSION}-0 \
        kubectl && \
    gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud config set metrics/environment github_docker_image && \
    gcloud --version && \
    docker --version && kubectl version --client
VOLUME ["/root/.config"]

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
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
