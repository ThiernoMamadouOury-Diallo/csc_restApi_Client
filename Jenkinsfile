node {
   stage('Preparation') { // for display purposes
      // Get some code from a GitHub repository
      git branch: 'master', 
        url: 'http://gitlab.tas.inside.esiag.info/PDSING3/restapiclient.git',
        credentialsId: 'bac1be3b-5d3a-4657-947a-55b44a7250bb'
   }
   stage('Setting variables'){
       script{
           env.VERSION = readFile 'version.txt'
           env.KUBE_IP = sh(script: 'eval echo "\\${KUBE_${ENV}}"', returnStdout: true).trim()
           env.PSQL_IP = sh(script: 'eval echo "\\${PSQL_${ENV}}"', returnStdout: true).trim()
       }
   }
   environment{
       PSQL_IP = ${env.PSQL_IP}
       KUBE_IP = ${env.KUBE_IP}
       VERSION = ${env.VERSION}
   }
   stage('Replacing environment variable'){
       sh "echo '${PSQL_IP}'"
       sh "echo '${env.PSQL_IP}'"
       sh "envsubst < deployment/deployment.yaml > deployment/deployment.yaml.new"
       sh "mv deployment/deployment.yaml.new deployment/deployment.yaml"
       sh "envsubst < configuration.yml > configuration.yml.new"
       sh "mv configuration.yml.new configuration.yml"
       sh "envsubst < swagger.yaml > swagger.yaml.new"
       sh "mv swagger.yaml.new swagger.yaml"
   }
   stage('Build') {
       sh "envsubst < deployment/deployment.yaml > deployment/deployment.yaml.new"
       sh "mv deployment/deployment.yaml.new deployment/deployment.yaml"
       sh "docker build -t restapiclient:${env.VERSION} ."
   }
   stage('Push Image') {
       sh "docker tag restapiclient:${env.VERSION} docker-registry.com/restapiclient:${env.VERSION}"
       sh "docker push docker-registry.com/restapiclient:${env.VERSION}"
   }
   stage('Deployment'){
       sh 'ssh tas@${KUBE_IP} rm -rf /opt/workspace/restapiclient'
       sh 'ssh tas@${KUBE_IP} mkdir -p /opt/workspace'
       sh 'scp -r deployment tas@${KUBE_IP}:/opt/workspace/restapiclient'
       sh 'ssh tas@${KUBE_IP} "kubectl delete deployment restapiclient-deploy"'
       sh 'ssh tas@${KUBE_IP} "kubectl apply -f /opt/workspace/restapiclient/deployment.yaml"'
   }
}
