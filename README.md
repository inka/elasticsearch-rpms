h1. Elasticsearch RPMs

This fork is derived from https://github.com/tavisto/elasticsearch-rpms

I have made some minor changes to use it with current version 0.19.8 on RHEL6/CentOS6:
* changed version in SPECS/elasticsearch.spec
* removed dependency to jpackage
* replaced java requirement with jdk (matching the standard oracle sun jdk package)
* enabled sysconfig entries by default

To build the rpm for your system of choice (included one plugin as example):

    install oracle jdk rpm
    yum install rpm-build rpmdevtools
    rpmdev-setuptree
    git clone git@github.com:inka/elasticsearch-rpms.git
    cp elasticsearch-rpms/SPECS/* rpmbuild/SPECS/
    cp elasticsearch-rpms/SOURCES/* rpmbuild/SOURCES/
    spectool -g rpmbuild/SPECS/elasticsearch.spec
    spectool -g rpmbuild/SPECS/elasticsearch-plugin-river-couchdb.spec
    mv elasticsearch*.tar.gz rpmbuild/SOURCES/
    rpmbuild -bb rpmbuild/SPECS/elasticsearch.spec
    rpmbuild -bb rpmbuild/SPECS/elasticsearch-plugin-river-couchdb.spec
    rpm -ivh rpmbuild/RPMS/*/elasticsearch*rpm
    check the config in /etc/elasticsearch/elasticsearch.yml
    service elasticsearch start
    chkconfig elasticsearch on
