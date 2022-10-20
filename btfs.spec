Name:           btfs
Version:        2.24
Release:        1%{?dist}
Summary:        A bittorrent filesystem based on FUSE

License:        GPLv3
URL:            https://github.com/johang/btfs
Source0:        %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++

BuildRequires:  fuse-devel
BuildRequires:  libcurl-devel
BuildRequires:  rb_libtorrent-devel

%description
With BTFS, you can mount any .torrent file or magnet link and then use it as
any read-only directory in your file tree. The contents of the files will be
downloaded on-demand as they are read by applications. Tools like ls, cat
and cp works as expected. Applications like vlc and mplayer
can also work without changes.

%prep
%autosetup


%build
autoreconf -i
%configure
%make_build


%install
%make_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}stat
%{_bindir}/btplay
%{_mandir}/man1/%{name}.*



%changelog
* Thu Oct 20 2022 ElXreno <elxreno@gmail.com>
- Initial packaging
