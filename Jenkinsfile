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

        stage('Push Report to GitHub') {
            steps {
                bat '''
                    git config user.email "deepanvinayagam2912@gmail.com"
                    git config user.name "Deepandeeps29"
                    git add report.html
                    git commit -m "Update test report" || echo "No changes to commit"
                    git push origin HEAD:main
                '''
            }
        }
    }

    post {
    always {
        emailext (
            subject: "🧪 Jenkins Test Report - ${BUILD_STATUS} - Build #${BUILD_NUMBER}",
            body: """Hi Team,<br><br>
                     The test job <b>${JOB_NAME}</b> completed with status: <b>${BUILD_STATUS}</b>.<br>
                     Please find the test report attached.<br><br>
                     <b>Report:</b> <a href="${BUILD_URL}artifact/report.html">Click here</a><br><br>
                     Regards,<br>Jenkins""",
            from: 'deepanvinayagam2912@gmail.com',
            to: 'deepanvinayagam1411@gmail.com',
            attachmentsPattern: 'report.html',
            mimeType: 'text/html'
        )
    }
}

}
