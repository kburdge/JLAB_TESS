import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import scipy.stats as ss
import corner
import math
import ultranest
import ellc
from white_dwarf_relations import MR_Relation

param_names = ["m1","m2","incl","t_zero","sbratio","heat_1", "heat_2", "amp"]
df = pd.read_excel("1719ac.xlsx", header=None)
t = df[1].to_numpy()
y = df[2].to_numpy()
dy = df[3].to_numpy()

def my_prior_transform(cube):
    params = cube.copy()
    params[0] = cube[0]*0.4 + 0.01
    params[1] = cube[1]*0.3 + 0.01
    params[2] = cube[2]*0.999 + 0.001
    params[3] = cube[3]*0.06416 + 0.0
    params[4] = cube[4]*10000 + 1.0
    params[5] = cube[5]*10000 + 0.0
    params[6] = cube[6]*10000 + 0.0
    params[7] = cube[7]*0.3 + 0.9
    return params

def my_likelihood(cube):
    try:
        period = 0.06416281918142659
        r1 = cube[0]
        r2 = cube[1]
#        a = ((((0.0043*3.085*10**13)*((0.006110357523148*86400)**2)*(m1+m2))/(4*(3.141593**2))))**(1./3.)
#        a_R = a/(6.957*10**5)
#        r1 = MR_Relation(m1, 22200)/a_R
#        r2 = MR_Relation(m2, 16200)/a_R
        i = np.arccos(cube[2])*180.0/np.pi
        t_zero = cube[3]
        sbratio = cube[4]
        heat_1 = cube[5]
        heat_2 = cube[6]
        A = cube[7]
        model = A * ellc.lc(t_obs=t,radius_1=r1,radius_2=r2,sbratio=sbratio, incl=incl, t_zero=t_zero,period=period, heat_1=heat_1, heat_2=heat_2, shape_1='roche',shape_2='roche')
        chisq=((model-y)/dy)**2
        log_prob=-0.5*chisq.sum()
    except:
        log_prob = -10000000.0 # -np.inf
    if np.isnan(log_prob):
        log_prob = -10000000.0 # -np.inf
    return log_prob
num = 5
sampler = ultranest.ReactiveNestedSampler(param_names, my_likelihood, my_prior_transform,log_dir=f'results{num}') #,resume=True)
result = sampler.run(min_num_live_points=1000, dKL=np.inf, min_ess=500)
sampler.print_results()
from ultranest.plot import cornerplot
cornerplot(result)
plt.savefig(f'UltranestMCMC00{num}.jpg')
