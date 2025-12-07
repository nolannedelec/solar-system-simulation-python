import numpy as np
import matplotlib . pyplot as plt
import matplotlib.animation as animation
import math
from mpl_toolkits.mplot3d import Axes3D

#fonction qui va calculer la vitesse initial et la retourner
def vitesse_periphélie(G,masse,demi_grand_axe,excentricité):
    v0=(((G*masse)/demi_grand_axe)*(1+excentricité)/(1-excentricité))**(1/2)
    return v0

#fonction qui va permettre de calculer tout les positions, les vitesses et les accélérations grâce à la méthode d'Euler
def graphique_euler(x0,y0,vx0,vy0,h,N,G,Ms):
    yn=[y0]                     # On créé une liste qui nous donne toute les valeurs de y selon des petits intervalles indiqués.
    xn=[x0]
    vxn=[vx0]
    vyn=[vy0]
    axn=[-G*Ms/(x0**2)]
    ayn=[0]
    r=math.sqrt(xn[0]**2+yn[0]**2)
    XN=x0
    YN=y0
    VXN=vx0
    VYN=vy0

    Z=[0]
    
    for n in range(N):
        
        r=math.sqrt(XN**2+YN**2)

        AXN=-G*Ms*XN/(r**(3))        # On prend le dernier element x de la liste qu'on multiplie par a.
        AYN=-G*Ms*YN/(r**(3))        # On prend le dernier element y de la liste qu'on multiplie par a.

        XN=XN+VXN*(h)  
        YN=YN+VYN*(h)

        VXN=VXN+AXN*(h)
        VYN=VYN+AYN*(h)
        
        xn.append(XN)
        yn.append(YN)
        axn.append(AXN)            # On ajoute chaques valeurs de y dans la liste.
        ayn.append(AYN)            # On ajoute chaques valeurs de y dans la liste.
        vxn.append(VXN)
        vyn.append(VYN)

        Z.append(0)

    return xn,yn,Z,vxn,vyn,Z                   # On renvoie les coordonées de la planète a tout temps de l'orbite.

def graphique_euler_asym(x0,y0,vx0,vy0,N,h,G,Ms):
    yn=[y0]                     # On créé des listes qui nous donneront toute les valeurs de y selon des petits intervalles indiqués.
    xn=[x0]
    vxn=[vx0]                   # On créé des listes qui contiendront plus tard tous nos valeurs
    vyn=[vy0]
    axn=[-G*Ms/(x0**2)]
    ayn=[0]
    r=math.sqrt(xn[0]**2+yn[0]**2)
    XN=x0
    YN=y0
    VXN=vx0
    VYN=vy0

    Z=[0]

    for n in range(N):
       
        r=math.sqrt(XN**2+YN**2)

        XN=XN+VXN*(h)
        YN=YN+VYN*(h)
       
        AXN=-G*Ms*XN/(r**(3))        # On prend le dernier element de la liste qu'on multiplie par a.
        AYN=-G*Ms*YN/(r**(3))        # On prend le dernier element de la liste qu'on multiplie par a.

        VXN=VXN+AXN*(h)
        VYN=VYN+AYN*(h)
       
        xn.append(XN)
        yn.append(YN)
        axn.append(AXN)            # On ajoute chaques valeurs de y dans la liste.
        ayn.append(AYN)            # On ajoute chaques valeurs de y dans la liste.
        vxn.append(VXN)
        vyn.append(VYN)

        Z.append(0)

    return xn,yn,Z,vxn,vyn,Z                   # On renvoie les coordonées de la planète a tout temps de l'orbite.

def erenyeager(xn,yn,vxn,vyn,Ms,Mp,G,h,lenMinimal):
    Em=[]
    temps=[]
    for i in range(lenMinimal):
        r=math.sqrt(xn[i]**2+yn[i]**2)
        Ep=G*Ms*Mp/r
        Ec=(1/2)*Mp*math.sqrt(vxn[i]**2+vyn[i]**2)**2
        Em.append(Ep+Ec)
        temps.append(i*h)
    
    return Em,temps

def nbI(T,h):           #nb d'intervalles pour faire un tour avec le même pas de temps entre les planètes
    N=T/h
    return int(N)

def update(frame,planete, t, conditions_initiales, xp, yp, zp, ps, h, G, Ms, ax, couleurs,vip):

    for i in conditions_initiales:# Euler Asymétrique
        if i =='Mercure':
            k=frame%88
        elif i =='Terre':
            k=frame%365
        if i =='Venus':
            k=frame%225
        if i =='Mars':
            k=frame%687
        f0=np.array(conditions_initiales[i])
        print(f0)
        xp[i].append(f0[0]) #ajout de x dans les listes
        yp[i].append(f0[1]) #ajout de y dans les listes
        zp[i].append(f0[2]) #ajout de z dans les listes

        x,y,z,vx,vy,vz=graphique_euler_asym(planete[i]['Périhélie'],0,0,vip[i],conditions_initiales[i][6],h,G,Ms)
        f0=[x[k],y[k],z[k],vx[k],vy[k],vz[k],conditions_initiales[i][6]]
        conditions_initiales[i] = f0   
    ligne = []

    for i in conditions_initiales:          #permet de créé la sphère au bout de la ligne
        point = ax.plot(xp[i], yp[i], zp[i], color=couleurs[i])
        ligne.append(point)

        xs = xp[i][-1]
        ys = yp[i][-1]
        zs = zp[i][-1]

        if ps[i] is not None:               #permet de retirer la sphere représentant la planete de l'instant d'avant
            ps[i].remove()

        ps2 = ax.plot([xs], [ys], [zs], 'o', markersize=5, color=couleurs[i])
        ps[i] = ps2[0]
    ax.plot([0], [0], [0], 'o', markersize=10, color="yellow")
    return ligne + list(ps.values())

