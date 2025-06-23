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
                    git commit -m "Updated test report with radio page" || echo "No changes to commit"
                    git push origin HEAD:main
                '''
            }
        }
    }

    post {
        always {
            emailext (
                subject: "🧪 Test Report - Jenkins CI Pipeline",
                body: '''Hi Team,<br><br>
                         Test execution is complete. Please find the attached HTML report.<br><br>
                         Regards,<br>Jenkins''',
                to: 'deepanvinayagam2912@gmail.com',
                attachmentsPattern: 'C:\ProgramData\Jenkins\.jenkins\workspace\23062025\report.html
',
                mimeType: 'text/html'
            )
        }
    }
}
