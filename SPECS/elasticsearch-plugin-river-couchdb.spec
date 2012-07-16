%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-river-couchdb
Version:        1.1.0
Release:        2%{?dist}
Summary:        ElasticSearch plugin to hook into CouchDB

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-river-couchdb

Source0:        https://github.com/downloads/elasticsearch/elasticsearch-river-couchdb/elasticsearch-river-couchdb-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.19

%description
The CouchDB River plugin allows to hook into
couchdb _changes feed and automatically index it into elasticsearch.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/river-couchdb

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/river-couchdb/elasticsearch-river-couchdb-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/river-couchdb/elasticsearch-river-couchdb.jar

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/river-couchdb
%{base_install_dir}/plugins/river-couchdb/*

%changelog
* Wed Jul 16 2012 Ingo Kampe ingo.kampe@kreuzwerker.de 1.1.0-2
- fixed base_install_dir to match default plugins directory

* Wed Mar 21 2012 Tavis Aitken tavisto@tavisto.net 1.1.0-1
- Tweaked to make the package conform to fedora build specs

* Tue Feb 22 2012 Sean Laurent 1.1.0-0
- Initial package

