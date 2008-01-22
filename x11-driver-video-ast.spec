Name: x11-driver-video-ast
Version: 0.81.0
Release: %mkrel 5
Summary: The X.org driver for ASPEED Technology Inc
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-video-ast-0.81.0@mandriva suggested on upstream
# Tag at git checkout 8bbdddf6025e1421e91ce12c509840822b395fb6
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-ast  xorg/drivers/xf86-video-ast
# cd xorg/drivers/xf86-video/ast
# git-archive --format=tar --prefix=xf86-video-ast-0.81.0/ xf86-video-ast-0.81.0@mandriva | bzip2 -9 > xf86-video-ast-0.81.0.tar.bz2
########################################################################
Source0: xf86-video-ast-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-ast-0.81.0@mandriva..origin/mandriva+gpl
Patch1: 0001-modified-ChangeLog.patch
Patch2: 0002-Add-to-.gitignore-to-skip-patch-emacs-droppings.patch
Patch3: 0003-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for ASPEED Technology Inc

%prep
%setup -q -n xf86-video-ast-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/ast_drv.so
