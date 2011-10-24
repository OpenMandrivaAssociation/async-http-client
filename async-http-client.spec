
Name:           async-http-client
Version:        1.6.1
Release:        1
Summary:        Asynchronous Http Client for Java

Group:          Development/Java
License:        ASL 2.0
URL:            https://github.com/AsyncHttpClient/%{name}
# git clone https://github.com/AsyncHttpClient/async-http-client.git
# git archive --prefix="async-http-client-1.6.1/" --format=tar async-http-client-1.6.1 | bzip2 > async-http-client-1.6.1.tar.bz2
Source0:        %{name}-%{version}.tar.bz2

Patch0:         0001-Remove-test-dependencies.patch

BuildArch:      noarch

BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-release-plugin
BuildRequires:  sonatype-oss-parent
BuildRequires:  netty

Requires:       netty
Requires:       java >= 0:1.6.0
Requires(post): jpackage-utils
Requires(postun): jpackage-utils


%description
Async Http Client library purpose is to allow Java applications to
easily execute HTTP requests and asynchronously process the HTTP
responses. The Async HTTP Client library is simple to use.


%package javadoc
Summary:   API documentation for %{name}
Group:     Development/Java
Requires:  jpackage-utils

%description javadoc
%{summary}.

%prep
%setup -q

%patch0 -p1

%build
# we don't have all test dependencies available so disable tests
mvn-rpmbuild -e \
        -Dmaven.test.skip=true \
        install javadoc:aggregate


%install

install -d -m 755 %{buildroot}%{_javadir}/
install -d -m 755 %{buildroot}%{_mavenpomdir}

install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap com.ning %{name} %{version} JPP %{name}

install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%post
%update_maven_depmap

%postun
%update_maven_depmap


%files
%defattr(-,root,root,-)
%doc README LICENSE-2.0.txt
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%defattr(-,root,root,-)
%doc LICENSE-2.0.txt
%{_javadocdir}/%{name}



