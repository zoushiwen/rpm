Name:		node_exporter
Version:	0.17.0	
Release:	1%{?dist}
Summary:	node_exporter

Group:		prometheus	
License:	GPL	
URL:		http://prometheus.io	
Source0:	node_exporter-0.17.0.tar.gz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	chkconfig	
Requires:	chkconfig	

%description
prometheus agent package


%prep
%setup -q


%build
%install
rm -rf %{buildroot}
install -d %{buildroot}/usr/local/%{name}
install -d %{buildroot}/var/log/prometheus
install -d %{buildroot}/var/run/prometheus
install -p -D %{_builddir}/%{name}-%{version}/NOTICE		%{buildroot}/usr/local/%{name}/NOTICE
install -p -D %{_builddir}/%{name}-%{version}/LICENSE		%{buildroot}/usr/local/%{name}/LICENSE
install -p -D %{_builddir}/%{name}-%{version}/node_exporter	%{buildroot}/usr/local/%{name}/node_exporter
install -p -D %{_sourcedir}/%{name}				%{buildroot}/etc/init.d/%{name}



%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/local/%{name}
/etc/init.d/%{name}

%changelog

