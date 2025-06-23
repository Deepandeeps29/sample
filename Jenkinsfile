pipeline {
    agent any

    environment {
//         EMAIL = 'your-email@gmail.com'
        EMAIL = 'deepanvinayagam1411@gmail.com'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --html=report.html || exit 0'
            }
        }

        stage('Push Report to GitHub') {
            steps {
                bat '''
                    git config user.email "deepanvinayagam2912@gmail.com.com"
                    git config user.name "Deepandeeps29"
                    git add report.html
                    git commit -m "Update test report" || echo "No changes"
                    git push origin HEAD:main
                '''
            }
        }
    }

    post {
        always {
            script {
                if (!fileExists('report.html')) {
                    writeFile file: 'report.html', text: '<html><body><h2>No Report Generated</h2></body></html>'
                }
            }

            emailext (
                subject: "🧪 Jenkins Test Report",
                body: """<html>
                    <p>Hi Team,</p>
                    <p>The Jenkins test build has completed.</p>
                    <p>See the attached report.</p>
                    <p>Regards,<br>Jenkins</p>
                </html>""",
                mimeType: 'text/html',
//                 to: "your-team-email@gmail.com",
                to: "deepanvinayagam1411@gmail.com",
//                 from: "your-email@gmail.com",
                from: "deepanvinayagam2912@gmail.com",
                attachmentsPattern: 'report.html'
            )
        }
    }
}
