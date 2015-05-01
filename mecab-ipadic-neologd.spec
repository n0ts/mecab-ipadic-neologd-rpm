# Disable *-debuginfo for this package as we don't have any ELF binaries
%global debug_package %{nil}

%define package_version 20150501
%define package_release 1

%define target_dirname mecab-ipadic-neologd-master
%define target_prefix /usr/lib64/mecab/dic/ipadic-neologd

Name:		mecab-ipadic-neologd
Version:	%{package_version}
Release:	%{package_release}%{?dist}
Summary:	Neologism dictionary based on the language resources on the Web for mecab-ipadic 
Group:		Applications/Text
License:	Apache2
URL:		https://github.com/neologd/mecab-ipadic-neologd
Source0:	https://github.com/neologd/mecab-ipadic-neologd/archive/master.zip
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# mecab-config command (in mecab package) is required to configure mecab-ipadic
BuildRequires:	mecab-devel mecab curl xz

Requires:	mecab mecab-ipadic

%description
mecab-ipadic-neologd is customized system dictionary for MeCab.

This dictionary includes many neologisms (new word), which are extracted from many language resources on the Web.

When you analyze the Web documents, it's better to use this system dictionary and default one (ipadic) together.

%prep
%setup -q -n %{target_dirname}

%install
%{__rm} -rf %{buildroot}
bin/install-mecab-ipadic-neologd --prefix %{buildroot}/%{target_prefix} --asuser --forceyes

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/mecab/dic/ipadic-neologd
