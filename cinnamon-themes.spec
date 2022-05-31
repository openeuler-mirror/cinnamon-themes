Name:           cinnamon-themes
Epoch:          1
Version:        1.9.6
Release:        1
Summary:        Cinnamon themes
License:        GPLv3+
URL:            https://github.com/linuxmint/mint-themes
Source0:        https://github.com/linuxmint/mint-themes/releases/download/1.9.6/mint-themes_1.9.6.tar.xz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  fdupes
BuildRequires:  python3
BuildRequires:  sassc
Requires:       filesystem
Requires:       mint-themes-gtk3 = %{epoch}:%{version}
Requires:       mint-y-theme = %{epoch}:%{version}

%description
Collection of the best themes available for Cinnamon
Use mint-themes instead of cinnamon-themes


%package -n     mint-y-theme
Summary:        The Mint-Y theme 
Requires:       mint-y-icons

%description -n	mint-y-theme
The Mint-Y theme.  This theme is based on the Arc theme.

%package -n     mint-themes-gtk3
Summary:        Mint themes for GTK3
Requires:       mint-themes = %{epoch}:%{version}
Requires:       mint-x-icons

%description -n	mint-themes-gtk3
A collection of mint themes for GTK3.


%package -n     mint-themes
Summary:        Mint themes

%description -n mint-themes
A collection of mint themes.

%prep
%autosetup -p1 -n mint-themes
%{__sed} -i -e 's@Ubuntu@Noto Sans@g' files/usr/share/themes/Linux\ Mint/cinnamon/cinnamon.css

%build
make

%install
%{__cp} -pr usr/ %{buildroot}
%fdupes -s %{buildroot}

%files 
%license debian/copyright
%doc debian/changelog
"%{_datadir}/themes/Linux Mint"
%{_datadir}/themes/Mint-X*/cinnamon/

%files -n mint-themes
%license debian/copyright
%doc debian/changelog
%dir %{_datadir}/themes/Mint-X*/
%dir %{_datadir}/themes/Mint-X*/gtk-3.0/
%{_datadir}/themes/Mint-X*/index.theme
%{_datadir}/themes/Mint-X*/metacity-1/
%{_datadir}/themes/Mint-X/xfce-notify-4.0/
%{_datadir}/themes/Mint-X/xfwm4/
%{_datadir}/themes/Mint-X*/gtk-2.0/
%{_datadir}/themes/Mint-X-compact/xfwm4/

%files -n mint-y-theme
%license debian/copyright
%doc debian/changelog
%{_datadir}/themes/Mint-Y*

%files -n mint-themes-gtk3
%license debian/copyright
%doc debian/changelog
%{_datadir}/themes/Mint-X*/gtk-3.0/*

%changelog
* Fri May 6 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 1:1.9.6-1
- Initial Packaging
