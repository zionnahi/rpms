# Authority: dag

Summary: Linux program for uncompressing *.ace files.
Name: unace
Version: 2.20
Release: 0
License: Shareware
Group: Applications/Archiving
URL: http://www.winace.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.maxeline.com/winace/linunace22.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: i386
ExclusiveArch: i386

%description
A compression tool that crunches the last free bit from your data, but takes
twice to ten times longer for compressing and - even worse - for extracting
your data probably will not work for you - or your customers.
 
On the other hand, a compression tool that deflates your files as quick as
lightning but leaves a lot of "air" in the compressed file will not take you
far either.

%prep
%setup -c -n %{name}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 unace %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*

%changelog
* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 2.20-0
- Initial package. (using DAR)
