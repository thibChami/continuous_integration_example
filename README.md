
You can install pytest using pip (`pip install -U pytest`) or in a conda environment (`conda install pytest`).

## Installation

Forkez ce repo sur votre compte.
Allez sur https://travis-ci.com/ et connectez-vous avec votre compte Github.
Activate Github Application.
Ne paniquez pas vous allez être redirigé sur Github -> Approve & Install.

![Imgur](https://i.imgur.com/MP15GTW.png)

Allez sur "Manage repositories" puis "Select repositories".

![Imgur](https://i.imgur.com/bA9OuLA.png)

Vous pouvez ensuite Commit et Push de façon à ce que Travis declenche le build.
(placez-vous dans le dossier)
```
git add .
git commit -m "message"
git push
```

Comme vous pouvez le voir... c'est cassé.


## Exercices
### 1. sum.py / Réparer le code pour que les tests réussissent.
### 2. sum_test.py / Améliorez la couverture du code en écrivant un test qui vérifie le type de valeur retournée. Observez votre taux de couverture augmenter.
### Bonus. Augmentez encore le coverage.
