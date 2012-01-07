Summary:	GNOME-based Bible research tool
Name:		xiphos
Version:	3.1.5svn
Release:	0.1
License:	GPL
Group:		X11/Applications
URL:		http://www.xiphos.org/
#Source0:	http://downloads.sourceforge.net/gnomesword/Xiphos/%{version}/%{name}-%{version}.tar.gz
# svn co https://gnomesword.svn.sourceforge.net/svnroot/gnomesword/branches/webkit xiphos-webkit-svn
# rm -rf xiphos-webkit-svn/.svn
# tar cvfz xiphos-webkit-svn.tar.gz xiphos-webkit-svn
Source0:	%{name}-webkit-svn.tar.gz
# Source0-md5:	6cc860c9e238137245307e4ae0f512f1
BuildRequires:	clucene-core-devel
BuildRequires:	gnome-spell
BuildRequires:	gtk-webkit3-devel
BuildRequires:	gtkhtml-devel >= 3.91.0
BuildRequires:	libbonobo-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.2
BuildRequires:	libgsf-devel >= 1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	scrollkeeper >= 0.3.5
BuildRequires:	sword-devel >= 1.6.2
Requires(post,postun):	scrollkeeper
Requires:	clucene-core
Requires:	gtkhtml >= 3.91.0
Requires:	libbonobo >= 2.0
Requires:	libgnomeui >= 2.2
Requires:	libgsf >= 1
Requires:	sword >= 1.6.2
Suggests:	festival
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
%setup -q -n %{name}-webkit-svn

%build
./waf configure \
	--prefix %{_prefix} \
	--debug-level optimized \
	--enable-delint
./waf build

%install
rm -rf $RPM_BUILD_ROOT
./waf install \
	--destdir $RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -r $RPM_BUILD_ROOT%{_iconsdir}/hicolor/scalable/apps/xiphos.svg
#rm -r $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}/*.xpm
#rm -r $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}/*.ico

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING AUTHORS INSTALL NEWS README TODO TRANSLATION-HOWTO RELEASE-NOTES ChangeLog
%doc %{_datadir}/gnome/help/*
%attr(755,root,root) %{_bindir}/xiphos
%attr(755,root,root) %{_bindir}/xiphos-nav
%{_datadir}/xiphos
%dir %{_datadir}/omf/xiphos
%{_datadir}/omf/xiphos/*.omf
#%dir %{_pixmapsdir}/%{name}
#%{_pixmapsdir}/%{name}/*.png
%{_desktopdir}/%{name}.desktop
