FROM centos:7
MAINTAINER Ventz Petkov <ventz_petkov@harvard.edu>

RUN yum -y install epel-release && yum -y update && \
    yum -y install rpm-build openssl libcurl libxml2 pinentry xclip openssl-devel libxml2-devel libcurl-devel gcc gcc-c++ make cmake asciidoc bash-completion git

WORKDIR /root
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
