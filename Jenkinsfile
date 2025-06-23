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
            echo 'Sending test report email...'
            emailext (
                subject: "🧪 Jenkins Test Report - Build #${BUILD_NUMBER}",
                body: """Hi Team,<br><br>
                         Test execution is complete.<br>
                         Please find the attached test report.<br><br>
                         Regards,<br>Jenkins""",
                from: 'deepanvinayagam1411@gmail.com',
                to: 'deepanvinayagam1411@gmail.com',
                attachmentsPattern: '**/report.html',
                mimeType: 'text/html'
            )
        }
    }
}
