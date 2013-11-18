# Requires sddsplot
# Argument one is the root filename of the simulation.
# Argument two and argument three are additional arguments for sddsplot

sddsplot -legend -column=s,ecnx -column=s,ecny -graph=line,vary $1.s \
         -column=s,Profile \
         -graph=line,type=7  -overlay=xmode=norm,yfact=0.1,yoffset=5e-6 $1.mag  \
         -title='' -topline=' '  $2
