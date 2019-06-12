#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-plexus-io
Version  : 2.0.2
Release  : 1
URL      : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.2/plexus-io-2.0.2.jar
Source0  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.2/plexus-io-2.0.2.jar
Source1  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.2/plexus-io-2.0.2.pom
Source2  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.jar
Source3  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.pom
Source4  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.5/plexus-io-2.0.5.jar
Source5  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.5/plexus-io-2.0.5.pom
Source6  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.7.1/plexus-io-2.7.1.jar
Source7  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.7.1/plexus-io-2.7.1.pom
Source8  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/3.0.0/plexus-io-3.0.0.jar
Source9  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/3.0.0/plexus-io-3.0.0.pom
Source10  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/3.0.1/plexus-io-3.0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-plexus-io-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-plexus-io package.
Group: Data

%description data
data components for the mvn-plexus-io package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.4
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.5
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.5
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.7.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.7.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.7.1
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.7.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.1
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.1


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.2/plexus-io-2.0.2.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.2/plexus-io-2.0.2.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.5/plexus-io-2.0.5.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.5/plexus-io-2.0.5.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.7.1/plexus-io-2.7.1.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.7.1/plexus-io-2.7.1.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.0/plexus-io-3.0.0.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.0/plexus-io-3.0.0.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.1/plexus-io-3.0.1.pom
