Summary:	A jungle of Erlang code: XMPP library
Name:		erlang-exmpp
Version:	0.9.2
Release:	5
License:	EPL
Group:		Development/Languages
Source0:	http://download.process-one.net/exmpp/exmpp-%{version}.tar.gz
# Source0-md5:	765778958bc5dd7eb0e91815482cecc0
Patch0:		bad-defines.patch
URL:		https://support.process-one.net/doc/display/EXMPP/exmpp+home
BuildRequires:	erlang
BuildRequires:	expat-devel
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	erlang
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast and scalable library for the Extensible Messaging and Presence
Protocol (XMPP).

%prep
%setup -q -n exmpp-%{version}
%patch0 -p1

%build
%configure \
	--prefix=%{_libdir}/erlang/lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* README
%{_libdir}/erlang/lib/exmpp-*
