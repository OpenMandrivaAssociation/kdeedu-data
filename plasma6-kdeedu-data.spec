#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Data files for the KDE educational suite
Name:		plasma6-kdeedu-data
Version:	24.02.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/kdeedu-data/-/archive/%{gitbranch}/kdeedu-data-%{gitbranchd}.tar.bz2#/kdeedu-data-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdeedu-data-%{version}.tar.xz
%endif
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	ninja
BuildArch:	noarch

%description
Data files for the KDE educational suite

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kdeedu-data-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build

%files
%{_datadir}/apps/kvtml
%{_datadir}/icons/*/*/*/*
