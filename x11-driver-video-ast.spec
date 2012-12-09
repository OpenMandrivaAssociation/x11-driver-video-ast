Name: x11-driver-video-ast
Version: 0.97.0
Release: 2
Summary: X.org driver for ASPEED Technology Inc
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-ast-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-ast is the X.org driver for ASPEED Technology Inc.

%prep
%setup -qn xf86-video-ast-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/ast_drv.so


%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.97.0-1
+ Revision: 810719
- version update 0.97.0

* Fri Jul 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.96.0-1
+ Revision: 808299
- version update 0.96.0

  + Bernhard Rosenkraenzer <bero@bero.eu>
    - 0.95.00

* Wed Apr 04 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.95.0-1
+ Revision: 789259
- Update to 0.95.0

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.93.10-2
+ Revision: 787194
- Build for x11-server 1.12

* Sun Mar 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.93.10-1
+ Revision: 786706
- version update 0.93.10

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.93.9-1
+ Revision: 748377
- new version 0.93.9
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.91.10-6
+ Revision: 703652
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.91.10-5
+ Revision: 683561
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.91.10-4
+ Revision: 671141
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 0.91.10-3mdv2011.0
+ Revision: 595736
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 0.91.10-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Aug 17 2010 Thierry Vignaud <tv@mandriva.org> 0.91.10-1mdv2011.0
+ Revision: 570774
- new release

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 0.89.9-1mdv2010.0
+ Revision: 407727
- new release

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 0.87.0-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Tue Dec 23 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 0.87.0-1mdv2009.1
+ Revision: 317839
- New version 0.87.0

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.85.0-2mdv2009.0
+ Revision: 265902
- rebuild early 2009.0 package (before pixel changes)
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.85.0-1mdv2009.0
+ Revision: 194214
- Update to version 0.85.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.81.0-6mdv2008.1
+ Revision: 165483
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.81.0-5mdv2008.1
+ Revision: 156598
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.81.0-4mdv2008.1
+ Revision: 154894
- Updated BuildRequires and resubmit package.
- Update release as there is no official newer version (just git head patches).
  Also Update build requires to, hopefully, match final spec format for some
  time.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Fix improper version bump as there is no official version yet, and correct
  @mandriva tags in git repository.
- Note local tag xf86-video-ast-0.81.0.0@mandriva suggested on upstream
  Tag at git checkout 8bbdddf6025e1421e91ce12c509840822b395fb6
  This also updates to 0.84.7 version, that has no tag on upstream, therefore
  no local tag was also added. Assuming that patch1 is correct, but still
  adding it to the rpm so that it still can be reverted to previous version,
  but assuming it is correct due to the long time since any other "functional"
  change to the repository files.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.81.0-3mdv2008.1
+ Revision: 98685
- minor spec cleanup
- build against new xserver (1.4)

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.81.0-2mdv2008.0
+ Revision: 75738
- rebuild

