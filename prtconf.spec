Summary: SPARC OpenPROM dump utility
Name: prtconf
Version: 1.2
Release: 3
Copyright: GPL
Group: Applications/System
Source: sunsite.mff.cuni.cz/OS/Linux/Sparc/local/prtconf/prtconf-1.2.tgz
URL: http://ultra.linux.cz/
ExclusiveArch: sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility will dump SPARC OpenPROM device tree
in the format similar to Solaris prtconf, that is,
in a nicely readable compact format.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{sbin,man/man8}
install -m 0755 -s prtconf $RPM_BUILD_ROOT/usr/sbin/prtconf
install -m 0644 prtconf.8 $RPM_BUILD_ROOT/usr/man/man8/prtconf.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/sbin/prtconf
/usr/man/man8/prtconf.8
