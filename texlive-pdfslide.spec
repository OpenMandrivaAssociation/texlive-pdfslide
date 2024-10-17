Name:		texlive-pdfslide
Version:	15878
Release:	2
Summary:	Presentation slides using pdftex
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfslide
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfslide.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfslide.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/pdfslide
%doc %{_texmfdistdir}/doc/latex/pdfslide

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
