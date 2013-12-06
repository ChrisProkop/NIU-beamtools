NIU-beamtools
=============

Analysis, Visualization, and Data Reading tools developed for the Northern Illinois University Beam Physics group.

http://www.niu.edu/nicadd/


Authors and Acknowledgements
==================

Christopher R. Prokop

*Northern Illinois Center for Accelerator & Detector Development*

*Northern Illinois University Department of Physics*

(cprokop@gmail.com)
--------
Work by Christopher R. Prokop supported by Los Alamos LDRD project \#20110067DR,  by the U.S. Department of Energy Contract No. DE-FG02-08ER41532 with Northern Illinois University, and No. DE-AC02-07CH11359 with Fermilab.


Introduction
==========
This repository contains many shell and python scripts used for analysis, data visualization, and data processing for several common particle accelerator codes.  There are scripts for reading the output of different simulations into python, some general visualization tools, and some shell scripting to assist with the use of existing tools.


The simulation programs mentioned can be found at the following URLs:
Elegant:  http://www.aps.anl.gov/Accelerator_Systems_Division/Accelerator_Operations_Physics/software.shtml#elegant
(Argonne will email you an access code.  There may be approval issues for IP addresses outside of the US)



Impact-Z:  Beam tracking with kick-step space charge model, as well as a simple 1D model for Coherent Synchrotron Radiation when passing through Dipole Magnet bends.
http://amac.lbl.gov/~jiqiang/IMPACT/


Impact-T:  Time-domain original to Impact-Z.  
http://amac.lbl.gov/~jiqiang/IMPACT-T/


CSRtrack:  Simulation code to model Coherent Synchrotorn Radiation (CSR) using a variety of differeny models of varying computation complexity.  
http://www.desy.de/xfel-beam/csrtrack/
http://www.desy.de/xfel-beam/csrtrack/files/CSRtrack_User_Guide_(actual).pdf

Some Python libraries are used.  NumPy and Matplotlib are used extensively due to their data processing and plotting capabilities, respectively, while parts of SciPy are used sparingly.  Information on these libraries can be found at:





Various tools regarding the SDDS data format, including sddsprintout and sddsplot, and sddsanalyze beam:




Some shell script simplified tools  for plotting the results of particle accelerator simulations in Elegant.

These scripts use sddsplot and command line arguments, and assume the default filename options for elegant output, i.e. that the core file is filename.ele, Courant-Snyder/Twiss parameters are filename.twi, etc.  The goal of this is to simplify the plots that are frequently used in diagnostics and studies, while eliminating the need to remember "Which of the output files contains the normalized corrected emittance?  What is its name agian?"

It requires sddsplot to be installed.  It uses command linees of the form:

elegant $1 $2 $3 $4

$1 is typically the root filename of the elegant simulation or the name of the distribution that you are inspecting, while the remainder are arguments.  Some arguments are optional, while others are mandatory.

As an example:
>> Elegant_BeamlineBeta.sh elegant_simulation

would automatically append the .mag and .twi file extensions.  It would open elegant_simulation.mag and elegant_simulation.twi to generate a plot of the betatron functions across a simple schematic of the beamline.  



List of Python Files
=============



bdplotter_pro.py
---------------
This a very powerful plotting tool that gives density plots for any two components of a phase space.  Special functionality is added for time-profile phases spaces, notably the current profile.


Most of these variables adjust the arguments used for Matplotlib's hexbin function:  
 http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hexbin


X, the X values of the data set.  MANDATORY
Y, the Y values of the data set to be plotted.  MANDATORY

numHexes=51,    This is the number of bins on each side for which to perform the hexbinning.

numXHistBins=51,  numYHistBins=51,    These values set the number of bins for the histogram.  Default is the same as numHexes, but there are situations where a different scale is justified. 
numYHistBins=51

show_density=1,   This parameter dictates whether to show the density plot.  By default, this is the only, as "bdplotter" is short for "beam density plotter".  There are some cases, such as current profiles, where this should be turned off.  

show_xcurrent=0,  Shows the current projection on the X-axis.  Scaling is TBD.  This should not be used as an overlay to a density hexbin plot.


show_xhist=0

show_yhist=0

These parameters determine whether a histogram projection is shown on the x and y axis, respectively.  



xhist_scale=0.3

yhist_scale=0.3

These two parameters set the normalization of the histogram heights, as a fraction of the total heigth and width of the plot.  



histogram_linecode='r-' 

The default histograms use a red-line that displays well over the default greyscale density plot, though a different color may be useful for different color schemes.


bunch_charge=0

The default bunch charge is 0.  

xoffset=0

yoffset=0

density_type='log'.  

Log plots the density as a function log_10(i+1).  If you want a linear scale, you DO NOT enter 'linear'.  Rather, use an integer that sets the number of gradients in color (divided from max to min).  This can also be used a sequence of values that specify the range for each color.

threshold_population=0.  This value is subtracted from the bin population.

color_scale=pl.cm.Greys. 

This uses standard matplotlib color scales.  brg and jet are two of the more popular ones, but examples of all standard color maps can be found at:  http://www.physics.ox.ac.uk/Users/msshin/science/code/matplotlib_cm/











List of Shell Script Files
===========


Elegant_BeamlineAlpha.sh
--------------
Requires sddsplot

Argument one is the root filename of the simulation.

Argument two and argument three are additional arguments for sddsplot.  Of much use is -scales=xmin,xmax,ymin,ymax, which will set the limits for the plot. -scales=0,0,0,0 uses the default limits.



Elegant_BeamlineBeta.sh
--------------

Requires sddsplot

Argument one is the root filename of the simulation.

Argument two and argument three are additional arguments for sddsplot.  Of much use is -scales=xmin,xmax,ymin,ymax, which will set the limits for the plot.  -scales=0,0,0,0 uses the default limits.









References
==========
Elegant, M. Borland,  http://www.aps.anl.gov/Accelerator_Systems_Division/Accelerator_Operations_Physics/manuals/elegant_latest/elegant.html

M. Borland, "Self Describing Data Sets" http://www.aps.anl.gov/Accelerator_Systems_Division/Accelerator_Operations_Physics/SDDSIntroTalk/slides.pdf

M. Borland, ``A Self-Describing File Protocol for Simulation Integration and Shared Postprocessors,'' Proc. 1995 PAC, May 1-5, 1995, Dallas, Texas, pp. 2184-2186 (1996). 
