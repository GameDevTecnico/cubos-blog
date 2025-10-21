The First Cubos Jam
###################

:date: 2025-10-21 17:00:00
:category: Meta
:tags: Game Jam
:summary: The Cubos Team hosted the first Cubos Jam! This game jam was open to the general public and was focused on our engine.
:cover: {static}/images/blog/meta/cubos-jam-2025/cover.png

From September 12th to September 21st, 2025, the first game jam focused on the Cubos Engine took place, with the theme "Retro".
This was a major milestone for the Cubos team, which we had been planning for a long time.
The idea behind it was to see how people would use the engine to create games, and to gather feedback on the engine and its tools.

The engine is still, of course, very hard to use, due to the lack of a proper editor and a scripting language.
Participants had to code their games in C++, which is, as usual, not the most user friendly language.
Even so, we still were able to attract 13 participants, which is a great start for a first-time event.
Four of the five teams were able to submit a game by the end of the event, which you can check out on the `Cubos Jam page <https://itch.io/jam/cubos-jam/entries>`_.  

.. image-grid::
    {static}/images/blog/meta/cubos-jam-2025/retrospective-penguin.png Restrospective Penguin
    {static}/images/blog/meta/cubos-jam-2025/rider-or-block.png Rider or Block
    {static}/images/blog/meta/cubos-jam-2025/space-runner.png Space Runner
    {static}/images/blog/meta/cubos-jam-2025/sushi-chef-shuffle.png Sushi Chef Shuffle

The jam itself was remote, with an in-person opening and closing event. At the opening event, we held a quick workshop to help participants get started with the engine.
At the closing event, we had a small ceremony to showcase the games made during the jam.

The workshop guided the participants through the process of installing the engine and compiling a template project we provided.
This required setting up CMake and a C++ compiler (Visual Studio on Windows). Installing the engine and compiling the project itself wasn't a very smooth experience.
In the future we plan to improve this process by providing pre-compiled binaries and installers for the engine, as well as better setup documentation.

.. figure:: {static}/images/blog/meta/cubos-jam-2025/workshop.jpg
  
  Cubos Jam workshop, at Instituto Superior Técnico, Lisbon.

After the jam we gathered a lot of useful feedback from the participants. Overall, they saw the potential of the engine, but also highlighted many areas that need improvement. Namely:

- **Tooling**: the engine is still very hard to use for non-programmers, particularly artists, due to the lack of an editor and proper asset management tools.

- **Documentation**: although the features are extensively documented, there are few examples and guides, which makes it hard for new users to get started.

- **Scripting**: integrating a language such as Lua (which is happening right now) would greatly reduce the barrier to entry for new users.

- **Physics**: add capsule shape collisions, and expose a nicer interface for handling multiple types of bodies.

We plan to hold more jams in the future, after improving the engine and its tools. We hope the experience will become more accessible and enjoyable for future participants.

.. figure:: {static}/images/blog/meta/cubos-jam-2025/gathering.jpg
  
  Cubos Jam closing event, at the Gaming Hub, Lisbon.
