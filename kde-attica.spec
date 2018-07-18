%define attica_major 0
%define attica_minor 4
%define attica_patchversion 2

%define libattica %mklibname kde4-attica %{attica_major}.%{attica_minor}
%define oldlibattica %mklibname attica 0
%define attica_devel %mklibname kde4-attica -d

%define module  attica

Summary:		Open Collaboration Service providers library
Name:		kde4-attica
Version:		%{attica_major}.%{attica_minor}.%{attica_patchversion}
Release:		1
License: 		GPLv2+
Group:		System/Base
Source0:		http://download.kde.org/stable/attica/%{module}-%{version}.tar.bz2
URL:			https://projects.kde.org/projects/kdesupport/attica
BuildRequires:	pkgconfig(QtCore) < 5.0.0
BuildRequires:	pkgconfig(QtNetwork) < 5.0.0
BuildRequires:	pkgconfig(QtTest) < 5.0.0
BuildRequires:	cmake

%description
A library to access Open Collaboration Service providers.
Required to access OSC providers in get hot new stuff in KDE4.

#--------------------------------------------------------------------

%package -n %{libattica}
Summary:		Qt library that implements the Open Collaboration Services API
Group:		System/Libraries

Obsoletes:		%oldlibattica < 0.4.1-2
Obsoletes:		%{_lib}attica0.4 < 0.4.3

%description -n %{libattica}
A library to access Open Collaboration Service providers
Required to access OSC providers in get hot new stuff.

%files -n %{libattica}
%{_libdir}/libattica.so.%{attica_major}.%{attica_minor}*

#--------------------------------------------------------------------

%package -n %{attica_devel}
Summary:		Devel stuff for %{module}
Group:		Development/KDE and Qt
Requires:		%{libattica} = %{EVRD}
Obsoletes:		attica-devel < 0.3.0
Provides:		attica-devel = %{EVRD}

%description -n %{attica_devel}
This package contains header files needed if you wish to build applications
based on %{module}.

%files -n %attica_devel
%{_includedir}/attica
%{_libdir}/libattica.so
%{_libdir}/pkgconfig/libattica.pc

#--------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%cmake_qt4 -DQT4_BUILD=ON
%make

%install
%makeinstall_std -C build
