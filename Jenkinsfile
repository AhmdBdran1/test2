pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pip3 install -r requirements.txt' // Install required packages

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

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}