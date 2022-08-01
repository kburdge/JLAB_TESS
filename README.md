# JLAB_TESS

This lab should mostly be done using subMIT. More details for setting up an account on subMIT are located in the subMIT [user guide](http://submit04.mit.edu./submit-users-guide/intro.html).

Once you can ssh onto a subMIT machine, proceed to the next section for setting up an environment for developing in Python.

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
5. Work on Jupyter hub here: https://submit00.mit.edu/jupyter and select the name of your conda environment (`tess` from above) before creating a Jupyter notebook.

## Tutorials on Lomb-Scargle (and related period-finding algorithms), ELLC, and MCMC Sampling
todo: briefly go over the notebooks and explain what students can learn from them





