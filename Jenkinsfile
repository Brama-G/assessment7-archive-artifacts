pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Brama-G/assessment7-archive-artifacts.git'
            }
        }

        stage('Generate Report') {
            steps {
                sh 'python3 generate_report.py'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.txt', fingerprint: true
            }
        }
    }
}
