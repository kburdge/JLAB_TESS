# JLAB_TESS
## Objective
Discover light curves for binary star systems and measure the stars' properties from analyzing the light curve data

## Background
Refer to the following sources: TODO (insert sources)


## Setup: subMIT, conda, the code repository for the lab, and JupyterHub.
This lab should mostly be done via an ssh into the subMIT cluster([user guide](http://submit04.mit.edu./submit-users-guide/intro.html)). We advise against doing this lab on your local computer as there are installation issues specific to the laptop's operating system (especially Windows) that the staff might not be able to help you on. 

Once you can ssh onto a subMIT machine, proceed to the next steps for setting up an environment for developing in Python.
1. ssh into submit.mit.edu, and install miniforge3 to `/work/submit/{your_kerb_user}`. In general, third-party software should be installed in your work directory, and your own code should be under your home directory (`/home/submit/{kerb_user}`). Additionally, `conda` memory requirements can be huge, and the work directory has a much larger disk quota than the home directory.

```
cd /work/submit/{kerb_user}
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh

# Run and follow instructions on screen
# Make sure to install into /work/submit/{kerb_user} instead of the default location, which is your user home directory!
bash Miniforge3-Linux-x86_64.sh
```

3. Create a new conda environment, let's name it ```tess```!

```
conda create --name tess python=3.9
``` 

4. Install packages for that environment
```
conda install gfortran_linux-64 gcc_linux-64
conda install pandas matplotlib scipy lmfit
pip install ellc astropy ultranest
```
5. Now go to your home directory and download this code repository from GitHub
```
cd /home/submit/{kerb_user}
git clone https://github.com/kburdge/JLAB_TESS.git
```
Congrats! You can now begin to made edits to the repository and start running iPython notebooks.
Go on [JupyterHub] (https://submit00.mit.edu/jupyter), launch the server, and select `tess` as the kernel.
<img width="400" alt="Screen Shot 2022-08-08 at 12 59 32 AM" src="https://user-images.githubusercontent.com/42904723/183342604-1faf4bb6-2d1c-45c4-b369-f0fcfbbbcdb1.png">


## Tutorials on Lomb-Scargle (and related period-finding algorithms), ELLC, and MCMC Sampling
There are several iPython notebooks that are useful to understand working with light curve data.
We recommend you to go through the following notebook tutorials in order.

#### 1_basic_lomb_scargle_tutorial.ipynb

This notebook introduces the basics of using the Lomb-Scargle period finding algorithm. Lomb-Scargle is an analog of the Fourier transform, adapted to the non-equispaced sampling characteristic of astronomical time series [1].

#### 2_applying_lomb_scargle_to_TESS_lightcurve.ipynb
This module will apply astropy's Lomb-Scargle algorithm to real data from the Transiting Exoplanet Survey Satellite (TESS). You will learn how to open and extract the relevant data from the TESS .fits files.

#### 3_applying_lomb_scargle_to_TESS_sector.ipynb
This module will apply the Lomb-Scargle algorithm onto an entire sector of TESS (containing ~20,000 targets). We implement multithreading to speed up processing the files and data.

#### 4_ellc_tutorial.ipynb

We demonstrate how to use the [ellc](https://github.com/pmaxted/ellc) python module to generate light curves from inputting binary star system parameters relating to the radii, semi-major axis, inclination angle, surface brightness ratio, etc [2].

#### 5_initial_ellc_fit.ipynb
We show how to perform an initial fit of the ellc model onto real light curve data. We make an initial estimate of the parameters, set up bounds, and use scipy's minimize function to perform the fitting.


## References
[1] Jacob T. VanderPlas 2018 ApJS 236 16
[2] Maxted, P.F.L. 2016. A fast, flexible light curve model for detached
   eclipsing binary stars and transiting exoplanets. A&A 591, A111
