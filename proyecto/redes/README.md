# Tercer parcial de procesos estocásticos

### ¿Cómo clono el repositorio? ###

Acontinuación como clonar el repositorio para hacer contribuciones.

Descargar el repositorio

```
#!shell
git init
git remote add upstream https://gitlab.com/adriangg/tercer-parcial-estocasticos.git
git checkout -b develop
git pull upstream develop
```

Correr el proyecto

```
#!shell
make run
```

### ¿Cómo contribuir?###

A continuación se describe el flujo de trabajo para enviar contribuciones al repositorio

Antes que nada hay que tener en cuenta que debemos haber hecho commit de todos nuestros cambios en nuestra rama local. Luego de esto irémos a la rama develop a actualizar los cambios que otros contribuyentes han realizado.
```
#!shell
git checkout develop
```
Ahora actualizamos la rama (bajamos los cambios)
```
#!shell
git pull upstream develop
```
A continuación nos pasamos a nuestra rama
```
#!shell
git checkout mi_rama
```
Y nos basamos en develop
```
#!shell
git rebase develop
```
Luego lanzamos nuestro push a nuestra rama en upstream
```
#!shell
git  push upstream mi_rama
```

Y por último hacemos pull request de la rama mi_rama a develop, los cambios se verán reflejados cuando el integrador acepte el pull request y haga el merge correspondiente, luego cada uno debe actualizar su rama de develop y hace rebase sobre su rama para poder seguir trabajando.
