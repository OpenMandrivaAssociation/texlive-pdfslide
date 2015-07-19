# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pdfslide
# catalog-date 2006-12-05 23:27:16 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-pdfslide
Version:	20061205
Release:	10
Summary:	Presentation slides using pdftex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfslide
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfslide.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfslide.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a package for use with pdftex, to make nice
presentation slides. Its aims are: to devise a method for
easier technical presentation; to help the mix of mathematical
formulae with text and graphics which the present day wysiwyg
tools fail to accomplish; to exploit the platform independence
of TeX so that presentation documents become portable; and to
offer the freedom and possibilities of using various
backgrounds and other embellishments that a user can imagine to
have in as presentation. The package can make use of the
facilities of the PPower4 post-processor.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdfslide/bg.jpg
%{_texmfdistdir}/tex/latex/pdfslide/d12.jpg
%{_texmfdistdir}/tex/latex/pdfslide/metablue.pdf
%{_texmfdistdir}/tex/latex/pdfslide/metagray.pdf
%{_texmfdistdir}/tex/latex/pdfslide/metagreen.pdf
%{_texmfdistdir}/tex/latex/pdfslide/metalgray.pdf
%{_texmfdistdir}/tex/latex/pdfslide/pdfslide.cfg
%{_texmfdistdir}/tex/latex/pdfslide/pdfslide.sty
%{_texmfdistdir}/tex/latex/pdfslide/slide.clo
%doc %{_texmfdistdir}/doc/latex/pdfslide/demo.pdf
%doc %{_texmfdistdir}/doc/latex/pdfslide/manual.tex
%doc %{_texmfdistdir}/doc/latex/pdfslide/meta.mp
%doc %{_texmfdistdir}/doc/latex/pdfslide/mpgraph.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061205-2
+ Revision: 754765
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061205-1
+ Revision: 719223
- texlive-pdfslide
- texlive-pdfslide
- texlive-pdfslide
- texlive-pdfslide

