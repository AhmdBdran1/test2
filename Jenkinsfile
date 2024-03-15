pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                // Add any build steps here if necessary
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Install required Python packages
                script {
                    sh 'pip3 install -r requirements.txt'
                }
                // Run the test script
                script {
                    sh "python3 ${PWD}/test/UI_test/ui_test_runner.py"
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Add deployment steps here if necessary
            }
        }
    }
}
