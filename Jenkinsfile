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
        emailext (
            subject: "🧪 Jenkins Test Report",
            body: "Hi Team,<br><br>Test completed. Please find the report attached.<br><br>Regards,<br>Jenkins",
            from: "deepanvinayagam1411@gmail.com",          // ✅ Must match SMTP config
            to: "deepanvinayagam1411@gmail.com",
            attachmentsPattern: '**/report.html',
            mimeType: 'text/html'
        )
    }
}

}
