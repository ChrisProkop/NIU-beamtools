import os as os
import numpy as np

### os and sys are used to execute the sddsprintout command.  Yes, it seems messy, and parts of it can be avoided with downloading the SDDSpython library from Argonne. 



### NumPy is used extensively, as the data is returned as structured data arrays.



### December 4th, 2013: CRP, more comments and cleaned up.
### 				The "PRINT" commands are typically placed only to remind the user what the various columns of the 
###				structured data array are.
###
###				Comments refer to the "default" filenames from Elegant, such as .mat for the SDDS file containing the matrix components.

### September 5th, 2013, CRP: Added more functions and comments, cleaned up the code.

#### March 22nd, 2013:  CRP:  Changed ENZ to unnormalized, as the calculation here was too specifc (assumed 40MeV)



#### Created December 2012
#dconfig=np.dtype({'names':['s','config'],'formats':[np.double,np.double,np.double]})
###def AdjustAcceleration(in_file,out_file,V0,phi0,V1,phi1,omega):
#.mag



# September 5th, 2013:   This just grabs the "schematic" outline of the beamline.  Typically in the .mag file, etc.
# The returned data are the vertices of a schematic drawing.  
def GrabElegantSchematic(fileName):
	os.system('sddsprintout ' + fileName + ' -column=s -column=Profile -nolabel -notitle > tmp.tmp')
	dconfig=np.dtype({'names':['s','config'],'formats':[np.double,np.double]})
	layoutData=np.loadtxt(open('tmp.tmp'), dtype=dconfig)
	return layoutData



#sddsprintout -columns=s -columns=betax -columns=betay -columns=alphax -columns=alphay -columns=etax -columns=etay -noLabel -noTitle -width=180 $1.twi
#.twi



# September 5th, 2013:  This reads the betatron and alpha out of the twiss file (.twi)
def GrabElegantBetaXY(fileName):
	os.system('sddsprintout ' + fileName + ' -columns=s -columns=betax -columns=betay -columns=alphax -columns=alphay -nolabel -notitle > tmp.tmp')
	dBeta=np.dtype({'names':['s','betax','betay','alphax','alphay'],'formats':[np.double,np.double,np.double,np.double,np.double]})
	BetaData=np.loadtxt(open('tmp.tmp'), dtype=dBeta)
	print ('BetaData[\'s\',\'betax\',\'betay\',\'alphax\',\'alphay\']')
	return BetaData



# September 5th, 2013:   Reads .mat for R52
def GrabElegantR52(fileName):
	os.system('sddsprintout ' + fileName + ' -columns=s -columns=R52  -nolabel -notitle > tmp.tmp')
	dR52=np.dtype({'names':['s','R52'],'formats':[np.double,np.double]})
	R52Data=np.loadtxt(open('tmp.tmp'), dtype=dR52)
	print ('R52Data[\'s\',\'R52\']')
	return R52Data


# September 5th, 2013:   Reads .mat for R51
def GrabElegantR51(fileName):
	os.system('sddsprintout ' + fileName + ' -columns=s -columns=R51  -nolabel -notitle > tmp.tmp')
	dR51=np.dtype({'names':['s','R51'],'formats':[np.double,np.double]})
	R51Data=np.loadtxt(open('tmp.tmp'), dtype=dR51)
	print ('R51Data[\'s\',\'R51\']')
	return R51Data

# September 5th, 2013:   Reads .mat for R16
def GrabElegantR16(fileName):
	os.system('sddsprintout ' + fileName + ' -columns=s -columns=R16  -nolabel -notitle > tmp.tmp')
	dR16=np.dtype({'names':['s','R16'],'formats':[np.double,np.double]})
	R16Data=np.loadtxt(open('tmp.tmp'), dtype=dR16)
	print ('R16Data[\'s\',\'R16\']')
	return R16Data


