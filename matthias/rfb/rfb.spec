# Authority: dag
# Distcc: 0

%define dfi %(which desktop-file-install &>/dev/null; echo $?)
%define _bindir /usr/X11R6/bin

Summary: heXoNet RFB (remote control for the X Window System)
Name: rfb
Version: 0.6.1
Release: 4
License: GPL
Group: User Interface/Desktops
URL: http://www.hexonet.de/software/rfb/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download.hexonet.com/software/rfb/%{name}-%{version}.tar.gz
Patch: rfb-0.6.1-rpmoptflags.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%{?rhfc1:BuildRequires: compat-gcc-c++}
%{?rhel3:BuildRequires: compat-gcc-c++}
%{?rh90:BuildRequires: compat-gcc-c++}
%{?rh80:BuildRequires: compat-gcc-c++}
BuildRequires: libxclass

### Fix problem with apt requiring compat-gcc-c++ (Panu)
Requires: compat-libstdc++

%description
The heXoNet RFB Software package includes many different projects. The
goal of this package is to provide a comprehensive collection of
rfb-enabled tools and applications. One application, x0rfbserver, was,
and maybe still is, the only complete remote control solution for the
X Window System.

%prep
%setup
%patch0 -p1

%{__cat} <<EOF >x0rfbserver.desktop
[Desktop Entry]
Name=Run VNC Server
Comment=Make current X session available via VNC
Icon=redhat-system_tools.png
Exec=x0rfbserver
Terminal=false
Type=Application
Categories=GNOME;System;Application;
EOF

%{__cat} <<EOF >xvncconnect.desktop
[Desktop Entry]
Name=Run VNC Viewer
Comment=Connect to a VNC server
Icon=redhat-system_tools.png
Exec=xvncconnect
Terminal=false
Type=Application
Categories=GNOME;System;Application;
EOF

%build
### FIXME: Workaround for RH80 and RH9
%{?rhfc1:export CXXFLAGS="&>/dev/null; g++296 -D\$(USE_ZLIB) `xc-config --cflags` -I../include -finline-functions -funroll-loops %{optflags}"}
%{?rhel3:export CXXFLAGS="&>/dev/null; g++296 -D\$(USE_ZLIB) `xc-config --cflags` -I../include -finline-functions -funroll-loops %{optflags}"}
%{?rh90:export CXXFLAGS="&>/dev/null; g++296 -D\$(USE_ZLIB) `xc-config --cflags` -I../include -finline-functions -funroll-loops %{optflags}"}
%{?rh80:export CXXFLAGS="&>/dev/null; g++296 -D\$(USE_ZLIB) `xc-config --cflags` -I../include -finline-functions -funroll-loops %{optflags}"}
%{?rhfc1:export CXX="g++296"}
%{?rhel3:export CXX="g++296"}
%{?rh90:export CXX="g++296"}
%{?rh80:export CXX="g++296"}
%{__make} %{?_smp_mflags} depend all

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1 \
			%{buildroot}%{_bindir}
%{__install} -m0644 man/man1/* %{buildroot}%{_mandir}/man1
%{__install} -s -m0755 x0rfbserver/x0rfbserver %{buildroot}%{_bindir}
%{__install} -s -m0755 xvncconnect/xvncconnect %{buildroot}%{_bindir}
%{__install} -s -m0755 xrfbviewer/{xrfbviewer,xplayfbs} %{buildroot}%{_bindir}
%{__install} -s -m0755 rfbcat/rfbcat %{buildroot}%{_bindir}

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Utilities/
	%{__install} -m0644 x0rfbserver.desktop xvncconnect.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/
%else
        install -d -m0755 %{buildroot}%{_datadir}/applications
        desktop-file-install --vendor "gnome"              \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                x0rfbserver.desktop xvncconnect.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README rfm_fbs.1.0.html
%doc %{_mandir}/man?/*
%{_bindir}/*
%if %{dfi}
	%{_datadir}/gnome/apps/Utilities/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif

%changelog
* Mon Jan 19 2004 Dag Wieers <dag@wieers.com> - 0.6.1-4
- Added desktop-files.
- Added requirements for compat-libstdc++.

* Tue Dec 02 2003 Dag Wieers <dag@wieers.com> - 0.6.1-3
- Rebuild against libxclass-0.8.2.

* Sat Apr 05 2003 Dag Wieers <dag@wieers.com> - 0.6.1-2
- Statically linked to libxclass, removing xclass dependency.

* Sun Dec 15 2002 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Initial package. (using DAR)
