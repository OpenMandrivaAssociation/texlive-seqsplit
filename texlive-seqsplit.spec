%global tl_name seqsplit
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Split long sequences of characters in a neutral way
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/seqsplit
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/seqsplit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/seqsplit.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/seqsplit.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
When one needs to type long sequences of letters (such as in base-
sequences in genes) or of numbers (such as calculations of
transcendental numbers), there's no obvious break points to be found.
The package provides a command \seqsplit, which makes its argument
splittable anywhere, and then leaves the TeX paragraph-maker to do the
splitting. While the package may obviously be used to typeset DNA
sequences, the user may consider the dnaseq as a rather more powerful
alternative.

