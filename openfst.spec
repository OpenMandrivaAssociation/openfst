Name:           openfst
Summary:        Weighted finite-state transducer tools
Version:        1.8.3
Release:        1
Source0:        https://www.openfst.org/twiki/pub/FST/FstDownload/openfst-%{version}.tar.gz
URL:		http://www.openfst.org/
Group:          System/Libraries
License:        Apache-2.0
BuildSystem:	autotools

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
echo %{_includedir}/fst/script >>%{specpartsdir}/%{mklibname -d fstscript}.specpart
sed -i -e '/^Group:/aRequires: %{mklibname -d fst} = %{EVRD}' %{specpartsdir}/%{mklibname -d fstscript}.specpart

%files
%{_bindir}/*
