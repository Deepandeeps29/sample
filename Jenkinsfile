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
        always {
            emailext (
                subject: "🧪 Test Report - Pytest Results",
                body: """Hello,<br><br>The test execution has completed.<br>Please find the attached report.<br><br>Regards,<br>Jenkins""",
                mimeType: 'text/html',
                to: 'deepanvinayagam1411@gmail.com',
                attachmentsPattern: 'report.html'
            )
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }

}
