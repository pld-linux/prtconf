Summary:	SPARC OpenPROM dump utility
Summary(pl):	Narzêdzie do zrzucania zawarto¶ci sparcowych OpenPROM-ów
Name:		prtconf
Version:	1.2
Release:	3
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://sunsite.mff.cuni.cz/OS/Linux/Sparc/local/prtconf/%{name}-%{version}.tgz
URL:		http://ultra.linux.cz/
ExclusiveArch:	sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility will dump SPARC OpenPROM device tree in the format
similar to Solaris prtconf, that is, in a nicely readable compact
format.

%description -l pl
To narzêdzie zrzuca drzewo urz±dzeñ sparcowych OpenPROM-ów w formacie
podobnym do solarisowego prtconf, czyli ³atwo czytelnym.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{%{_sbindir},%{_mandir}/man8}

install prtconf $RPM_BUILD_ROOT%{_sbindir}/prtconf
install prtconf.8 $RPM_BUILD_ROOT%{_mandir}/man8/prtconf.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/prtconf
%{_mandir}/man8/prtconf.8*
