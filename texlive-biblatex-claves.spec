%global tl_name biblatex-claves
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.1
Release:	%{tl_revision}.1
Summary:	A tool to manage claves of old literature with BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-claves
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-claves.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-claves.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
When studying antique and medieval literature, we may find many
different texts published with the same title, or, in contrary, the same
text published with different titles. To avoid confusion, scholars have
published claves, which are books listing ancient texts, identifying
them by an identifier -- a number or a string of text. For example, for
early Christianity, we have the Bibliotheca Hagiographica Graeca, the
Clavis Apocryphorum Novi Testamenti and other claves. It could be useful
to print the identifier of a texts in one specific clavis, or in many
claves. The package allows us to create new field for different claves,
and to present all these fields in a consistent way.

