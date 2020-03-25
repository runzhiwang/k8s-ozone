FROM apache/ozone-runner:20191107-1

RUN sudo rm -rf /opt/hadoop && sudo mkdir -p /usr/local/java && sudo chmod 777 /opt/ && sudo rm -rf /etc/localtime && sudo ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

ADD jdk/ /usr/local/java/jdk
ADD ozone/ /opt/hadoop
ADD ozone-config/ozone-site.xml /opt/hadoop/etc/hadoop/

ENV JAVA_HOME /usr/local/java/jdk
ENV JRE_HOME ${JAVA_HOME}/jre
ENV CLASSPATH .:${JAVA_HOME}/lib:${JRE_HOME}/lib
ENV PATH ${JAVA_HOME}/bin:$PATH
ENV no_proxy om,scm,s3g,om-0,scm-0,s3g-0,kdc,localhost,127.0.0.1,jaeger,jaeger-0



