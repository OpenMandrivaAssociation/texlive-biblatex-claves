Name:		texlive-biblatex-claves
Version:	43723
Release:	2
Summary:	A tool to manage claves of old litterature with BibLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-claves
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-claves.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-claves.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
When studying antic and medieval literature, we may find many
different texts published with the same title, or, in contrary,
the same text published with different titles. To avoid
confusion, scholars have published claves, which are books
listing ancient texts, identifying them by an identifier -- a
number or a string of text. For example, for early
Christianity, we have the Bibliotheca Hagiographica Graeca, the
Clavis Apocryphorum Novi Testamenti and other claves. It could
be useful to print the identifier of a texts in one specific
clavis, or in many claves. The package allows us to create new
field for different claves, and to present all these fields in
a consistent way.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-claves
%doc %{_texmfdistdir}/doc/latex/biblatex-claves

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
