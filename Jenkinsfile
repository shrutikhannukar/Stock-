pipeline {
    agent any

    environment {
        DOCKER_HOST_IP = "13.201.166.12"        // Replace with your EC2 public IP
        DOCKER_USER = "ubuntu"                  // Default EC2 user (Ubuntu)
        DOCKER_APP_DIR = "stock-app"            // Folder on EC2 where code will be copied
    }

    stages {
       stage('Clone Repository') {
    steps {
        git branch: 'main', url: 'https://github.com/shrutikhannukar/Stock-.git'
    }
}


        stage('Copy Code to EC2') {
            steps {
                // Create directory and copy project to EC2
                sh """
                    ssh -o StrictHostKeyChecking=no ${DOCKER_USER}@${DOCKER_HOST_IP} 'mkdir -p ~/${DOCKER_APP_DIR}'
                    scp -o StrictHostKeyChecking=no -r * ${DOCKER_USER}@${DOCKER_HOST_IP}:~/${DOCKER_APP_DIR}
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                // SSH into EC2 and build Docker image
                sh """
                    ssh -o StrictHostKeyChecking=no ${DOCKER_USER}@${DOCKER_HOST_IP} '
                        cd ~/${DOCKER_APP_DIR} &&
                        docker build -t django-stock-app .
                    '
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                // Remove old container if exists and run new container
                sh """
                    ssh -o StrictHostKeyChecking=no ${DOCKER_USER}@${DOCKER_HOST_IP} '
                        docker rm -f django-stock-container || true &&
                        docker run -d -p 8000:8000 --name django-stock-container django-stock-app
                    '
                """
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful! Access your app at http://${DOCKER_HOST_IP}:8000"
        }
        failure {
            echo "❌ Deployment failed. Check the Jenkins console output."
        }
    }
}
