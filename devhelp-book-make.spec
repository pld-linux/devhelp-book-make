Summary:	DevHelp book: make
Summary(pl):	Ksi±¿ka do DevHelp'a o make
Name:		devhelp-book-make
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/make.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about make

%description -l pl
Ksi±¿ka do DevHelp o make

%prep
%setup -q -c make -n make

%build
mv -f book make
mv -f book.devhelp make.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/make
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install make.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install make/* $RPM_BUILD_ROOT%{_prefix}/books/make

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
