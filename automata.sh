echo "Starting VPN"
nmcli con up "My VPN"
sleep 10

echo "Starting Sublime text"
sublime-text.subl
sleep 5

echo "Opening firefox"
nohup firefox &
sleep 5

echo "Starting lampp"
echo mysecretpassword | sudo -S /opt/lampp/lampp start
sleep 5

echo "Starting sql developer"
nohup /opt/sqldeveloper/sqldeveloper.sh &
sleep 5

echo "Starting IntelliJ"
nohup /opt/intellij/bin/idea.sh &
sleep 5


cd /opt/kafka/kafka_2.11-0.10.2.0
echo "Starting zookeeper"
./bin/zookeeper-server-start.sh ./config/zookeeper.properties &
sleep 10

echo "Starting kafka"
./bin/kafka-server-start.sh ./config/server.properties &
sleep 10


#kill.sh
#arr=( "$@" )
#sleep 1m
#  for i in "${arr[@]}"; do
#    kill -9 $(( $i ));
#  done
#exit 0

#####

#env.sh
#export YPT_SECURITY_OPTS="-Dencrypt.keyStore.location=file://${HOME}/yopter/server.jks -Dencrypt.keyStore.password=yptstorepass -Dencrypt.keyStore.alias=yopter -Dencrypt.keyStore.secret=yptkey"
#export YPT_OPTS="-Xmx96m -Xms50m -Dspring.profiles.active=dev -Duser.timezone=GMT"
#export YPT_OPTS_OLD="-Xmx200m -Xms50m -Dspring.profiles.active=dev -Duser.timezone=GMT"

#####

#api.sh (compile an api)
#if [ "$2" == "" ]; then
#	echo "Third argument to compile"
#else
#    case $2 in
#        -c )           mvn clean install -DskipDockerBuild
#    esac
#fi
#. ../env.sh

#if [ "$1" == "" ]; then
#	echo "Second argument for instance number"
#else
#    1) backup pid in array
#    declare -a my_array=( $(while read p; do
#      echo $p
#    done <pid.txt ) )

#    2) delete pid file
#    rm pid.txt

#    3) launch new instances
#    c=1
#    while [ $c -le $1 ]
#    do
#        nohup java -Xmx400m -Xms100m -Dspring.profiles.active=dev -Duser.timezone=GMT -jar target/my-api.jar &> output.log&
#    	echo $! >> pid.txt
#    	(( c++ ))
#    done

#    4) kill old instances from step 1
#. ../kill.sh "${my_array[@]}" &
#fi
#exit 0

#####

#zuul.sh (compile zuul gateway)
#while [ "$1" != "" ]; do
#    case $1 in
#        -c )           mvn clean install -DskipDockerBuild
#    esac
#    shift
#done
#. ../env.sh
#kill -9 `cat pid.txt`
#nohup java -Xmx128m -Xms64m -Dspring.profiles.active=dev -Duser.timezone=GMT -jar target/zuul-gateway.jar &> output.log&
#echo $! > pid.txt
