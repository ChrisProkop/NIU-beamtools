# Requires sddsplot
# Argument one is the root filename of the simulation.
# Argument two and argument three are additional arguments for sddsplot

<<<<<<< HEAD
sddsplot -legend -column=s,enx -column=s,eny -graph=line,vary $1.s \
         -column=s,Profile \
         -graph=line,type=7  -overlay=xmode=norm,yfact=0.1,yoffset=1e-6 $1.mag  \
         -title='' -topline=' '  $2
=======
sddsxref $1.twi $1.s temp.tmp -take=Sx,Sy,ex,ey,Sdelta,Sxp,Syp
sddsprocess temp.tmp -nowarn  \
	"-define=column,Betax,Sx sqr etax Sdelta * sqr - ex /,symbol=\$gb\$r\$bx\$n,units=m" \
	"-define=column,Betay,Sy sqr etay Sdelta * sqr - ey /,symbol=\$gb\$r\$by\$n,units=m" 


sddsplot -legend -column=s,enx -column=s,eny -graph=line,vary temp.tmp \
         -column=s,Profile \
         -graph=line,type=7  -overlay=xmode=norm,yfact=0.1,yoffset=$2 $1.mag  \
         -title='' -topline=' '  $3
>>>>>>> afadc69d5b62a1cca49fc22f889b7125af0c7ace
