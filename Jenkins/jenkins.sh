#!/bin/bash
# Jenkins install instructions for Ubuntu:
sudo apt-get update -y

#Install Java sdk
sudo apt install openjdk-8-jdk-headless -y

# Get the keys for jenkins 
wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -

sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update -y

# Install Jenkins
sudo apt-get install jenkins -y

# To use Jenkins: Open browser and type the http://<<Public Ip of the node on which you installed Jenkins>>:8080
# Then follow the instruction displayed on the browser.
