import os
import time
import subprocess

def count_lines(filename):
    """Compte le nombre de lignes dans un fichier."""
    with open(filename, 'r') as file:
        return sum(1 for line in file)

def split_file(filename, part1, part2):
    """Divise un fichier en deux parties égales."""
    line_count = count_lines(filename)
    mid_point = line_count // 2

    with open(filename, 'r') as file:
        lines = file.readlines()

    # Ecrire la première moitié dans part1
    with open(part1, 'w') as file1:
        file1.writelines(lines[:mid_point])

    # Ecrire la deuxième moitié dans part2
    with open(part2, 'w') as file2:
        file2.writelines(lines[mid_point:])

def canplayer_test(filename):
    """Exécute canplayer pour tester un fichier."""
    print(f"Test du fichier : {filename}")
    os.system(f"canplayer -I {filename}")

def ask_user_if_door_opened():
    """Demande à l'utilisateur si la porte s'est ouverte."""
    while True:
        result = input("La porte s'est-elle ouverte ? (y/n) : ").strip().lower()
        if result in ['y', 'n']:
            return result == 'y'
        print("Veuillez répondre par 'y' (oui) ou 'n' (non).")

def capture_can_data():
    """Capture les données CAN et les enregistre dans candump.log."""
    
    #Changer de répertoire si nécessaire
    #os.chdir("ICSim/builddir")
    
    # Capture des données CAN via candump et les enregistrer dans candump.log
    #print("Capture des données CAN avec candump...")
    #os.system("candump -c -l vcan0")

    # Spécifie le répertoire contenant les fichiers
    directory = '.'  # Change ceci si nécessaire

    # Variable pour stocker si un fichier a déjà été renommé
    renamed = False

    # Parcours tous les fichiers dans le répertoire
    for filename in os.listdir(directory):
        # Vérifie si le fichier commence par "candump-2024"
        if filename.startswith('candump-2024') and not renamed:
            # Nouveau nom de fichier
            new_filename = 'candump.log'
            
            # Renomme le fichier
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f'Renamed: {filename} to {new_filename}')
            
            # Indique qu'un fichier a été renommé
            renamed = True

    if not renamed:
        print("Aucun fichier à renommer.")

    


def main():
    # Étape 1 : Capture des données CAN
    capture_can_data()

    file_to_test = "candump.log"

    while True:
        # Compter le nombre de lignes restantes
        line_count = count_lines(file_to_test)
        print(f"Nombre de lignes dans {file_to_test} : {line_count}")

        # Si une seule ligne reste, sortir de la boucle
        if line_count == 1:
            print("Il ne reste qu'une seule ligne dans le fichier :")
            with open(file_to_test, 'r') as file:
                print(file.read())
            print("Fichier final enregistré dans 'candump_output.log'.")
            os.system(f"cp {file_to_test} candump_output.log")
            break

        # Diviser le fichier en deux
        part1 = "candump_part_1.log"
        part2 = "candump_part_2.log"
        split_file(file_to_test, part1, part2)

        # Tester la première partie
        canplayer_test(part1)
        time.sleep(5)  # Attendre quelques secondes pour l'utilisateur
        if ask_user_if_door_opened():
            print(f"Le premier fichier {part1} a fonctionné.")
            os.system(f"cp {part1} {file_to_test}")
            continue

        # Tester la deuxième partie
        canplayer_test(part2)
        time.sleep(5)  # Attendre quelques secondes pour l'utilisateur
        if ask_user_if_door_opened():
            print(f"Le deuxième fichier {part2} a fonctionné.")
            os.system(f"cp {part2} {file_to_test}")
        else:
            print("Aucun des fichiers n'a permis de déverrouiller la porte.")
            exit(1)

if __name__ == "__main__":
    main()
