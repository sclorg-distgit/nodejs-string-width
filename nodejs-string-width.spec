%{?scl:%scl_package nodejs-string-width}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename string-width
%global enable_tests 0
# tests disabled until such time as 'ava' is packaged for Fedora

Name:		%{?scl_prefix}nodejs-string-width
Version:	1.0.1
Release:	3%{?dist}
Summary:	Get the visual width of a string

License:	MIT
URL:		https://github.com/sindresorhus/string-width
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# Get the test from the upstream repo, as the npm tarball doesn't contain tests
Source1:	https://raw.githubusercontent.com/sindresorhus/string-width/f279cfd14835f0a3c8df69ba18e9a3960156e135/test.js


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(ava)
%endif

%description
Get the visual width of a string - the number of columns required to display it

%prep
%setup -q -n package
# setup the tests
cp -r %{SOURCE1} .

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#%{__nodejs} -e 'require("./")'
#%if 0%{?enable_tests}
#%{__nodejs} test.js
#%else
#%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
#%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}

%changelog
* Thu Sep 15 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-3
- Built for RHSCL
- Remove %%BuildRequires

* Wed Mar 02 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-2
- Fix BuildRequires

* Fri Oct 23 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-1
- Initial packaging
