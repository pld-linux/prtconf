Summary:	SPARC OpenPROM dump utility
Summary(pl):	Narzêdzie do zrzucania zawarto¶ci sparcowych OpenPROM-ów
Name:		prtconf
Version:	1.3
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://www.cs.elte.hu/pub/Linux/sunsite.mff.cuni.cz/prtconf/%{name}-%{version}.tgz
# Source0-md5:	ddc65b86d8642086943c4d169634b37f
ExclusiveArch:	sparc sparc64 sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
prtconf utility will dump SPARC OpenPROM device tree in the format
similar to Solaris prtconf, that is, in a nicely readable compact
format.

There is also eeprom utility included, which displays or modifies
OpenPROM options.

%description -l pl
Narzêdzie prtconf zrzuca drzewo urz±dzeñ ze sparcowych OpenPROM-ów w
formacie podobnym do solarisowego prtconf, czyli ³atwo czytelnym.

Za³±czone jest tak¿e narzêdzie eeprom, wy¶wietlaj±ce lub modyfikuj±ce
opcje w OpenPROM-ie.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install prtconf eeprom $RPM_BUILD_ROOT%{_sbindir}
install prtconf.8 eeprom.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/eeprom
%attr(755,root,root) %{_sbindir}/prtconf
%{_mandir}/man8/eeprom.8*
%{_mandir}/man8/prtconf.8*
