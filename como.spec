# Internal QML imports
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.KWin\\.Effect\\.WindowView.*

%global commit 33c6450166d0ec56b7261016358909d245e488f4
%global kf6_version 6.0.0
%define qt6_version 6.6.0
%define wlr_version 0.19

Name:           como
Version:        0.2.80
Release:        0
Summary:        The Compositor Modules (COMO)
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/winft/%{name}
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         find-wlroots.patch
# Patch1:         remove-breeze-tabbox.patch
# Patch2:         path.patch
Patch3:         add-effect-config.patch
Patch4:         drop-wlr-renderer.patch
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(Breeze) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KDecoration2) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
# BuildRequires:  cmake(KF6ConfigWidgets) >= %%{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
# BuildRequires:  cmake(KF6Declarative) >= %%{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KScreenLocker) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Wrapland)
BuildRequires:  libcap-progs
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-%{wlr_version})
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xwayland)
Requires:       breeze6-decoration >= %{_plasma6_bugfix}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kglobalacceld6  >= %{_plasma6_bugfix}
# WinFT
Requires:       wrapland
# SECTION QML dependencies
Requires:       kf6-kdeclarative-imports >= %{kf6_version}
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Requires:       plasma6-framework-components >= %{_plasma6_bugfix}
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-multimedia-imports >= %{qt6_version}
# /SECTION
# For post and verifyscript
Requires(post): permissions
Requires(verify): permissions
# /usr/share/kwin/tabbox/thumbnail_grid/metadata.json conflicts with plasma5-addons
Conflicts:      plasma5-addons < 6.0
Conflicts:      plasma5-addons-lang < 6.0
#
Provides:       qt6qmlimport(org.kde.kwin)
Provides:       qt6qmlimport(org.kde.kwin.3) = 0

%description
The Compositor Modules (COMO) are a robust and versatile set of libraries
to create compositors for the Wayland and X11 windowing systems on Linux.

%package libbase-x11
Summary:        COMO X11 backend

%description libbase-x11
This package provides the COMO X11 backend.

%package devel
Summary:        Como Build Environment
Requires:       kdecoration6-devel >= %{_plasma6_bugfix}
Requires:       cmake(KF6Auth) >= %{kf6_version}
Requires:       cmake(KF6Config) >= %{kf6_version}
Requires:       cmake(KF6ConfigWidgets) >= %{kf6_version}
Requires:       cmake(KF6Declarative) >= %{kf6_version}
Requires:       cmake(KF6GlobalAccel) >= %{kf6_version}
Requires:       cmake(KF6I18n) >= %{kf6_version}
Requires:       cmake(KF6IdleTime) >= %{kf6_version}
Requires:       cmake(KF6KCMUtils) >= %{kf6_version}
Requires:       cmake(KF6NewStuff) >= %{kf6_version}
Requires:       cmake(KF6Notifications) >= %{kf6_version}
Requires:       cmake(KF6Service) >= %{kf6_version}
Requires:       cmake(KF6Svg) >= %{kf6_version}
Requires:       cmake(KF6WidgetsAddons) >= %{kf6_version}
Requires:       cmake(KF6XmlGui) >= %{kf6_version}
Requires:       cmake(Wrapland)
Requires:       pkgconfig(epoxy)
Requires:       pkgconfig(pixman-1)
Requires:       pkgconfig(wlroots-%{wlr_version})
Requires:       qt6-gui-private-devel >= %{qt6_version}
Conflicts:      kwin5-devel
Conflicts:      kwinft-devel

%description devel
Como Build Environment.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}%{_kf6_libdir}
%fdupes %{buildroot}%{_kf6_sharedir}

%preun
%{systemd_user_preun plasma-kwin_wayland.service}
%{systemd_user_preun plasma-kwin_x11.service}

%post
%ldconfig
%ldconfig -n libbase-x11
%{systemd_user_post plasma-kwin_wayland.service}
%{systemd_user_post plasma-kwin_x11.service}

%postun
%ldconfig
%ldconfig -n libbase-x11
%{systemd_user_postun plasma-kwin_wayland.service}
%{systemd_user_postun plasma-kwin_x11.service}

%ldconfig_scriptlets libbase-x11

