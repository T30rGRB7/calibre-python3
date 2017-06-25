#!/bin/sh
pkgdir="$1"

# Create directories
install -d "${pkgdir}/usr/share/zsh/site-functions" "${pkgdir}"/usr/share/{applications,desktop-directories,icons/hicolor}

# Install mimetype file
install -Dm644 resources/calibre-mimetypes.xml "${pkgdir}/usr/share/mime/packages/calibre-mimetypes.xml"

# Run "setup.py install" using Python 3
XDG_DATA_DIRS="${pkgdir}/usr/share" LANG='en_US.UTF-8' python3 setup.py install --staging-root="${pkgdir}/usr" --prefix=/usr

# Compile python bytecode
python3 -m compileall "${pkgdir}/usr/lib/calibre/"
python3 -O -m compileall "${pkgdir}/usr/lib/calibre/"
