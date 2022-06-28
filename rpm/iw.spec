Name:       iw
Summary:    A nl80211 based wireless configuration tool
Version:    5.0.1
Release:    2
License:    ISC
URL:        https://github.com/sailfishos/iw
Source0:    %{name}-%{version}.tar.bz2
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
