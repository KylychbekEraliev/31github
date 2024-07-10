pipeline {
    agent { label 'test' }

    stages {
        stage('Connect to MongoDB and Update Documents') {
            steps {
                script {
                    // Define MongoDB URI
                    def mongoUri = "mongodb+srv://nur23anttech:admin@cluster0.b9lybep.mongodb.net/"

                    // Update command to execute
                    def updateCommand = """
                    db.studentInfo.updateMany(
                        {},
                        {
                            \$set: {
                                'attendance.December': '95%',
                                'attendance.March': '96%',
                                'attendance.April': '98%'
                            }
                        }
                    )
                    """

                    // Connect to MongoDB and execute the update command
                    echo "Executing update command..."
                    sh """
                    mongosh "${mongoUri}" --eval '${updateCommand}'
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Finished MongoDB update stage.'
        }

        success {
            echo 'Successfully connected to MongoDB and updated documents!'
        }

        failure {
            echo 'Failed to connect to MongoDB or update documents.'
        }
    }
}

