%define major 0
%define libname %mklibname visio %{major}

Name:		libvisio
Version:	0.0.17
Release:	1
Summary:	A library providing ability to interpret and import visio diagrams
Group:		System/Libraries
License:	GPL+ or LGPLv2+ or MPLv1.1
URL:		http://www.freedesktop.org/wiki/Software/libvisio
Source:		http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	pkgconfig(libwpd-0.9)
BuildRequires:	pkgconfig(libwpg-0.2)

%description
Libvisio is library providing ability to interpret and import visio
diagrams into various applications. You can find it being used in
libreoffice.

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Development files for %{name}
Group:		System/Libraries

%description -n %{libname}
Libvisio is library providing ability to interpret and import visio
diagrams into various applications. You can find it being used in
libreoffice.

%files -n %{libname}
%{_libdir}/%{name}-0.0.so.%{major}*

#--------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files devel
%{_includedir}/%{name}-0.0
%{_libdir}/%{name}-0.0.so
%{_libdir}/pkgconfig/%{name}-0.0.pc

#--------------------------------------------------------------------

%package doc
Summary:	Documentation of %{name} API
Group:		Books/Howtos
BuildArch:	noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html

#--------------------------------------------------------------------

%package tools
Summary:	Tools to transform Visio diagrams into other formats
Group:		Publishing

%description tools
Tools to transform Visio diagrams into other formats.
Currently supported: XHTML, raw.

%files tools
%{_bindir}/vsd2raw
%{_bindir}/vsd2xhtml

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std
