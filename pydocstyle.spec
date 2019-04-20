#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pydocstyle
Version  : 3.0.0
Release  : 11
URL      : https://files.pythonhosted.org/packages/e1/e6/a0669df17a97e462915a10a7d6c567658b60eceddebf62a3fb9975c00196/pydocstyle-3.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e1/e6/a0669df17a97e462915a10a7d6c567658b60eceddebf62a3fb9975c00196/pydocstyle-3.0.0.tar.gz
Summary  : Python docstring style checker
Group    : Development/Tools
License  : MIT
Requires: pydocstyle-bin = %{version}-%{release}
Requires: pydocstyle-license = %{version}-%{release}
Requires: pydocstyle-python = %{version}-%{release}
Requires: pydocstyle-python3 = %{version}-%{release}
Requires: six
Requires: snowballstemmer
BuildRequires : buildreq-distutils3

%description
====================================

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
%setup -q -n pydocstyle-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539565652
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pydocstyle
cp LICENSE-MIT %{buildroot}/usr/share/package-licenses/pydocstyle/LICENSE-MIT
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
/usr/share/package-licenses/pydocstyle/LICENSE-MIT

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
