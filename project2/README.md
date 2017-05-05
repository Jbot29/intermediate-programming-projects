# Project 2 - Simple text adventure game.

Lets make a simple text based game. The goal of the game is to escape from a 3 room castle.

The user has the following commands

look <direction> - look in a direction north|south|east|west

go <direction> - go into a direction. If that direction is another room, move into that room

take <object> - if an object is found, the user can take that object.

help - list commands to user


The room layout looks like

```
 ___    ___
|   |  | K |
|    -     |
|_ _|  |___|
 _|_
|   |
| S |
|_ _|
  |
Outside
```

The user starts in at S. There is a door to the south, but it is locked. They can not leave until
they navigate to the third room and take the key, navigate back, and only then they can exit through the door.

```
Example run:

Current room: You find yourself in a large candle lit room
Command:look south
You see a large locked door
Command:go south
You need a key for that door
Command:look north
Another dark room
Command:go north
Current room: Another dark room
Command:look east
Another smaller dark room
Command:go east
Current room: Another smaller dark room
Command:look north
You see a shiny key lying on the floor
Command:take key
Command:go west
Current room: Another dark room
Command:go south
Current room: You find yourself in a large candle lit room
Command:go south
You did it!

```

Before begining, think about how you would design if you knew that you would need to add more rooms and possibly more objects and exit conditions.


How would you debug the levels? Tests cases can be great, but sometimes with a complex running
thing you need to be able to debug live, can you build in debugging ahead of time?



#Part Two

Product came back and decided a cat burlgar game is all the rage, so they want to change the game.
Now you have to steal a painting and get out of the castle.

Add another room, to the west of the second room. Add a painting to one of the walls in that room.

Only allow the user to leave if they have taken both the painting and the key.
