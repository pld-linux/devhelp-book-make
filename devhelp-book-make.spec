Summary:	DevHelp book: make
Summary(pl):	Ksi±¿ka do DevHelpa o make'u
Name:		devhelp-book-make
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/make.tar.gz
# Source0-md5:	a9a947a09f58d7034271d21a8f66b673
URL:		http://www.devhelp.net/
Requires:	devhelp >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about make.

%description -l pl
Ksi±¿ka do DevHelpa o make'u.

%prep
%setup -q -c -n make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/books/make

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/books/make/make.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/make

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
