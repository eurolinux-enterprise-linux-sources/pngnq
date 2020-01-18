Name: pngnq
Summary: Pngnq is a tool for quantizing PNG images in RGBA format
Version: 1.1
Release: 7%{?dist}
License: BSD with advertising and MIT and BSD
Group: Applications/Multimedia
URL: http://pngnq.sourceforge.net/
Source0: http://downloads.sourceforge.net/pngnq/pngnq-%{version}.tar.gz
Patch0: pngnq-libpng15.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libpng-devel

%description
Pngnq is a tool for quantizing PNG images in RGBA format.

The neuquant algorithm uses a neural network to optimise the color
map selection. This is fast and quite accurate, giving good results
on many types of images.

%prep
%setup -q
%patch0 -p1 -b .libpng15

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README*
%{_bindir}/*
%{_mandir}/man1/*1*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Nils Philippsen <nils@redhat.com> - 1.1-6
- update sourceforge download URL

* Wed Aug 01 2012 Jon Ciesla <limburgher@gmail.com> - 1.1-5
- Tom Lane's libpng15 fixes, BZ 843655.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.1-2
- Rebuild for new libpng

* Thu Jun 23 2011 - Gerd Hoffmann <kraxel@redhat.com> - 1.1-1
- Update to version 1.1 (#714728).

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 16 2010 - Gerd Hoffmann <kraxel@redhat.com> - 0.5-8
- Fix FTBFS by adding -lz -lm to ldlibs (#564721).

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 3 2008 - Gerd Hoffmann <kraxel@redhat.com> - 0.5-5.fc9
- add comments to the patches.
- fix rpm macro usage.

* Fri Oct 31 2008 - Gerd Hoffmann <kraxel@redhat.com> - 0.5-4.fc9
- Updated Licence tag, according to advice from fedora-legal.

* Fri Oct 31 2008 - Gerd Hoffmann <kraxel@redhat.com> - 0.5-3.fc9
- Use $RPM_OPT_FLAGS.
- Also package up pngcomp.

* Wed Oct 15 2008 - Gerd Hoffmann <kraxel@redhat.com> - 0.5-2.fc9
- add dist tag to release.
- fix rpmlint warnings.
- TODO: licence to be clarified.

* Mon Jul 26 2008 - Patrick Steiner <patrick.steiner@a1.net> - 0.5-1
- Initial package.
