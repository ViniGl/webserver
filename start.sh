#!/bin/bash

sudo apt install zip -y
sudo apt install python3-pip
pip3 install -r requirements.txt
touch ~/script_inicializacao
echo '#!/bin/bash' >> ~/script_inicializacao
echo 'python3 webServer.py ${aws_instance.OpenVPN.public_ip} &' >> ~/script_inicializacao
sudo chmod +x ~/script_inicializacao
sudo mv ~/script_inicializacao /etc/init.d/
python3 ~/webServer.py ${aws_instance.OpenVPN.public_ip} &
