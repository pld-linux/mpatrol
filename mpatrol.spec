Summary:	A library for controlling and tracing dynamic memory allocations
Summary(pl):	Biblioteka do kontroli i ¶ledzenia dynamicznej alokacji pamiêcie
Name:		mpatrol
Version:	1.3.4
Release:	1
License:	LGPL
Group:		Development/Debuggers
Group(de):	Entwicklung/Debugger
Group(pl):	Programowanie/Odpluskwiacze
Source0:	http://www.cbmamiga.demon.co.uk/mpatrol/files/%{name}_%{version}.tar.gz
Patch0:		%{name}-info.patch
BuildRequires:	texinfo
URL:		http://www.cbmamiga.demon.co.uk/mpatrol/index.html
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q -n mpatrol
%patch -p1

%build
(cd build/unix
 %{__make} libmpatrol.a libmpatrol.so mpatrol mprof mleak \
	OFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"
)
(cd doc; makeinfo mpatrol.texi)

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

gzip -9nf README NEWS ChangeLog

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_infodir}/*
%{_mandir}/man[13]/*

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT
