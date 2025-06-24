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

        stage('Send Email') {
            steps {
                emailext (
                    subject: "🧪 Test Report - Jenkins Build #${BUILD_NUMBER}",
                    body: "Hello Team,<br><br>Please find the attached <b>HTML Test Report</b> for Jenkins Build #${BUILD_NUMBER}.<br><br>Regards,<br>Jenkins",
                    to: 'deepanvinayagam2912@gmail.com',
                    from: 'deepanvinayagam2912@gmail.com',
                    attachLog: false,
                    attachmentsPattern: 'report.html'
                )
            }
        }
    }
}
