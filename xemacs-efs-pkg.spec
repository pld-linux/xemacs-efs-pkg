Summary:	Treat files on remote systems the same as local files
Summary(pl):	Traktowanie plików na zdalnych systemach jako lokalne
Name:		xemacs-efs-pkg
%define 	srcname	efs
Version:	1.28
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
Patch0:		%{name}-info.patch
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
Requires:	xemacs-vm-pkg
Requires:	xemacs-dired-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EFS is a system for transparent file-transfer between remote VMS, CMS,
MTS, MVS, Twenex, Explorer (the last two are Lisp machines), TOPS-20,
DOS (running the Distinct, Novell, FTP software, NCSA, Microsoft in
both unix and DOS mode, Super TCP, and Hellsoft FTP servers), Windows
NT (running the Microsoft or Hummingbird ftp servers), Unix
descriptive listings (dl), KA9Q, OS/2 hosts using FTP. This means that
you can edit, copy and otherwise manipulate files on any machine you
have access to from within Emacs as if it were a local file. EFS works
by introducing an extended filename syntax, and overloading functions
such as `insert-file-contents' so that accessing a remote file causes
appropriate commands to be sent to an FTP process. EFS includes and
enhanced version of Dired to facilitate directory browsing and
multiple file transfer from remote hosts.

%description -l pl
EFS jest systemem przezroczystego transferu plików pomiêdzy zdalnym
VMS, CMS, MTS, MVS, Twenex, Explorer (przynajmniej dwa s± maszynami
lispowymi), TOPS-20, DOS (z dzia³aj±cym Distinct, Novell, FTP, NCSA,
Microsoft w trybie Unix lub DOS, Super TCP, Hellsoft FTP), Windows NT
(z serwerem FTP Microsoftu lub Hummingbird), Unix descriptive listings
(dl), KA9Q, OS/2 z u¿yciem FTP. To znaczy, ¿e mo¿esz modyfikowaæ,
kopiowaæ i w inny sposób manipulowaæ plikami na dowolnej maszynie do
której masz dostêp ze swojego Emacsa tak, jakby by³y to lokalne pliki.
EFS dzia³a przez rozszerzon± sk³adniê nazw plików i przeci±¿enie
funkcji typu "insert-file-contents" , wiêc dostêp do pliku zdalnego
powoduje wys³anie odpowiednich komend do procesu FTP. EFS zawiera
rozszerzon± wersjê Dired, aby u³atwiæ przegl±danie katalogów i
¶ci±ganie wielu plików ze zdalnych maszyn.

%prep
%setup -q -c
%patch0 -p1

%build
(cd man/efs; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

gzip -9nf lisp/efs/ChangeLog

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc lisp/efs/ChangeLog.gz
%{_infodir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
