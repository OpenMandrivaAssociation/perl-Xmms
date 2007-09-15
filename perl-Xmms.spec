%define modname	Xmms

Name:		perl-%{modname}
Version:	0.12
Release:	%mkrel 6
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl modules to control and configure XMMS
Source:		http://search.cpan.org/CPAN/authors/id/D/DO/DOUGM/%{modname}-Perl-%{version}.tar.gz
URL:		http://search.cpan.org/~dougm/%{modname}-Perl-%{version}/
BuildRequires:	perl-devel
BuildRequires:  xmms-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This package provides the following modules:

 Xmms::Remote - Perl interface to the xmms_remote API

 Xmms::Config - Perl interface to the xmms_cfg API

 Xmms - Exports the remote control shell routine

 Xmms::Plugin - Embeds a Perl interpreter inside xmms and provides
                Input/Output/Effect/General plugin interfaces for
                Perl (not yet released, may never be)

%prep
%setup -q -n %{modname}-Perl-%{version}

%build
perl Makefile.PL
%make

%install
rm -Rf %{buildroot}
%makeinstall_std INSTALLSITEARCH=%perl_vendorarch INSTALLSITEMAN3DIR=%{_mandir}/man3

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{perl_vendorarch}/auto/%{modname}
%{perl_vendorarch}/auto/%{modname}/*
%{perl_vendorarch}/%{modname}*
%{perl_vendorarch}/*/%{modname}.pm
%{_mandir}/man?/*
%doc README

