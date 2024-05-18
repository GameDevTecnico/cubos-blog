Coffee'n Jam and... 0.2!
########################

:date: 2024-05-15 19:00:00
:category: Release
:summary: CUBOS. 0.2 Release and Coffee'n Jam!

.. role:: dim
    :class: m-text m-dim

Coffee'n Jam
============

From 26th of April to 3rd of May, @RiscadoA and @joaomanita participated in the Coffee'n Jam, a game jam organized by GameDev Técnico, with our engine, **CUBOS**.
The goal was to create a game in a week, with the theme "Apocalypse" - and we had a blast!

The game jam was a great opportunity to test the engine in a real game development scenario, and we learned a lot from it.
The game is called *Scraps vs Zombies*, and you can download it from its `itch.io page <https://riscadoa.itch.io/scraps-vs-zombies>`_.
You can also check out its source code in our `demo repository <https://github.com/GameDevTecnico/cubos-demo>`_.

We managed to win the "Best Gameplay" and "People's Choice" awards, which we're very proud of!

.. image:: images/scraps_vs_zombies.png

We found a lot of bugs and missing features during the jam. Additionally, we had performance become a problem for the first time.
One particular area that is in dire need of development is Audio, which we've been ignoring so far - people expect to hear something when they play a game!
We'll be working on fixing these issues in the next release, and we'll also be profiling the engine to find out where the bottlenecks are.

New 0.2 Engine Features
=======================

Our focus on this release was to continue working on improving and implementing base functionality, such as rendering and physics, and also to improve on the tools available to the developer.
We've compiled here some of the most important changes (if you're curious, you can check out the full changelog in our `repository <https://github.com/GameDevTecnico/cubos/blob/main/CHANGELOG.md>`_):

Physics Improvements :dim:`(@fallenatlas)`
------------------------------------------

This update we introduced the ``Solver``, which works to satisfy the physics constraints applied to entities (eg. Spring, Fixed distance between entities, etc.).

This means that the developers can now give entities any number of constraints, either engine defined or their own, and the solver will handle their expected interaction.
As of now, we have one constraint, internal to the engine, the ``PenetrationConstraint``, which separates bodies that are inside each other, and comes in to replace our previous collision solving system.

With the ability to have repeating systems, it was possible to introduce the physics substeps loop, which
will perform the physics update in multiple smaller steps. This is important to increase the convergence rate of the solver and preservation of energy, by reducing the errors caused by approximations of the simulation.

These changes should lead to more realistic behaviour, as well as better consistency between systems with different performance levels.

.. image:: images/complex_physics_sample.gif

Sub-scene importing in scene editor :dim:`(@teres4)`
-----------------------------------------------------

One of the improvements we wanted to make in this milestone was on our Scene Editor features in tesseratos.

Using the ``assetSelectionPopup`` for selecting a asset of a certain type, we can now import sub-scenes in a scene!

This ensures that developers save time and avoid re-doing their work, and also allows for better organization and workflow of the project.

New 0.2 Core Features
=====================

On this release, we also had to make a lot of changes to the core of the engine.
Here are some of the most relevant ones:

Observers :dim:`(@RiscadoA)`
----------------------------

Very often while working with **CUBOS**, we find the need to react to the addition and removal of components in entities.
One use case, for example, is setting up the AABB of an entity when we add a collider to it.
Previously, we had to manually implement this logic, for example, by adding a flag to the collider which was initially ``false``, and having a system initializing all colliders with the flag set to ``false``.

To solve this problem in a more elegant way, I added a new special kind of system: *observers*. Observers are essentially systems which instead of running on a specific schedule, run immediately after a certain change occurs in the ECS (akin to callbacks).

We also found another unexpected use for this feature. Complex plugins with lots of components, such as the physics plugin, where previously cumbersome to work with, as all the required components had to be manually added to each entity we wanted physics to apply to.
With observers, we instead now add a single component ``PhysicsBundle``. An observer picks up this addition, and immediately replaces this component with all of the required components for the physics plugin to work.

Introducing Inheritance in Reflection :dim:`(@roby2014)`
--------------------------------------------------------

**CUBOS** has a powerful reflection system to examine and interact with a structures and types at runtime.

``InheritsTrait`` is a new feature in **CUBOS** that allows you to represent and query inheritance relationships
in a reflective context. With this trait, you can define which types inherit from others and then check those relationships at runtime.

Check our documentation page for more information: https://gamedevtecnico.github.io/cubos/docs/examples-core-reflection-traits-inherits.html.

Repeating systems and fixed-step updates :dim:`(@joaomanita)`
------------------------------------------------------------

