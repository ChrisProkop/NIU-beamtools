import numpy as np
import matplotlib.pyplot as plt


## Commenters: CRP=Christopher R. Prokop, NIU

###### Code Outline:

# September 5th, 2013:::  
# This script is a set of reading and plottingfunctions, designed to work with our version of Impact-Z that has been modified to make a Format #"-2" that is similar to Impact-T's format.  This is kind of a messy work around, but is only applicable to the functions that read a specific distribution.  The functions that read the .18, .24, .25, .26 should work regardless.



# Suggested default plotting parameters. 

def ImpactZPlot_Init():
	params = {'backend': 'ps',
	  'axes.labelsize': 25,
	  'text.fontsize': 25,
	  'legend.fontsize': 18,
	  'font.size': 20,
	  'label.size': 20,
	  'xtick.labelsize': 20,
	  'ytick.labelsize': 20,
	  'text.usetex': False}
	plt.rcParams.update(params)


# Each file in Impact-Z


# The default filename is "fort", such that output files are named fort.18, fort.24, fort.25, fort.26, etc.  This is not a very elegant solution, so some kind of wrapper that copies and renames files is recommended.  


# This is used for the longitudinal beam data along the beamline, fort.18.
dt=np.dtype({'names':['z','avg','rms','bgavg','bgrms','CS','emit'],'formats' :[np.double,np.double,np.double,np.double,np.double,np.double,np.double,np.double]}) 

# This format is used for the directional data along the beamline, fort.24, fort.25, and fort.26.
dr=np.dtype({'names':['z','phase','gamma','K','beta','Rmax'],'formats': [np.double,np.double,np.double,np.double,np.double,np.double]})

dDist=np.dtype({'names':['x','px','y','py','z','pz'],'formats': [np.double,np.double,np.double,np.double,np.double,np.double]})


# A data type for storing the beam emittances.
dSigEmits=np.dtype({'names':['sigx','enx','sigy','eny','sigz','enz'],'formats':[np.double,np.double,np.double,np.double,np.double,np.double]})

# A structured data array for the beam centers.
dCenters=np.dtype({'names':['x', 'xp', 'y', 'yp', 'z', 'delta', 'gamma'],'formats':[np.double,np.double,np.double,np.double,np.double,np.double,np.double]})
## Appends .18, .24, .25, .26


# September 5th, 2013:  Takes a filename and adds the four "default" file extnesions that go with the default .fort naming conventions used by Impact-Z.
def ImpactZ_AppendStandardExtension(fileBase):

	path24= fileBase + '.24'
	path25= fileBase + '.25'
	path26= fileBase + '.26'
	path18= fileBase + '.18'

	return path18, path24, path25, path26



# September 5th, 2013:  Simple append function of a file extension.  Just here to help deal with some of Impact-Z's screwier naming conventions.  
def ImpactZ_AppendDumpExtension(fileBase, extensionNumber):
	fileDist= fileBase + '.' + extensionNumber
	print fileDist
	return fileDist



# September 5th, 2013:  Takes the four files specified by "ImpactZ_AppendStandardExtension" and reads the four data files.
def ImpactZ_ReadDataXYZ(file18,file24,file25,file26):
	Rp=np.loadtxt(open(file18), dtype=dr)
	Xp=np.loadtxt(open(file24), dtype=dt)
	Yp=np.loadtxt(open(file25), dtype=dt)
	Zp=np.loadtxt(open(file26), dtype=dt)
	return Rp, Xp, Yp, Zp
	


# September 5th, 2013: Appends and reads only the x parameters.
def ImpactZ_ReadDataX(fileBase):
	Xp=np.loadtxt(open(fileBase+'.24'), dtype=dt)
	return Xp


# September 5th, 2013: Appends and reads only the y parameters.
def ImpactZ_ReadDataY(fileBase):
	Yp=np.loadtxt(open(fileBase+'.25'), dtype=dt)
	return Yp



# September 5th, 2013: Appends and reads only the z parameters.
def ImpactZ_ReadDataZ(fileBase):
	Zp=np.loadtxt(open(fileBase+'.26'), dtype=dt)
	return Zp




