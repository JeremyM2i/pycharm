from casino import Casino
from jeu import Jeu
from roulette import Roulette
from joueur import Joueur
from machineasous import MachineASous


def main():
    casino = Casino(100000)
    jeu1 = Roulette("my wheel", casino)
    jeu2 = MachineASous("bandit manchot", casino)
    joueur = Joueur("Clement", 1000)
    joueur.entrer_casino(casino)
    joueur.jouer()

main()