Certain plugins, like the physics plugin, required some of their systems to run multiple times per frame so that they could make more accurate
aproximations. In addition, some of them need to be executed in ordered groups (ex: physics integrate position > update velocities > clear forces > clear impulses).
To do this I added tags that make systems tagged by them be repeated while a condition is true (cubos.tag(exampleTag).repeatWhile({});).
And to create subgroups, all you need to do is tag your subgroup tag with a parent tag 
(cubos.tag(groupTag).repeatWhile({});
 cubos.tag(subgroupTag).repeatWhile({}).tagged(groupTag); )

 This way the subgroup will repeat n x m times (n-grouptag m-subgrouptag)

 With this it was easy to implement a fixed-step plugin, which adds a tag that forces systems to repeat according to
 the DeltaTime passed, avoiding variance due to different framerates and more/less powerful PCs.

Serialization overhaul :dim:`(@Dacops)`
---------------------------------------

Serialization is a crucial part of the game engine that allows for the saving of any CUBOS. game components aswell as then loading them in. Due to the new reflections
system used by CUBOS. serialization needed an overhaul to use these newer tecnologies that allow not only for a more user friendly usage but also to considerably reduce
the lines of code taken by this component. Previously only primitive types were natively supported for saving/loading, any newer structures implemented by the game
developers would need to be accompanied with overwrites of the saving/loading methods for the given structure. This, apart from being annoying could easily also amount 
to an unecessary increase of lines of code written.
With the new reflections, this is no longer needed, developers just need to "reflect" their structures via a macro that ammounts to a single line, to declare their types.
The new saving/loading methods will then pick up on these structures and iteratively decompose them into primitive types. The methods for primitive types were also removed 
for a common method, significantly reducing the space occupied by this feature.
Furthermore several other parts of the CUBOS. unnecessarely used serialization (such as voxel grids, palettes and input bindings) these were removed and replaced by faster 
methods contributing to a more efficient engine.

Improved graphics renderer :dim:`(@RiscadoA, @tomas7770)`
---------------------------------------

Before this update, our graphics renderer was very monolithic, with a lot of the code being held in a single file. This posed some problems,
namely that if we wanted to implement new rendering methods in the future (e.g. raytracing), we would end up with duplicate code.
It also didn't fit well with our ECS design, since things such as the renderer and its active cameras were just global resources.

To overcome this, we've restructured the renderer, splitting it into several components with their respective plugins. The most important ones
are perhaps ``RenderTarget``, representing something that can be drawn to, and ``PerspectiveCamera``, which draws to render targets using perspective projection.
Entities with these components are related using a ``DrawsTo`` relation. There are also components that individually enable various parts of the renderer,
such as deferred shading, or effects like bloom and SSAO. This separation opens up possibilities for more customizability from the user side,
and makes the renderer code easier to deal with by engine developers.

New 0.2 Tools Features
======================

Transform Gizmo Upgrades :dim:`(@DiogoMendonc-a)`
-------------------------------------------------

The biggest change was the addition of a rotation gizmo, so now you can rotate entities using your mouse!

We also added a toggle that allows changing between using global or local space with the Transform Gizmo,
and a new type of gizmo, a ``Rotated Box``, which, unlike the old boz gizmos, does no need to be axis-alligned.

Finally, the transform gizmo is now always rendered at the same size, regardless of the selected entity's distance to the camera.
This should hopefully make it easier to use the tool when moving entities either very far away, or very close.

.. image:: images/transform_gizmo.gif

WorldInspector Overhaul :dim:`(@diogomsmiranda)`
----------------------------------------------------

The WorldInspector as been on our radar for quite some time now, as a tool that could be improved.
This release we particularly aimed on making it better by focusing on:

    * Making it easier to find the entities you are looking for.

    * Getting more information about the entities in the scene.

To tackle the first point we added a search bar that allows you to filter the entities in the scene, either by their ``Name.value``, or by their components. i.e:

    * Searching for "player" will show all entities that have "player" in their ``Name.value``.

    * Searching for "Transform" will show all entities that have a ``Transform`` component.

    * Searching for "player, Transform" will show all entities that have a ``Transform`` component and contain "player" in their ``Name.value``.

To tackle the second point on our list we added an hierarchy view that shows the entities in the scene in a tree-like structure representing the ``ChildOf`` relation between entities.
For further visualisation of this hierarchy, we changed our main.cubos scene on ``Tesseratos`` to have a more complex structure, with entities being children of other entities.

Next steps
==========

TODO: UI

TODO: voxel collisions

TODO: proper tesseratos-game flow and integration

TODO: friction, new physics features etc

TODO: hint at new recruitment coming soon
