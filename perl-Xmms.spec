%define upstream_name	 Xmms
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl modules to control and configure XMMS
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/~dougm/%{upstream_name}-Perl-%{upstream_version}/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DO/DOUGM/%{upstream_name}-Perl-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:  xmms-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This package provides the following modules:

 Xmms::Remote - Perl interface to the xmms_remote API

 Xmms::Config - Perl interface to the xmms_cfg API

 Xmms - Exports the remote control shell routine

 Xmms::Plugin - Embeds a Perl interpreter inside xmms and provides
                Input/Output/Effect/General plugin interfaces for
                Perl (not yet released, may never be)

%prep
%setup -q -n %{upstream_name}-Perl-%{upstream_version}

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
%doc README
%dir %{perl_vendorarch}/auto/%{upstream_name}
%{perl_vendorarch}/auto/%{upstream_name}/*
%{perl_vendorarch}/%{upstream_name}*
%{perl_vendorarch}/*/%{upstream_name}.pm
%{_mandir}/man?/*
