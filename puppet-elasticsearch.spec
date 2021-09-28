%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-elasticsearch
%global commit a46f52e9b1ea8f2f62d61d8084d025e5fc90dd31
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-elasticsearch
Version:        7.0.0
Release:        2%{?alphatag}%{?dist}
Summary:        Module for managing and configuring Elasticsearch nodes
License:        ASL 2.0

URL:            https://github.com/elastic/puppet-elasticsearch

Source0:        https://github.com/elastic/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
#Requires:       puppet-apt
#Requires:       puppet-yum
Requires:       puppet-datacat
Requires:       puppet >= 2.7.0

%description
Module for managing and configuring Elasticsearch nodes

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/elasticsearch/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/elasticsearch/



%files
%{_datadir}/openstack-puppet/modules/elasticsearch/


%changelog
* Tue Sep 28 2021 RDO <dev@lists.rdoproject.org> 7.0.0-2.a46f52egit
- Update to post 7.0.0 (a46f52e9b1ea8f2f62d61d8084d025e5fc90dd31)



