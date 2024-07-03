#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v10
# autospec commit: 5905be9
#
Name     : gimp
Version  : 2.10.38
Release  : 128
URL      : https://download.gimp.org/mirror/pub/gimp/v2.10/gimp-2.10.38.tar.bz2
Source0  : https://download.gimp.org/mirror/pub/gimp/v2.10/gimp-2.10.38.tar.bz2
Summary  : GIMP Library
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-3.0
BuildRequires : alsa-lib-dev
BuildRequires : appstream-glib
BuildRequires : buildreq-configure
BuildRequires : bzip2-dev
BuildRequires : desktop-file-utils
BuildRequires : docbook-xml
BuildRequires : gdk-pixbuf
BuildRequires : gegl-dev
BuildRequires : gettext
BuildRequires : ghostscript-dev
BuildRequires : glib-networking
BuildRequires : gtk+
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : gtk3-bin
BuildRequires : gtk3-dev
BuildRequires : intltool
BuildRequires : lcms2-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libmypaint-dev
BuildRequires : libwebp-dev
BuildRequires : libxslt-bin
BuildRequires : mypaint-brushes
BuildRequires : mypaint-brushes-dev
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(atk)
BuildRequires : pkgconfig(babl-0.1)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-pdf)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gexiv2)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gmodule-no-export-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(pangoft2)
BuildRequires : pkgconfig(shared-mime-info)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xmu)
BuildRequires : pkgconfig(xpm)
BuildRequires : poppler
BuildRequires : poppler-data-clr-rename-dev
BuildRequires : poppler-dev
BuildRequires : tiff-dev
BuildRequires : webkitgtk-dev
BuildRequires : xdg-utils
BuildRequires : xvfb-run
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: fastmath.patch
Patch2: buffer.patch
Patch3: floataintdouble.patch

%description
------------------------------
GNU Image Manipulation Program
2.10 Stable Branch
------------------------------

%prep
%setup -q -n gimp-2.10.38
cd %{_builddir}/gimp-2.10.38
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
pushd ..
cp -a gimp-2.10.38 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1714748845
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --without-libtiff --disable-python --enable-sse --with-script-fu --enable-bundled-mypaint-brushes  --without-cairo-pdf --disable-gtk-doc-pdf --sysconfdir=/usr/share/defaults/gimp
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --without-libtiff --disable-python --enable-sse --with-script-fu --enable-bundled-mypaint-brushes  --without-cairo-pdf --disable-gtk-doc-pdf --sysconfdir=/usr/share/defaults/gimp
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1714748845
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gimp
cp %{_builddir}/gimp-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gimp/0dd432edfab90223f22e49c02e2124f87d6f0a56 || :
cp %{_builddir}/gimp-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/gimp/d0836463afc5e3d4bde884de8bff3be3998db6d1 || :
cp %{_builddir}/gimp-%{version}/libgimp/COPYING %{buildroot}/usr/share/package-licenses/gimp/a393f03af92371f6aa7c379c82077fe419283aa1 || :
cp %{_builddir}/gimp-%{version}/plug-ins/file-dds/COPYING %{buildroot}/usr/share/package-licenses/gimp/093f1a5009a4ff69e9075fd00aa29968778315cf || :
cp %{_builddir}/gimp-%{version}/plug-ins/script-fu/ftx/LICENSE %{buildroot}/usr/share/package-licenses/gimp/8d629cc7c615f0311a8a93c37d754d1ccb8c47cb || :
cp %{_builddir}/gimp-%{version}/plug-ins/script-fu/tinyscheme/COPYING %{buildroot}/usr/share/package-licenses/gimp/caf3c22163d024d0943740fd0c1b1c80513fea7b || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## install_append content
for i in %{buildroot}/usr/share/gimp/2.0/icons/*; do  /usr/bin/gtk-update-icon-cache $i ; done
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
