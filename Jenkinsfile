pipeline {
    
    agent any

    stages {

        stage("build") {
            
            steps {
                echo 'installing python'
                sh 'sudo apt-get update -y && apt-get install -y python3'
            }
            
        }

        stage("test"){
            steps {
                echo 'another test'
            }
        }

        stage("deploy"){
            steps {
                echo 'if success'
            }
        }
    }
}