def main():
    # Données
    G=6.67408E-11
    Ms=1.9884E30
    h=86400
    t = 0
    planete={
      'Terre':{
         'Masse':5.972E24,
         'Périhélie':1.47E11,
         'excentricité':1.67E-2,
         'demi_grand_axe':1.496E11,
         'Periode':365*24*3600
      },
      'Venus':{
         'Masse':4.8675E024,
         'Périhélie':10.748E10,
         'excentricité':6.8E-3,
         'demi_grand_axe':108209500E3,
         'Periode':225*24*3600
      },
      'Mercure':{
         'Masse': 3.3011E23,
         'Périhélie':4.60E10,
         'excentricité':0.2056,
         'demi_grand_axe':57909050E3,
         'Periode':88*24*3600
      },
      'Mars':{
         'Masse':6.39E23,
         'Périhélie':206.7E9,
         'excentricité':9.34E-2,
         'demi_grand_axe': 227.9E9,
         'Periode':687*24*3600
      },
      'Jupiter':{
         'Masse':1.898e27,
         'Périhélie':740.7e9,
         'excentricité':4.84E-2,
         'demi_grand_axe': 778E9,
         'Periode':11.86 * 365 * 24 * 3600
      },
      'Saturne':{
         'Masse': 5.683e26,
         'Périhélie':1.35e12,
         'excentricité':5.56*10**-2,
         'demi_grand_axe': 1.43e12,
         'Periode': 29.46 * 365 * 24 * 3600
      },
      'Ur_anus':{
         'Masse': 8.681e25,
         'Périhélie':2.74e12,
         'excentricité':4.61e-2,
         'demi_grand_axe': 2.87e12,
         'Periode': 84.02 * 365 * 24 * 3600
      },
      'Neptune':{
         'Masse':  1.024e26,
         'Périhélie':4.45e12 ,
         'excentricité': 8.6E-3,
         'demi_grand_axe': 4.5e12,
         'Periode': 164.8 * 365 * 24 * 3600

      }
    }
    vy=0 #on va calculer les vitesses aux différentes périhélie
    N=0  #on va calculer les nombres d'intervalles à temps égaux
    conditions_initiales = {
        'Mercure': [46e9, 0, 0, 0, vy, 0,N],
        "Venus": [107e9, 0, 0, 0, vy, 0,N],
        "Terre": [147e9, 0, 0, 0, vy, 0,N],
        "Mars": [206.7e9, 0, 0, 0, vy, 0,N],
    }
    couleurs = {
        "Mercure": 'orange',
        "Venus": 'yellow',
        "Terre": 'blue',
        "Mars": 'red',
    }
    vip = {
        "Mercure": vy,
        "Venus": vy,
        "Terre": vy,
        "Mars": vy,
        
    }
    xp = {}
    yp = {}
    zp = {}
    ps = {}

    for i in conditions_initiales:
        conditions_initiales[i][6]=nbI(planete[i]['Periode'],h)
        vip[i]=vitesse_periphélie(G,Ms,planete[i]['demi_grand_axe'],planete[i]['excentricité']) #on met dans un dictionnaire els vitesses aux perihelies
        conditions_initiales[i][4]=vip[i]

        # Traçage Energie euler_asym
        x,y,z,vx,vy,vz=graphique_euler_asym(planete[i]['Périhélie'],0,0,vip[i],conditions_initiales[i][6],h,G,Ms)
        Em,T=erenyeager(x,y,vx,vy,Ms,planete[i]['Masse'],G,h,   conditions_initiales[i][6]  )
        plt.subplot(1,2,1)
        plt.plot(T,Em,color=couleurs[i])
        plt.title("Energie euler asym")
        plt.grid()
        # Traçage Energie euler
        x,y,z,vx,vy,vz=graphique_euler(planete[i]['Périhélie'],0,0,vip[i],conditions_initiales[i][6],h,G,Ms)
        Em,T=erenyeager(x,y,vx,vy,Ms,planete[i]['Masse'],G,h,   conditions_initiales[i][6]  )
        plt.subplot(1,2,2)
        plt.plot(T,Em,color=couleurs[i])
        plt.title("energie euler")
        plt.grid()
    
    for i in conditions_initiales:

        xp[i] = []
        yp[i] = []
        zp[i] = []
        ps[i] = None
    print(conditions_initiales)

    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.axis('off')
    def init():
        ax.set_xlim3d(-2e11, 2e11)
        ax.set_ylim3d(-2e11, 2e11)
        ax.set_zlim3d(-2e11, 2e11)
        ax.set_xlabel('X (mètres)')
        ax.set_ylabel('Y (mètres)')
        ax.set_zlabel('Z (mètres)')
        ax.set_title("Orbites des planètes intérieures du système solaire")
        return []
    
    anim=animation.FuncAnimation(fig, update, frames=10000, fargs=( planete, t, conditions_initiales, xp, yp, zp, ps, h, G, Ms, ax, couleurs,vip),init_func=init)
    
    plt.show()
main()