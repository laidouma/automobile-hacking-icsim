# README

## Description

Ce script Python permet de capturer des données CAN à partir d'une interface virtuelle, de diviser les données en deux fichiers, et de tester ces fichiers pour déterminer lequel déverrouille une porte. L'utilisateur est interrogé après chaque test pour savoir si la porte s'est ouverte, et le processus continue jusqu'à ce qu'il ne reste qu'une seule ligne dans le fichier.

## Fonctionnalités

- Capture des données CAN et enregistrement dans un fichier `candump.log`.
- Division du fichier `candump.log` en deux parties égales.
- Test des fichiers résultants en utilisant `canplayer`.
- Interaction avec l'utilisateur pour savoir si la porte s'est ouverte.
- Sauvegarde du fichier final contenant la ligne qui a permis de déverrouiller la porte.

## Prérequis

- **Python 3.x** : Assurez-vous que Python est installé sur votre machine.
- **canplayer** : Cet outil doit être installé pour exécuter les tests.
- **Git** : Si vous ne l'avez pas encore installé, suivez les instructions ci-dessous pour l'installer.

## Installation

### Étape 1 : Installer Git

Si Git n'est pas déjà installé, vous pouvez le télécharger et l'installer en suivant ces étapes :

- **Pour Windows** :
  1. Téléchargez l'installateur de Git depuis [git-scm.com](https://git-scm.com/download/win).
  2. Exécutez l'installateur et suivez les instructions à l'écran.

- **Pour macOS** :
  1. Vous pouvez installer Git via Homebrew en exécutant :
     ```bash
     brew install git
     ```
  2. Alternativement, vous pouvez télécharger l'installateur à partir de [git-scm.com](https://git-scm.com/download/mac).

- **Pour Linux** :
  ```bash
  sudo apt-get install git  # Pour les distributions basées sur Debian/Ubuntu
  sudo yum install git      # Pour les distributions basées sur Red Hat/Fedora
  ```

### Étape 2 : Cloner le Dépôt

Une fois que Git est installé, vous pouvez cloner le dépôt contenant le script :

```bash
git clone https://github.com/zombieCraig/ICSim.git
cd ICSim
```


## Utilisation

1. **Lancer le script :**
   Exécutez le script dans le terminal :
   ```bash
   python script.py
   ```

2. **Suivre les instructions :**
   - Le script capture d'abord les données CAN et les enregistre dans `candump.log`.
   - Ensuite, il divise le fichier en deux parties et teste chaque partie pour savoir si la porte s'ouvre.
   - **Veuillez vous assurer que toutes les portes sont bien fermées avant de répondre aux questions concernant l'ouverture de la porte.**
   - Répondez aux questions posées pour indiquer si la porte s'est ouverte.

## Détails du Code

### Fonctionnalités Principales

- `count_lines(filename)`: Compte le nombre de lignes dans un fichier spécifié.
- `split_file(filename, part1, part2)`: Divise un fichier en deux fichiers, en écrivant la première moitié dans `part1` et la deuxième moitié dans `part2`.
- `canplayer_test(filename)`: Exécute le test avec `canplayer` sur le fichier spécifié.
- `ask_user_if_door_opened()`: Demande à l'utilisateur si la porte s'est ouverte, jusqu'à obtenir une réponse valide.
- `capture_can_data()`: Capture les données CAN et renomme le fichier en `candump.log`.

### Structure du Script

Le script est structuré avec une fonction principale `main()` qui orchestre l'ensemble du processus, depuis la capture des données jusqu'au test et à la sauvegarde du fichier final.

## Avertissements

- Assurez-vous de disposer des permissions nécessaires pour exécuter `canplayer` et écrire dans le répertoire de travail.
- Ce script est conçu pour être utilisé avec une interface CAN virtuelle (par exemple, `vcan0`). Assurez-vous que cette interface est configurée avant de l'exécuter.
