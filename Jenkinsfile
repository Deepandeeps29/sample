pipeline {
    agent any

    environment {
        REPORT_FILE = "report.html"
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-token', url: 'https://github.com/Deepandeeps29/sample.git', branch: 'main'
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --html=report.html --self-contained-html'
            }
        }
    }

    post {
        failure {
            emailext (
                subject: "Test Failed - Pytest Report",
                body: "Hello,<br><br>Pytest automation test failed. Find the attached HTML report.<br><br>Regards,<br>Jenkins",
                mimeType: 'text/html',
                to: 'deepanvinayagam1411@gmail.com',
                attachmentsPattern: 'report.html'
            )
        }
        success {
            echo "Tests passed, no email sent."
        }
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}
