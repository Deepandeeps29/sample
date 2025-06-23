pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --html=report.html'
            }
        }
    }

    post {
        always {
            emailext(
                subject: "🧪 Jenkins Test Report - ${BUILD_STATUS}",
                body: """Hi Team,<br><br>
                         Build #${BUILD_NUMBER} finished with status <b>${BUILD_STATUS}</b>.<br>
                         Please check the attached report.<br><br>
                         Thanks,<br>Jenkins""",
                to: 'deepanvinayagam1411@gmail.com',
                mimeType: 'text/html',
                attachmentsPattern: 'report.html'
            )
        }
    }
}