%files
%license LICENSE*
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/*
%{_kf6_configkcfgdir}/*
%{_kf6_debugdir}/org_kde_kwin.categories
%{_kf6_iconsdir}/hicolor/*/apps/kwin.png
%{_kf6_iconsdir}/hicolor/scalable/apps/kwin.svgz
%{_kf6_knsrcfilesdir}/*.knsrc
%{_kf6_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-delete-desktop-switching-shortcuts
# %%{_kf6_libdir}/kconf_update_bin/kwin-6.0-remove-breeze-tabbox-default
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-reset-active-mouse-screen
%{_kf6_libdir}/libcomo-*.so.0
%{_kf6_libdir}/libcomo-*.so.0.*
%{_kf6_notificationsdir}/kwin.notifyrc
%dir %{_kf6_plugindir}/kf6
%dir %{_kf6_plugindir}/kf6/kwindowsystem
%{_kf6_plugindir}/kf6/kwindowsystem/KF6WindowSystemComoPlugin.so
%dir %{_kf6_plugindir}/kf6/packagestructure
%{_kf6_plugindir}/kf6/packagestructure/kwin_aurorae.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_decoration.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_effect.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_scripts.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_windowswitcher.so
%dir %{_kf6_plugindir}/kf6/org.kde.kidletime.platforms
%{_kf6_plugindir}/kf6/org.kde.kidletime.platforms/KF6IdleTimeComoPlugin.so
%dir %{_kf6_plugindir}/kwin
%dir %{_kf6_plugindir}/kwin/effects
%dir %{_kf6_plugindir}/kwin/effects/configs
%{_kf6_plugindir}/kwin/effects/configs/kwin_blur_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_colorblindnesscorrection_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_diminactive_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_glide_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_invert_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_lookingglass_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_magiclamp_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_magnifier_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_mouseclick_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_mousemark_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_overview_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_resize_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_showpaint_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_slide_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_thumbnailaside_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_trackmouse_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_windowview_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_wobblywindows_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_zoom_config.so
%dir %{_kf6_plugindir}/kwin/effects/plugins
%{_kf6_plugindir}/kwin/effects/plugins/blendchanges.so
%{_kf6_plugindir}/kwin/effects/plugins/blur.so
%{_kf6_plugindir}/kwin/effects/plugins/colorblindnesscorrection.so
%{_kf6_plugindir}/kwin/effects/plugins/colorpicker.so
%{_kf6_plugindir}/kwin/effects/plugins/contrast.so
# %%{_kf6_plugindir}/kwin/effects/plugins/cube.so
# %%{_kf6_plugindir}/kwin/effects/plugins/cubeslide.so
%{_kf6_plugindir}/kwin/effects/plugins/diminactive.so
%{_kf6_plugindir}/kwin/effects/plugins/fallapart.so
%{_kf6_plugindir}/kwin/effects/plugins/glide.so
%{_kf6_plugindir}/kwin/effects/plugins/highlightwindow.so
%{_kf6_plugindir}/kwin/effects/plugins/invert.so
%{_kf6_plugindir}/kwin/effects/plugins/kscreen.so
%{_kf6_plugindir}/kwin/effects/plugins/lookingglass.so
%{_kf6_plugindir}/kwin/effects/plugins/magiclamp.so
%{_kf6_plugindir}/kwin/effects/plugins/magnifier.so
%{_kf6_plugindir}/kwin/effects/plugins/mouseclick.so
%{_kf6_plugindir}/kwin/effects/plugins/mousemark.so
%{_kf6_plugindir}/kwin/effects/plugins/overview.so
%{_kf6_plugindir}/kwin/effects/plugins/resize.so
%{_kf6_plugindir}/kwin/effects/plugins/screenedge.so
%{_kf6_plugindir}/kwin/effects/plugins/screenshot.so
%{_kf6_plugindir}/kwin/effects/plugins/sheet.so
%{_kf6_plugindir}/kwin/effects/plugins/showfps.so
%{_kf6_plugindir}/kwin/effects/plugins/showpaint.so
%{_kf6_plugindir}/kwin/effects/plugins/slide.so
%{_kf6_plugindir}/kwin/effects/plugins/slideback.so
%{_kf6_plugindir}/kwin/effects/plugins/slidingpopups.so
%{_kf6_plugindir}/kwin/effects/plugins/snaphelper.so
%{_kf6_plugindir}/kwin/effects/plugins/startupfeedback.so
%{_kf6_plugindir}/kwin/effects/plugins/thumbnailaside.so
%{_kf6_plugindir}/kwin/effects/plugins/touchpoints.so
%{_kf6_plugindir}/kwin/effects/plugins/trackmouse.so
%{_kf6_plugindir}/kwin/effects/plugins/windowview.so
%{_kf6_plugindir}/kwin/effects/plugins/wobblywindows.so
%{_kf6_plugindir}/kwin/effects/plugins/zoom.so
%dir %{_kf6_plugindir}/org.kde.kdecoration2.kcm
%{_kf6_plugindir}/org.kde.kdecoration2.kcm/kcm_auroraedecoration.so
%dir %{_kf6_plugindir}/org.kde.kdecoration2
%{_kf6_plugindir}/org.kde.kdecoration2/org.kde.kwin.aurorae.so
%dir %{_kf6_plugindir}/platforms
%{_kf6_plugindir}/platforms/ComoQpaPlugin.so
%dir %{_kf6_qmldir}/org/kde/kwin/
%{_kf6_qmldir}/org/kde/kwin/decoration/
%{_kf6_qmldir}/org/kde/kwin/decorations/
%{_kf6_qmldir}/org/kde/kwin/private/
%{_kf6_sharedir}/como/
%{_kf6_sharedir}/kconf_update/kwin.upd
%{_kf6_sharedir}/kwin/
%{_libexecdir}/como_killer_helper
%{_userunitdir}/plasma-kwin_wayland.service
%{_userunitdir}/plasma-kwin_x11.service

%files libbase-x11
%{_kf6_libdir}/libbase-x11-backend.so

%files devel
%{_includedir}/como_version.h
%{_includedir}/como/
%{_kf6_cmakedir}/KWinDBusInterface/
%{_kf6_cmakedir}/como/
%{_kf6_dbusinterfacesdir}/org.kde.kwin.*
%{_kf6_dbusinterfacesdir}/org.kde.KWin.*
