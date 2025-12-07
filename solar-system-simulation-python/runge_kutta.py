import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
#fonction runge kutta f(t,p(t))
def f(t, p,G,M):
    x, y,z, vx, vy,vz = p         #composantes du vecteur p
    r = np.sqrt(x**2 + y**2) #norme du rayon
    ax = -G * M * x / r**3   #accelération selon X
    ay = -G * M * y / r**3   #accélération selon Y
    az = -G * M * z / r**3
    return np.array([vx, vy, vz, ax, ay, az]) #retourne f(t,p(t)) qui correspond à la dérivée de p, np.array est utilisé pour transformer la liste des valurs de p en matrice (2,1) contenant la vitesse et la position



def update(frame, t, conditions_initiales, xp, yp, zp, ps, dt, G, M, ax, couleurs):

    for i in conditions_initiales:#Boucle de Runge Kutta d'ordre qui va rajouter les valeurs de x et de y pour chaque planetes

        p0 = np.array(conditions_initiales[i]) #correspond au vecteur p0 qui contient la matrice 2,1 contenant le vecteur position initial ainsi que le vecteur vitesse initial


        xp[i].append(p0[0]) #ajout de x dans les listes
        yp[i].append(p0[1]) #ajout de y dans les listes
        zp[i].append(p0[2]) #ajout de z dans les listes

        k1 = dt * f(t, p0, G, M)                    #calcul des coefficients k.
        k2 = dt * f(t + dt/2, p0 + k1/2, G, M)
        k3 = dt * f(t + dt/2, p0 + k2/2, G, M)
        k4 = dt * f(t + dt, p0 + k3, G, M)

        p0 = p0 + (k1 + 2*k2 + 2*k3 + k4)/6   #calcul du vecteur p+1 qui va servir à calculer la position suivante

        conditions_initiales[i] = p0.tolist()   #converti le vecteur po qui était en tableau Numpy (matrice 2,1) en liste

    t += dt #calcul du nouveau temps pour la prochaine position

    lines = []

    for i in conditions_initiales:
        line, = ax.plot(xp[i], yp[i], zp[i], color=couleurs[i])
        lines.append(line)

        xs = xp[i][-1]
        ys = yp[i][-1]
        zs = zp[i][-1]

        if ps[i] is not None:
            ps[i].remove()

        ps2 = ax.plot([xs], [ys], [zs], 'o', markersize=5, color=couleurs[i])
        ps[i] = ps2[0]

    return lines + list(ps.values())

def main():
    #données constantes
    conditions_initiales = {
        "Mercure": [46e9, 0, 0,0, 58980,0],#x0,y0,vx0,vy0
        "Vénus": [107e9, 0, 0, 0, 35260,0],
        "Terre": [147e9, 0, 0, 0, 30300,0],
        "Comète": [8.783e10, 0, 0, 0, 54460, 0],
    }
    #constantes
    Tm=365*24*3600
    G = 6.67430e-11 #constante gravitationnelle
    M = 1.989e30 #masse du soleil
    dt = 3600*24 #delta T
    t = 0  #temps initial

    couleurs = {
        "Mercure": 'orange',
        "Vénus": 'yellow',
        "Terre": 'blue',
        "Mars": 'red',
        "Comète": 'black'
    }
    #initialisation des dictionnaires contenant pour chaque planetes les valeurs des x et des y
    xp = {}
    yp = {}
    zp = {}
    ps = {}
    #création de listes qui contiendrons les valeurs de x et de y pour chaque planetes
    for i in conditions_initiales:
        xp[i] = []
        yp[i] = []
        zp[i] = []
        ps[i] = None
    #affichage des planètes ainsi que leurs orbites
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    def init():
        ax.set_xlim3d(-2e11, 2e11)
        ax.set_ylim3d(-2e11, 2e11)
        ax.set_zlim3d(-2e11, 2e11)
        ax.set_xlabel('X (mètres)')
        ax.set_ylabel('Y (mètres)')
        ax.set_zlabel('Z (mètres)')
        ax.set_title("Orbites des planètes intérieures du système solaire")
        return []

    ani = FuncAnimation(fig, update, frames=100, fargs=( t, conditions_initiales, xp, yp, zp, ps, dt, G, M, ax, couleurs),init_func=init)

    plt.show()

# Appel de la fonction main
main()