%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Data files for the KDE educational suite
Name:		plasma6-kdeedu-data
Version:	24.01.85
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdeedu-data-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	ninja
BuildArch:	noarch

%description
Data files for the KDE educational suite

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kdeedu-data-%{version}

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
