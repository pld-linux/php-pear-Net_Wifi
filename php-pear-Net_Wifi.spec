%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Wifi
%define		_status		stable
%define		_pearname	Net_Wifi

Summary:	%{_pearname} - Scans for wireless networks
Summary(pl.UTF-8):	%{_pearname} - Wyszukiwanie sieci bezprzewodowych
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	cd867d4c0b4ede3757c724baa872550f
URL:		http://pear.php.net/package/Net_Wifi/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_Wifi utilizes the command line tools "iwconfig" and "iwlist" to
get information about wireless lan interfaces on the system and the
current configuration. The class enables you to scan for wireless
networks and get a bunch of information about them.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Net_Wifi wykorzystuje programy "iwconfig" oraz "iwlist" do pobrania
informacji na temat interfejsów sieci bezprzewodowych oraz bieżącej
konfiguracji. Klasa ta pozwala także na skanowanie w poszukiwaniu
nowych sieci oraz uzyskanie o nich zestawu informacji.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/examples/Wifi_usage.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/Wifi.php
%{php_pear_dir}/Net/Wifi

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Net_Wifi
