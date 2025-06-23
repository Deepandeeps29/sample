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
                    git config user.email "deepanvinayagam1411@gmail.com"
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
        script {
            if (!fileExists('report.html')) {
                echo "⚠️ report.html not found, writing fallback..."
                writeFile file: 'report.html', text: '<html><body><h1>No report generated.</h1></body></html>'
            } else {
                echo "✅ report.html found"
            }
        }

        emailext(
            subject: "🧪 Jenkins Test Report",
            mimeType: 'text/html',
            to: "deepanvinayagam1411@gmail.com",
            from: "deepanvinayagam1411@gmail.com",
            attachmentsPattern: '**/report.html',
            body: """<html>
                <p>Hi Team,</p>
                <p>The Jenkins build has completed. Please find the attached test report.</p>
                <p>Regards,<br>Jenkins</p>
            </html>"""
        )
    }
}

}
