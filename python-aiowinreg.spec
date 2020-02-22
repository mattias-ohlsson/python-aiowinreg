%global pypi_name aiowinreg

Name:           python-%{pypi_name}
Version:        0.0.2
Release:        1%{?dist}
Summary:        Windows registry file reader

License:        MIT
URL:            https://github.com/skelsec/aiowinreg
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/skelsec/%{pypi_name}/master/LICENSE
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
A Python library to parse and read Microsoft Windows registry.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python library to parse and read Microsoft Windows registry.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Add LICENSE file
cp -a %{SOURCE1} LICENSE

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Feb 22 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.0.2-1
- Initial build
