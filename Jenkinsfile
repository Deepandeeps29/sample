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
                    git commit -m "Updated test report" || echo "No changes"
                    git push origin HEAD:main
                '''
            }
        }
    }

    post {
        always {
            bat 'if exist report.html (echo ✅ report.html found) else (echo ❌ report.html NOT found)'
            emailext (
                subject: "🧪 Test Report - Jenkins",
                body: '''
Hi Team,<br><br>
The test run is complete. Please find the attached report.<br><br>
Regards,<br>Jenkins
''',
                to: 'deepanvinayagam2912@gmail.com',
                attachmentsPattern: '**/report.html',
                mimeType: 'text/html'
            )
        }
    }
}
