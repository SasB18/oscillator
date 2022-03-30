# Szükséges könyvtárak meghívása
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class oscillator:
    """
    Létrehozunk egy 'oscillator' nevű osztályt. Ennek az objektumnak a segítségével fogjuk megoldani a mogzást.
    
    Függvényei:
    Range: megadja a vizsgált mozgás tartományát
    in_val: megadja a kezdeti értékeket
    model: megadja az általános modelt, amit az 'odeint' meg fog oldani
    ode_solver: megoldja a mozgás differenciálegyenletét
    position: visszaadja a kitérés értékeit
    velocity: visszaadja a sebesség értékeit
    plot: kirajzolja a mozgás grafikonját
    """
    def __init__(self):
        # ha a 'Range' nincs megadva, akkor ez legyen az alapértelmezett tartomány
        self.t = np.linspace(0, 150, 200)

    def Range(self, a):
        """
        Megadja a mozgás tartományát.

        paraméterek:
        a: felső határ, megadja, hogy meddig vizsgáljuk a mozgást
        """
        # a mozgás tartományát a 3/2-edszeresére osztja be (ez elég pontos, de nem túl sok)
        x = 3/2 * a
        self.t = np.linspace(0, a, int(x))
        return self.t

    def in_val(self, x0, v0, omega_null, beta, a0, omega):
        """
        Kezdeti értékeket adja meg.

        paraméterek:
        x0: kezdeti kitérés
        v0: kezdeti sebesség
        omega_null: rezgés körfrekvenciája
        beta: csillapodási tényező
        a0: gerjesztő erő gyorsulása
        omega: gerjesztő erő körfrekvenciája
        """
        # a kezdeti értékeket egy listába helyezi, ezt fogja később felhasználni
        self.in_val_ = [x0, v0, omega_null, beta, a0, omega]
        return self.in_val_

    def model(self, O, t, in_val_):
        """Megadja a mozgás modelljét, amit az 'odeint' függvény fog megoldani"""
        # az 'x' értékek, a 'v' értékek pedig a második elemei lesznek 'O'-nak
        x = O[0]
        v = O[1]
        # megadjuk a differenciálegyenlet(ek)et
        dxdt = v
        dvdt = -in_val_[2]**2*x -2*in_val_[3]*v + in_val_[4]*np.sin(in_val_[5]*t)
        # visszaadja a deriváltak értékét
        return [dxdt, dvdt]

    def ode_solver(self):
        """Megoldja a differenciálegyenlet-rendszert"""
        C = [self.in_val_[0], self.in_val_[1]]
        # az odeint függvénnyel megoldjuk a modelt a kezdeti értékek ismeretében
        solution = odeint(self.model, C, self.t, args=(self.in_val_,))
        # külön listába rakjuk az 'x' és a 'v' értékeket
        self.x = solution[:,0]
        self.v = solution[:,1]
        # visszaadja az 'x' és 'v' értékeket
        return [self.x, self.v]

    def position(self):
        """Visszaadja a kitérés értékeit"""
        return self.x

    def velocity(self):
        """Visszaadja a sebesség értékeit"""
        return self.v

    def plot(self, position=True, velocity=True):
        """Kirajzolja a mozgás grafikonját

        paraméterek:
        position: ha hamisra van állítva, akkor csak a sebességet rajzolja ki
        velocity: ha hamisra van állítva, akkor csak a kitérést rajzolja ki
        legalább az egyiknek igaznak kell lennie."""
        # létrehozunk egy grafikont
        fig, ax = plt.subplots()
        # címkék beállítása
        ax.set_xlabel("idő(s)")
        ax.set_title("A mozgás kitérése és sebessége idő függvényében")
        # a 'position' illetve a 'velocity' változókkal tudjuk befolyásolni, hogy melyiket rajzolja ki
        if position == True: 
            ax.plot(self.t, self.x, 'b-', label="Kitérés")
        if velocity == True:
            ax.plot(self.t, self.v, 'g-', label="Sebesség")
        if position == False and velocity == False:
            print("Legalább az egyik függvényt ki kell iratni!")
            return
        ax.legend()
        ax.grid(True)
        plt.show()

# Példa
osc = oscillator() # megadunk egy oszcillátort
osc.Range(200) # beállítjuk a tartományt
osc.in_val(2, 1, 0.3, 0.05, 0.02, 0.2) # megadjuk a kezdeti értékeket
osc.ode_solver() # megoldjuk a mozgást
osc.plot() # kirajzoltatjuk


