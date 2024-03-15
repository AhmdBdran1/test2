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
                sh 'pip install -r requirements.txt' // Install required packages
                sh "python ${PWD}/test/UI_test/ui_test_runner.py"


            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}