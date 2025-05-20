Roll Racers
###########

:date: 2025-05-20 9:00:00
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

Physics
=======

**TODO**: cover these topics

- Voxel collision shapes were used extensively.
- Physics solving bugs were fixed.
- Tried using distance constraint for the toilet paper but ended up dropping it.
- Wheels using raycasts.
- Ramp performance bug?

.. figure:: {static}/images/blog/demo/coffee-n-jam-2025/image2.png

    A player can steal another player's toilet paper by hitting them with their car.

.. figure:: {static}/images/blog/demo/coffee-n-jam-2025/going-over-sidewalk.png

    Since each wheel is simulated independently, the cars tilts when going over the sidewalk.

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

**TODO**: add a video here

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
