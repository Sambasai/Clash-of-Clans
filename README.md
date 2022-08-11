# Clash of Clans

A terminal-based version of Clash Of Clans using Python and OOPs principles. Here's a glimpse of the gameplay:

<!-- <p align="center">
    <img src="gameplay.gif" width="512"/>
</p> -->


The game starts with the user selecting which hero he/she wants to use (King or Queen)

Controls:

Spawning at ``spawn point 1``:

<kbd>j</kbd> - Spawns a barbarian <br>
<kbd>b</kbd> - Spawns an archer <br>
<kbd>i</kbd> - Spawns a balloon <br>

Spawning at ``spawn point 2``:

<kbd>k</kbd> - Spawns a barbarian <br>
<kbd>n</kbd> - Spawns an archer <br>
<kbd>o</kbd> - Spawns a balloon <br>

Spawning at ``spawn point 3``:

<kbd>l</kbd> - Spawns a barbarian <br>
<kbd>m</kbd> - Spawns an archer <br>
<kbd>p</kbd> - Spawns a balloon <br>

Swawning hero:
<kbd>1</kbd> - Spawns King <br>
<kbd>2</kbd> - Spawns Queen <br>


Controlling the movement of Hero:

<kbd>w</kbd> - Move one cell up <br>
<kbd>a</kbd> - Move one cell left <br>
<kbd>s</kbd> - Move one cell down <br>
<kbd>d</kbd> - Move one cell right <br>

Attack using Queen/King:

<kbd>space</kbd>: Normal attack <br>
<kbd>x</kbd>: Leviathan axe of king/ Eagle Arrow of Queen

Spells:

<kbd>r</kbd> - Activate the ``rage spell``, which doubles the speed and damage done by the troops <br>
<kbd>h</kbd> - Activate the ``heal spell``, which can heal a troop upto 1.5 times its current health. <br>





## OOPs concepts used:

### Inheritance: 
Generic classes for game objects and all the objects inheriting these classes. Basic character and building classes are inherited by all other classes specific to different types of game objects.

### Polymorphism: 
Multiple functions with the same name but a varying number of arguments used.

### Encapsulation: 
Class and object-based approach for all the functionality implemented.

### Abstraction: 
Intuitive functionality like move(), attack(), etc, showing away inner details from the end user.

## Setup

1. colorama is required for the app to run. To install colorama,

```bash
pip3 install colorama
pip3 install art
```

2. To run the game,

```bash
python3 game.py
```




