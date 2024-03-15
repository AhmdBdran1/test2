pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pip3 install -r requirements.txt' // Install required packages

            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Add the parent directory of the 'test' module to the Python path
                sh "PYTHONPATH=${PWD}/test/UI_test python3 test/UI_test/ui_test_runner.py"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}