#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Term-Shell
Version  : 0.10
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Term-Shell-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Term-Shell-0.10.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libterm-shell-perl/libterm-shell-perl_0.09-1.debian.tar.xz
Summary  : 'A simple command-line shell framework.'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Term-Shell-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Term::ReadKey)
BuildRequires : perl(Text::Autoformat)

%description
This archive contains the distribution Term-Shell,
version 0.10:
A simple command-line shell framework.

%package dev
Summary: dev components for the perl-Term-Shell package.
Group: Development
Provides: perl-Term-Shell-devel = %{version}-%{release}

%description dev
dev components for the perl-Term-Shell package.


%package license
Summary: license components for the perl-Term-Shell package.
Group: Default

%description license
license components for the perl-Term-Shell package.


%prep
%setup -q -n Term-Shell-0.10
cd ..
%setup -q -T -D -n Term-Shell-0.10 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Term-Shell-0.10/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Term-Shell
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Term-Shell/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Term/Shell.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Term::Shell.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Term-Shell/LICENSE
