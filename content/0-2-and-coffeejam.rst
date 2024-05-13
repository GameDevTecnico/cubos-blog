Coffee'n Jam and... 0.2!
########################

:date: 2024-05-07 19:00:00
:category: Meta
:summary: CUBOS. 0.2 Release and Coffee'n Jam!

Coffee'n Jam
============

insert very interesting text here, problems occurred, final result, etc,

New 0.2 features
================


Introducing Inheritance in Reflection
-------------------------------------
> Trait for representing inheritance relationships under reflection. (#693, @roby2014).

``CUBOS.`` has a powerful reflection system to examine and interact with a structures and types at runtime.

``InheritsTrait`` is a new feature in ``CUBOS.`` that allows you to represent and query inheritance relationships
in a reflective context. With this trait, you can define which types inherit from others and then check those relationships at runtime.

You can define inheritance as the following:

.. code-block:: c++

    #include <cubos/core/reflection/traits/inherits.hpp>

    using cubos::core::reflection::InheritsTrait;
    using cubos::core::reflection::Type;

    struct GrandParent
    {
        CUBOS_REFLECT;
    };

    struct Parent
    {
        CUBOS_REFLECT;
    };

    struct Son
    {
        CUBOS_REFLECT;
    };

    CUBOS_REFLECT_IMPL(GrandParent)
    {
        return Type::create("GrandParent");
    }

    CUBOS_REFLECT_IMPL(Parent)
    {r
        return Type::create("Parent").with(InheritsTrait::from<GrandParent>());
    }

    CUBOS_REFLECT_IMPL(Son)
    {
        return Type::create("Son").with(InheritsTrait::from<Parent>());
    }

or you can also check inheritance:

.. code-block:: c++

    void reflectType()
    {
        const auto& type = reflect<Son>();
        if (type.has<InheritsTrait>() && type.get<InheritsTrait>().inherits<Parent>())
        {
            std::cout << type.name() << " inherits from Parent\n";
        }
    }

you can check more information on the documentation page: https://gamedevtecnico.github.io/cubos/docs/examples-core-reflection-traits-inherits.html.


Transform Gizmo Upgrades
-------------------------------------

The biggest change was the addition of a rotation gizmo, so now you can rotate entities using your mouse!

We also added a toggle that allows changing between using global or local space with the Transform Gizmo,
and a new type of gizmo, a ``Rotated Box``, which, unlike the old boz gizmos, does no need to be axis-alligned.

Finally, the transform gizmo is now always rendered at the same size, regardless of the selected entity's distance to the camera.
This should hopefully make it easier to use the tool when moving entities either very far away, or very close.

.. image:: images/transform_gizmo.gif

Next steps
==========

