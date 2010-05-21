#
# TODO:
# - PLDify post/postun scrollkeper updates?
# - Use %lang macro?
#

Summary:	GNOME-based Bible research tool
Name:		xiphos
Version:	3.1.3
Release:	1
License:	GPL
Group:		X11/Applications
URL:		http://xiphos.org
Source0:	http://downloads.sourceforge.net/gnomesword/Xiphos/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gnome-spell
BuildRequires:	gtkhtml-devel >= 3.0
BuildRequires:	libbonobo-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.2
BuildRequires:	scrollkeeper >= 0.3.5
BuildRequires:	sword-devel >= 1.6.1
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

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{_docdir}/%{name}/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rmdir $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if which scrollkeeper-update>/dev/null 2>&1; then scrollkeeper-update -q -o %{_datadir}/omf/%{name}; fi

%postun
if which scrollkeeper-update>/dev/null 2>&1; then scrollkeeper-update -q; fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xiphos
%dir %{_datadir}/xiphos
%{_datadir}/xiphos/*
%{_datadir}/locale/*
%dir %{_datadir}/omf/xiphos
%{_datadir}/omf/xiphos/*.omf
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/scalable/apps/xiphos.svg
%doc %{_datadir}/gnome/help/*
%doc ABOUT-NLS AUTHORS COPYING INSTALL NEWS README TODO
%{_desktopdir}/%{name}.desktop
