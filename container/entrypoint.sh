#!/bin/bash
cd /root/rpmbuild
git clone https://github.com/harvard-itsecurity/rpm-lastpass-cli.git .
rpmbuild -v -bb --clean SPECS/lastpass-cli.spec

echo "### RPM CREATED ###"
echo "In your mounted directory, look at: RPMS/x86_64/lastpass-cli-$VERSION.el7.centos.x86_64.rpm"
echo "###################"