# September 5th, 2013:   Grab the first (x) line of the transfer matrix.
def GrabElegantR1x(fileName):
	os.system('sddsprintout ' + fileName + ' -columns=s -columns=R11  -columns=R12 -columns=R13 -columns=R14 -columns=R15 -columns=R16 -nolabel -notitle > tmp.tmp')
	dR1x=np.dtype({'names':['s','R11','R12','R13','R14','R15','R16'],'formats':[np.double,np.double,np.double,np.double,np.double,np.double,np.double]})
	R1xData=np.loadtxt(open('tmp.tmp'), dtype=dR1x)
	print ('R1xData[\'s\',\'R11\',\'R12\',\'R13\',\'R14\',\'R15\',\'R16\']')
	return R1xData



# September 5th, 2013:   Grab the second (xprime) line of the transfer matrix.
def GrabElegantR2x(fileName):
	os.system('sddsprintout ' + fileName + ' -columns=s -columns=R21  -columns=R22 -columns=R23 -columns=R24 -columns=R25 -columns=R26 -nolabel -notitle > tmp.tmp')
	dR2x=np.dtype({'names':['s','R21','R22','R23','R24','R25','R26'],'formats':[np.double,np.double,np.double,np.double,np.double,np.double,np.double]})
	R2xData=np.loadtxt(open('tmp.tmp'), dtype=dR2x)
	print ('R2xData[\'s\',\'R21\',\'R22\',\'R23\',\'R24\',\'R25\',\'R26\']')
	return R2xData



# September 5th, 2013:   Grab the third (y) line of the transfer matrix.
def GrabElegantR3x(fileName):
	os.system('sddsprintout ' + fileName + ' -columns=s -columns=R31  -columns=R32 -columns=R33 -columns=R34 -columns=R35 -columns=R36 -nolabel -notitle > tmp.tmp')
	dR3x=np.dtype({'names':['s','R31','R32','R33','R34','R35','R36'],'formats':[np.double,np.double,np.double,np.double,np.double,np.double,np.double]})
	R3xData=np.loadtxt(open('tmp.tmp'), dtype=dR3x)
	print ('R3xData[\'s\',\'R31\',\'R32\',\'R33\',\'R34\',\'R35\',\'R36\']')
	return R3xData


# September 5th, 2013:   Grab the fourth (yprime) line of the transfer matrix.
def GrabElegantR4x(fileName):
	os.system('sddsprintout ' + fileName + ' -columns=s -columns=R41  -columns=R42 -columns=R43 -columns=R44 -columns=R45 -columns=R46 -nolabel -notitle > tmp.tmp')
	dR4x=np.dtype({'names':['s','R41','R42','R43','R44','R45','R46'],'formats':[np.double,np.double,np.double,np.double,np.double,np.double,np.double]})
	R4xData=np.loadtxt(open('tmp.tmp'), dtype=dR4x)
	print ('R4xData[\'s\',\'R41\',\'R42\',\'R43\',\'R44\',\'R45\',\'R46\']')
	return R4xData



# September 5th, 2013:   Grab the fifth (z) line of the transfer matrix.
def GrabElegantR5x(fileName):
	os.system('sddsprintout ' + fileName + ' -columns=s -columns=R51  -columns=R52 -columns=R53 -columns=R54 -columns=R55 -columns=R56 -nolabel -notitle > tmp.tmp')
	dR5x=np.dtype({'names':['s','R51','R52','R53','R54','R55','R56'],'formats':[np.double,np.double,np.double,np.double,np.double,np.double,np.double]})
	R5xData=np.loadtxt(open('tmp.tmp'), dtype=dR5x)
	print ('R5xData[\'s\',\'R51\',\'R52\',\'R53\',\'R54\',\'R55\',\'R56\']')
	return R5xData




