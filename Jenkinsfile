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
                sh 'python3 -m unittest test/API_test/login_test.py' // Run your unit test
                sh 'python3 -m unittest test/UI_test/test_login_page.py' // Run UI testss
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}