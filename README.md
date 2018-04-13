# Container to build EPEL RPM of LastPass CLI

We have created a small docker container in order to make building the RPM super easy:

1.) Create a directory for your "docker data" (ex: ```/docker/rpm```)

**NOTE: make sure that directory is completely empty!**

2.) Let the container BUILD the RPM for you:

```
docker run -it --rm -v /docker/rpm:/root/rpmbuild harvarditsecurity/rpm-lastpass-cli
```

3.) Look for the RPM at: ```/docker/rpm/RPMS/x86_64/lastpass-cli-$VERSION.el7.centos.x86_64.rpm```
