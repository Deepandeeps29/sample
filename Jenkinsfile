pipeline {
    agent any

    environment {
        REPORT_FILE = 'report.html'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-token',
                    url: 'https://github.com/Deepandeeps29/Automation_Pratice_Site.git',
                    branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat "pytest tests/test_login.py --html=${REPORT_FILE} --self-contained-html"
            }
        }

        stage('Archive and Publish Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', onlyIfSuccessful: true
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Selenium Test Report'
                ])
            }
        }

        stage('Send Email') {
            steps {
                emailext (
                    subject: "🧪 Test Report - Jenkins Build #${BUILD_NUMBER}",
                    body: """
                        <p>Hello Team,</p>
                        <p>Please find the attached <b>HTML Test Report</b> for Jenkins Build #${BUILD_NUMBER}.</p>
                        <p><a href="${BUILD_URL}HTML_Report">Click here to view the report</a></p>
                        <br>
                        <p>Regards,<br>Jenkins</p>
                    """,
                    mimeType: 'text/html',
                    to: 'deepanvinayagam2912@gmail.com',
                    from: 'deepanvinayagam2912@gmail.com',
                    attachLog: false,
                    attachmentsPattern: 'report.html'
                )
            }
        }
    }

    post {
        always {
            echo "📨 Pipeline finished. HTML report sent via Jenkins email."
        }
    }
}
