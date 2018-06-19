%global __requires_exclude_from ^%{_docdir}/.*$

Name:           lastpass-cli
Version:        1.3.1
Release:        1%{?dist}
Summary:        Command line interface to LastPass (Free, Premium, and Enterprise)

License:        GPLv2
URL:            https://github.com/LastPass/lastpass-cli
Source0:        https://github.com/lastpass/lastpass-cli/archive/v%{version}.tar.gz#/lastpass-cli-%{version}.tar.gz

BuildRequires:  openssl
BuildRequires:  libcurl
BuildRequires:  libxml2
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libcurl-devel
BuildRequires:  asciidoc
BuildRequires:  pkgconfig
BuildRequires:  bash-completion
Requires:       /usr/bin/pinentry
# /usr/bin/xclip isn't available in EPEL
%{?fedora:Requires: /usr/bin/xclip}

%description
A command line interface to LastPass (Free, Premium, and Enterprise)

%prep
%setup -q


%build
CFLAGS="${CFLAGS:-%optflags}" LDFLAGS="${LDFLAGS:-%__global_ldflags}" make %{?_smp_mflags}


%install
%make_install install-doc

# Setup bash completion
bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
install -Dpm 644 contrib/lpass_bash_completion %{buildroot}$bashcompdir/lpass


%files
%{_bindir}/lpass
%{_mandir}/man1/lpass.1.*
%license COPYING
%license LICENSE.OpenSSL
%doc README.md
%doc CONTRIBUTING
%doc contrib/examples
%{_datadir}/bash-completion/


%changelog
* Tue Jun 19 2018 Ventz Petkov - 1.3.1-1
- Updated package to latest 1.3.1
- Includes fixes (see release notes):
-- https://github.com/lastpass/lastpass-cli/releases/tag/v1.3.1

* Fri Apr 13 2018 Ventz Petkov - 1.3.0-1
- Taking over LastPass-CLI EPEL package
- Updated package to latest 1.3.0
- Includes fixes (see release notes):
-- https://github.com/lastpass/lastpass-cli/releases/tag/v1.3.0
-- https://github.com/lastpass/lastpass-cli/releases/tag/v1.2.2
-- https://github.com/lastpass/lastpass-cli/releases/tag/v1.2.1
-- https://github.com/lastpass/lastpass-cli/releases/tag/v1.2.0
-- https://github.com/lastpass/lastpass-cli/releases/tag/v1.1.2
-- https://github.com/lastpass/lastpass-cli/releases/tag/v1.1.1
-- https://github.com/lastpass/lastpass-cli/releases/tag/v1.1.0
-- https://github.com/lastpass/lastpass-cli/releases/tag/v1.0.0
-- https://github.com/lastpass/lastpass-cli/releases/tag/v0.9.0

* Mon Jan 04 2016 Tom Prince - 0.8.0-1
- Version number bump
- Install bash completions

* Thu Dec 24 2015 Tom Prince - 0.7.0-3
- Remove xclip dependency for EPEL.

* Sun Dec 6 2015 Tom Prince - 0.7.0-2
- Address review comments.

* Mon Nov 16 2015 Tom Prince - 0.7.0-1
- Version number bump

* Wed Oct 7 2015 Tom Prince - 0.6.0-1
- Version number bump

* Tue Dec 30 2014 Rohan Ferris - 0.4.0-2
- Include asciidoc

* Tue Dec 30 2014 Rohan Ferris - 0.4.0-1
- Version number bump

* Fri Nov  7 2014 Rohan Ferris
- Initial packaging.
