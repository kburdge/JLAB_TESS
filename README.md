# JLAB_TESS
## Objective
Discover light curves for binary star systems and measure the stars' properties from analyzing the light curve data

## Background
Refer to the following sources: TODO (insert sources)


This lab should mostly be done using subMIT. More details for setting up an account on subMIT are located in the subMIT [user guide](http://submit04.mit.edu./submit-users-guide/intro.html). Once you can ssh onto a subMIT machine, proceed to the next section for setting up an environment for developing in Python.

## Setting up conda on subMIT and using JupyterHub

1. Copy and paste the following into ~/.bash_profile (create the file first if it does not exist already):
```
# .bash_profile
# Get the aliases and functions
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi
```
2. Install miniforge3
```
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
# Run and follow instructions on screen
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
5. Work on Jupyter hub here: https://submit00.mit.edu/jupyter and select the name of your conda environment (`tess` from above) before creating an iPython notebook.

## Tutorials on Lomb-Scargle (and related period-finding algorithms), ELLC, and MCMC Sampling
There are several iPython notebooks that are useful to understand working with light curve data.
We recommend you to go through the following notebook tutorials in order.

1_basic_lomb_scargle_tutorial.ipynb

2_applying_lomb_scargle_to_TESS_lightcurve.ipynb

3_applying_lomb_scargle_to_TESS_sector.ipynb

4_ellc_tutorial.ipynb

5_initial_ellc_fit.ipynb


