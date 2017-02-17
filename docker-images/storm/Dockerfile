FROM ubuntu:14.04

RUN apt-get update -qq && apt-get install -yqq build-essential \
  supervisor \
  thrift-compiler \
  zookeeperd \
  wget vim

# setup storm environment variables
ENV STORM_VERSION 0.9.6
ENV STORM_HOME /opt/apache-storm
ENV SUPVSR_CONF /etc/supervisord.conf

# Create storm group and user
RUN groupadd storm; useradd --gid storm --home-dir /home/storm --create-home --shell /bin/bash storm

# download and install storm
RUN wget http://apache.mirrors.ovh.net/ftp.apache.org/dist/storm/apache-storm-$STORM_VERSION/apache-storm-$STORM_VERSION.tar.gz && \
tar -xzvf apache-storm-$STORM_VERSION.tar.gz -C /opt && ln -s $STORM_HOME-$STORM_VERSION $STORM_HOME && \
rm apache-storm-$STORM_VERSION.tar.gz && \
chown -R storm:storm $STORM_HOME-$STORM_VERSION && \
chown storm:storm $STORM_HOME

# create supervisord log folders
RUN mkdir -p /var/log/storm && \
chown -R storm:storm /var/log/storm

# configure supervisord
ADD conf/supervisord.conf $SUPVSR_CONF

# FVD dependencies
RUN apt-get install -y \
  libldap2-dev \
  libsasl2-dev

# fix error in "pip install cryptography" (http://askubuntu.com/questions/499714/error-installing-scrapy-in-virtualenv-using-pip)
RUN apt-get install -y libffi-dev

RUN apt-get install -y libopencv-dev python-opencv

RUN apt-get install -y libpq-dev python-dev libmysqlclient-dev python-mysqldb python-pip

RUN apt-get install -y protobuf-compiler redis-server

COPY requirements.txt ./
RUN pip install -r requirements.txt

# setup entry point
ADD scripts/entrypoint.sh /home/storm/entrypoint.sh
ENTRYPOINT ["/bin/bash", "/home/storm/entrypoint.sh"]
