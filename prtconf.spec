Summary:	SPARC OpenPROM dump utility
Name:		prtconf
Version:	1.2
Release:	3
License:	GPL
Group:		Utilities/System
Source0:	ftp://sunsite.mff.cuni.cz/OS/Linux/Sparc/local/prtconf/prtconf-1.2.tgz
URL:		http://ultra.linux.cz/
ExclusiveArch:	sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility will dump SPARC OpenPROM device tree in the format
similar to Solaris prtconf, that is, in a nicely readable compact
format.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{%{_sbindir},%{_mandir}/man8}

install -s prtconf $RPM_BUILD_ROOT%{_sbindir}/prtconf
install prtconf.8 $RPM_BUILD_ROOT%{_mandir}/man8/prtconf.8

gzip -9nf RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/prtconf
%{_mandir}/man8/prtconf.8*
