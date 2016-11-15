echo 'starting installation process' >> /var/log/sga-npcomplete-forecast-decision-install.log
cd '/home/ec2-user/docker'
sudo docker login -e="kedar.gn20@gmail.com" -u="kedargn" -p="npcomplete"   #TODO : hide password
sudo docker pull kedargn/forecastrun

#sudo docker ps -a | grep 'forecastrun1' | awk '{print $1}' | xargs --no-run-if-empty docker stop
#sudo docker ps -a | grep 'forecastrun1' | awk '{print $1}' | xargs --no-run-if-empty docker rm
sudo docker run -d -p 64000:64000 --name forecastrun1 $(sudo docker images | grep kedargn/forecastrun | awk '{print $3}') >> ./log.txt

sleep 2

#sudo docker ps -a | grep 'forecastrun2' | awk '{print $1}' | xargs --no-run-if-empty docker stop
#sudo docker ps -a | grep 'forecastrun2' | awk '{print $1}' | xargs --no-run-if-empty docker rm
sudo docker run -d -p 64001:64001 --name forecastrun2 $(sudo docker images | grep kedargn/forecastrun | awk '{print $3}') >> ./log.txt

