# Honeypot
A honeypot is like a pretend target in a computer network to attract attackers. It's not real, but it seems valuable. When an attacker interacts with it, the security team can watch what they do. This helps organizations understand new threats and attack patterns. By studying the attacker's behaviour in a safe place, cybersecurity experts learn important things to make defences better. So, a honeypot is a smart trick that not only confuses potential threats but also lets cybersecurity experts see what's changing in the world of cyber threats.

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

# Implementation
Here we have 3 virtual machines are deployed in a controlled network environment: one hosting a web application, one acting as an attacker machine (Kali), and the third serving as a honeypot. The honeypot is configured to detect unauthorized access attempts to the web application and triggers alerts containing information about the attacker, including their IP address, location, and the type of attack being executed. These alerts are forwarded to Splunk, a log analysis tool, for graphical representation and consolidated analysis. Splunk enables visualization of the attack data, allowing for the correlation of events and providing valuable insights for proactive security monitoring, incident response, and threat intelligence.

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

Web application 

![MicrosoftTeams-image (23)](https://github.com/snehaljambare/MHN/assets/74786817/d6158459-55b1-473f-ad54-15dcc505cef5)

Splunk 

![splunk](https://github.com/snehaljambare/MHN/assets/74786817/cde0c938-8337-4122-9a6a-40f28383ba78)

# Future Scope
The honeypot that we have implemented is on a local network but is not limited to expansion in future. There is huge upside potential in the market if implemented correctly, with the right connecters we can deploy the honeypot so that there is Advanced Threat Detection capabilities, AI integration would be possible, Deception Technology can be implemented, Cloud Security deployed, Threat Intelligence can be gathered, Automated Response Mechanisms placed strategically , Regulatory Compliance performed and audited , Cybersecurity Training and Research conducted periodically , Integration with Security Operations Centers is also a possibility . 
The Future scope and potential of Honeypot is limitless and huge as we are all moving towards a complete digital era in the near future, we will definitely need safety measures and checks in place to safeguard us in the digital platform. 

# Conclusion
Finally, this honeypot demonstrated the efficiency of using Modern Honey Network (MHN) in conjunction with Splunk to improve cybersecurity measures. The deployment and integration of MHN and Splunk has proven to be an effective combination for identifying, redirecting, and investigating hostile activity on computer systems and networks. The use of MHN gave useful insights into new dangers, and the interface with Splunk enabled a more efficient and complete study of honeypot data. The technique aided early detection strategies, improved threat intelligence, and provided practical direction for security experts. The collaboration between MHN and Splunk resulted in a comprehensive technique for real-time monitoring and response to growing cyber threats. This thesis not only emphasizes the need of honeypots in cybersecurity, but it also demonstrates the effectiveness of MHN and Splunk integration as a proactive and perceptive protection mechanism against sophisticated threats.

### References
- https://github.com/pwnlandia/mhn/wiki/Running-MHN-Over-HTTPS

