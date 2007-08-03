#
# Conditional build:
%bcond_without	gui	# build without GTK gui
#
Summary:	Hardware Lister
Summary(pl.UTF-8):	Narzędzie wypisujące sprzęt
Name:		lshw
Version:	B.02.11
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://ezix.org/software/files/%{name}-%{version}.tar.gz
# Source0-md5:	e88d3a3bfef80f998a18d80fe99b36e2
Patch0:		%{name}-make.patch
URL:		http://ezix.org/project/wiki/HardwareLiSter
%{?with_gui:BuildRequires:	gtk+2-devel >= 1:2.0}
BuildRequires:	libstdc++-devel
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

%description -l pl.UTF-8
lshw (Hardware Lister) to małe narzędzie mające udostępnić szczegółowe
informacje dotyczące sprzętowej konfiguracji maszyny. Może określić
dokładną konfigurację pamięci, wersję firmware, konfigurację płyty
głównej, wersję i szybkość CPU, konfigurację cache, szybkość szyny
itp. na systemach x86 obsługujących DMI oraz niektórych maszynach
PowerPC (wiadomo, że działa na PowerMacu G4).

Informacje mogą być podawane jako czysty tekst, XML lub HTML.

Aktualnie program obsługuje DMI (tylko x86), drzewo urządzeń
OpenFirmware (tylko PowerPC), PCI/AGP, CPUID (x86), IDE/ATA/ATAPI,
PCMCIA (testowane tylko na x86) oraz SCSI.

%package gtk
Summary:	GTK+ version of lshw
Summary(pl.UTF-8):	lshw w wersji GTK+
Group:		Applications/System
Requires:	lshw

%description gtk
GTK+ version of lshw.

%description gtk -l pl.UTF-8
lshw w wersji GTK+.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -I./core"

%if %{with gui}
%{__make} gui \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -I../core `pkg-config --cflags gtk+-2.0`"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with gui}
%{__make} install-gui \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/TODO docs/Changelog docs/lshw.xsd README
%attr(755,root,root) %{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*

%if %{with gui}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/gtk-%{name}
%endif
