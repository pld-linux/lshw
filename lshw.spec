Summary:	Hardware Lister
Summary(pl):	Narzêdzie wypisuj±ce sprzêt
Name:		lshw
Version:	B.02.03
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/ezix/%{name}-%{version}.tar.gz
# Source0-md5:	f0de8716c63cd4692a1dec604824d90e
URL:		http://ezix.sourceforge.net/software/lshw.html
BuildRequires:	libstdc++-devel
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
Requires:	pciutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lshw (Hardware Lister) is a small tool to provide detailed informaton
on the hardware configuration of the machine. It can report exact
memory configuration, firmware version, mainboard configuration, CPU
version and speed, cache configuration, bus speed, etc. on DMI-capable
x86 systems and on some PowerPC machines (PowerMac G4 is known to
work).

Information can be output in plain text, XML or HTML.

It currently supports DMI (x86 only), OpenFirmware device tree
(PowerPC only), PCI/AGP, CPUID (x86), IDE/ATA/ATAPI, PCMCIA (only
tested on x86) and SCSI.

%description -l pl
lshw (Hardware Lister) to ma³e narzêdzie maj±ce udostêpniæ szczegó³owe
informacje dotycz±ce sprzêtowej konfiguracji maszyny. Mo¿e okre¶liæ
dok³adn± konfiguracjê pamiêci, wersjê firmware, konfiguracjê p³yty
g³ównej, wersjê i szybko¶æ CPU, konfiguracjê cache, szybko¶æ szyny
itp. na systemach x86 obs³uguj±cych DMI oraz niektórych maszynach
PowerPC (wiadomo, ¿e dzia³a na PowerMacu G4).

Informacje mog± byæ podawane jako czysty tekst, XML lub HTML.

Aktualnie program obs³uguje DMI (tylko x86), drzewo urz±dzeñ
OpenFirmware (tylko PowerPC), PCI/AGP, CPUID (x86), IDE/ATA/ATAPI,
PCMCIA (testowane tylko na x86) oraz SCSI.

%package gtk
Summary:	GTK+ version of lshw
Summary(pl):	lshw w wersji GTK+
Group:		Applications/System
Requires:	lshw

%description gtk
GTK+ version of lshw.

%description gtk -l pl
lshw w wersji GTK+.

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -I./core"

%{__make} gui \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -I../core `pkg-config --cflags gtk+-2.0`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install-gui \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/TODO docs/Changelog docs/lshw.xsd
%attr(755,root,root) %{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/gtk-%{name}
