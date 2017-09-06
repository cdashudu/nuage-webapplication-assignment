# nuage-webapplication-assignment

The Automation folder contains all the file used for automation the description of each is as follows.

IPTable.sh: Adds IPTABLES entries 

joinLB: Adds the web server to the LoadBalancer 

leaveLB: removes the web server from the Load Balancer

leaveLB.service: runs during shut down to evoke leaveLB

flask.conf: runs the web server as daemon process

AddWebServer.yml: Adds a web server to the AWS environment

rc.local: waits for the Virtual NIC to come up and evokes IPTable.sh and joinLB during startup

