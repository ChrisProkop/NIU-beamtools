# Requires sddsplot
# Argument one is the root filename of the simulation.
# Argument two and argument three are additional arguments for sddsplot

sddsplot -legend -column=s,enx -column=s,eny -graph=line,vary $1.s \
         -column=s,Profile \
         -graph=line,type=7  -overlay=xmode=norm,yfact=0.1,yoffset=1e-6 $1.mag  \
         -title='' -topline=' '  $2
