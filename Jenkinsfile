pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
