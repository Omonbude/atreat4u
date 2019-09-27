<<<<<<< HEAD
if {[catch {package present Tcl 8.6.1}]} { return }
if {($::tcl_platform(platform) eq "unix") && ([info exists ::env(DISPLAY)]
	|| ([info exists ::argv] && ("-display" in $::argv)))} {
    package ifneeded Tk 8.6.1 [list load [file join $dir .. .. bin libtk8.6.dll] Tk]
} else {
    package ifneeded Tk 8.6.1 [list load [file join $dir .. .. bin tk86t.dll] Tk]
}
=======
if {[catch {package present Tcl 8.6.1}]} { return }
if {($::tcl_platform(platform) eq "unix") && ([info exists ::env(DISPLAY)]
	|| ([info exists ::argv] && ("-display" in $::argv)))} {
    package ifneeded Tk 8.6.1 [list load [file join $dir .. .. bin libtk8.6.dll] Tk]
} else {
    package ifneeded Tk 8.6.1 [list load [file join $dir .. .. bin tk86t.dll] Tk]
}
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
