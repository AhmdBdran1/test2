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

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}