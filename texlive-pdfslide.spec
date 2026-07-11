%global tl_name pdfslide
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Presentation slides using pdfTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfslide
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfslide.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfslide.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a package for use with pdfTeX, to make nice presentation slides.
Its aims are: to devise a method for easier technical presentation; to
help the mix of mathematical formulae with text and graphics which other
present day document processing tools fail to accomplish; to exploit the
platform independence of TeX so that presentation documents become
portable; and to offer the freedom and possibilities of using various
backgrounds and other embellishments that a user can imagine to have in
as presentation. The package can make use of the facilities of the
PPower4 post-processor.

