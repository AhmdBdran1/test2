# Use Python 3.8 as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update && apt-get install -y \
    unzip \
    wget \
    gnupg \
    libnss3 \
    && rm -rf /var/lib/apt/lists/*

# Download and install Chrome
RUN wget -q -O chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./chrome.deb \
    && rm ./chrome.deb

# Download and install ChromeDriver
RUN LATEST_CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE") \
    && wget -q "https://chromedriver.storage.googleapis.com/${LATEST_CHROMEDRIVER_VERSION}/chromedriver_linux64.zip" -O chromedriver.zip \
    && unzip chromedriver.zip \
    && mv chromedriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && rm chromedriver.zip

# Print ChromeDriver version for verification
RUN chromedriver --version

# Print Chrome version for verification
RUN google-chrome --version

# Copy the requirements.txt file into the container at /usr/src/app/
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code into the container at /usr/src/app/
COPY . .

# Define environment variable
ENV PATH="/usr/src/app:${PATH}"

# Command to run your tests
CMD ["python", "-m", "unittest", "test.UI_test.test_login_page"]
