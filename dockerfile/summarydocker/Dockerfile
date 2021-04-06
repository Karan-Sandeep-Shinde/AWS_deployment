FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get install -y git
RUN apt-get -y install python3-pip
RUN mkdir project
#RUN cd project
RUN git clone https://github.com/Karan-Sandeep-Shinde/AWS_deployment.git
#RUN cd AWS_deployment
RUN pip3 install -r AWS_deployment/requirements.txt


CMD ["python3","AWS_deployment/summarize.py"]

# sudo docker build -t summaryimage:0.1 dockerfile/summarydocker