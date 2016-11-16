%define _disable_ld_no_undefined 1

Summary:	X.org driver for ASPEED Technology Inc
Name:		x11-driver-video-ast
Version:	1.1.5
Release:	3
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-ast-%{version}.tar.bz2

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-ast is the X.org driver for ASPEED Technology Inc.

%prep
%setup -qn xf86-video-ast-%{version}
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/ast_drv.so
