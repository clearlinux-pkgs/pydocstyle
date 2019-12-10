#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pydocstyle
Version  : 5.0.1
Release  : 16
URL      : https://files.pythonhosted.org/packages/ac/97/878e4216091aa92550e721344792be599e664ed3088ccdfa807e27316908/pydocstyle-5.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/97/878e4216091aa92550e721344792be599e664ed3088ccdfa807e27316908/pydocstyle-5.0.1.tar.gz
Summary  : Python docstring style checker
Group    : Development/Tools
License  : MIT
Requires: pydocstyle-bin = %{version}-%{release}
Requires: pydocstyle-license = %{version}-%{release}
Requires: pydocstyle-python = %{version}-%{release}
Requires: pydocstyle-python3 = %{version}-%{release}
Requires: snowballstemmer
BuildRequires : buildreq-distutils3
BuildRequires : snowballstemmer

%description
pydocstyle - docstring style checker
====================================
.. image:: https://travis-ci.org/PyCQA/pydocstyle.svg?branch=master
:target: https://travis-ci.org/PyCQA/pydocstyle

%package bin
Summary: bin components for the pydocstyle package.
Group: Binaries
Requires: pydocstyle-license = %{version}-%{release}

%description bin
bin components for the pydocstyle package.


%package license
Summary: license components for the pydocstyle package.
Group: Default

%description license
license components for the pydocstyle package.


%package python
Summary: python components for the pydocstyle package.
Group: Default
Requires: pydocstyle-python3 = %{version}-%{release}

%description python
python components for the pydocstyle package.


%package python3
Summary: python3 components for the pydocstyle package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pydocstyle package.


%prep
%setup -q -n pydocstyle-5.0.1
cd %{_builddir}/pydocstyle-5.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575997544
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pydocstyle
cp %{_builddir}/pydocstyle-5.0.1/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pydocstyle/7c81edfbc257f17950f67d0a398146ef25e467e4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pydocstyle

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pydocstyle/7c81edfbc257f17950f67d0a398146ef25e467e4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
