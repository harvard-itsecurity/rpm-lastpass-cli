# EPEL RPM of LastPass CLI

## To Build:
1.) cd /tmp; git clone https://github.com/harvard-itsecurity/rpm-lastpass-cli.git
2.) docker run -it --rm -v /tmp/rpm-lastpass-cli:/root/rpmbuild centos:7
3.) yum -y install epel-release
4.) yum -y install rpm-build openssl libcurl libxml2 pinentry xclip openssl-devel libxml2-devel libcurl-devel gcc gcc-c++ make cmake asciidoc bash-completion
5.) cd /root/rpmbuild
6.) rpmbuild -v -bb --clean SPECS/lastpass-cli.spec

## Release Path:
/tmp/rpm-lastpass-cli/RPMS/x86_64/lastpass-cli-$version.el7.centos.x86_64.rpm
