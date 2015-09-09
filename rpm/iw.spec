Name:       iw
Summary:    A nl80211 based wireless configuration tool
Version:    4.1
Release:    2
Group:      System/Networking
License:    ISC
URL:        http://wireless.kernel.org/en/users/Documentation/iw
Source0:    http://wireless.kernel.org/download/iw/iw-%{version}.tar.bz2
BuildRequires:  pkgconfig(libnl-3.0)
Provides:  wireless-tools > 29
Obsoletes:  wireless-tools <= 29

%description
iw is a new nl80211 based CLI configuration utility for wireless devices.
Currently you can only use this utility to configure devices which use a
mac80211 driver as these are the new drivers being written - only because most
new wireless devices being sold are now SoftMAC.



%prep
%setup -q -n %{name}-%{version}

%build
cd %{name}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
cd %{name}
%make_install


%files
%defattr(-,root,root,-)
%doc %{name}/COPYING
%doc %{name}/README
%{_sbindir}/iw
%{_mandir}/man8/iw.8.gz
