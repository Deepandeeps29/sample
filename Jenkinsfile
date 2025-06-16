pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'git@github.com:Deepandeeps29/CICD_1.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                sh 'pytest --html=report.html --self-contained-html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML (target: [
                    reportName : 'Pytest HTML Report',
                    reportDir: '.',
                    reportFiles: 'report.html',
                    alwaysLinkToLastBuild: true,
                    keepAll: true
                ])
            }
        }
    }
}
