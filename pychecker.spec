%define name pychecker
%define version 0.8.16
%define release %mkrel 2

Summary: A python source code checking tool
Name: %{name}
Version: %{version}
Release: %{release}
Url: http://pychecker.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/pychecker/%{name}-%{version}.tar.bz2
Patch0: pychecker-0.8.10-add-manpage
Patch1: pychecker-0.8.16-root.patch
License: BSD-like
Group: Development/Python
Requires: python
BuildArch: noarch
BuildRequires: python python-devel

%description
PyChecker is a tool for finding bugs in python source code. It finds problems
that are typically caught by a compiler for less dynamic languages, like C and
C++. It is similar to lint. Because of the dynamic nature of python, some
warnings may be incorrect; however, spurious warnings should be fairly
infrequent.

%prep
%setup -q
%patch0 -p1 -b .add_manpage
%patch1 -p1 -b .root

chmod a+rX -R .

%build
python setup.py config
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=%{buildroot}
rm -f $RPM_BUILD_ROOT/%{py_puresitedir}/%{name}/{CHANGELOG,COPYRIGHT,KNOWN_BUGS,MAINTAINERS,README,TODO,pycheckrc}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG COPYRIGHT KNOWN_BUGS MAINTAINERS README TODO pycheckrc
%{_bindir}/pychecker
%{py_puresitedir}/pychecker
%{py_puresitedir}/*.egg-info


