%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Data files for the KDE educational suite
Name:		kdeedu-data
Version:	24.02.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	ninja
BuildArch:	noarch

%description
Data files for the KDE educational suite

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%files
%{_datadir}/apps/kvtml
%{_datadir}/icons/*/*/*/*
