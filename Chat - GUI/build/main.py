from MainMenuGui import MainMenuGui
from configparser import *

if __name__ == "__main__":
    print(r"""

   ___  _                          __   
  / _ \(_)__ _______  __ _________/ /__ 
 / // / (_-</ __/ _ \/ // / __/ _  / -_)
/____/_/___/\__/\___/\_,_/_/  \_,_/\__/ 
                                        

                                                
    """)
    print("Initializing...")

    #on créer le fichier de configuration. Il aura une section "Utilisateur", avec 4 paramètres de couleur ainsi que le pseudo.
    config = ConfigParser()
    print("Checking config file...")
    config.read("config.ini")
    if not config.has_section("Utilisateur"):
        config.add_section("Utilisateur")
        config.set("Utilisateur", "pseudo", "")
        config.set("Utilisateur", "couleur", "#000000")
        config.set("Utilisateur", "couleur2", "#000000")
        config.set("Utilisateur", "couleur3", "#000000")
        config.set("Utilisateur", "couleur4", "#000000")
        with open("config.ini", "w") as configfile:
            config.write(configfile)
    if not config.has_section("Serveur"):
        config.add_section("Serveur")
        config.set("Serveur", "ip", "")
        config.set("Serveur", "port", "")
        config.set("Serveur", "mode", "")
        with open("config.ini", "w") as configfile:
            config.write(configfile)
    print("Config file checked")
    print("Starting GUI...")
    MainMenuGui()
