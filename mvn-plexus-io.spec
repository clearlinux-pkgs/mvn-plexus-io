#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-plexus-io
Version  : 2.0.2
Release  : 3
URL      : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.2/plexus-io-2.0.2.jar
Source0  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.2/plexus-io-2.0.2.jar
Source1  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.10/plexus-io-2.0.10.jar
Source2  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.10/plexus-io-2.0.10.pom
Source3  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.2/plexus-io-2.0.2.pom
Source4  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.3/plexus-io-2.0.3.jar
Source5  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.3/plexus-io-2.0.3.pom
Source6  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.jar
Source7  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.pom
Source8  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.5/plexus-io-2.0.5.jar
Source9  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.5/plexus-io-2.0.5.pom
Source10  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.6/plexus-io-2.0.6.jar
Source11  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.0.6/plexus-io-2.0.6.pom
Source12  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.4/plexus-io-2.4.jar
Source13  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.4/plexus-io-2.4.pom
Source14  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.7.1/plexus-io-2.7.1.jar
Source15  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/2.7.1/plexus-io-2.7.1.pom
Source16  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/3.0.0/plexus-io-3.0.0.jar
Source17  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/3.0.0/plexus-io-3.0.0.pom
Source18  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/3.0.1/plexus-io-3.0.1.jar
Source19  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/3.0.1/plexus-io-3.0.1.pom
Source20  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/3.1.0/plexus-io-3.1.0.jar
Source21  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-io/3.1.0/plexus-io-3.1.0.pom
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
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.2/plexus-io-2.0.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.10
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.10/plexus-io-2.0.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.10
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.10/plexus-io-2.0.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.2/plexus-io-2.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.3/plexus-io-2.0.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.3
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.3/plexus-io-2.0.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.4
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.4
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.5
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.5/plexus-io-2.0.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.5
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.5/plexus-io-2.0.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.6
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.6/plexus-io-2.0.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.6
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.6/plexus-io-2.0.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.4
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.4/plexus-io-2.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.4
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.4/plexus-io-2.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.7.1
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.7.1/plexus-io-2.7.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.7.1
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.7.1/plexus-io-2.7.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.0
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.0/plexus-io-3.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.0
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.0/plexus-io-3.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.1
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.1/plexus-io-3.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.1
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.1/plexus-io-3.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.1.0
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.1.0/plexus-io-3.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.1.0
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.1.0/plexus-io-3.1.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.10/plexus-io-2.0.10.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.10/plexus-io-2.0.10.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.2/plexus-io-2.0.2.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.2/plexus-io-2.0.2.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.3/plexus-io-2.0.3.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.3/plexus-io-2.0.3.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.5/plexus-io-2.0.5.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.5/plexus-io-2.0.5.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.6/plexus-io-2.0.6.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.0.6/plexus-io-2.0.6.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.4/plexus-io-2.4.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.4/plexus-io-2.4.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.7.1/plexus-io-2.7.1.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/2.7.1/plexus-io-2.7.1.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.0/plexus-io-3.0.0.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.0/plexus-io-3.0.0.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.1/plexus-io-3.0.1.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.0.1/plexus-io-3.0.1.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.1.0/plexus-io-3.1.0.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-io/3.1.0/plexus-io-3.1.0.pom
