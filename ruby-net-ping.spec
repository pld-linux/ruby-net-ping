%define	gem_name net-ping
Summary:	A ping interface for Ruby
Name:		ruby-%{gem_name}
Version:	1.6.0
Release:	1
License:	Artistic 2.0
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	297c7f3d8d85b96a51407da982a3057e
URL:		http://www.rubyforge.org/projects/shards
BuildRequires:	iputils
BuildRequires:	ruby-fakeweb
BuildRequires:	ruby-ffi
BuildRequires:	ruby-net-ldap
BuildRequires:	ruby-test-unit
Requires:	ruby-ffi
# ??? really?
Requires:	ruby-net-ldap
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The net-ping library provides a ping interface for Ruby. It includes
separate TCP, HTTP, ICMP, UDP, WMI (for Windows) and external ping
classes.

%package doc
Summary:	A ping interface for Ruby - documentation
Group:		Development/Languages

%description doc
This package contains the documentation files for the %{gem_name} Ruby
library.

%prep
%setup -q -n %{gem_name}-%{version}

%build
%if %{with tests}
# three tests are ignored because of missing network connectivity
RUBYOPT="-Ilib" testrb2 test/test_net_ping.rb \
	--ignore-name=test_duration_basic_functionality \
	--ignore-name=test_pinging_a_good_host_results_in_no_exception_data \
	--ignore-name=test_pinging_a_good_host_returns_true
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc README CHANGES
%{ruby_vendorlibdir}/net/ping.rb
%{ruby_vendorlibdir}/net/ping
