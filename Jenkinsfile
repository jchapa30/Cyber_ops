pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from GitHub repository
                git branch: 'main', url: 'https://github.com/jchapa30/Cyber_ops.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the specified Dockerfile
                    docker.build('cybersecurity-logs', '-f Dockerfile .')
                }
            }
        }
        stage('Run Log Generator') {
            steps {
                script {
                    // Run the Python script inside the Docker container
                    docker.image('cybersecurity-logs').inside {
                        sh 'python log_generator.py'
                    }
                }
            }
        }
    }
    
    post {
        always {
            // This will run regardless of success or failure
            echo 'Job Completed!'
        }
    }
}
