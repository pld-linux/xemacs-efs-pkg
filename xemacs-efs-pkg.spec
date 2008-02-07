Summary:	Treat files on remote systems the same as local files
Summary(pl.UTF-8):	Traktowanie plików na zdalnych systemach jako lokalne
Name:		xemacs-efs-pkg
%define 	srcname	efs
Version:	1.32
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	6123c11bc7a9c993429e9976f7bf42c4
Patch0:		%{name}-info.patch
URL:		http://www.xemacs.org/
BuildRequires:	texinfo
Requires:	xemacs
Requires:	xemacs-base-pkg
Requires:	xemacs-dired-pkg
Requires:	xemacs-vm-pkg
Conflicts:	xemacs-sumo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EFS is a system for transparent file-transfer between remote VMS, CMS,
MTS, MVS, Twenex, Explorer (the last two are Lisp machines), TOPS-20,
DOS (running the Distinct, Novell, FTP software, NCSA, Microsoft in
both Unix and DOS mode, Super TCP, and Hellsoft FTP servers), Windows
NT (running the Microsoft or Hummingbird FTP servers), Unix
descriptive listings (dl), KA9Q, OS/2 hosts using FTP. This means that
you can edit, copy and otherwise manipulate files on any machine you
have access to from within Emacs as if it were a local file. EFS works
by introducing an extended filename syntax, and overloading functions
such as `insert-file-contents' so that accessing a remote file causes
appropriate commands to be sent to an FTP process. EFS includes and
enhanced version of Dired to facilitate directory browsing and
multiple file transfer from remote hosts.

%description -l pl.UTF-8
EFS jest systemem przezroczystego transferu plików pomiędzy zdalnym
VMS, CMS, MTS, MVS, Twenex, Explorer (przynajmniej dwa są maszynami
lispowymi), TOPS-20, DOS (z działającym Distinct, Novell, FTP, NCSA,
Microsoft w trybie Unix lub DOS, Super TCP, Hellsoft FTP), Windows NT
(z serwerem FTP Microsoftu lub Hummingbird), Unix descriptive listings
(dl), KA9Q, OS/2 z użyciem FTP. To znaczy, że możesz modyfikować,
kopiować i w inny sposób manipulować plikami na dowolnej maszynie do
której masz dostęp ze swojego Emacsa tak, jakby były to lokalne pliki.
EFS działa przez rozszerzoną składnię nazw plików i przeciążenie
funkcji typu "insert-file-contents" , więc dostęp do pliku zdalnego
powoduje wysłanie odpowiednich komend do procesu FTP. EFS zawiera
rozszerzoną wersję Dired, aby ułatwić przeglądanie katalogów i
ściąganie wielu plików ze zdalnych maszyn.

%prep
%setup -q -c
%patch0 -p1

%build
cd man/efs
awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc lisp/efs/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
%{_infodir}/*.info*
