%define		status		beta
%define		pearname	Payment_PayPal_SOAP
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - PayPal SOAP API client
Summary(pl.UTF-8):	%{pearname} - klient API SOAP PayPal
Name:		php-pear-%{pearname}
Version:	0.4.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	570f627d7bce69bbda93ecb4690ffa07
URL:		http://pear.php.net/package/Payment_PayPal_SOAP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-soap >= 4:5.1.0
Obsoletes:	php-pear-Payment_PayPal_SOAP-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an easy-to-use wrapper of PHP 5's SOAP client
for use with the PayPal SOAP API.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Pakiet ten dostarcza łatwy w użyciu wrapper klienta SOAP PHP5
umożliwiający dostep do API SOAP serwisu PayPal.

Ta klasa ma w PEAR status: %{status}.

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
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Payment/PayPal
%{php_pear_dir}/data/%{pearname}
