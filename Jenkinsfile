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
                sh 'python3 -m test.UI_test.ui_test_runner' // Run the test suite

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}