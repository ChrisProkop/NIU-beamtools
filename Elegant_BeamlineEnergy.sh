# Requires sddsplot
# Argument one is the root filename of the simulation.
# Argument two and argument three are additional arguments for sddsplot
sddsplot $2 -legend -column=s,pCentral -graph=line,vary \
      $1.cen -column=s,Profile -graph=line,type=7 -overlay=xmode=norm,yfact=0.1,yoffset=10 $1.mag -title='' -topline=' ' $3
