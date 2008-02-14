%define name    openfst
%define version 0.0.beta
%define release %mkrel 1

Name:           %{name} 
Summary:        Weighted finite-state transducer tools
Version:        %{version} 
Release:        %{release} 
Source0:        %{name}-beta-iupr.tar.bz2
URL:		http://www.openfst.org/

Group:          System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:        Apache
BuildRequires:	chrpath

## Packager note:
## This is the autoconf-enabled version produced at http://www.iupr.org/

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

%description    devel
Static library and header files from %name.

%prep 
%setup -q -n %name/fst

%build 
%configure2_5x
%make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_libdir
%makeinstall
chrpath -d %buildroot/%_bindir/*

%clean 
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc README* ChangeLog*
%{_bindir}/*

%files devel
%defattr(-,root,root)
%{_includedir}/fst
%{_libdir}/*.so
%{_libdir}/*.a