# September 5th, 2013: Appends, reads, and plots (without the show()!) the three beam sizes.  It reads the wavelength due to how Impact-Z reports the z bunch lengths in terms of phase.
def ImpactZ_PlotSigmas_m(fileBase,wavelength,soffset):
	Rp=np.loadtxt(open(fileBase+'.18'), dtype=dr)
	Xp=np.loadtxt(open(fileBase+'.24'), dtype=dt)
	Yp=np.loadtxt(open(fileBase+'.25'), dtype=dt)
	Zp=np.loadtxt(open(fileBase+'.26'), dtype=dt)


	plt.plot(Xp['z']+soffset,Xp['rms'],'b-', label='\sigma_{x}')
	plt.plot(Yp['z']+soffset,Yp['rms'],'r-', label='\sigma_{y}')
	plt.plot(Zp['z']+soffset,Zp['rms']*(wavelength)/360.0,'g-',label='\sigma_{z}')
	# The wavelength conversion here is due to Impact-Z's use of phase as its longitudinal unit of measurement.



# September 5th, 2013: Appends, reads, and plots (without the show()!) the three beam sizes.  It reads the wavelength due to how Impact-Z reports the z bunch lengths in terms of phase.
def ImpactZ_PlotSigmas_mm(fileBase,wavelength,soffset):

	Rp=np.loadtxt(open(fileBase+'.18'), dtype=dr)
	Xp=np.loadtxt(open(fileBase+'.24'), dtype=dt)
	Yp=np.loadtxt(open(fileBase+'.25'), dtype=dt)
	Zp=np.loadtxt(open(fileBase+'.26'), dtype=dt)

	plt.plot(Xp['z']+soffset,Xp['rms']*1000.0,'b-', label='\sigma_{x}')
	plt.plot(Yp['z']+soffset,Yp['rms']*1000.0,'r-', label='\sigma_{y}')
	plt.plot(Zp['z']+soffset,Zp['rms']*(wavelength)*1000.0/360.0,'g-',label='\sigma_{z}')

# September 5th, 2013: Appends, reads, and plots (without the show()!) the three beam sizes on a semilog scale.  It reads the wavelength due to how Impact-Z reports the z bunch lengths in terms of phase.
def ImpactZ_PlotNormalizedEmittancesUM_SemiLog(fileBase,wavelength,soffset):

	Rp=np.loadtxt(open(fileBase+'.18'), dtype=dr)
	Xp=np.loadtxt(open(fileBase+'.24'), dtype=dt)
	Yp=np.loadtxt(open(fileBase+'.25'), dtype=dt)
	Zp=np.loadtxt(open(fileBase+'.26'), dtype=dt)

	plt.semilogy(Xp['z']+soffset,Xp['emit']*1.0e6,'b-', label='\sigma_{x}')
	plt.semilogy(Yp['z']+soffset,Yp['emit']*1.0e6,'r-', label='\sigma_{y}')
	plt.semilogy(Zp['z']+soffset,Zp['emit']*1.0e6/0.511*(wavelength)/360,'g-',label='\sigma_{z}')
	# The y units are here in micrometers by default.   This can easily be adjusted by 



### Added July 2nd, as shortcut to getting the relevant things in a single file.
def ImpactZ_SigmaEmittance_FromDist(distName):

	particleData=np.loadtxt(open(distName), dtype=dDist)

	sigx=np.std(particleData['x'])
	sigy=np.std(particleData['y'])
	sigz=np.std(particleData['z'])

	CenteredX=particleData['x'][2:]-np.average(particleData['x'][2:])
	CenteredXPrime=(particleData['px'][2:] - np.mean(particleData['px'][2:]))/np.mean(particleData['pz'][2:])

	CenteredY=particleData['y'][2:]-np.average(particleData['y'][2:])
	CenteredYPrime=(particleData['py'][2:] - np.mean(particleData['py'][2:]))/np.mean(particleData['pz'][2:])

	CenteredZ=particleData['z'][2:]-np.average(particleData['z'][2:])
	CenteredDelta=(particleData['pz'][2:] - np.mean(particleData['pz'][2:]))/np.mean(particleData['pz'][2:])

	gamma=np.mean(particleData['pz'][2:])


	enx=np.sqrt(np.average( CenteredX**2) * np.average(CenteredXPrime**2) - np.average(CenteredX * CenteredXPrime)**2   ) * gamma
	eny=np.sqrt(np.average( CenteredY**2) * np.average(CenteredYPrime**2) - np.average(CenteredY * CenteredYPrime)**2   ) * gamma
	enz=np.sqrt(np.average( CenteredZ**2) * np.average(CenteredDelta**2) - np.average(CenteredZ * CenteredDelta)**2   ) * gamma


