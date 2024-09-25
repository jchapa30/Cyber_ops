pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/jchapa30/Cyber_ops.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('cybersecurity-logs', '-f Dockerfile .')
                }
            }
        }
        stage('Run Log Generator') {
            steps {
                script {
                    docker.image('cybersecurity-logs').inside {
                        sh 'python log_generator.py'
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Job Completed!'
        }
    }
}
