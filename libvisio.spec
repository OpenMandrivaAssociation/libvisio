%define api	0.1
%define major	1
%define libname %mklibname visio %{api} %{major}
%define devname %mklibname visio -d

Summary:	A library providing ability to interpret and import visio diagrams
Name:		libvisio
Version:	0.1.7
Release:	3
Group:		System/Libraries
License:	GPLv2+ or LGPLv2+ or MPLv1.1
Url:		https://wiki.documentfoundation.org/DLP/Libraries/libvisio
Source0:	http://dev-www.libreoffice.org/src/libvisio/%{name}-%{version}.tar.xz
BuildRequires:	doxygen
BuildRequires:	gperf
BuildRequires:	boost-devel
BuildRequires:	boost-core-devel
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(librevenge-0.0)
BuildRequires:	pkgconfig(icu-uc)

%description
Libvisio is library providing ability to interpret and import visio
diagrams into various applications. You can find it being used in
libreoffice.

%package tools
Summary:	Tools to transform Visio diagrams into other formats
Group:		Publishing

%description tools
Tools to transform Visio diagrams into other formats.
Currently supported: XHTML, raw.

%package -n %{libname}
Summary:	Development files for %{name}
Group:		System/Libraries

%description -n %{libname}
Libvisio is library providing ability to interpret and import visio
diagrams into various applications. You can find it being used in
libreoffice.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
export CPPFLAGS='-DBOOST_ERROR_CODE_HEADER_ONLY -DBOOST_SYSTEM_NO_DEPRECATED'
%configure \
	--disable-static \
	--disable-werror
    
%make_build

%install
%make_install

%files tools
%{_bindir}/vsd2raw
%{_bindir}/vsd2xhtml
%{_bindir}/vsd2text
%{_bindir}/vss2xhtml
%{_bindir}/vss2text
%{_bindir}/vss2raw

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}*

%files -n %{devname}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc

