FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

ENV PYTHONPATH="/usr/src/app:${PYTHONPATH}"

# Define environment variable
ENV PATH="/usr/src/app:${PATH}"


# Copy the requirements.txt file into the container at /usr/src/app/
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code into the container at /usr/src/app/
COPY . .


# Command to run your main script
CMD ["python", "test/API_test/api_test_runner.py"]
