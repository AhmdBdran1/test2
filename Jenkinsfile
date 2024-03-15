pipeline {
    agent any
    environment {
        VIRTUAL_ENV = "${WORKSPACE}/venv"
        PATH = "${VIRTUAL_ENV}/bin:${PATH}"
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python3 -m venv venv' // Create a virtual environment
                sh 'source venv/bin/activate && pip3 install -r requirements.txt' // Activate virtual environment and install required packages
            }
        }

        stage('Start Selenium Servers') {
            steps {
                echo 'Starting Selenium Hub...'
                sh 'java -jar selenium-server-4.17.0.jar hub &'

                echo 'Starting Selenium Node...'
                sh 'java -jar selenium-server-4.17.0.jar node &'

                // Wait for a moment to allow servers to start
                sleep 30
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'source venv/bin/activate && python3 -m test.API_test.api_test_runner' // Activate virtual environment and run tests
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}
