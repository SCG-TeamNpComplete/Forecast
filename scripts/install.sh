echo 'starting installation process' >> /var/log/sga-npcomplete-forecast-decision-install.log
cd '/home/ec2-user/docker'
sudo docker login -e="kedar.gn20@gmail.com" -u="kedargn" -p="npcomplete"   #TODO : hide password
sudo docker pull kedargn/forecast
sudo docker run -d -p 64000:64000 --name forecast $(sudo docker images | grep kedargn/forecast | awk '{print $3}') >> ./log.txt
