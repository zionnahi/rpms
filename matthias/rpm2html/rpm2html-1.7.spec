# Authority: dag

# Dists: rh73
# SourceDists: rh73

Summary: Translates an RPM database and dependency information into HTML.
Name: rpm2html
Version: 1.7
Release: 0
Group: Applications/System
License: MIT
URL: http://rpmfind.net/linux/rpm2html/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://rpmfind.net/pub/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: rpm-devel, db3-devel

%description
The rpm2html utility automatically generates web pages that describe a
set of RPM packages.  The goals of rpm2html are to identify the
dependencies between various packages, and to find the package(s) that
will provide the resources needed to install a given package.
Rpm2html analyzes the provides and requires of the given set of RPMs,
and then shows the dependency cross-references using hypertext links.
Rpm2html can now dump the metadata associated with RPM files into
standard RDF files.

Install rpm2html if you want a utility for translating information
from an RPM database into HTML.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags} %{?rh73: LIBXML_FLAGS="-I/usr/include/libxml2 -I/usr/include/libxml2/libxml"}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
		%{buildroot}%{_sysconfdir} \
		%{buildroot}%{_datadir}/rpm2html \
		%{buildroot}%{_mandir}/man1
%{__install} -s -m0755 rpm2html %{buildroot}%{_bindir}
%{__install} -m0644 rpm2html.config  %{buildroot}%{_sysconfdir}
%{__install} -m0644 rpm2html.1  %{buildroot}%{_mandir}/man1

for i in msg.*; do
  %{__install} -m0644 $i %{buildroot}%{_datadir}/rpm2html/msg.$ll
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES PRINCIPLES README TODO 
%doc rpm2html-cdrom.config rpm2html-en.config
%doc %{_mandir}/man1/*
%config %{_sysconfdir}/rpm2html.config
%{_bindir}/*
%{_datadir}/rpm2html/

%changelog
* Mon Feb 10 2003 Dag Wieers <dag@wieers.com> - 1.7
- Initial package. (using DAR}
