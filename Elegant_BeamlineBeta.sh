# Requires sddsplot
# Argument one is the root filename of the simulation.
# Argument two and argument three are additional arguments for sddsplot
sddsplot $2 -legend -column=s,betax -column=s,betay -graph=line,vary \
      $1.twi -column=s,Profile -graph=line,type=7 -overlay=xmode=norm,yfact=0.1,yoffset=5 $1.mag -title='' -topline=' ' $3
