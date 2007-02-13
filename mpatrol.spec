Summary:	A library for controlling and tracing dynamic memory allocations
Summary(pl.UTF-8):	Biblioteka do kontroli i śledzenia dynamicznej alokacji pamięci
Name:		mpatrol
Version:	1.4.8
Release:	3
License:	LGPL
Group:		Development/Debuggers
Source0:	http://www.cbmamiga.demon.co.uk/mpatrol/files/%{name}_%{version}.tar.gz
# Source0-md5:	ada423c49bc5bfa7c3e7a80a711c2a1a
Patch0:		%{name}-info.patch
Patch1:		%{name}-sparc.patch
URL:		http://www.cbmamiga.demon.co.uk/mpatrol/index.html
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A link library that attempts to diagnose run-time errors that are
caused by the wrong use of dynamically allocated memory. Along with
providing a comprehensive and configurable log of all dynamic memory
operations that occurred during the lifetime of a program, the mpatrol
library performs extensive checking to detect any misuse of
dynamically allocated memory. All of this functionality can be
integrated into existing code through the inclusion of a single header
file at compile-time. All logging and tracing output from the mpatrol
library is sent to a separate log file in order to keep its
diagnostics separate from any that the program being tested might
generate. A wide variety of library settings can also be changed at
run-time via an environment variable, thus removing the need to
recompile or relink in order to change the library's behaviour.

%description -l pl.UTF-8
Biblioteka próbująca zdiagnozować błędy działania programu spowodowane
złym używaniem dynamicznie alokowanej pamięci. Oprócz dawania
obszernego i konfigurowalnego loga wszystkich dynamicznych operacji na
pamięci, które wystąpiły podczas działania programu, biblioteka
mpatrol stara się wykryć wszelkie niewłaściwe użycia dynamicznie
przydzielonej pamięci. Cała funkcjonalność może być zintegrowana z
istniejącym kodem poprzez dołączenie jednego pliku nagłówkowego w
czasie kompilacji. Całe logi i zapis śledzenia z biblioteki mpatrol są
zapisywane do oddzielnego pliku aby oddzielić je od wszystkiego
innego, co program może wygenerować. Szeroki zakres ustawień
biblioteki może być zmieniany bez rekompilacji poprzez ustawianie
zmiennych środowiskowych.

%prep
%setup -q -n mpatrol
%patch0 -p1
%patch1 -p1

%build
%{__make} -C build/unix libmpatrol.a libmpatrol.so mpatrol mprof mleak \
	OFLAGS="%{rpmcflags}"

cd doc
makeinfo mpatrol.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_infodir}} \
	$RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man{1,3}}

install build/unix/{mpatrol,mprof,mleak} $RPM_BUILD_ROOT%{_bindir}

install src/mpatrol.h $RPM_BUILD_ROOT%{_includedir}
install build/unix/libmpatrol.{a,so*} $RPM_BUILD_ROOT%{_libdir}

install doc/mpatrol.info* $RPM_BUILD_ROOT%{_infodir}
install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so*
%{_libdir}/*.a
%{_includedir}/*
%{_infodir}/*.info*
%{_mandir}/man[13]/*
