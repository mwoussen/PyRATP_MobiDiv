# PyRATP (MobiDiv)
Fork de PyRATP : https://github.com/openalea-incubator/PyRATP

RATP: Radiation Absorption, Transpiration and Photosynthesis

## Dépendances
- make
- gcc 64 bits 
- numpy
- pandas
- scipy
- openalea.plantgl
- openalea.mtg

## Modifications 
- Installation avec make : compilation de la partie fortran avec f2py puis installation avec setuptools et pip 
- Calcul du rayonnement transmis dans chaque voxel
- Rayonnement intercepté et transmis dans les résultats
- Distribution des angles foliaires par voxel
- Paramètre heure locale ou solaire dans le calcul de la position du soleil
- Utilisation externe de la routine calcul du soleil

## Exemple d'installation avec conda
1) installer gcc en 64 bits (MinGW sous Windows)
2) installer miniconda 64 bits : https://docs.conda.io/en/latest/miniconda.html
3) Création d'un environnement conda :
```shell
conda create -n myenvname openalea.mtg openalea.plantgl numpy=1.20.3 scipy pandas -c conda-forge -c fredboudon
```
4) On se place dans l'environnement : `conda activate myenvname`
5) Télécharge le dépôt :
   1) `git clone git@github.com:mwoussen/PyRATP_MobiDiv.git` ou `git clone https://github.com/mwoussen/PyRATP_MobiDiv.git`
   2) `cd PyRATP_MobiDiv`
6) Installation du package : `make`
    si on veut pouvoir éditer les fichiers sources dans le dossier courant : `make mode=develop`
7) Nettoyage de l'étape de compilation : `make clean`
8) Test du package : `python tests/smalltests.py`

## TroubleShootings
### Installation sous Windows
- PyRATP_Mobidiv fonctionne uniquement en 64 bits
- A priori, l'installation ne fonctionne pas pour numpy >= 1.23
- Erreur compilation : `undefined reference to __intrinsic_setjmpex l.3335 pyratpmodule.c` 
    1) remplacer `#include<setjmp.h>` en `#include<setjmpex.h>` dans le fichier `pyratpmodule.c` (dossier building)
    2) relancer la compilation `f2py -c ...` l.58 du Makefile
