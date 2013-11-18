<<<<<<< HEAD
# Requires sddsplot
# Argument one is the root filename of the simulation.
# Argument two and argument three are additional arguments for sddsplot
=======
# Requires sddsplot
# Argument one is the root filename of the simulation.
# Argument two and argument three are additional arguments for sddsplot
>>>>>>> 114b49eb133b17b49333f96f7269d629e0cf3532
sddsplot $2 -legend -column=s,alphax -column=s,alphay -graph=line,vary \
      $1.twi -column=s,Profile -graph=line,type=7 -overlay=xmode=norm,yfact=0.1,yoffset=10 $1.mag -title='' -topline=' ' $3