#	ProcessedImpactZ=np.zeros((1,),dtype=dSigEmits)
#	ProcessedImpactZ[0]=(sigx, enx, sigy, eny, sigz, enz)
	ProcessedImpactZ=[sigx, enx, sigy, eny, sigz, enz]

	return ProcessedImpactZ




# September 5th, 2013:  Reports the beam center in six dimensions for a given distribution (-2, impact-T format).  This was necessary for diagnostics of the EEX, but is overall of fairly marginal use.
def ImpactZ_Centroids_FromDist(distName):

	particleData=np.loadtxt(open(distName), dtype=dDist)

	CenterX=np.average(particleData['x'][2:])
	CenterXPrime=np.mean(particleData['px'][2:])/np.mean(particleData['pz'][2:])

	CenterY=np.average(particleData['y'][2:])
	CenterYPrime=np.mean(particleData['py'][2:])/np.mean(particleData['pz'][2:])

	CenterZ=np.mean(particleData['z'][2:])
	CenterDelta=np.mean(particleData['pz'][2:]/np.mean(particleData['pz'][2:])-1)

	gamma=np.mean(particleData['pz'][2:])

	ProcessedImpactZCenters=(CenterX, CenterXPrime, CenterY, CenterYPrime, CenterZ, CenterDelta, gamma)

	return ProcessedImpactZCenters


# September 5th, 2013: Plots sigma_x with a label.  You don't have to show with the legend() command, but it is there if you need it.
def plotXrms_label(fileBase,label):
	Xp=np.loadtxt(open(fileBase+'.24'), dtype=dt)
	plt.plot(Xp['z'],Xp['rms'],label)
### Testing!
	return


# September 5th, 2013: Plots sigma_y with a label.  You don't have to show with the legend() command, but it is there if you need it.
def plotYrms_label(fileBase,label):
	Yp=np.loadtxt(open(fileBase+'.25'), dtype=dt)
	plt.plot(Yp['z'],Yp['rms'],label)
	return


# September 5th, 2013: Plots sigma_z with a label, but note that this is the RAW data, not the corrected length.  Needs scale/phase adjustments.  You don't have to show with the legend() command, but it is there if you need it.
def plotZrms_label(fileBase,label):
	Zp=np.loadtxt(open(fileBase+'.26'), dtype=dt)
	plt.plot(Zp['z'],Zp['rms'],label)
	return



# September 5th, 2013: Plots the x emittance with a label.  You don't have to show with the legend() command, but it is there if you need it.
def plotXemit_label(fileBase,label):
	Xp=np.loadtxt(open(fileBase+'.24'), dtype=dt)
	plt.plot(Xp['z'],Xp['emit'],label)
	return





# September 5th, 2013: Plots the y emittance with a label.  You don't have to show with the legend() command, but it is there if you need it.
def plotYemit_label(fileBase,label):
	Yp=np.loadtxt(open(fileBase+'.25'), dtype=dt)
	plt.plot(Yp['z'],Yp['emit'],label)
	return



# September 5th, 2013: Plots the z emittance with a label.  You don't have to show with the legend() command, but it is there if you need it.
def plotZemit_label(fileBase,label):
	Zp=np.loadtxt(open(fileBase+'.26'), dtype=dt)
	plt.plot(Zp['z'],Zp['emit'],label)
	return


# September 5th, 2013:  Reads a 
def ImpactZ_ReadDistribution35(distPath):
	particleData=np.loadtxt(open(distPath), dtype=dDist)
	return particleData
