Summary:	A library for controlling and tracing dynamic memory allocations
Name:		mpatrol
Version:	1.2.0
Release:	1
License:	LGPL
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Source0:	http://www.cbmamiga.demon.co.uk/mpatrol/files/%{name}_%{version}.tar.gz
Source1:	http://www.cbmamiga.demon.co.uk/mpatrol/files/%{name}_doc.tar.gz
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
%setup -q -n mpatrol -b 1


%build
cd build/unix
%{__make} libmpatrol.a libmpatrol.so.%{libversion} mpatrol mprof mleak


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_infodir}} \
	$RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man{1,3}

cp build/unix/mpatrol $RPM_BUILD_ROOT%{_bindir}
cp build/unix/mprof $RPM_BUILD_ROOT%{_bindir}
cp build/unix/mleak $RPM_BUILD_ROOT%{_bindir}
cp README $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp doc/README $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}/README.DOC
cp FAQ $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp COPYING $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp COPYING.LIB $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp NEWS $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp ChangeLog $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp doc/mpatrol.txt $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp doc/mpatrol.guide $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp doc/mpatrol.html $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp doc/mpatrol.dvi $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp doc/mpatrol.ps $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp doc/mpatrol.pdf $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp doc/refcard.dvi $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp doc/refcard.ps $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp doc/refcard.pdf $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}
cp doc/images/mpatrol.txt $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}/images
cp doc/images/mpatrol.jpg $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}/images
cp doc/images/mpatrol.eps $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}/images
cp doc/images/mpatrol.pdf $RPM_BUILD_ROOT%{_prefix}/doc/mpatrol-%{version}/images
cp src/mpatrol.h $RPM_BUILD_ROOT%{_includedir}
cp doc/mpatrol.info $RPM_BUILD_ROOT%{_prefix}/info
cp build/unix/libmpatrol.a $RPM_BUILD_ROOT%{_libdir}
cp build/unix/libmpatrol.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}
cp man/man1/mpatrol.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp man/man1/mprof.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp man/man1/mleak.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp man/man3/mpatrol.3 $RPM_BUILD_ROOT%{_mandir}/man3


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_prefix}/doc
%{_includedir}/*
%{_infodir/*
%{_libdir}/*
%{_mandir}/man[13]/*


%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%preun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT
