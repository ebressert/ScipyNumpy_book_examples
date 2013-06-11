import string
import subprocess
import numpy as np
import scipy.stats as s
import matplotlib.pyplot as plt

# Setting up fiture size and spacing
fig = plt.figure(figsize=(8, 9))
fig.subplots_adjust(hspace=0, wspace=0)

# The distributions that will be plotted
dists = ['norm', 'lognorm', 'gamma', 'invgauss', 'cauchy',
         'logistic', 'maxwell', 'powerlaw', 'rdist',
         'wald', 'alpha', 'rayleigh', 'triang', 'lomax',
         'laplace', 'gilbrat', 'fisk', 'erlang', 't', 'nakagami']

dists = np.sort(dists)

for i, D in enumerate(dists):
    print D
    x = np.linspace(-5, 5, 1000)
    func = s.__dict__[D]

    try:
        dist = func(loc=0)
        pdf = dist.pdf(x)
    except:
        dist = func(0.7)
        pdf = dist.pdf(x)

    ax = fig.add_subplot(5, 4, i + 1)
    D = string.upper(D[0]) + D[1::]
    ax.plot(x, pdf, label=D)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, pdf.max() * 1.5)
    ax.legend(loc='upper right', markerscale=0.0001, prop={'size': 10})

    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    llines = leg.get_lines()
    frame = leg.get_frame()
    plt.setp(llines, linewidth=0)
    leg.draw_frame(False)

savename = 'scipy_341_ex1.pdf'
fig.savefig(savename, bbox_inches='tight')

# Calling OS for pdfcrop (Unix and Linux based systems only)
try:
    subprocess.call(['pdfcrop', savename, savename])
except:
    print 'This feature will only work if pdfcrop is available'
