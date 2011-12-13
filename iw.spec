# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       iw
Summary:    A nl80211 based wireless configuration tool
Version:    0.9.22
Release:    1
Group:      System/Networking
License:    ISC
URL:        http://wireless.kernel.org/en/users/Documentation/iw
Source0:    http://wireless.kernel.org/download/iw/iw-%{version}.tar.bz2
Source100:  iw.yaml
BuildRequires:  pkgconfig(libnl-1)


%description
iw is a new nl80211 based CLI configuration utility for wireless devices.
Currently you can only use this utility to configure devices which use a
mac80211 driver as these are the new drivers being written - only because most
new wireless devices being sold are now SoftMAC.




%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre


make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post






%files
%defattr(-,root,root,-)
%doc COPYING
%doc README
%{_sbindir}/iw
%{_mandir}/man8/iw.8.gz
# >> files
# << files


