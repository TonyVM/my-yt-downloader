pipeline {
    agent any
    environment {
        PATH = "/opt/homebrew/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check ffmpeg') {
            steps {
                sh 'ffmpeg -version'
            }
        }

        stage('Set up Python') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh '. .venv/bin/activate && pytest --junitxml=tests/results.xml'
            }
        }
    }

    post {
        always {
            junit 'tests/results.xml'
        }
        failure {
            echo 'Tests failed. Please check the logs.'
        }
        success {
            echo 'All tests passed!'
        }
    }
}
