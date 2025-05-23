Roll Racers
###########

:date: 2025-05-23 9:00:00
:category: Demo
:tags: Demo, Game Jam, Coffee N' Jam
:summary: We once again made a game in a week for the Coffee N' Jam with Cubos, and this time, with a lot of physics!
:cover: {static}/images/blog/demo/coffee-n-jam-2025/cover.png

The Theme
=========

From 2nd of May to the 10th of May, :author:`fallenatlas`, :author:`tomas7770`, :author:`fkatar`, :author:`PedroSimoes24`, :author:`RiscadoA`, :author:`joaomanita` and :author:`mcanais` participated in the Coffee N' Jam, a game jam organized by GameDev Técnico, with our engine, **Cubos**.
The goal was to create a game in a week, this time with theme "Blackout" - the huge power outage in the Iberian Peninsula had happened the prior week, and just like during the Covid lockdown, people rushed to the supermarkets to buy toilet paper.

We thought it would be funny to make a game about racing to the supermarket to buy toilet paper - and that's what we ended up doing.
Our priorities were to test new features of the engine, and to make a fun local multiplayer game.
This idea was a great opportunity to fully use the physics and collision plugins in a game for the first time.

The game is called *Roll Racers*, and you can play it on its `itch.io page <https://riscadoa.itch.io/roll-racers>`_.
It has a web build and a downloadable version for both Windows and Linux.
You can also check out its source code in our `demo repository <https://github.com/GameDevTecnico/cubos-demo>`_.

.. figure:: {static}/images/blog/demo/coffee-n-jam-2025/cover.png

    The game supports up to 4 players, each having a different car model.

.. figure:: {static}/images/blog/demo/coffee-n-jam-2025/image1.png

    A player holding toilet paper, racing back to the start line to score points.

We had a lot of fun making the game, and we fixed a ton of bugs and missing features in the engine as we went along.
Since the jam was a week long, we had some more time to work on the game than in the `previous jam <{filename}./azul-jam-2025.rst>`_.

Voxel Modeling
==============

One major problem we had was that we didn't have any artists in the team, only programmers.
We ended up going full programmer art mode, and we used, as usual, `MagicaVoxel <https://ephtracy.github.io/>`_ for this purpose.
:author:`PedroSimoes24` focused on making the buildings and the road models, :author:`RiscadoA` focused on the cars and some tiles and :author:`mcanais` made a few props.

Map Generation
==============

To make our jobs easier, the map is divided into tiles. Each tile is 68x68 voxels wide. Tiles can be road tiles, building tiles or park tiles.
:author:`RiscadoA` and :author:`mcanais` worked on the map generation, which is done procedurally. First, road tiles are placed in a river-like fashion, and then, building tiles are placed around them.

To make the map prettier we also added some park tiles with trees and bushes, which are randomly placed adjacent to the road tiles.
For an extra challenge, we added a 'river' tile where the road has a big hole in the middle, and the players have to jump over it by going fast enough on the ramps.

We also have special start and end tiles, the end tile being the supermarket, where the toilet paper is placed.
The map regenerates every time a round ends, i.e., when a player brings the toilet paper back to the start line.

.. figure:: {static}/images/blog/demo/coffee-n-jam-2025/supermarket.png
    :alt: Supermarket

    Supermarket tile, where the toilet paper can be picked up.

Physics and Collisions
======================

For this game, we decided to go all in on physics. :author:`fallenatlas` and :author:`RiscadoA` developed physically realistic cars.
The cars are essentially composed of a box shape, representing the chasis, and then four empty child entities representing each of the wheels, with origin on the point where the suspension connects to the car. When turning, these wheel entities are rotated on the y-axis.
Then, the forces for each individual wheel are calculated and applied on the connection point with the chasis, for realistic behaviour. These forces include:

- The suspension force, which lifts the car up and makes it react realistically to the ground bellow.
- The steering force, which simulates the cars steering with tire friction and splip angle.
- The acceleration force, which applies acceleration and breaking to the cars. The acceleration forces are applied to different wheels, depending if the car is front wheel drive or rear wheel drive, affecting it's handling.

.. figure:: {static}/images/blog/demo/coffee-n-jam-2025/going-over-sidewalk.png

    Since each wheel is simulated independently, the cars tilts when going over the sidewalk.

However, if the cars are not on the ground, we do not want to calculate any forces besides gravity. Therefore, we perform a raycast from the wheel origin to the ground.
In case it hits bellow the max distance, we calculate the forces, and particularly, we use it's hitpoint for determining the strength of the suspension force.

As mentioned previously, the map is divided into tiles. As it's much fast and accurate than trying to put collision shapes manually,
we decided to use voxel collision shapes for every tile. This worked surprisingly well, and the framerate didn't drop as much as we where expecting given how many voxel shapes we had,
and the little optimization we currently have for collisions. It's worth noting that we were taking advantage of the collision layers and masks to determine which shapes should detect collision between themselves, which lead to better performance in this scenario.

