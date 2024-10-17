%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

Summary:	A python source code checking tool
Name:		pychecker
Version:	0.8.19
Release:	2
License:	BSD-like
Group:		Development/Python
Url:		https://pychecker.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		pychecker-0.8.10-add-manpage
Requires:	python
BuildRequires:	python-devel
BuildArch:	noarch

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
python setup.py install --root=%{buildroot} --compile --optimize=2
rm -f %{buildroot}/%{py_puresitedir}/%{name}/{CHANGELOG,COPYRIGHT,KNOWN_BUGS,MAINTAINERS,README,TODO,pycheckrc}
perl -pi -e 's|%{buildroot}||' %{buildroot}%{_bindir}/pychecker

# pychecker2
mkdir -p %{buildroot}%{py_puresitedir}/pychecker2
#install -m 0644 pychecker2/*.py %{buildroot}%{py_puresitedir}/pychecker2/
#pushd pychecker2
%{python_compile_opt}
%{python_compile}
install *.pyc *.pyo %{buildroot}%{py_puresitedir}/pychecker2/

#install rc file
mkdir %buildroot%_sysconfdir
cp pycheckrc %buildroot%_sysconfdir
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYRIGHT KNOWN_BUGS MAINTAINERS README TODO pycheckrc
%{_bindir}/pychecker
%{py_puresitedir}/pychecker
%{py_puresitedir}/pychecker2
%{py_puresitedir}/*.egg-info
%{_sysconfdir}/pycheckrc


%changelog
* Tue May 10 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.8.19-1mdv2011.0
+ Revision: 673221
- no more pycheck2/*py files
- new version
- install pycheckrc file
- little clean of spec

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.8.18-3mdv2011.0
+ Revision: 592423
- rebuild for python 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.8.18-2mdv2010.0
+ Revision: 441983
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.8.18-1mdv2009.1
+ Revision: 319603
- rebuild with python 2.6
- new release 0.8.18

* Wed Aug 20 2008 Adam Williamson <awilliamson@mandriva.org> 0.8.17-3mdv2009.0
+ Revision: 274404
- add pychecker2 as well (spe needs it)
- use --optimize=2 to get .pyo files
- no point setting optimization flags on a noarch package

* Tue Jun 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.17-2mdv2009.0
+ Revision: 228551
- fix wrapper (spotted by Laurent Poligny <laurent.poligny@ibisc.univ-evry.fr>

* Thu Dec 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.17-1mdv2008.1
+ Revision: 138597
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 05 2006 Michael Scherer <misc@mandriva.org> 0.8.16-2mdv2007.0
+ Revision: 91351
- Rebuild for new python
- use macro to compile on x86_64, and clean the file listing, by using rm instead of %%exclude
- Import pychecker

