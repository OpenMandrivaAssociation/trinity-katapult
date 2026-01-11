%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg katapult
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:		0.3.2.1
Release:		%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Faster access to applications, bookmarks, and other items.
Group:			Applications/Utilities
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/system/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

%description
Katapult is an application for TDE, designed to allow faster access to
applications, bookmarks, and other items. It is plugin-based, so it can
launch anything that is has a plugin for. Its display is driven by
plugins as well, so its appearance is completely customizable. It was
inspired by Quicksilver for OS X. 


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg}

# Removes useless files (-devel ?)
%__rm -f %{?buildroot}%{tde_prefix}/%{_lib}/*.so
%__rm -f %{?buildroot}%{tde_prefix}/%{_lib}/*.la

# Fix desktop files (openSUSE only)
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/%{tde_pkg}.desktop"


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_prefix}/bin/katapult
%{tde_prefix}/%{_lib}/libkatapult.so.2
%{tde_prefix}/%{_lib}/libkatapult.so.2.0.0
%{tde_prefix}/%{_lib}/trinity/katapult_amarokcatalog.la
%{tde_prefix}/%{_lib}/trinity/katapult_amarokcatalog.so
%{tde_prefix}/%{_lib}/trinity/katapult_bookmarkcatalog.la
%{tde_prefix}/%{_lib}/trinity/katapult_bookmarkcatalog.so
%{tde_prefix}/%{_lib}/trinity/katapult_calculatorcatalog.la
%{tde_prefix}/%{_lib}/trinity/katapult_calculatorcatalog.so
%{tde_prefix}/%{_lib}/trinity/katapult_documentcatalog.la
%{tde_prefix}/%{_lib}/trinity/katapult_documentcatalog.so
%{tde_prefix}/%{_lib}/trinity/katapult_execcatalog.la
%{tde_prefix}/%{_lib}/trinity/katapult_execcatalog.so
%{tde_prefix}/%{_lib}/trinity/katapult_glassdisplay.la
%{tde_prefix}/%{_lib}/trinity/katapult_glassdisplay.so
%{tde_prefix}/%{_lib}/trinity/katapult_googlecatalog.la
%{tde_prefix}/%{_lib}/trinity/katapult_googlecatalog.so
%{tde_prefix}/%{_lib}/trinity/katapult_o2display.la
%{tde_prefix}/%{_lib}/trinity/katapult_o2display.so
%{tde_prefix}/%{_lib}/trinity/katapult_programcatalog.la
%{tde_prefix}/%{_lib}/trinity/katapult_programcatalog.so
%{tde_prefix}/%{_lib}/trinity/katapult_puredisplay.la
%{tde_prefix}/%{_lib}/trinity/katapult_puredisplay.so
%{tde_prefix}/%{_lib}/trinity/katapult_spellcatalog.la
%{tde_prefix}/%{_lib}/trinity/katapult_spellcatalog.so
%{tde_prefix}/share/applications/tde/katapult.desktop
%{tde_prefix}/share/icons/crystalsvg/128x128/actions/katapultspellcheck.png
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/katapultspellcheck.svgz
%{tde_prefix}/share/icons/hicolor/128x128/actions/checkmark.png
%{tde_prefix}/share/icons/hicolor/128x128/actions/no.png
%{tde_prefix}/share/icons/hicolor/128x128/apps/xcalc.png
%{tde_prefix}/share/icons/hicolor/*/apps/katapult.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/katapult.svgz
%{tde_prefix}/share/services/katapult_amarokcatalog.desktop
%{tde_prefix}/share/services/katapult_bookmarkcatalog.desktop
%{tde_prefix}/share/services/katapult_calculatorcatalog.desktop
%{tde_prefix}/share/services/katapult_documentcatalog.desktop
%{tde_prefix}/share/services/katapult_execcatalog.desktop
%{tde_prefix}/share/services/katapult_glassdisplay.desktop
%{tde_prefix}/share/services/katapult_googlecatalog.desktop
%{tde_prefix}/share/services/katapult_o2display.desktop
%{tde_prefix}/share/services/katapult_programcatalog.desktop
%{tde_prefix}/share/services/katapult_puredisplay.desktop
%{tde_prefix}/share/services/katapult_spellcatalog.desktop
%{tde_prefix}/share/servicetypes/katapultcatalog.desktop
%{tde_prefix}/share/servicetypes/katapultdisplay.desktop
%{tde_prefix}/share/man/man1/*.1*
%{tde_prefix}/share/doc/tde/HTML/en/katapult/

