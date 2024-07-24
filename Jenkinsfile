/* groovylint-disable NestedBlockDepth */
pipeline {
    agent { label 'ec2-user' }
    environment {
        DEPLOYMENT_ID = "${env.CHANGE_ID}-${env.BUILD_NUMBER}"
    }
    options {
        timestamps()
        parallelsAlwaysFailFast()
    }

    stages {
        stage('Build and Deploy') {
            parallel {
                stage('ui-config Management') {
                    when {
                        allOf {
                           expression { env.CHANGE_TARGET == 'staging'  }
                        }
                    }
                    steps {
                        sh 'pwd'
                        echo "latest tag is staging-${DEPLOYMENT_ID}"
                        dir('packages/core/services/ui-configuration-management')  {
                            sh 'pwd'
                            sh 'mkdir kylych'

                        }
                    }
                }
            }
        }
    }
}
