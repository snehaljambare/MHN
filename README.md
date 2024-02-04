# MHN
MHN is a centralized server for management and data collection of honeypots. MHN allows you to deploy sensors quickly and to collect data immediately, viewable from a neat web interface. Honeypot deploy scripts include several common honeypot technologies, including Snort, Cowrie, Dionaea, and glastopf, among others.
# Objectives:
- Identify and Incorporate Vulnerabilities in Honeypots
- Design and Implement Database Integration
- Unauthorized access and potential data breaches.
- Develop Web Application Interface
- Implement and Monitor SIEM Integration
- Establish Attack-Chain Mechanisms
By incorporating these objectives into our project, we aim to develop a comprehensive and effective cybersecurity infrastructure that can protect web applications and their underlying infrastructure from various threats and effectively mitigate potential attacks.

# System Architecture
![Honeypot Architecture1 drawio](https://github.com/snehaljambare/MHN/assets/74786817/cc16b507-3558-43c8-991d-f28a02c673b9)


# Installation
- The MHN server is supported on Ubuntu 18.04, Ubuntu 16.04, and Centos 6.9.
- Other versions of Linux may work but are generally not tested or supported.
**Install Git**
- on Debian or Ubuntu
- $ sudo apt install git -y
**Install MHN**
- $ cd /opt/
- $ sudo git clone https://github.com/pwnlandia/mhn.git
- $ cd mhn/
**Run the following script** to complete the installation. While this script runs, you will be prompted for some configuration options. See below for how this looks.
- $ sudo ./install.sh
### Configuration
<img width="296" alt="MicrosoftTeams-image (19)" src="https://github.com/snehaljambare/MHN/assets/74786817/a61eb5b5-2052-4b87-9150-0e063e3e85ef">

### Running
If the installation scripts ran successfully, you should have a number of services running on your MHN server. See below for checking these.
<img width="752" alt="MicrosoftTeams-image (20)" src="https://github.com/snehaljambare/MHN/assets/74786817/36921e6d-b3b0-4090-9875-ecf1bf0e5a7e">
<img width="387" alt="MicrosoftTeams-image (21)" src="https://github.com/snehaljambare/MHN/assets/74786817/5cc91e09-9d12-473e-8976-098077e7cfe9">

# Deploying honeypots with MHN
MHN was designed to make scalable deployment of honeypots easier. Here are the steps for deploying a honeypot with MHN:
- Login to your MHN server web app.
- Click the "Deploy" link in the upper left hand corner.
- Select a type of honeypot from the drop down menu (e.g. "Ubuntu Dionaea").
- Copy the deployment command.
- Login to a honeypot server and run this command as root.
- If the deploy script successfully completes you should see the new sensor listed under your deployed sensor list. For a full list of supported sensors, check the list here:

# Integration with Splunk
hpfeeds-logger can be used to integrate MHN with Splunk.
**Splunk**
- cd /opt/mhn/scripts/
- sudo ./install_hpfeeds-logger-splunk.sh
- sudo ./install_splunk_universalforwarder.sh
This will log the events as key/value pairs to /var/log/mhn-splunk.log. This log should be monitored by the SplunkUniversalForwarder.

# Integrate Splunk with Modern honey network. 
We need to install the latest version of Splunk for Linux as tgz compressed file from: https://www.splunk.com/en_us/products/splunk-enterprise.html Now we need to install Splunk by using following commands:
- $ cd /opt/
- $ tar –zxvf Splunk_package.tgz
- $ cd /opt/splunk/bin
- $ ./splunk start

  
![splunk install](https://github.com/snehaljambare/MHN/assets/74786817/1a4992c2-7b85-4859-b84a-7e9902d34390)

# Output
MHN attack count
![MicrosoftTeams-image (22)](https://github.com/snehaljambare/MHN/assets/74786817/1ab0a867-6bd8-4deb-b2bd-503dec7e697d)



