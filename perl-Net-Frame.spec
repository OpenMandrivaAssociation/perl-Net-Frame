%define upstream_name    Net-Frame
%define upstream_version 1.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.09
Release:	1

Summary:	BSD loopback layer object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/Net-Frame-1.09.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Bit::Vector)
BuildRequires:	perl(Class::Gomor)
BuildRequires:	perl(Net::IPv6Addr)
BuildRequires:	perl(Socket6)
BuildArch:	noarch

%description
*Net::Frame* is a fork of *Net::Packet*. The goal here was to greatly
simplify the use of the frame crafting framework. *Net::Packet* does many
things undercover, and it was difficult to document all the thingies.

Also, *Net::Packet* may suffer from unease of use, because frames were
assembled using layers stored in L2, L3, L4 and L7 attributes. *Net::Frame*
removes all this, and is splitted in different modules, for those who only
want to use part of the framework, and not whole framework.

Finally, anyone can create a layer, and put it on his CPAN space, because
of the modularity *Net::Frame* offers. For an example, see
*Net::Frame::Layer::ICMPv4* on my CPAN space.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.70.0-2mdv2011.0
+ Revision: 657341
- rebuild for updated spec-helper

* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.70.0-1
+ Revision: 639678
- update to new version 1.07

* Thu Jan 07 2010 Olivier Thauvin <nanardon@mandriva.org> 1.60.0-1mdv2011.0
+ Revision: 487174
- import perl-Net-Frame


* Thu Jan 07 2010 cpan2dist 1.06-1mdv
- initial mdv release, generated with cpan2dist

