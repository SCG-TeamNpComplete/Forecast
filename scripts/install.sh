cd '/home/ec2-user/Forecast'
echo 'Activating virtualenv for Forecast Microservice' >> /var/log/sga-npcomplete-forecast-install.log
pip install virtualenv >> /var/log/sga-npcomplete-forecast-install.log
virtualenv venv >> /var/log/sga-npcomplete-forecast-install.log
. venv/bin/activate >> /var/log/sga-npcomplete-forecast-install.log
pip install requests
pip install Flask >> /var/log/sga-npcomplete-forecast-install.log
#echo 'Running Flask Server' >> /var/log/sga-npcomplete-flask-install.log
export FLASK_APP=forecast.py
flask run --host=0.0.0.0 --port=64000 >> /var/log/sga-npcomplete-forecast-server.log 2>&1 &