But this is where things went a little wrong... As we tried to put the car on the map, we noticed that the car would just completly fall through the tile.
After finding the root issue, :author:`fallenatlas` started working quickly on fixing it. The issue had two parts. The first was related to the component matching on the penetration constraint solving, where we were missing some checks for certain components, leading to the solving being done in the opposite way, effectively pulling bodies to each other, instead of pushing them apart.
The second issue was related to the local contact points calculation for voxel shapes, in the narrow phase, where the points were always relative to the center of the entity rather than relative to their relative box center (since the voxel shape is composed of multiple boxes). This lead to the penetration distance being miscalculated in the penetration constraint solving, and therefore, the impulses applied to each entity were incorrect.

Since, we were at it, we wanted to use as much physics features as we wanted, so :author:`joaomanita` experimented with using the new Distance Constraint to attach the paper roll to the car, and having it be dragged along.
However, the team felt like it was too hard to steal the toilet paper, since it moved around too much, and discarted this idea.

On the last day, a comical situation happened when we where putting ramps on the map. We (:author:`RiscadoA`) tried to rotate one of the ramps, by rotating it, and then putting it as a child entity of another entity with the same rotation applied to it. This lead to a huge framerate drop, which took as a couple of hours to figure out. 
The exact reason for why this happened is still unknown, but we'll be investigating it in the future.

.. figure:: {static}/images/blog/demo/coffee-n-jam-2025/image2.png

    A player can steal another player's toilet paper by hitting them with their car.

UI
===

This game was also the first time UI was used on a demo. :author:`tomas7770` picked up this task, and made multiple menus and screens for the game.
We wanted to briefly explain the game mechanics to the players, so we added a title screen with some information.

.. figure:: {static}/images/blog/demo/coffee-n-jam-2025/title-screen.png
    :alt: Title screen

    The "Press Space/A ..." text color is animated, fading in and out.

Additionally, the players can choose how many players will play the game by pressing the spacebar or the "A" on the gamepad for each of them.
Instructions were added to the top of the screen.

.. figure:: {static}/images/blog/demo/coffee-n-jam-2025/start.png
    :alt: Start screen

    After advancing, the players must choose the number of players.

In game, it was important to show the players their score and how it changed over time, to make the game more competitive.
We decided to add a score indicator to the top of the screen, which shows the score of each player.

.. figure:: {static}/images/blog/demo/coffee-n-jam-2025/mid-game.png
    :alt: Score indicators

    Points are gained by holding the toilet paper.

Finally, at the end of the game, we wanted to reward the players with a scoreboard, showing the score of each player.

.. figure:: {static}/images/blog/demo/coffee-n-jam-2025/scoreboard.png
    :alt: Scoreboard

    The text color helps associate the players with their scores.

The UI ended up working well during the jam. There were only three issues:

- Our UI and ImGui were not compatible - this was easily fixed by ensuring they were drawn in the correct order. 
- There is no support for text wrapping or newlines, so we had to create a different text element for each line.
- The text contents only updated when its respective component was reinserted - simply modifying it wasn't enough. We're still unsure on how to handle these scenarios, but the most likely solution is to make the component unmodifiable and thus force the user to reinsert it.

Audio
=====

On the last day of the jam :author:`RiscadoA` decided to focus on adding audio to the game.
Previously, when making `Ondisseia <{filename}./azul-jam-2025.rst>`_, we had a lot of trouble with adding sound effects.
They didn't play reliably and the audio system was a bit of a mess.

To use audio in *Roll Racers*, we ended up fixing all of the problems we previously had, which means that we can now rely on it for future projects.
We added a few sound effects to the game, such as:

- Car engine sound, which changes pitch and gain based on RPM and gear.
- Pickup sound when picking up toilet paper.
- Steal sound when stealing toilet paper from other players.
- Fireworks sound when winning the game.
- Power cut sound when the race starts.
- Honking sound when honking the horn.

While the audio still sounded a bit janky, it was very satisfying to hear sound being used so extensively in a Cubos game for the first time.

ECS Troubles
============

At the end of the jam, the game's performance was very bad.
A bit of profiling quickly showed that a lot of time was being spent iterating over tens of thousands of relation tables - the ones introduced in the `relations development note <{filename}/blog/dev-notes/hello-relations.rst>`_.
This was a waste of time, as only less than 15 actually contained entities.

:author:`RiscadoA` quickly fixed this by adding logic to clean up unused relation tables every frame.
This immediately improved performance by a lot - on one machine, the framerate went from 40FPS to stable 240FPS.
In the future, this logic should probably be improved to only clean up the tables when they're not used for a while, to avoid wasting time recreating tables constantly.

Whats Next?
===========

We are very happy with the results of this jam - this demo is and will continue to be a great testbed for the engine, as it really pushes it to its limits.
After the jam ended, we met to discuss what went wrong and what issues we should prioritize fixing.
One of the biggest problems continues to be the lack of proper tooling for the engine - this will be the focus for the next few months.
