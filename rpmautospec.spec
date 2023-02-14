%include macros.rpmautospec

Name:           rpm-macros 
Version:        %autversion
Release:        %autorelease
Summary:        Package and CLI tool to generate release fields and changelogs

License:        GPL
URL:            https://forge.dgfip.finances.rie.gouv.fr/dgfip/design/rpm/macros
Source0:        %{name}-%{version}.tgz

%description
DGFiP RPM macros

%package -n rpmautospec-rpm-macros
Summary: Rpmautospec RPM macros for local rpmbuild
Requires: rpm

%description -n rpmautospec-rpm-macros
autorelease and autochangelog RPM macros

%files -n rpmautospec-rpm-macros
%{rpmmacrodir}/macros.rpmautospec

%prep
%setup -q -c ${name}

%install
mkdir -p %{buildroot}%{rpmmacrodir}
install -m 644 macros.rpmautospec %{buildroot}%{rpmmacrodir}/

%clean
rm -rf %{buildroot} $(pwd)

%changelog
%autochangelog