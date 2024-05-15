Coffee'n Jam and... 0.2!
########################

:date: 2024-05-07 19:00:00
:category: Meta
:summary: CUBOS. 0.2 Release and Coffee'n Jam!

.. role:: dim
    :class: m-text m-dim

Coffee'n Jam
============

insert very interesting text here, problems occurred, final result, etc,

New 0.2 Engine Features
=======================

Our focus on this release was to continue working on improving and implementing base functionality, such as rendering and physics, and also to improve on the tools available to the developer.
We've compiled here some of the most important changes (if you're curious, you can check out the full changelog in our `repository <https://github.com/GameDevTecnico/cubos/blob/main/CHANGELOG.md>`_):

Transform Gizmo Upgrades :dim:`(@DiogoMendonc-a)`
-------------------------------------------------

The biggest change was the addition of a rotation gizmo, so now you can rotate entities using your mouse!

We also added a toggle that allows changing between using global or local space with the Transform Gizmo,
and a new type of gizmo, a ``Rotated Box``, which, unlike the old boz gizmos, does no need to be axis-alligned.

Finally, the transform gizmo is now always rendered at the same size, regardless of the selected entity's distance to the camera.
This should hopefully make it easier to use the tool when moving entities either very far away, or very close.

.. image:: images/transform_gizmo.gif

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

Next steps
==========

TODO: talk about
- UI
- voxel collisions
- proper tesseratos-game flow and integration
