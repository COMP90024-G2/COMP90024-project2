#
# Cluster and Cloud Computing - Team 2 
# 
# Authors: 
#
#  * Yi Yang (Student ID: 1074365)
#  * Claire Zhang (Student ID: 1080915)
#  * Hengzhi Qiu (Student ID: )
#  * Terry (Student ID: 955797)
#  * Yonghao Hu (Student ID: 1049814)
#

# Can run without host.ini
# . ./openrc.sh; ansible-playbook main_deploy.yaml
. ./openrc.sh; ansible-playbook -i host.ini main_deploy.yaml