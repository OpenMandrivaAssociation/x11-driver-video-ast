%define _disable_ld_no_undefined 1
%global optflags %{optflags} -Wno-error -Wno-implicit-function-declaration

Summary:	X.org driver for ASPEED Technology Inc
Name:		x11-driver-video-ast
Version:	1.1.6
Release:	1
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-ast-%{version}.tar.xz

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-ast is the X.org driver for ASPEED Technology Inc.

%prep
%setup -qn xf86-video-ast-%{version}
%autopatch -p1

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/ast_drv.so
