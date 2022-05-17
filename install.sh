!#/bin/bash

clear
echo "Script created by kacppy"
sleep 5
sudo
apt-get update
apt-get -y install python3
apt-get -y install python3-pip
apt-get -y install firefox
pip3 install selenium
echo "Now install geckodriver"
mv geckodriver /usr/local/bin/
chmod 777 /usr/local/bin/geckodriver
echo "END"
