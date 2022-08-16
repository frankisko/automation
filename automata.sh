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