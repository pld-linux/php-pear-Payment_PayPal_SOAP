%include	/usr/lib/rpm/macros.php
%define		_class		Payment
%define		_subclass	PayPal_SOAP
%define		_status		beta
%define		_pearname	Payment_PayPal_SOAP
Summary:	%{_pearname} - PayPal SOAP API client
Summary(pl.UTF-8):	%{_pearname} - klient API SOAP PayPal
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8808276d9490a456f4029a83250df59a
URL:		http://pear.php.net/package/Payment_PayPal_SOAP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-soap >= 4:5.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an easy-to-use wrapper of PHP 5's SOAP client
for use with the PayPal SOAP API.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten dostarcza łatwy w użyciu wrapper klienta SOAP PHP5
umożliwiający dostep do API SOAP serwisu PayPal.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
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
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/PayPal

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Payment_PayPal_SOAP
