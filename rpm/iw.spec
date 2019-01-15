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

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
Man page for %{name}.

%prep
%setup -q -n %{name}-%{version}/iw

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} README

%files
%defattr(-,root,root,-)
%license COPYING
%{_sbindir}/iw

%files doc
%defattr(-,root,root,-)
%{_mandir}/man8/%{name}.*
%{_docdir}/%{name}-%{version}
