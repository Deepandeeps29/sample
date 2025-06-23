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
                    writeFile file: 'report.html', text: '<html><body><h1>No report generated. Tests might have crashed early.</h1></body></html>'
                }
            }

            emailext (
                subject: "🧪 Jenkins Test Report",
                body: """<html>
                    <p>Hi Team,</p>
                    <p>Jenkins build has completed. See attached report.</p>
                    <p>Regards,<br>Jenkins</p>
                    </html>""",
                mimeType: 'text/html',
                to: "deepanvinayagam1411@gmail.com",
                attachmentsPattern: 'report.html'
            )
        }
    }
}
