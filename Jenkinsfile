pipeline {
    agent { label 'test' }

    environment {
        SCRIPTS_DIR = "/home/ec2-user/workspace/afsdf"
        MARKER_DIR = "/home/ec2-user/workspace/afsdf/markers"
    }

    stages {
        stage('Connect to MongoDB and Load Commands') {
            steps {
                script {
                    // Define the list of scripts to run
                    def scripts = ["test1.js", "test2.js"]

                    // Ensure the marker directory exists
                    sh "mkdir -p ${MARKER_DIR}"

                    for (script in scripts) {
                        def markerFile = "${MARKER_DIR}/${script}.marker"
                        
                        // Check if the script has been updated or not run before
                        if (fileExists(script) && changeset(script) || !fileExists(markerFile)) {
                            // Run the MongoDB script
                            sh """
                            mongosh "mongodb+srv://nur23anttech:admin@cluster0.b9lybep.mongodb.net/" --eval "load('${SCRIPTS_DIR}/${script}')"
                            """

                            // Create the marker file to indicate the script has been run
                            sh "touch ${markerFile}"
                        } else {
                            echo "Skipping ${script} as it has not changed or has been run before."
                        }
                    }
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
