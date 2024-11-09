%define		qt_ver		5.12.0
Summary:	KDiagram - libraries for creating business charts
Summary(pl.UTF-8):	KDiagram - biblioteki do tworzenia diagramów biznesowych
Name:		kdiagram-qt5
# keep 2.x here for Qt5
Version:	2.8.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/kdiagram/%{version}/kdiagram-%{version}.tar.xz
# Source0-md5:	a63593335d382d4c6518e1a98a9e013f
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5PrintSupport-devel >= %{qt_ver}
BuildRequires:	Qt5Svg-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 5.60.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5PrintSupport >= %{qt_ver}
Requires:	Qt5Svg >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The KDiagram Libraries consist of KChart, a library for creating
business charts, and KGantt, a library for creating Gantt diagrams.

%description -l pl.UTF-8
Biblioteki KDiagram składają się z biblioteki KChart do tworzenia
wykresów biznesowych oraz biblioteki KGantt do tworzenia diagramów
Gantta.

%package devel
Summary:	Header files for KDiagram development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających bibliotek KDiagram
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qt_ver}
Requires:	Qt5PrintSupport-devel >= %{qt_ver}
Requires:	Qt5Svg-devel >= %{qt_ver}
Requires:	Qt5Widgets-devel >= %{qt_ver}

%description devel
Header files for KDiagram development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających bibliotek KDiagram.

%prep
%setup -q -n kdiagram-%{version}

%build
install -d build
cd build
%cmake .. \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# kchart_qt and kgantt_qt qm domains
%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libKChart.so.2.*.*
%ghost %{_libdir}/libKChart.so.2
%attr(755,root,root) %{_libdir}/libKGantt.so.2.*.*
%ghost %{_libdir}/libKGantt.so.2

%files devel
%defattr(644,root,root,755)
%{_libdir}/libKChart.so
%{_libdir}/libKGantt.so
%{_includedir}/KChart
%{_includedir}/KGantt
%{_includedir}/kchart_version.h
%{_includedir}/kgantt_version.h
%{_libdir}/cmake/KChart
%{_libdir}/cmake/KGantt
%{_libdir}/qt5/mkspecs/modules/qt_KChart.pri
%{_libdir}/qt5/mkspecs/modules/qt_KGantt.pri
