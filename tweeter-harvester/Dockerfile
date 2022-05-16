#
# Cluster and Cloud Computing - Team 2 
# 
# Authors: 
#
#  * Yi Yang (Student ID: 1074365)
#  * Claire Zhang (Student ID: 1080915)
#  * Hengzhi Qiu (Student ID: 1253748)
#  * Terry (Student ID: 955797)
#  * Yonghao Hu (Student ID: 1049814)
#

FROM python:3

ADD  . /

RUN apt install -y libc-dev
RUN apt update
RUN apt install -y build-essential gdal-bin libgdal-dev python3-dev python3-pandas python3-numpy python3-gdal python3-fiona
RUN pip install pyproj 
RUN pip install -r requirements.txt

CMD [ "./run-py.sh" ]
