pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'pip3 install -r requirements.txt' // Install required packages
                sh 'python3 test/UI_test/ui_test_runner.py' // Run the test suite

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}