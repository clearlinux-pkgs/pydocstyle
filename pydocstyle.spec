#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pydocstyle
Version  : 5.0.2
Release  : 19
URL      : https://files.pythonhosted.org/packages/39/f4/3f670e71f11c4c65f0d5f4153f5191fb38786483513c90de66f08ef6e810/pydocstyle-5.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/39/f4/3f670e71f11c4c65f0d5f4153f5191fb38786483513c90de66f08ef6e810/pydocstyle-5.0.2.tar.gz
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

.. image:: https://ci.appveyor.com/api/projects/status/40kkc366bmrrttca/branch/master?svg=true
    :target: https://ci.appveyor.com/project/Nurdok/pydocstyle/branch/master

.. image:: https://readthedocs.org/projects/pydocstyle/badge/?version=latest
    :target: https://readthedocs.org/projects/pydocstyle/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/pyversions/pydocstyle.svg
    :target: https://pypi.org/project/pydocstyle


**pydocstyle** is a static analysis tool for checking compliance with Python
docstring conventions.

**pydocstyle** supports most of
`PEP 257 <http://www.python.org/dev/peps/pep-0257/>`_ out of the box, but it
should not be considered a reference implementation.

**pydocstyle** supports Python 3.5, 3.6, 3.7 and 3.8.


Quick Start
-----------

Install
^^^^^^^

.. code::

    pip install pydocstyle


Run
^^^^

.. code::

    $ pydocstyle test.py
    test.py:18 in private nested class `meta`:
            D101: Docstring missing
    test.py:27 in public function `get_user`:
        D300: Use """triple double quotes""" (found '''-quotes)
    test:75 in public function `init_database`:
        D201: No blank lines allowed before function docstring (found 1)
    ...


Links
-----

* `Read the full documentation here <http://pydocstyle.org>`_.

* `Fork pydocstyle on GitHub <http://github.com/PyCQA/pydocstyle>`_.

* `PyPI project page <https://pypi.python.org/pypi/pydocstyle>`_.

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
Provides: pypi(pydocstyle)

%description python3
python3 components for the pydocstyle package.


%prep
%setup -q -n pydocstyle-5.0.2
cd %{_builddir}/pydocstyle-5.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583205928
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
cp %{_builddir}/pydocstyle-5.0.2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pydocstyle/7c81edfbc257f17950f67d0a398146ef25e467e4
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