# September 5th, 2013:   Grab the fifth (energy) line of the transfer matrix.
def GrabElegantR6x(fileName):
	os.system('sddsprintout ' + fileName + ' -columns=s -columns=R61  -columns=R62 -columns=R63 -columns=R64 -columns=R65 -columns=R66 -nolabel -notitle > tmp.tmp')
	dR6x=np.dtype({'names':['s','R61','R62','R63','R64','R65','R66'],'formats':[np.double,np.double,np.double,np.double,np.double,np.double,np.double]})
	R6xData=np.loadtxt(open('tmp.tmp'), dtype=dR6x)
	print ('R6xData[\'s\',\'R61\',\'R62\',\'R63\',\'R64\',\'R65\',\'R66\']')
	return R6xData


# December 4th, 2013:  This returns the unnormalized Z emittance, as the data necessary to normalize the z emittance is in a different file.
def GrabElegantEXYZ_Updated (fileName):
	'''input:  .s file path and name
        output: EmitData['s','enx','eny','enz']'''
	os.system('rm tmp.s')
	os.system('sddsprocess ' + fileName + ' -nowarn "-define=column,ez,  Ss Ss * Sdelta * Sdelta * s56 s56 * - sqrt, units=m,symbol=\$ge\$r\$bz\,n$n" tmp.s')
	os.system('sddsprintout tmp.s -columns=s -columns=enx -columns=eny -columns=ez -nolabel -notitle > tmp.tmp')
	demitn=np.dtype({'names':['s','enx','eny','ez'],'formats':[np.double,np.double,np.double,np.double]})
	EmitData=np.loadtxt(open('tmp.tmp'), dtype=demitn)
	print('EmitData[\'s\',\'enx\',\'eny\',\'enz\']')
	return EmitData



# December 4th, 2013:   RMS lengths and momentum spreads, which are sigma_z, sigma_xprime, sigma_y, sigma_yprime, sigma_s, and sigma_delta.
def GrabElegantStd (fileName):
	os.system('sddsprintout '+fileName+' -columns=s -columns=Sx -columns=Sxp -columns=Sy -columns=Syp -columns=Ss -column=Sdelta -nolabel -notitle > tmp.tmp')
	dstd=np.dtype({'names':['s','Sx','Sxp','Sy','Syp','Ss','Sdelta'],'formats':[np.double,np.double,np.double,np.double,np.double,np.double,np.double]})
	StdData=np.loadtxt(open('tmp.tmp'), dtype=dstd)
	print ('StdData[\'s\',\'Sx\',\'Sxp\',\'Sy\',\'Syp\',\'Ss\',\'Sdelta\']')
	return StdData


# December 4th, 2013:   grabs the data from a specific elegant WATCH point (or final distribution), and returns it as a Python Numpy structured data type with Doubles.  GrabElegantWatchPrecision should typically be used, as the longitudinal coordinate "time" is often unsuitable for use as a double.
def GrabElegantWatch (fileName):
	os.system('sddsprintout '+ fileName + ' -columns=x -columns=xp -columns=y -columns=yp -columns=t -columns=p -nolabel -notitle > tmp.tmp')
	dwatch=np.dtype({'names':['x','xp','y','yp','t','p'],'formats':[np.double,np.double,np.double,np.double,np.double,np.double]})
	WatchData=np.loadtxt(open('tmp.tmp'), dtype=dwatch)
	print ('WatchData[\'x\',\'xp\',\'y\',\'yp\',\'t\',\'p\']')
	return WatchData

# December 4th, 2013:  This returns data from a WATCH point with floating-point precision, rather than as a double.  This is what should typically be used.
def GrabElegantWatchPrecision (fileName):
	os.system('sdds2stream '+ fileName + ' -columns=x -columns=xp -columns=y -columns=yp -columns=t -columns=p -nolabel -notitle > tmp.tmp')
	dwatch=np.dtype({'names':['x','xp','y','yp','t','p'],'formats':[np.float,np.float,np.float,np.float,np.float,np.float]})

	WatchData=np.loadtxt(open('tmp.tmp'), dtype=dwatch)
	print ('WatchData[\'x\',\'xp\',\'y\',\'yp\',\'t\',\'p\']')
	return WatchData
