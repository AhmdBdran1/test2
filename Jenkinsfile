pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from your version control system (e.g., Git)
                git 'https://github.com/AhmdBdran1/test2.git'
            }
        }

        stage('Build') {
            steps {
                // Install dependencies and set up environment
                sh 'pip install -r requirements.txt'
            }
        }


        stage('Run') {
            steps {
                // Run the main file of your Python project
                sh 'python test/API_test/api_test_runner.py'
            }
        }
    }

    post {
        always {
            // Clean up, notify, or perform any other post-build actions here
        }
    }
}