pipeline {
    agent any

    environment {
        DOCKER_HOST_IP = "13.201.166.12"          // Your Docker Host EC2 IP
        DOCKER_USER = "ubuntu"                   // Default EC2 user
        DOCKER_APP_DIR = "stock-app"             // Your app folder on EC2
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/shrutikhannukar/Stock-main.git'  // Full GitHub repo URL
            }
        }

        stage('Copy Code to Docker Host') {
            steps {
                sh """
                    ssh -o StrictHostKeyChecking=no ${DOCKER_USER}@${DOCKER_HOST_IP} 'mkdir -p ${DOCKER_APP_DIR}'
                    scp -o StrictHostKeyChecking=no -r . ${DOCKER_USER}@${DOCKER_HOST_IP}:${DOCKER_APP_DIR}
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    ssh -o StrictHostKeyChecking=no ${DOCKER_USER}@${DOCKER_HOST_IP} '
                        cd ${DOCKER_APP_DIR} &&
                        docker build -t django-stock-app .
                    '
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                sh """
                    ssh ${DOCKER_USER}@${DOCKER_HOST_IP} '
                        docker rm -f django-stock-container || true &&
                        docker run -d -p 8000:8000 --name django-stock-container django-stock-app
                    '
                """
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful! Visit http://${DOCKER_HOST_IP}:8000"
        }
        failure {
            echo "❌ Deployment failed. Check Jenkins logs."
        }
    }
}
