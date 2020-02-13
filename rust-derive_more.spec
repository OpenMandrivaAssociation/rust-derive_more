# Generated by rust2rpm 12
# No test files in this release but included in the next thanks to Debian
%bcond_with check
%global debug_package %{nil}

%global crate derive_more

Name:           rust-%{crate}
Version:        0.99.2
Release:        2%{?dist}
Summary:        Adds #[derive(x)] macros for more traits

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/derive_more
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Adds #[derive(x)] macros for more traits.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+add-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+add-devel %{_description}

This package contains library source intended for building other packages
which use "add" feature of "%{crate}" crate.

%files       -n %{name}+add-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+add_assign-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+add_assign-devel %{_description}

This package contains library source intended for building other packages
which use "add_assign" feature of "%{crate}" crate.

%files       -n %{name}+add_assign-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+as_mut-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+as_mut-devel %{_description}

This package contains library source intended for building other packages
which use "as_mut" feature of "%{crate}" crate.

%files       -n %{name}+as_mut-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+as_ref-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+as_ref-devel %{_description}

This package contains library source intended for building other packages
which use "as_ref" feature of "%{crate}" crate.

%files       -n %{name}+as_ref-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+constructor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+constructor-devel %{_description}

This package contains library source intended for building other packages
which use "constructor" feature of "%{crate}" crate.

%files       -n %{name}+constructor-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+deref-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deref-devel %{_description}

This package contains library source intended for building other packages
which use "deref" feature of "%{crate}" crate.

%files       -n %{name}+deref-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+deref_mut-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deref_mut-devel %{_description}

This package contains library source intended for building other packages
which use "deref_mut" feature of "%{crate}" crate.

%files       -n %{name}+deref_mut-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+display-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+display-devel %{_description}

This package contains library source intended for building other packages
which use "display" feature of "%{crate}" crate.

%files       -n %{name}+display-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+from-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+from-devel %{_description}

This package contains library source intended for building other packages
which use "from" feature of "%{crate}" crate.

%files       -n %{name}+from-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+from_str-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+from_str-devel %{_description}

This package contains library source intended for building other packages
which use "from_str" feature of "%{crate}" crate.

%files       -n %{name}+from_str-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+generate-parsing-rs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+generate-parsing-rs-devel %{_description}

This package contains library source intended for building other packages
which use "generate-parsing-rs" feature of "%{crate}" crate.

%files       -n %{name}+generate-parsing-rs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+index-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+index-devel %{_description}

This package contains library source intended for building other packages
which use "index" feature of "%{crate}" crate.

%files       -n %{name}+index-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+index_mut-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+index_mut-devel %{_description}

This package contains library source intended for building other packages
which use "index_mut" feature of "%{crate}" crate.

%files       -n %{name}+index_mut-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+into-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+into-devel %{_description}

This package contains library source intended for building other packages
which use "into" feature of "%{crate}" crate.

%files       -n %{name}+into-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+into_iterator-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+into_iterator-devel %{_description}

This package contains library source intended for building other packages
which use "into_iterator" feature of "%{crate}" crate.

%files       -n %{name}+into_iterator-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+iterator-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+iterator-devel %{_description}

This package contains library source intended for building other packages
which use "iterator" feature of "%{crate}" crate.

%files       -n %{name}+iterator-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+mul-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mul-devel %{_description}

This package contains library source intended for building other packages
which use "mul" feature of "%{crate}" crate.

%files       -n %{name}+mul-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+mul_assign-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mul_assign-devel %{_description}

This package contains library source intended for building other packages
which use "mul_assign" feature of "%{crate}" crate.

%files       -n %{name}+mul_assign-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+not-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+not-devel %{_description}

This package contains library source intended for building other packages
which use "not" feature of "%{crate}" crate.

%files       -n %{name}+not-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+peg-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+peg-devel %{_description}

This package contains library source intended for building other packages
which use "peg" feature of "%{crate}" crate.

%files       -n %{name}+peg-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sum-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sum-devel %{_description}

This package contains library source intended for building other packages
which use "sum" feature of "%{crate}" crate.

%files       -n %{name}+sum-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+try_into-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+try_into-devel %{_description}

This package contains library source intended for building other packages
which use "try_into" feature of "%{crate}" crate.

%files       -n %{name}+try_into-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 00:21:58 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.99.2-1
- Update to 0.99.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 09:56:43 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.0-1
- Update to 0.15.0

* Thu May 30 18:33:43 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.1-1
- Initial package
