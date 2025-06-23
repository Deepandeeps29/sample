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
            // ✅ Debug to confirm file exists and has content
            bat 'echo ===== File Listing ====='
            bat 'dir'
            bat 'echo ===== Report Preview ====='
            bat 'type report.html'
            bat 'if exist report.html (echo ✅ report.html FOUND) else (echo ❌ report.html NOT FOUND)'

            // ✅ Send email with report.html attached
            emailext (
                subject: "🧪 Jenkins Test Report",
                body: '''
Hi Team,<br><br>
The automated test run has completed.<br>
Please find the attached test report below.<br><br>
Regards,<br>Jenkins
''',
                mimeType: 'text/html',
                to: 'deepanvinayagam2912@gmail.com',
                attachmentsPattern: '**/report.html'
            )
        }
    }
}
