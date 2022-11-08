#!/usr/bin/env python
"""
Installs olltolls using distutils

Run:
    python setup.py install

to install this package.

(setup script partly borrowed from cherrypy)
"""

#--- IMPORTS ------------------------------------------------------------------

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

#from distutils.command.install import INSTALL_SCHEMES

import os, fnmatch


#--- METADATA -----------------------------------------------------------------

name         = "olltools"
desc         = "Python tools to analyze security characteristics of MS Office and OLE files (also called Structured Storage, Compound File Binary Format or Compound Document File Format), for Malware Analysis and Incident Response #DFIR"
long_desc    = open('olltools/README.rst').read()
author       = "TEAM-DEV KMI"


# see https://pypi.org/pypi?%3Aaction=list_classifiers
classifiers=[
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Science/Research",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Security",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

#--- PACKAGES -----------------------------------------------------------------

packages=[
    "olltools",
    "olltools.common",
    "olltools.common.log_helper",
    'olltools.thirdparty',
    'olltools.thirdparty.xxxswf',
    'olltools.thirdparty.prettytable',
    'olltools.thirdparty.xglob',
    'olltools.thirdparty.tablestream',
    'olltools.thirdparty.oledump',
]
##setupdir = '.'
##package_dir={'': setupdir}

#--- PACKAGE DATA -------------------------------------------------------------

## Often, additional files need to be installed into a package. These files are
## often data that?s closely related to the package?s implementation, or text
## files containing documentation that might be of interest to programmers using
## the package. These files are called package data.
##
## Package data can be added to packages using the package_data keyword argument
## to the setup() function. The value must be a mapping from package name to a
## list of relative path names that should be copied into the package. The paths
## are interpreted as relative to the directory containing the package
## (information from the package_dir mapping is used if appropriate); that is,
## the files are expected to be part of the package in the source directories.
## They may contain glob patterns as well.
##
## The path names may contain directory portions; any necessary directories will
## be created in the installation.


# the following functions are used to dynamically include package data without
# listing every file here:

def riglob(top, prefix='', pattern='*'):
    """
    recursive iterator glob
    - top: path to start searching from
    - prefix: path to use instead of top when generating file path (in order to
      choose the root of relative paths)
    - pattern: wilcards to select files (same syntax as fnmatch)

    Yields each file found in top and subdirectories, matching pattern
    """
    #print 'top=%s prefix=%s pat=%s' % (top, prefix, pattern)
    dirs = []
    for path in os.listdir(top):
        p = os.path.join(top, path)
        if os.path.isdir(p):
            dirs.append(path)
        elif os.path.isfile(p):
            #print ' - file:', path
            if fnmatch.fnmatch(path, pattern):
                yield os.path.join(prefix, path)
    #print ' dirs =', dirs
    for d in dirs:
        dtop = os.path.join(top, d)
        dprefix = os.path.join(prefix, d)
        #print 'dtop=%s dprefix=%s' % (dtop, dprefix)
        for p in riglob(dtop, dprefix, pattern):
            yield p

def rglob(top, prefix='', pattern='*'):
    """
    recursive glob
    Same as riglob, but returns a list.
    """
    return list(riglob(top, prefix, pattern))

package_data={
    'olltools': [
        'README.rst',
        'README.html',
        'LICENSE.txt',
        ],
        # # doc folder: md, html, png
        # + rglob('olltools/doc', 'doc', '*.html')
        # + rglob('olltools/doc', 'doc', '*.md')
        # + rglob('olltools/doc', 'doc', '*.png'),

    'olltools.thirdparty.xglob': [
        'LICENSE.txt',
        ],
    'olltools.thirdparty.xxxswf': [
        'LICENSE.txt',
        ],
    'olltools.thirdparty.prettytable': [
        'CHANGELOG', 'COPYING', 'README'
        ],
    'olltools.thirdparty.DridexUrlDecoder': [
        'LICENSE.txt',
        ],
    'olltools.thirdparty.tablestream': [
        'LICENSE', 'README',
         ],
    }


#--- data files ---------------------------------------------------------------

# not used for now.

## The data_files option can be used to specify additional files needed by the
## module distribution: configuration files, message catalogs, data files,
## anything which doesn?t fit in the previous categories.
##
## data_files specifies a sequence of (directory, files) pairs in the following way:
##
## setup(...,
##       data_files=[('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
##                   ('config', ['cfg/data.cfg']),
##                   ('/etc/init.d', ['init-script'])]
##      )
##
## Note that you can specify the directory names where the data files will be
## installed, but you cannot rename the data files themselves.
##
## Each (directory, files) pair in the sequence specifies the installation
## directory and the files to install there. If directory is a relative path,
## it is interpreted relative to the installation prefix (Python?s sys.prefix for
## pure-Python packages, sys.exec_prefix for packages that contain extension
## modules). Each file name in files is interpreted relative to the setup.py
## script at the top of the package source distribution. No directory information
## from files is used to determine the final location of the installed file;
## only the name of the file is used.
##
## You can specify the data_files options as a simple sequence of files without
## specifying a target directory, but this is not recommended, and the install
## command will print a warning in this case. To install data files directly in
## the target directory, an empty string should be given as the directory.



##data_files=[
##    ('balbuzard', [
##        'balbuzard/README.txt',
##                  ]),
##]

##if sys.version_info >= (3, 0):
##    required_python_version = '3.0'
##    setupdir = 'py3'
##else:
##    required_python_version = '2.3'
##    setupdir = 'py2'

##data_files = [(install_dir, ['%s/%s' % (setupdir, f) for f in files])
##              for install_dir, files in data_files]


##def fix_data_files(data_files):
##    """
##    bdist_wininst seems to have a bug about where it installs data files.
##    I found a fix the django team used to work around the problem at
##    http://code.djangoproject.com/changeset/8313 .  This function
##    re-implements that solution.
##    Also see http://mail.python.org/pipermail/distutils-sig/2004-August/004134.html
##    for more info.
##    """
##    def fix_dest_path(path):
##        return '\\PURELIB\\%(path)s' % vars()
##
##    if not 'bdist_wininst' in sys.argv: return
##
##    data_files[:] = [
##        (fix_dest_path(path), files)
##        for path, files in data_files]
##fix_data_files(data_files)


# --- SCRIPTS ------------------------------------------------------------------

# Entry points to create convenient scripts automatically

entry_points = {
    'console_scripts': [
        'ezhexviewer=olltools.ezhexviewer:main',
        'ftguess=olltools.ftguess:main',
        'mraptor=olltools.mraptor:main',
        'msodde=olltools.msodde:main',
        'ollbrowse=olltools.ollbrowse:main',
        'olldir=olltools.olldir:main',
        'ollid=olltools.ollid:main',
        'ollmap=olltools.ollmap:main',
        'ollmeta=olltools.ollmeta:main',
        'olltimes=olltools.olltimes:main',
        'ollvba=olltools.ollvba:main',
        'pyxswf=olltools.pyxswf:main',
        'rtfobj=olltools.rtfobj:main',
        'ollobj=olltools.ollobj:main',
        'ollfile=ollfile.ollfile:main',
    ],
}

# scripts=['oletools/olevba.py', 'oletools/mraptor.py']


# === MAIN =====================================================================

def main():
    # TODO: warning about Python 2.6
##    # set default location for "data_files" to
##    # platform specific "site-packages" location
##    for scheme in list(INSTALL_SCHEMES.values()):
##        scheme['data'] = scheme['purelib']

    dist = setup(
        name=name,
        description=desc,
        long_description=long_desc,
        classifiers=classifiers,
        author=author,
        # package_dir=package_dir,
        packages=packages,
        package_data = package_data,
        # data_files=data_files,
        entry_points=entry_points,
        test_suite="tests",
        # scripts=scripts,
        install_requires=[
            "pyparsing>=2.1.0,<3",  # changed from 2.2.0 to 2.1.0 for issue #481
            "olefile>=0.46",
            "easygui",
            'colorclass',
            # msoffcrypto-tool is not installable on PyPy+Windows (see issue #473),
            # so we only require it if the platform is not Windows or not PyPy:
            'msoffcrypto-tool; platform_python_implementation!="PyPy" or (python_version>="3" and platform_system!="Windows" and platform_system!="Darwin")',
            'pcodedmp>=1.2.5',
        ],
        extras_require={
            # Optional packages - to be installed with pip install -U oletools[full]
            'full': [
                'XLMMacroDeobfuscator',
                # Disabled the direct links to GitHub as it's now refused by PyPI:
                # For XLMMacroDeobfuscator, the release on PyPI is quite old compared
                # to the github version, so for now we have to install from github:
                # 'xlrd2@https://github.com/DissectMalware/xlrd2/archive/master.zip',
                # 'pyxlsb2@https://github.com/DissectMalware/pyxlsb2/archive/master.zip',
                # 'XLMMacroDeobfuscator@https://github.com/DissectMalware/XLMMacroDeobfuscator/archive/master.zip',
                # References for the syntax:
                # https://github.com/decalage2/oletools/issues/690
                # https://stackoverflow.com/questions/30239152/specify-extras-require-with-pip-install-e
            ]
        }
    )


if __name__ == "__main__":
    main()

