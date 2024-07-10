pipeline {
    agent { label 'test' }

    stages {
        stage('Connect to MongoDB and Load Scripts') {
            steps {
                withCredentials([string(credentialsId: 'mongo', variable: 'MONGODB_URI')]) {
                    script {
                        echo "Connecting to MongoDB using URI: ${MONGODB_URI}"
                        sh """
                        mongosh "${MONGODB_URI}" --eval "load('studentInfo.js'); load('update.js')"
                        """
                    }
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



