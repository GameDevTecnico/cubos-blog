Cubos Engine
############

:save_as: index.html
:url:
:cover: {static}/images/landing/cover.png
:landing:
    .. container:: m-row

        .. container:: m-col-s-12

            .. raw:: html

                <img src="/images/logo.png" alt="Cubos Engine" class="m-image">

    .. container:: m-row

        .. container:: m-col-l-12 m-text-center m-nopadt

            .. raw:: html

                <h2 class="landing-caption">An open-source student-developed game engine built in modern C++ where everything is made of voxels.</h2>

    .. container:: m-row

        .. container:: m-col-m-4 m-push-m-2 m-col-t-6

            .. button-primary:: https://docs.cubosengine.org/getting-started.html
                :class: m-fullwidth

                Get Started

        .. container:: m-col-m-4 m-push-m-2 m-col-t-6

            .. button-primary:: #join-us
                :class: m-fullwidth

                Join the Team

:more_content:
    .. container:: m-container-inflate landing-features

        .. raw:: html

            <div class="feature-container feature-container-reverse">
                <div class="feature-image">
                    <img src="/images/landing/puzzle.svg" alt="Plugin" class="m-image" style="filter: invert(1); width: 40%;"/>
                </div>
                <div class="feature-text">
                    <h2>Modular</h2>
                    <p>In <span class="cubos">Cubos</span>, everything is a plugin: do you prefer to use your own renderer or some other physics framework? Simply swap any of our plugins by your own one.</p>
                </div>
            </div>

            <div class="feature-container ">
                <div class="feature-text">
                    <h2>Data Oriented Design</h2>
                    <p><span class="cubos">Cubos</span> is built on top of our own custom Entity Component System, designed both for performance and flexibility.</p>
                </div>
                <div class="feature-image">
                    <img src="/images/landing/ecs.png" alt="Entity Component System" class="m-image"/>
                </div>
            </div>

            <div class="feature-container feature-container-reverse">
                <div class="feature-image">
                    <img src="/images/landing/voxels.svg" alt="Voxels" class="m-image" style="filter: invert(1); width: 50%;"/>
                </div>
                <div class="feature-text">
                    <h2>Voxels First</h2>
                    <p>Voxels are a first class citizen in <span class="cubos">Cubos</span>: our engine comes with many plugins built specifically to enable you to create voxel games.</p>
                </div>
            </div>


            <div class="feature-container feature-container">
                <div class="feature-text">
                    <h2>Physics</h2>
                    <p>Custom physics and collisions engine built specifically for ECS and voxel games.</p>
                </div>
                <div class="feature-image">
                    <img src="/images/landing/physics.svg" alt="Physics" class="m-image" style="filter: invert(1); width: 40%;"/>
                </div>
            </div>
            
            <div class="feature-container feature-container-reverse">
                <div class="feature-image">
                    <img src="/images/landing/audio.svg" alt="Audio" class="m-image" style="filter: invert(1); width: 40%;"/>
                </div>
                <div class="feature-text">
                    <h2>Audio</h2>
                    <p>Sounds can be easily played from audio assets by creating Audio Source entities.</p>
                </div>
            </div>

            <div class="feature-container">
                <div class="feature-text">
                    <h2>UI Framework</h2>
                    <p>A custom UI framework built on top of our ECS framework where every element can be manipulated in the same way as any other entity.</p>
                </div>
                <div class="feature-image">
                    <img src="/images/landing/ui.svg" alt="UI" class="m-image" style="filter: invert(1); width: 40%;"/>
                </div>
            </div>

            <div class="feature-container feature-container-reverse">
                <div class="feature-image">
                    <img src="/images/landing/cross-platform.png" alt="Physics" class="m-image" style="filter: invert(1); width: 50%;"/>
                </div>
                <div class="feature-text">
                    <h2>Cross Platform</h2>
                    <p>Support for all major desktop platforms: Windows, MacOS, Linux and Web.</p>
                </div>
            </div>

            <div class="feature-container">
                <div class="feature-text">
                    <h2>Free and Open Source</h2>
                    <p>The engine and its demos are licensed under the permissive MIT license, which means anyone is free to use, modify and distribute it.</p>
                </div>
                <div class="feature-image">
                    <img src="/images/landing/open-source.svg" alt="Open Source" class="m-image" style="filter: invert(1); width: 65%;"/>
                </div>
            </div>

            <div class="feature-container feature-container-reverse">
                <div class="feature-image">
                    <img src="/images/landing/gdt.png" alt="GameDev Técnico" class="m-image" style="width: 65%;"/>
                </div>
                <div class="feature-text">
                    <h2>Built by Students</h2>
                    <p><span class="cubos">Cubos</span> is developed by students at <a href="https://gamedev.tecnico.ulisboa.pt/" target="_blank">GameDev Técnico</a>, a student association based at Instituto Superior Técnico, Lisbon, and open to anyone studying in Portugal.</p>
                </div>
            </div>

    .. container:: m-container-inflate

        .. container:: join-us

            .. raw:: html

                <h2 id="join-us">Join us</h2>
                <p>
                    Are you interested in helping build a game engine from the ground up?
                    Do you want to hone your programming skills and get practical experience on a real C++ codebase?
                    Or, perhaps, would you like to help manage the project, the community, or even improve this website?
                </p>
                <p>
                    Join the <span class="cubos">Cubos</span> <a href="https://discord.com/invite/WjTtcNTRqD">Discord server</a>, where we have more information about you can join the team!
                </p>