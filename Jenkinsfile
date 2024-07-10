pipeline {
    agent { label 'test' }

    environment {
        MONGODB_URI = credentials('mongo')
    }

    stages {
        stage('Connect to MongoDB and Load Scripts') {
            steps {
                script {
                    // Use environment variable MONGODB_URI
                    echo "Connecting to MongoDB using URI: ${MONGODB_URI}"
                    sh """
                    mongosh "${MONGODB_URI}" --eval "load('${studentInfoScript}'); load('${updateScript}')"
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Finished MongoDB script execution.'
        }

        success {
            echo 'Successfully executed MongoDB scripts!'
        }

        failure {
            echo 'Failed to execute MongoDB scripts.'
        }
    }
}

