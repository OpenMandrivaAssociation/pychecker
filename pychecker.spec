%define name pychecker
%define version 0.8.18
%define release %mkrel 1

%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

Summary: A python source code checking tool
Name: %{name}
Version: %{version}
Release: %{release}
License: BSD-like
Group: Development/Python
Url: http://pychecker.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: pychecker-0.8.10-add-manpage
Requires: python
BuildRequires: python-devel
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
PyChecker is a tool for finding bugs in python source code. It finds problems
that are typically caught by a compiler for less dynamic languages, like C and
C++. It is similar to lint. Because of the dynamic nature of python, some
warnings may be incorrect; however, spurious warnings should be fairly
infrequent.

%prep
%setup -q
%patch0 -p1 -b .add_manpage

chmod a+rX -R .

%build
python setup.py config
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2
rm -f %{buildroot}/%{py_puresitedir}/%{name}/{CHANGELOG,COPYRIGHT,KNOWN_BUGS,MAINTAINERS,README,TODO,pycheckrc}
perl -pi -e 's|%{buildroot}||' %{buildroot}%{_bindir}/pychecker

# pychecker2
mkdir -p %{buildroot}%{py_puresitedir}/pychecker2
install -m 0644 pychecker2/*.py %{buildroot}%{py_puresitedir}/pychecker2/
pushd pychecker2
%{python_compile_opt}
%{python_compile}
install *.pyc *.pyo %{buildroot}%{py_puresitedir}/pychecker2/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG COPYRIGHT KNOWN_BUGS MAINTAINERS README TODO pycheckrc
%{_bindir}/pychecker
%{py_puresitedir}/pychecker
%{py_puresitedir}/pychecker2
%{py_puresitedir}/*.egg-info
