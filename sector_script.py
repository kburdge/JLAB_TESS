import numpy as np
from astropy.timeseries import LombScargle
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.timeseries import BoxLeastSquares
from astropy.io import fits

def load_LC(f):
    hdul = fits.open(f)
    t=hdul[1].data['TIME']
    y=hdul[1].data['PDCSAP_FLUX']
    dy=hdul[1].data['PDCSAP_FLUX_ERR']
    
    TICID=hdul[1].header['TICID']
    RA=hdul[1].header['RA_OBJ']
    Dec=hdul[1].header['DEC_OBJ']
    idx=y>0
    t=t[idx]
    y=y[idx]
    dy=dy[idx]

    return t, y, dy, RA, Dec, TICID

def binning(phases,y,dy,N=100):
    binned_LC=[]
    mean_phases=np.linspace(0,1-1/N,N)
    lightcurve=np.array((phases,y,dy)).T
    lightcurve=lightcurve[np.argsort(lightcurve[:,0])]
    for i in mean_phases:
        lightcurve_bin=lightcurve[lightcurve[:,0]>i]
        lightcurve_bin=lightcurve_bin[lightcurve_bin[:,0]<i+1/N]
        weights=1/(lightcurve_bin[:,2]**2)
        weighted_mean_flux=np.sum(lightcurve_bin[:,1]*weights)/np.sum(weights)
        weighted_mean_flux_error=np.sqrt(1/np.sum(weights))
        binned_LC.append((i+0.5/N,weighted_mean_flux,weighted_mean_flux_error))
    binned_LC=np.array(binned_LC)

    return binned_LC
    
#You are now ready to unleash this algorithm on the full TESS dataset. As a test, let us check how long it actually takes the execute.

import time
import pathlib
from tqdm import tqdm
from multiprocessing.pool import ThreadPool
#from astropy.timeseries import BoxLeastSquares
import astropy.units as u
t1=time.perf_counter()

def process_file(f):

    t, y, dy, RA, Dec, TICID = load_LC(f)
    frequency, power = LombScargle(t, y, dy).autopower(maximum_frequency=360)
    #model = BoxLeastSquares(t * u.day, y, dy)
    #periodogram = model.autopower(0.05)
    #period_BLS=periodogram.period
    #power_BLS=periodogram.power
    best_period=1/frequency[np.argmax(power)]
    best_power=np.max(power)
    #best_period=period_BLS[np.argmax(power_BLS)]
    #best_power=np.max(power_BLS)
    return TICID, RA, Dec, best_period, best_power


p = [str(pp) for pp in pathlib.Path('2min/').glob('*')]

#print(p)

t2=time.perf_counter()
with ThreadPool(processes=16) as pool:
    r_LS = list(tqdm(pool.imap(process_file, p), total=len(p)))
    np.savetxt('LS.result',r_LS)
t2=time.perf_counter()
print(t2-t1)

#Here is a slower algorithm designed to detect eclipses. We'll probably want to use GPU based implementations of this one.


from astropy.timeseries import BoxLeastSquares

t1=time.perf_counter()

def process_file(f):

    t, y, dy, RA, Dec, TICID = load_LC(f)
    model = BoxLeastSquares(t * u.day, y, dy)
    periodogram = model.autopower(0.5)
    period_BLS=periodogram.period
    power_BLS=periodogram.power
    best_period=period_BLS[np.argmax(power_BLS)]
    best_power=np.max(power_BLS)
    return TICID, RA, Dec, best_period.value, best_power


p = [str(pp) for pp in pathlib.Path('2min/').glob('*')]

#print(p)

t2=time.perf_counter()
with ThreadPool(processes=16) as pool:
    r_BLS = list(tqdm(pool.imap(process_file, p), total=len(p)))
    np.savetxt('BLS.result',r_BLS)
t2=time.perf_counter()
print(t2-t1)

r_BLS=np.array(r_BLS)
r_LS=np.array(r_LS)

for f in p:
    print(f)
    t, y, dy, RA, Dec, TICID = load_LC(f)
    #print(r[:,0])
    solution_LS=r_LS[r_LS[:,0]==TICID][0]
    solution_BLS=r_BLS[r_BLS[:,0]==TICID][0]
    best_period_LS=solution_LS[3]
    best_power_LS=1000*solution_LS[4]
    phase=(t%best_period_LS)/best_period_LS
    binned_LC=binning(phase,y,dy,N=100)
    if best_power_LS>10:
        plt.errorbar(binned_LC[:,0],binned_LC[:,1],binned_LC[:,2],ls=' ')
        plt.savefig('output_LS/'+str(best_power_LS)+'_'+str(TICID)+'_'+str(RA)+'_'+str(Dec)+'_'+str(best_period_LS)+'.png')
        plt.close()
        best_period_LS=solution_LS[3]
    best_period_BLS=solution_LS[3]
    best_power_BLS=10*solution_BLS[4]
    phase=(t%best_period_BLS)/best_period_BLS
    binned_LC=binning(phase,y,dy,N=100)
    if best_power_BLS>10:
        plt.errorbar(binned_LC[:,0],binned_LC[:,1],binned_LC[:,2],ls=' ')
        plt.savefig('output_BLS/'+str(best_power_BLS)+'_'+str(TICID)+'_'+str(RA)+'_'+str(Dec)+'_'+str(best_period_BLS)+'.png')
        plt.close()
