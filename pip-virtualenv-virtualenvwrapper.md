# Pip, VirtualEnv, and VirtualEnvWrapper

What?

Pip - is a package manager for Python, like npm is for Node.js.
VirtualEnv - an package environment manager, used for isolating the package environments of various Python projects from each other. npm does this for Node.js as well.
VirtualEnvWrapper - is a set of convinience wrapper scripts for working with VirtualEnv, because working with VirtualEnv itself is a bit cumbersome.

The use of VirtualEnv is recommended for production Python apps.

## Step 1

Install Python using Homebrew (we are doing this because this allows us to install anything with pip wo having root permission)

brew install python

## Step 2

Do a `brew list python` to see the files that were added. Add your new python to your path. Add this line (if the version of Python is different, you will need to change that in the line below):

export PATH=/usr/local/Cellar/python/2.7.12/bin:$PATH

To your ~/.bash_profile if you are using Bash and add it to your ~/.zshrc if you are using zsh.

## Step 3

Install virtualenv

pip install virtualenv

## Step 4

Install virtualenvwrapper

pip install virtualenvwrapper

## How to Use VirtualEnvWrapper

To create a new virtual environment with VirtualEnvWrapper to use with a project, you use the `mkvirtualenv` command:

mkvirtualenv MY_PROJECT

To switch to an existing virtual environment, use

workon MY_PROJECT

When you are "working on" the virtual environment associated with a project, certain environment variables are set up in your shell for you. You will also see the name of that environment in your shell prompt. If you want to deactivate these environment variables because you are no longer working on that project, do:

deactivate
