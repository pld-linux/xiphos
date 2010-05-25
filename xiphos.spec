Summary:	GNOME-based Bible research tool
Name:		xiphos
Version:	3.1.3
Release:	0.1
License:	GPL
Group:		X11/Applications
URL:		http://www.xiphos.org/
Source0:	http://downloads.sourceforge.net/gnomesword/Xiphos/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	aaded6bc81b29935edd989d204928ba3
BuildRequires:	clucene-core-devel
BuildRequires:	gnome-spell
BuildRequires:	gtkhtml-devel >= 3.0
BuildRequires:	libbonobo-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.2
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	scrollkeeper >= 0.3.5
BuildRequires:	sword-devel >= 1.6.1
Requires(post,postun):	scrollkeeper
Requires:	clucene-core
Requires:	gtkhtml >= 3.0
Requires:	libbonobo >= 2.0
Requires:	libgnomeui >= 2.2
Requires:	sword >= 1.6.1
Obsoletes:	gnomesword
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bible Study Software for the Linux community. Lookup and search Bible
texts and commentaries. Xiphos uses modules and libraries from the
SWORD Project. Display multiple translations in the interlinear
window. Search for passages in any translation by word, phrase, or
regular expression. Install this package if you want to browse the
Bible translations and reference works distributed by Crosswire Bible
Society through the SWORD Project.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ABOUT-NLS AUTHORS INSTALL NEWS README TODO
%doc %{_datadir}/gnome/help/*
%attr(755,root,root) %{_bindir}/xiphos
%{_datadir}/xiphos
%dir %{_datadir}/omf/xiphos
%{_datadir}/omf/xiphos/*.omf
%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}/*.png
%{_pixmapsdir}/%{name}/*.xpm
%{_pixmapsdir}/%{name}/*.ico
# TODO: create non-scaled pixmaps
%{_iconsdir}/hicolor/scalable/apps/xiphos.svg
%{_desktopdir}/%{name}.desktop
