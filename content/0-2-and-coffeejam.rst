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

New 0.2 features
================

Introducing Inheritance in Reflection :dim:`(@roby2014)`
--------------------------------------------------------

**CUBOS** has a powerful reflection system to examine and interact with a structures and types at runtime.

``InheritsTrait`` is a new feature in **CUBOS** that allows you to represent and query inheritance relationships
in a reflective context. With this trait, you can define which types inherit from others and then check those relationships at runtime.

Check our documentation page for more information: https://gamedevtecnico.github.io/cubos/docs/examples-core-reflection-traits-inherits.html.


Transform Gizmo Upgrades :dim:`(@DiogoMendonc-a)`
-------------------------------------------------

The biggest change was the addition of a rotation gizmo, so now you can rotate entities using your mouse!

We also added a toggle that allows changing between using global or local space with the Transform Gizmo,
and a new type of gizmo, a ``Rotated Box``, which, unlike the old boz gizmos, does no need to be axis-alligned.

Finally, the transform gizmo is now always rendered at the same size, regardless of the selected entity's distance to the camera.
This should hopefully make it easier to use the tool when moving entities either very far away, or very close.

.. image:: images/transform_gizmo.gif

Next steps
==========

