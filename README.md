# JLAB_TESS
## Objective
Discover light curves for binary star systems, measure the stars' properties from analyzing the light curve data, and measuring uncertainties using MCMC sampling when working with complex functions.

## Background
From studying light curve data (brightness over time, we can deduce a considerable amount of information about the properties of astronomical objects. In this lab, we are interested in utilizing a repository of light curve data from Transiting Exoplanet Survey Satellite (TESS) to discover binary stars and understand their properties.

[Binary stars](https://en.wikipedia.org/wiki/Binary_star) have lightcurves containing certain distinctive features. In the figure below, we see two dips in brightness during every period (corresponding to an orbit of one star around another). These correspond to eclipsing events when one star partially blocks the light from the other in the detector's line-of-sight, decreasing the total amount of light reaching the detector. The depths, widths, curvatures, and other characteristics of light curve depend on many physical parameters of the stars, and in this lab, you will learn how to calculate these parameters.

<img width="540" alt="Screen Shot 2022-08-08 at 1 26 55 AM" src="https://user-images.githubusercontent.com/42904723/183345514-1238da26-6d95-4ded-98d2-90eb1f3e2853.png">

TESS was primarily designed to discover exoplanets orbiting nearby bright stars, but as you will see, there are quite a few TESS candidate light curves that are highly unlikely due to exoplanets, but instead binary stars!

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
Go on [JupyterHub](https://submit00.mit.edu/jupyter), launch the server, and select `tess` as the kernel.
<img width="400" alt="Screen Shot 2022-08-08 at 12 59 32 AM" src="https://user-images.githubusercontent.com/42904723/183342604-1faf4bb6-2d1c-45c4-b369-f0fcfbbbcdb1.png">


## Tutorials on Lomb-Scargle (and related period-finding algorithms), ELLC, and MCMC Sampling
There are several iPython notebooks that are useful to understand working with light curve data.
We recommend you to go through the following notebook tutorials in order.

#### 1_basic_lomb_scargle_tutorial.ipynb

This notebook introduces the basics of using the Lomb-Scargle period finding algorithm. Lomb-Scargle is an analog of the Fourier transform, adapted to the non-equispaced sampling characteristic of astronomical time series [1]. We phase-fold the light curves and generate their plots, which will aid in discovering binary star candidates later on.

#### 2_applying_lomb_scargle_to_TESS_lightcurve.ipynb
This module will apply astropy's Lomb-Scargle algorithm to real data from the Transiting Exoplanet Survey Satellite (TESS). You will learn how to open and extract the relevant data from the TESS .fits files.

#### 3_applying_lomb_scargle_to_TESS_sector.ipynb
This module will apply the Lomb-Scargle algorithm onto an entire sector of TESS (containing ~20,000 targets). We implement multithreading to speed up processing the files and data.

#### 4_ellc_tutorial.ipynb

We demonstrate how to use the [ellc](https://github.com/pmaxted/ellc) python module to generate light curves from inputting binary star system parameters relating to the radii, semi-major axis, inclination angle, surface brightness ratio, etc [2].

#### 5_initial_ellc_fit.ipynb
We show how to perform an initial fit of the ellc model onto real light curve data. We make an initial estimate of the parameters, set up bounds, and use scipy's minimize function to perform the fitting.

#### TODO: there are multiple python libraries that support MCMC library. Figure out which could be the most appropriate for a JLAB student. 
An advantage of using ultranest is both speed, and the fact that students will be able to interface with slurm.

## Experiment and Analysis
Discover a binary star light curve candidate from the repository of TESS data. Once you've found your candidate, fit an ELLC model and measure the parameters of the star system. Perform an MCMC sampling of the model on the data to get uncertainty values for the lightcurve parameters.

You may NOT use any of the candidates used in our example code (todo: insert target object ids).

Alternative suggestion for JLAB experiment
- provide students with white dwarf-white dwarf binary system light curve used for calibrating LISA
- model the experiment after Joan's RSI project
- Pros: we can incorporate the white dwarf mass-radii relationship so students can get the absolute masses from fitting ELLC, perform further calculations such as solving for the system's semi-major axis with Kepler's laws, etc.

## References
[1] Jacob T. VanderPlas 2018 ApJS 236 16

[2] Maxted, P.F.L. 2016. A fast, flexible light curve model for detached
   eclipsing binary stars and transiting exoplanets. A&A 591, A111
