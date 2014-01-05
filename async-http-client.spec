%{?_javapackages_macros:%_javapackages_macros}
Name:           async-http-client
Version:        1.7.19
Release:        1.0%{?dist}
Summary:        Asynchronous Http Client for Java

License:        ASL 2.0
URL:            https://github.com/AsyncHttpClient/%{name}
Source0:        https://github.com/AsyncHttpClient/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(io.netty:netty)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
# Test dependencies
BuildRequires:  mvn(commons-fileupload:commons-fileupload)


%description
Async Http Client library purpose is to allow Java applications to
easily execute HTTP requests and asynchronously process the HTTP
responses. The Async HTTP Client library is simple to use.


%package javadoc
Summary:   API documentation for %{name}

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Remove test deps
%pom_remove_dep ch.qos.logback:logback-classic
%pom_remove_dep org.eclipse.jetty:jetty-websocket
%pom_remove_dep org.eclipse.jetty:jetty-servlets
%pom_remove_dep org.eclipse.jetty:jetty-server
%pom_remove_dep org.eclipse.jetty:jetty-servlet
%pom_remove_dep org.eclipse.jetty:jetty-security
%pom_remove_dep org.apache.tomcat:coyote
%pom_remove_dep org.apache.tomcat:catalina

# Remove tests that we can't build because of missing dependencies
# Some tests require jetty 8 or tomcat 6
rm -Rf src/test/java/com/ning/http/client/async
rm -Rf src/test/java/com/ning/http/client/websocket

# Remove things for which we are missing dependencies
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-gitsite']]"
%pom_xpath_remove "pom:profiles/pom:profile[pom:id[text()='grizzly']]"

# Animal sniffer is causing more trouble than good
%pom_remove_plugin :animal-sniffer-maven-plugin

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc README.md LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt


%changelog
* Tue Sep 03 2013 Michal Srb <msrb@redhat.com> - 1.7.19-1
- Update to upstream version 1.7.19

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Michal Srb <msrb@redhat.com> - 1.7.18-1
- Update to upstream version 1.7.18

* Wed Jun 26 2013 Michal Srb <msrb@redhat.com> - 1.7.17-4
- Fix licensing
- Run at least some tests

* Mon Jun 17 2013 Michal Srb <msrb@redhat.com> - 1.7.17-3
- Add CDDL+GPLv2 license text

* Fri Jun 14 2013 Michal Srb <msrb@redhat.com> - 1.7.17-2
- Fix license tag

* Mon Jun 03 2013 Michal Srb <msrb@redhat.com> - 1.7.17-1
- Update to upstream version 1.7.17

* Fri May 24 2013 Michal Srb <msrb@redhat.com> - 1.7.16-2
- Fix BR

* Fri May 24 2013 Michal Srb <msrb@redhat.com> - 1.7.16-1
- Update to upstream version 1.7.16

* Tue May 07 2013 Michal Srb <msrb@redhat.com> - 1.7.15-1
- Update to upstream version 1.7.15

* Thu May 02 2013 Michal Srb <msrb@redhat.com> - 1.7.14-1
- Update to upstream version 1.7.14

* Mon Apr 15 2013 Michal Srb <msrb@redhat.com> - 1.7.13-1
- Update to upstream version 1.7.13

* Fri Mar 15 2013 Michal Srb <msrb@redhat.com> - 1.7.12-1
- Update to upstream version 1.7.12

* Wed Mar 06 2013 Michal Srb <msrb@redhat.com> - 1.7.11-1
- Update to latest upstream version 1.7.11
- Build with XMvn

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.7.10-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 24 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.10-1
- Update to upstream version 1.7.10

* Wed Dec 19 2012 Michal Srb <msrb@redhat.com> - 1.7.8-2
- Update to upstream version 1.7.9

* Mon Dec  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.8-1
- Update to upstream version 1.7.8

* Mon Nov 12 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.7-1
- Update to upstream version 1.7.7

* Thu Oct 25 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.6-1
- Update to upstream version 1.7.6
- Update to current packaging guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.1-3
- Add maven-enforcer-plugin to BR

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 25 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6.1-1
- Update to latest upstream

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.1-2
- Add maven-shade-plugin to BR

* Mon Jan 17 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.1-1
- Initial version

