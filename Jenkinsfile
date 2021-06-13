pipeline {
    
    agent { docker { image 'ubuntu:18.04' } }

    stages {

        stage("build") {
            
            steps {
                echo 'installing python'
                sh 'apt-get update -y && apt-get install -y python3'
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