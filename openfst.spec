%define name    openfst
%define version 1.1
%define release %mkrel 3

Name:           %{name}
Summary:        Weighted finite-state transducer tools
Version:        %{version} 
Release:        %{release} 
Source0:        %{name}-%{version}.tar.gz
Patch0:		openfst-1.1-fix-linking.patch
URL:		http://www.openfst.org/
Group:          System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:        Apache

%description
OpenFst is a library for constructing, combining, optimizing, and searching 
weighted finite-state transducers (FSTs). Weighted finite-state transducers
are automata where each transition has an input label, an output label, and
a weight.

This library was developed at Google Research (M. Riley, J. Schalkwyk, W.
Skut) and NYU's Courant Institute (C. Allauzen, M. Mohri). It is intended
to be comprehensive, flexible, efficient and scale well to large problems.

%package        devel
Summary:        Development files from %name
Group:          Development/C++
Requires:	%{name} = %{version}

%description    devel
Static library and header files from %name.

%prep
%setup -q -n %name-%{version}
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS NEWS
%{_bindir}/*
%{_libdir}/*.so.0*

%files devel
%defattr(-,root,root)
%{_includedir}/fst
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
