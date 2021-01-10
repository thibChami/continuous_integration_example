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
 * Add a .travis.yml file to your repository to tell Travis CI what to do.
   * Travis can test your code using different versions of Python.
     See this example of [.travis.yml](https://github.com/OceanParcels/continuous_integration_example/blob/master/travis.yml.simple)
   * Testing Python under OSX is currently broken. You can't do it as for the linux example above, but you can still
     test an OSX Python by installing it with conda. To use any conda environment, you can also use such approach, with this
     [.travis.yml](https://github.com/OceanParcels/continuous_integration_example/blob/master/.travis.yml)
 * Now, each time you'll push a commit on github, your full code will be tested.
 * You can setup Travis in your settings to only test master branch, every branch, the pull requests, etc.

### The AppVeyor CI tool
To test your code on Windows, you can use [AppVeyor](https://www.appveyor.com), which is similar to Travis.
