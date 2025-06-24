pipeline {
    agent any

    environment {
        REPORT_FILE = 'report.html'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-token',
                    url: 'https://github.com/Deepandeeps29/Sample.git',
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

        stage('Archive and Email Report') {
            steps {
                script {
                    archiveArtifacts artifacts: "${REPORT_FILE}", onlyIfSuccessful: true
                    emailext(
                        subject: "🧪 Selenium Test Report - Build #${BUILD_NUMBER}",
                        body: """
                            <p>Hello Team,</p>
                            <p>Please find the attached <b>HTML Test Report</b> for Jenkins Build #${BUILD_NUMBER}.</p>
                            <p>Regards,<br>Jenkins</p>
                        """,
                        to: 'deepanvinayagam1411@gmail.com',
                        from: 'deepanvinayagam1411@gmail.com',
                        attachLog: false,
                        attachmentsPattern: "${REPORT_FILE}"
                    )
                }
            }
        }
    }

    post {
        always {
            echo "✅ Pipeline finished. Report generated and email sent."
        }
    }
}
