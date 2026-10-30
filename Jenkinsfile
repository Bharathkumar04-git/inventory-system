pipeline {
    agent any

    environment {
        IMAGE_NAME = 'bhxrxth0409/inventory-system'
        IMAGE_TAG = 'v2'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Getting code from GitHub'
                checkout scm
            }
        }

        stage('Install') {
            steps {
                echo 'Installing requirements'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests'
                bat 'python -m pytest'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building docker image'
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage('Docker Push') {
            steps {
                echo 'Pushing image to DockerHub'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat 'echo %DOCKER_PASS%| docker login -u %DOCKER_USER% --password-stdin'
                    bat 'docker push %IMAGE_NAME%:%IMAGE_TAG%'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully'
        }
        failure {
            echo 'Pipeline failed, check the console output'
        }
    }
}