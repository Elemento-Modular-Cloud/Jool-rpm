Name:           jool-dkms
Version:        %{module_version}
Release:        1%{?dist}
Summary:        Jool NAT64/SIIT kernel module (DKMS)
License:        GPL-2.0
BuildArch:      noarch
Source0:        jool-%{version}.tar.gz

# DKMS will pull in gcc and make as its own dependencies
Requires:       dkms
Requires:       kernel-devel
Requires:       kernel-headers

%description
Jool kernel module, built on the user's machine via DKMS.

%prep
%autosetup -n jool-%{version}

%install
install -d %{buildroot}/usr/src/jool-%{version}/
cp -r . %{buildroot}/usr/src/jool-%{version}/

%post
dkms add     /usr/src/jool-%{version} --rpm_safe_upgrade
dkms build   -m jool -v %{jool_version}
dkms install -m jool -v %{jool_version}

%preun
dkms remove -m jool -v %{jool_version} --all --rpm_safe_upgrade || true

%files
/usr/src/jool-%{version}/

%changelog
* %(date "+%a %b %d %Y") CI Build <ci@example.com> - %{version}-1
- Automated DKMS package build
