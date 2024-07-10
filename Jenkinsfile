pipeline {
    agent { label 'test' }

    stages {
        stage('Connect to MongoDB and Load Command') {
            steps {
                script {
                    // Connect to MongoDB and load the command
                    sh '''
                    mongosh "mongodb+srv://nur23anttech:admin@cluster0.b9lybep.mongodb.net/" --eval "load('https://github.com/KylychbekEraliev/31github/blob/main/studentInfo.js')"
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Finished MongoDB connection stage.'
        }

        success {
            echo 'Successfully connected to MongoDB and executed the command!'
        }

        failure {
            echo 'Failed to connect to MongoDB or execute the command.'
        }
    }
}
