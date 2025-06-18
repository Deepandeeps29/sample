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
                    git config --global user.email "deepanvinayagam2912@gmail.com"
                    git config --global user.name "Deepandeeps29"
                    git add report.html
                    git commit -m "Updated test report with radio page"
                    git push origin main
                '''
            }
        }
    }
}
