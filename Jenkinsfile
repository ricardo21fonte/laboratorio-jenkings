pipeline { 
    agent { label 'ci-python-docker' } 
 
    options { 
        skipDefaultCheckout(true) 
        timestamps()
         disableConcurrentBuilds() 
        timeout(time: 20, unit: 'MINUTES') 
    } 
 
    stages { 
        stage('Checkout') { 
            steps { 
                deleteDir() 
                checkout scm 
                sh 'git log -1 --oneline' 
            } 
        } 
 
        stage('Setup') { 
            steps { 
                sh ''' 
                    set -eu 
                    python3 -m venv .venv 
                    .venv/bin/python -m pip install -r requirements-dev.txt 
                ''' 
            } 
        } 
 
        stage('Test') { 
            steps { 
                sh ''' 
                    set -eu 
                    mkdir -p reports 
                    .venv/bin/python -m pytest -q --junitxml=reports/junit.xml 
                ''' 
            } 
            post { 
                always { 
                    script { 
                        if (fileExists('reports/junit.xml')) { 
                            junit testResults: 'reports/junit.xml'                    } else { 
                            echo 'Relatório de testes indisponível' 
                        } 
                    } 
                } 
            } 
        } 
    } 
 
    post { 
        success { echo 'CI concluída com sucesso' } 
        failure { echo 'CI com erro — consultar Console Output' } 
    } 
}