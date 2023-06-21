#
# Tcl package index file
#
# On Tk 8.7 and higher, do a no-op load, as svg support is buildin.
# As Tk may be loaded as a package, do the test on package require.
# Note, that multiple Tk packages with different versions may be available.
# The right Tk should be loaded before package require tksvg anyway.

package ifneeded @PACKAGE_NAME@ @PACKAGE_VERSION@ \
	"if {\[package vcompare 8.7a0 \[package require Tk\]\] == 1} {
		[list load [file join $dir @PKG_LIB_FILE@] [string totitle @PACKAGE_NAME@]]
	} else {
		package provide @PACKAGE_NAME@ @PACKAGE_VERSION@
	}"