%ifarch %{x86_64}
# openfst is used by vosk, which is used by
# proton-experimental
%bcond_without compat32
%endif

Name:           openfst
Summary:        Weighted finite-state transducer tools
Version:        1.8.4
Release:        1
Source0:        https://www.openfst.org/twiki/pub/FST/FstDownload/openfst-%{version}.tar.gz
URL:		https://www.openfst.org/
Group:          System/Libraries
License:        Apache-2.0
BuildRequires:	pkgconfig(python3)
BuildSystem:	autotools
BuildOption:	--enable-compress
BuildOption:	--enable-fsts
BuildOption:	--enable-grm
BuildOption:	--enable-special
BuildOption:	--enable-bin

%patchlist
openfst-compile-on-x86_32.patch

%description
OpenFst is a library for constructing, combining, optimizing, and searching 
weighted finite-state transducers (FSTs). Weighted finite-state transducers
are automata where each transition has an input label, an output label, and
a weight.

This library was developed at Google Research (M. Riley, J. Schalkwyk, W.
Skut) and NYU's Courant Institute (C. Allauzen, M. Mohri). It is intended
to be comprehensive, flexible, efficient and scale well to large problems.

%install -a
%libpackages

sed -i -e '/fst\/script\//d' %{specpartsdir}/%{mklibname -d fst}.specpart
echo '%{_libdir}/fst' >>%{specpartsdir}/%{mklibname -d fst}.specpart
echo %{_includedir}/fst/script >>%{specpartsdir}/%{mklibname -d fstscript}.specpart
sed -i -e '/^Group:/aRequires: %{mklibname -d fst} = %{EVRD}' %{specpartsdir}/%{mklibname -d fstscript}.specpart

%if %{with compat32}
sed -i -e '/fst\/script\//d' %{specpartsdir}/%{mklib32name -d fst}.specpart
echo '%{_prefix}/lib/fst' >>%{specpartsdir}/%{mklib32name -d fst}.specpart
sed -i -e '/^Group:/aRequires: %{mklibname -d fst} = %{EVRD}' %{specpartsdir}/%{mklib32name -d fst}.specpart
sed -i -e '/^Group:/aRequires: %{mklib32name -d fst} = %{EVRD}' %{specpartsdir}/%{mklib32name -d fstscript}.specpart
sed -i -e '/^Group:/aRequires: %{mklibname -d fstscript} = %{EVRD}' %{specpartsdir}/%{mklib32name -d fstscript}.specpart
%endif

%files
%{_bindir}/*
