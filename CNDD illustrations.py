import numpy as np
import matplotlib.pyplot as plt

# Constants and functions --------------------------------------------------------------------

a=1 # pathogen density at x=0
b=5.7 # difference in dispersiveness
c=2.8
d=1
g=0 # background spore density
k=1

def s(x): # seed dispersal
    return np.exp(-(x**2))

def p(x): # pathogen dispersal
    return a*np.exp(-b*(x**2))

def i(x): # infection rate
    return g + k/(1+d*np.exp(-c*x))

def dead(x): # death rate
    return i(p(x))

def t(x): # total seedling survival
    return s(x)*(1-i(p(x)))

# Generate data -------------------------------------------------------------------------------
xdata = np.linspace(0,3,300)
sdata = [s(x) for x in xdata]
pdata = [p(x) for x in xdata]
# print(pdata)
idata = [i(p(x)) for x in xdata] # note THIS is the one currently on the website
# idata = [i(x) for x in xdata]
# propdata = [dead(x)/s(x) for x in xdata] # proportion dead
# print(idata)
tdata = [t(x) for x in xdata]

# Aesthetics --------------------------------------------------------------------------------
font = {'size'   : 30}
plt.style.use('default')
plt.rc('font', **font)


from matplotlib import font_manager

font_dirs = ["C:/Users/jaked/Desktop/website"]
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Libre Caslon Text'

# First plot ----------------------------------------------------------------------------------
linewidth =4

fig, ax0 = plt.subplots(figsize=(15,12))
ax0.plot(xdata, sdata, label='seeds', color='black', linewidth=linewidth)
ax0.plot(xdata, pdata, label='pathogen spores', color='orange', linewidth=linewidth)
# ax0.plot(xdata, idata, label='infection success', color='xkcd:blue violet', linewidth=linewidth)
ax0.plot(xdata, idata, label='% seedlings dead', color='xkcd:blue violet', linewidth=linewidth)
ax0.plot(xdata, tdata, label='surviving seedlings', color='green', linewidth=linewidth)
ax0.set_ylim(0, 1)
ax0.set_xlim(0, 3)
ax0.set_ylabel("Density", labelpad=15)
ax0.set_xlabel("Distance from parent plant", labelpad=15)
fig.gca().xaxis.set_major_locator(plt.NullLocator())
fig.gca().yaxis.set_major_locator(plt.NullLocator())
ax0.legend(frameon=False)
ax0.set_facecolor('#fffdf5')
# fig.show()
fig.savefig('CNDD.svg', facecolor='#fffdf5', edgecolor='none', bbox_inches='tight')

# Second plot ---------------------------------------------------------------------------
fig, ax0 = plt.subplots(figsize=(15,12))
ax0.plot(xdata, sdata, label='seeds', color='black', linewidth=linewidth)
ax0.plot(xdata, pdata, label='pathogen spores', color='orange', linewidth=linewidth)
# ax0.plot(xdata, idata, label='infection success', color='xkcd:blue violet', linewidth=linewidth)
# ax0.plot(xdata, idata, label='% seedlings dead', color='xkcd:blue violet', linewidth=linewidth)
ax0.plot(xdata, tdata, label='surviving seedlings', color='green', linewidth=linewidth)
ax0.set_ylim(0, 1)
ax0.set_xlim(0, 3)
ax0.set_ylabel("Density", labelpad=15)
ax0.set_xlabel("Distance from parent plant", labelpad=15)
fig.gca().xaxis.set_major_locator(plt.NullLocator())
fig.gca().yaxis.set_major_locator(plt.NullLocator())
ax0.legend(frameon=False)
ax0.set_facecolor('#fffdf5')
# fig.show()
fig.savefig('CNDD2.svg', facecolor='#fffdf5', edgecolor='none', bbox_inches='tight')

