import pylab as pyl
import math
dt = 0.01
ena = 55
gna = 35
ek = -90
gk = 9
el = 65
gl = 0.1
cm = 1
phi= 5
iap= 0.2
v0= -65

def ina(m, h, v): return ( gna * ( m ** 3 )  * h * ( v - ena ) )
def ik (n, v)   : return ( gk  * ( n ** 4 ) * ( v - ek ) )
def il (v)      : return ( gl  * ( v - el ) )

def am (v) : return ( 0.1  * (v + 35) / ( 1 - math.exp (-(v + 35)/10) ))
def bm (v) : return ( 4    * math.exp(-(v + 60)/18) )
def an (v) : return ( 0.01 * (v + 34) / ( 1- math.exp (-0.1*(v + 34)) ) )
def bn (v) : return ( 0.125* math.exp(-(v + 44)/80) )
def ah (v) : return ( 0.07 * math.exp(-(v + 58)/20) )
def bh (v) : return (   1             / ( math.exp (-0.1*(v + 28)) + 1 ) )

def mnh  (a , b) : return ( a /( a + b ) )
def tau  (a , b) : return ( (1 /phi) * (1 /( a + b )) )

def HH (v, m, n, h, t) :    
    
    vp = v + (dt * (1 / cm) * ( iap - ( ina (m, h, v) + ik (n, v) + il (v))))
    tp = t + dt
    mp =    mnh ( am(vp), bm(vp))
    h_inf = mnh ( ah(vp), bh(vp))
    h_tau = tau ( ah(vp), bh(vp))
    n_inf = mnh ( an(vp), bn(vp))
    n_tau = tau ( an(vp), bn(vp))

    hp  = (( h - h_inf ) * math.exp( - dt / h_tau ) ) + h_inf
    np  = (( n - n_inf ) * math.exp( - dt / n_tau ) ) + n_inf   
    return (vp, mp, np, hp, tp)

vs = []
ms = []
ns = []
hs = []
ts = []

a = v0
b = mnh( am(v0), bm(v0) )
c = mnh( an(v0), bn(v0) )
d = mnh( ah(v0), bh(v0) )
e =  0.0 
vs . append (a)
ms . append (b)
ns . append (c)
hs . append (d)
ts . append (e)
    
for  i in ( range (1 ,3000)):
    a, b, c, d, e = HH(vs[-1],ms[-1],ns[-1],hs[-1],ts[-1])
    vs . append (a)
    ms . append (b)
    ns . append (c)
    hs . append (d)
    ts . append (e)
pyl . plot (ts , vs)
pyl . show ( )
