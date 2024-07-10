pipeline {
    agent any

    environment {
        MONGODB_URI = credentials('mongo')
        STUDENT_INFO_SCRIPT = '/home/ec2-user/studentInfo.js' // Adjust the path as per your setup
        UPDATE_SCRIPT = '/home/ec2-user/update.js' // Adjust the path as per your setup
    }

    stages {
        stage('Connect to MongoDB and Load Scripts') {
            steps {
                script {
                    // Use environment variable MONGODB_URI
                    echo "Connecting to MongoDB using URI: ${MONGODB_URI}"
                    sh """
                    mongosh "${MONGODB_URI}" --eval "load('${STUDENT_INFO_SCRIPT}'); load('${UPDATE_SCRIPT}')"
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


