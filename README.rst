===============================
Hello World Example Plugin
===============================

This repository defines a *UfoTest Plugin*. UfoTest is an application which was developed for the continuous testing
of various scientific camera systems at the `Institute of Data Processing (IPE) <https://www.ipe.kit.edu/>`_ of the
`Karlsruhe Institute of Technology (KIT) <https://www.kit.edu/>`_. By implementing a plugin management system and
exposing various action and filter hooks within it's core routines, UfoTest allows functionality to be added or
modified by third party code such as this plugin.

An example ufotest plugin implementation

Installation
============

UfoTest plugins are installed by placing their source code folder into the special ``plugins`` folder of a local
UfoTest installation. This is best done by cloning the repository using git:

.. code-block:: console

    cd ~/.ufotest/plugins
    git clone https://github.com/the16thpythonist/hello_world_example.git

With each start of an UfoTest runtime all plugins within this folder are automatically discovered and the ``main.py``
files contained within each plugin folder is imported. Within these main files, it is important to register all the
necessary callbacks to the corresponding hooks.

If the plugin requires additional dependencies for its operation, these can be installed from the ``requirements.txt``
file:

.. code-block:: console

    pip3 install -r hello_world_example/requirements.txt

Usage
=====

This is only an example implementation showcasing of how to write ufotest plugins. In particular it implements the
following mock functionality:

- Prints hello world before the execution of every test
- A special hello world test case
- Adds a new CLI command "hello_world"

The CLI command can be invoked like this:

.. code-block:: console

    ufotest plugin hello_world

Development
===========

For the development of this plugin an UfoTest installation is required. The plugin will have to be installed into the
plugin folder of the UfoTest installation folder ``.ufotest``. This UfoTest installation can be created manually on
the local system, but a docker container can also be used. Using a docker container to provide the UfoTest installation
has several advantages: Testing and development are less heavily by side effects of any one specific local development
environment. It is possible to manage multiple concurrent installations for different purposes and different
configurations. The necessary configuration is provided "out of the box".

Using the docker container
--------------------------

As a prerequisite of using the docker UfoTest environment, both ``docker`` and ``docker-compose`` have to be installed:

.. code-block:: console

    sudo apt-get install docker docker-compose

Initially building the container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The container can then be build using the composer YML file which defines the necessary environment. For this step
navigate to the root folder of the local clone of this repository.

.. code-block:: console

    sudo docker-compose -f docker/local.yml

If at one point in the future the development environment is irreparably damaged, the whole container can be wiped and
rebuild by using the ``rebuild.sh`` script:

.. code-block:: console

    ./docker/rebuild.sh

Running UfoTest commands in the container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use docker compose to execute UfoTest commands using the UfoTest installation from within the container:

.. code-block:: console

    sudo docker-compose -f docker/local.yml run ufotest_hello_world_example ufotest --help

Since writing out this command is a bit tedious, the same can be achieved by invoking the ``run.sh`` script, which can
be found at the top level of this repository with the command string to be executed within the container.

.. code-block:: console

    ./run.sh "ufotest --help"

Using the web interface
~~~~~~~~~~~~~~~~~~~~~~~

It is also possible to start the UfoTest web interface within the container and then view it as if it were running on
the local machine. This is achieved by mapping the port from the container to the same port of the local machine.
UfoTest web interface runs on the port 8030, so make sure that no other service is bound to this port and then run
the following command to start the server:

.. code-block:: console

    ./run.sh "ufotest ci serve"

Compiling this README
---------------------

The ufotest web interfaces is able to display the :code:`README.html` file for every ufotest plugin. Writing a
separate HTML readme would be tedious though. Luckily this very RST file can be converted easily into HTML format.

For this make sure that :code:`docutils` is installed:

.. code-block:: console

    python3 -m pip install docutils

Then you can simply run the :code:`doc.sh` bash script and it will create the HTML file:

.. code-block:: console

    bash doc.sh
