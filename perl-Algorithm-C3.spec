#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	Algorithm
%define	pnam	C3
Summary:	Algorithm::C3 - A module for merging hierarchies using the C3 algorithm
Summary(pl.UTF-8):	Algorithm::C3 - moduł do łączenia hierarchii przy użyciu algorytmu C3
Name:		perl-Algorithm-C3
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Algorithm/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	978c6343c542aa8ba61a73674a93c587
URL:		https://metacpan.org/dist/Algorithm-C3
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C3 is the name of an algorithm which aims to provide a sane method
resolution order under multiple inheritance. It was first introduced
in the Dylan language (see links in the manual SEE ALSO section), and
then later adopted as the preferred MRO (Method Resolution Order) for
the new-style classes in Python 2.3. Most recently it has been adopted
as the 'canonical' MRO for Perl 6 classes, and the default MRO for
Parrot objects as well.

%description -l pl.UTF-8
C3 to nazwa algorytmu, którego celem jest dostarczenie rozsądnej
kolejności rozwiązywania metod przy wielokrotnym dziedziczeniu. Po raz
pierwszy został wprowadzony w języku Dylan (odnośniki w sekcji SEE
ALSO manuala), a następnie zaadoptowany jako preferowana MRO (Method
Resolution Order - kolejność rozwiązywania metod) dla nowego stylu
klas w Pythonie 2.3. Ostatnio został zaadoptowany jako "kanoniczna"
MRO dla klas Perla 6 i domyślna MRO dla obiektów Parrota.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Algorithm/C3.pm
%{_mandir}/man3/Algorithm::C3.3pm*
