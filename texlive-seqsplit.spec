# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/seqsplit
# catalog-date 2007-07-23 22:41:48 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-seqsplit
Version:	0.1
Release:	11
Summary:	Split long sequences of characters in a neutral way
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/seqsplit
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seqsplit.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seqsplit.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seqsplit.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
When one needs to type long sequences of letters (such as in
base-sequences in genes) or of numbers (such as calculations of
transcendental numbers), there's no obvious break points to be
found. The package provides a command \seqsplit, which makes
its argument splittable anywhere, and then leaves the TeX
paragraph-maker to do the splitting. While the package may
obviously be used to typeset DNA sequences, the user may
consider the dnaseq as a rather more powerful alternative.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/seqsplit/seqsplit.sty
%doc %{_texmfdistdir}/doc/latex/seqsplit/README
%doc %{_texmfdistdir}/doc/latex/seqsplit/seqsplit.pdf
#- source
%doc %{_texmfdistdir}/source/latex/seqsplit/Makefile
%doc %{_texmfdistdir}/source/latex/seqsplit/seqsplit.dtx
%doc %{_texmfdistdir}/source/latex/seqsplit/seqsplit.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 755909
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719507
- texlive-seqsplit
- texlive-seqsplit
- texlive-seqsplit
- texlive-seqsplit

