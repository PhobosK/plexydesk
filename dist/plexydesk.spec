# Change the values below as needed
%define name plexydesk
%define version 0.6.0
%define rpm_release 1
%define debug_on 1



# Do not alter anything below this line.
# All you need to do is add a Changelog entry at the end of the file.
#####################################################################
# Test for rpm distros
%define is_unknown %(test -e /etc/mandrake-release -o -e /etc/SuSE-release -o -e /etc/fedora-release -o -e /etc/pclinuxos-release && echo 0 || echo 1)
%define is_suse %(test -e /etc/SuSE-release && echo 1 || echo 0)
%define is_fedora %(test -e /etc/fedora-release && echo 1 || echo 0)
%define is_mandrake %(test -e /etc/mandrake-release && echo 1 || echo 0)
%define is_pclinuxos %(test -e /etc/pclinuxos-release && echo 1 || echo 0)

# Check if we are in debug mode
%if %{debug_on}
%define _cmake_debug Debug
%define cmake_debug_flag -DCMAKE_BUILD_TYPE=Debug
%else
%define cmake_debug_flag %{nil}
# Do not produce debug packages
%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%endif


# Define the install prefix for all distros
%define prefix	/usr


# Is this SuSe? If yes, define specific options for it.
%if %{is_suse}
Group:		System/GUI/Other
Release:	%{rpm_release}.suse%(echo "%{suse_version}" | %__sed -e 's/.$//')
Requires:	ffmpeg
Requires:   libqimageblitz4 >= 4.0, libqtdeclarative4 >= 4.7.0, libqtdbus4 >= 4.7.0
Requires:	libqtwebkit4 >= 4.7.0, libqtopengl4 >= 4.7.0
Requires:	libsm6, libxext6, libxcomposite1, libxdamage1, libxrender1
BuildRequires:  libqt4-devel >= 4.7.0, libqimageblitz-devel, libffmpeg-devel
BuildRequires:  libsm6-devel, libxext6-devel, libxcomposite1-devel, libxdamage-devel, libxrender1-devel
%endif


# Is this Fedora? If yes, define specific options for it.
%if %{is_fedora}
%define fedora_version      %(rpm -q --queryformat '%{VERSION}' fedora-release)
%define fedora_vernum       %(echo "%{fedora_version}" | tr -d '.')
Group:		User Interface/Desktops
Release:	%{rpm_release}.fc%{fedora_vernum}
Requires:	ffmpeg, ffmpeg-libs
Requires:	qimageblitz
Requires:	libSM, libXext, libXcomposite, libXdamage, libXrender
BuildRequires:  qt4-devel >= 4.7.0, qimageblitz-devel, ffmpeg-devel
BuildRequires:  libSM-devel, libXext-devel, libXcomposite-devel, libXdamage-devel, libXrender-devel
%endif


# Is this Mandriva? If yes, define specific options for it.
%if %{is_mandrake}
%if %{is_pclinuxos} < 1
Group:		Graphical desktop/Other
Release:	%{rpm_release}mdv%{product_version}
Requires:	ffmpeg
Requires:   libqimageblitz4 >= 4.0, libqtdeclarative4 >= 4.7.0, libqtdbus4 >= 4.7.0
Requires:	libqtwebkit4 >= 4.7.0, libqtopengl4 >= 4.7.0
Requires:	libsm6, libxext6, libxcomposite1, libxdamage1, libxrender1
BuildRequires:  libqt4-devel >= 4.7.0, libqimageblitz-devel, libffmpeg-devel
BuildRequires:  libsm6-devel, libxext6-devel, libxcomposite1-devel, libxdamage-devel, libxrender1-devel
%endif
%endif


# Is this PCLinux? If yes, define specific options for it.
%if %{is_pclinuxos}
Group:		Graphical desktop/Other
Release:	%{rpm_release}.pclos%{product_version}
Requires:	ffmpeg
Requires:   libqimageblitz4 >= 4.0, libqtdeclarative4 >= 4.7.0, libqtdbus4 >= 4.7.0
Requires:	libqtwebkit4 >= 4.7.0, libqtopengl4 >= 4.7.0
Requires:	libsm6, libxext6, libxcomposite1, libxdamage1, libxrender1
BuildRequires:  libqt4-devel >= 4.7.0, libqimageblitz-devel, libffmpeg-devel
BuildRequires:  libsm6-devel, libxext6-devel, libxcomposite1-devel, libxdamage-devel, libxrender1-devel
%endif


# Unknown rpm distro. Define only general options.
%if %{is_unknown}
Group:		Graphical desktop/Other
Release:	%{rpm_release}
%endif


# All distros common options
Name:		%{name}
Version:	%{version}
License:	LGPLv3+
URL:		http://www.plexyplanet.org
Summary:	A Desktop extension which lets you efficiently organize and use your Desktop
BuildRoot:	%{_tmppath}/build-%{name}-%{version}-root
Vendor:		PlexyDesk Team
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	glibc-devel, cmake >= 2.6, automake, libtool


%description
PlexyDesk is a lightweight Desktop, and it's not a Desktop Environment like KDE or GNOME.
PlexyDesk will render your workspace and help organize all your information with a touch, yes heard us right.
PlexyDesk will support multi touch screens.
PlexyDesk might not be the new Desktop Environment you came looking for, but it will be the Ultimate Desktop Experience you would ever get.
The aim of the PlexyDesk Team is to create "A Desktop which is easy to communicate with, Create and Simply cool!"


%prep

%setup -n %{name}-%{version}

export DESTDIR=${RPM_BUILD_ROOT}

# If it is Mandriva, use its specific cmake macro
%if %{is_mandrake}
%{cmake}
%else
rm -Rf build
mkdir build
cd build
cmake  ../ -DCMAKE_INSTALL_PREFIX=%{prefix} %{cmake_debug_flag}
%endif


%build
cd build
make %{?_smp_mflags}

%install
cd build
[ "${RPM_BUILD_ROOT}" != "/" ] && [ -d ${RPM_BUILD_ROOT} ] && rm -Rf ${RPM_BUILD_ROOT};
export DESTDIR=${RPM_BUILD_ROOT}
make install
# Put quotes around filenames in the list of installed files
%__sed  -i -e 's|^.*$|"&"|' install_manifest.txt


%post
if [ -x /usr/bin/update-menus ]; then /usr/bin/update-menus || true ; fi
/sbin/ldconfig


%postun
if [ "$1" = "0" -a -x /usr/bin/update-menus ]; then /usr/bin/update-menus || true ; fi
/sbin/ldconfig


%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && [ -d ${RPM_BUILD_ROOT} ] && rm -Rf ${RPM_BUILD_ROOT};


%files -f build/install_manifest.txt
%defattr(-, root, root)
%doc README TODO COPYING AUTHORS ChangeLog


# You need to add new Changelog entries specific for the RPM here.
# Do not add the Changelog for the PlexyDesk package here.
%changelog

* Sun Jul 23 2011 0.6.0
 Initial rpm release
 - Version 0.6.0
