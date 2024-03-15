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
                   // Set PYTHONPATH and run the test suite
                withEnv(['PYTHONPATH=/usr/src/app:${PYTHONPATH}']) {
                    sh 'python3 -m test/UI_test/ui_test_runner' // Run the test suitee
                }
                sh 'python3 -m test/UI_test/ui_test_runner' // Run the test suite

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}