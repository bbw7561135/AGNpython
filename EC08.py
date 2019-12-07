import pencil as pc
import numpy as np
import pylab as plt
import math
import os

HEAD = os.getcwd()
print(HEAD)

ts = pc.read_ts()

t = ts.t/2/math.pi

ts = pc.read_ts()
t = ts.t
time = t/2*math.pi
len_t = len(ts.t)

# Max_Orbits=np.round((time[len(time)-1]))
Max_Orbits = 150

n = 1
dn = 1

i = 0
di = 1

Orbit_Len = []

while i <= len(time)-1:
    if np.round(n*2.0*math.pi) == np.round(t[i]):
        Orbit_Len.append(len(t[:i]))
        n = n+dn
        i = i+di
    else:
        i = i+di
# ------------------

t = ts.t/2/math.pi

par = pc.read_param()

ecc_int = par.eccentricity

r = ts.xq2
phi = ts.yq2
vr = ts.vxq2
vphi = ts.vyq2

v2 = vr**2 + vphi**2
a = 1./(2/r-v2)
h = r**2*(vphi/r)
ep1 = (h**2)/a
e = (1-ep1)**0.5

e = e[:]+0.02

N = 50

kernel = np.ones((N,))/N

time = np.convolve(t, kernel, mode='valid')
ecc = np.convolve(e, kernel, mode='valid')

Sigmap = 1.
Omegap = 1./a**1.5
mstar = 8.35e2
q = par.pmass[1]
aspect_ratio = 0.05
eh = e/aspect_ratio
twave = mstar * aspect_ratio**4 / (q * Sigmap * a**2 * Omegap)
te = twave/0.780 * (1 - 0.14*eh**2 + 0.06*eh**3)

line = ecc_int*np.exp(-t/te)

LEN = Orbit_Len[len(Orbit_Len)-1]

line = np.convolve(line, kernel, mode='valid')

i = 0
di = 1

div = []

while i <= len(t)-1:
    div.append(6e-2)
    i = i+di

plt.plot(time[:LEN], ecc[:LEN], label='data')
plt.plot(time[:LEN], line[:LEN], label='model (CN08)', linestyle=':')
plt.plot(time[:LEN], div[:LEN], label='divergence point',
         linestyle='--', color='black')

plt.title(
    r'$\varepsilon$ Decay: $q=10^{-4}$, $h=0.05$, $M_\star = 8.5\times 10^{-2}$')
plt.xlabel(r'$t/T_0$')
plt.ylabel(r'$\varepsilon$')
plt.yscale('log')
plt.xlim([0, t.max()])
# plt.xlim([0,300])
plt.tight_layout()
plt.grid(True)
plt.legend()

plt.savefig('eccentricity_decay_fix.png')
# plt.show()
