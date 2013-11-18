elegant-beamplots
=================

Some shell script simplified tools  for plotting the results of particle accelerator simulations in Elegant.

These scripts use sddsplot and command line arguments, and assume the default filename options for elegant output, i.e. that the core file is filename.ele, Courant-Snyder/Twiss parameters are filename.twi, etc.  The goal of this is to simplify the plots that are frequently used in diagnostics and studies, while eliminating the need to remember "Which of the output files contains the normalized corrected emittance?  What is its name agian?"

It requires sddsplot to be installed.  It uses command linees of the form:

elegant $1 $2 $3 $4

$1 is typically the root filename of the elegant simulation or the name of the distribution that you are inspecting, while the remainder are arguments.  Some arguments are optional, while others are mandatory.

