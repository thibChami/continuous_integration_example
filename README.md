# Continuous integration tutorial

This tutorial presents how to use continuous integration (CI) in a Python code development, using the [pytest](https://docs.pytest.org/en/latest/contents.html) and [Travis](https://travis-ci.com).
Through a few simple exercises, you'll go through different features of CI.

## pytest module of Python

[pytest](https://docs.pytest.org/en/latest/contents.html) is a framework that makes building simple and scalable tests easy.

You can install it using pip (`pip install -U pytest`) or in a conda environment (`conda install pytest`).
You can run pytest within a terminal (linux and osx) or in the anaconda prompt (Windows).

## Using github and Travis
Using Travis CI, you can automatically test every commit you push on github.

### How to get started with Travis (see more info in the [Travis tutorial](https://docs.travis-ci.com/user/tutorial/))?
 * You can find [Travic CI](https://github.com/marketplace/travis-ci) (and other Github Apps) on the [Github Marketplace]( https://github.com/marketplace).
 * Install and configure Travis, selecting the repository you want to test.

 * Now, each time you'll push a commit on github, your full code will be tested.
 * You can setup Travis in your settings to only test master branch, every branch, the pull requests, etc.

 ---------------------------------
## Installation

Forkez ce repo sur votre compte.
Allez sur https://travis-ci.com/ et connectez-vous avec votre compte Github.
Activate Github Application.
Ne paniquez pas vous allez être redirigé sur Github -> Approve & Install.
![Imgur](https://i.imgur.com/MP15GTW.png)
Allez sur "Manage repositories" puis "Select repositories".
![Imgur](https://i.imgur.com/bA9OuLA.png)
Vous pouvez ensuite Commit et Push de façon à ce que Travis declenche le build.
Comme vous pouvez le voir... c'est cassé.


## Exercices
### 1. sum.py Réparer le code pour que les tests réussissent.
### 2. sum_test.py Améliorez la couverture du code en écrivant un test qui vérifie le type de valeur retournée. Observez votre taux de couverture augmenter.
