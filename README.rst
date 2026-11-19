StratiGraph documentation
=========================

The landing project of ``docs.stratigraph-eccch.eu``: one address for the manuals of
the StratiGraph tools, each of which lives beside its own code and is published here
as a subproject.

- the node and its catalogue — ``stratigraph-server`` → ``/projects/node/``
- the field assistant — ``stratigraph-stratifield`` → ``/projects/field/``
- the recording templates — ``stratigraph-templates`` → ``/projects/templates/``

The StratiGraph Academy has an address of its own, ``academy.stratigraph-eccch.eu``,
because it teaches rather than describes, and may one day move to a course space.
EMStudio, EM Tools, s3Dgraphy, the 3D Survey Collection and Heriverse keep their
manuals in the Extended Matrix house, ``docs.extendedmatrix.org``; this project links
them and never copies them.

This repository holds only the welcome page. Changing a manual means changing it in
the repository of its own tool.

Build locally
-------------

.. code-block:: bash

   python3 -m venv .venv
   .venv/bin/pip install -r docs/requirements.txt
   .venv/bin/sphinx-build -W --keep-going -b html docs docs/_build/html

Authored by Emanuel Demetrescu, CNR-ISPC, for the StratiGraph consortium.

.. documentation-map:start

Where the documentation lives
-----------------------------

Every tool of the two families keeps its manual beside its code, and publishes it at one of the two addresses below. A manual is changed in the repository of its own tool, never here.

.. list-table::
   :header-rows: 1
   :widths: 26 26 26 22

   * - Tool
     - Code
     - Manual
     - Published at
   * - **Extended Matrix**
     -
     -
     -
   * - Extended Matrix (the language)
     - `zalmoxes-laran/ExtendedMatrix <https://github.com/zalmoxes-laran/ExtendedMatrix>`_
     - `zalmoxes-laran/ExtendedMatrix-doc <https://github.com/zalmoxes-laran/ExtendedMatrix-doc>`_
     - https://docs.extendedmatrix.org/en/1.5/
   * - EMStudio (editor)
     - `ExtendedMatrix/EMStudio <https://github.com/ExtendedMatrix/EMStudio>`_
     - `ExtendedMatrix/EMStudio-doc <https://github.com/ExtendedMatrix/EMStudio-doc>`_
     - https://docs.extendedmatrix.org/projects/emstudio-doc/en/1.6/
   * - EM Tools (Blender add-on)
     - `zalmoxes-laran/EM-blender-tools <https://github.com/zalmoxes-laran/EM-blender-tools>`_
     - `zalmoxes-laran/EM-blender-tools-doc <https://github.com/zalmoxes-laran/EM-blender-tools-doc>`_
     - https://docs.extendedmatrix.org/projects/EM-tools/en/1.5/
   * - s3Dgraphy (library)
     - `ExtendedMatrix/s3Dgraphy <https://github.com/ExtendedMatrix/s3Dgraphy>`_
     - same repository, ``docs/``
     - https://docs.extendedmatrix.org/projects/s3dgraphy/en/v1.5/
   * - 3D Survey Collection
     - `zalmoxes-laran/3D-survey-collection <https://github.com/zalmoxes-laran/3D-survey-collection>`_
     - `zalmoxes-laran/3D-survey-collection-doc <https://github.com/zalmoxes-laran/3D-survey-collection-doc>`_
     - https://docs.extendedmatrix.org/projects/3DSC/en/1.7.0/
   * - Heriverse (web runtime)
     - `StratiGraph-ECCCH/Heriverse <https://github.com/StratiGraph-ECCCH/Heriverse>`_
     - `StratiGraph-ECCCH/Heriverse-doc <https://github.com/StratiGraph-ECCCH/Heriverse-doc>`_
     - https://docs.extendedmatrix.org/projects/heriverse/en/1.5/
   * - **StratiGraph**
     -
     -
     -
   * - The node, and its catalogue
     - `StratiGraph-ECCCH/stratigraph-server <https://github.com/StratiGraph-ECCCH/stratigraph-server>`_
     - same repository, ``docs/``
     - https://docs.stratigraph-eccch.eu/projects/node/en/latest/
   * - StratiField (field assistant)
     - `StratiGraph-ECCCH/stratigraph-stratifield <https://github.com/StratiGraph-ECCCH/stratigraph-stratifield>`_
     - same repository, ``docs/``
     - https://docs.stratigraph-eccch.eu/projects/field/en/latest/
   * - Recording templates
     - `StratiGraph-ECCCH/stratigraph-templates <https://github.com/StratiGraph-ECCCH/stratigraph-templates>`_
     - same repository, ``docs/``
     - https://docs.stratigraph-eccch.eu/projects/templates/en/v0.1.0/
   * - The welcome page of the manuals
     - —
     - `StratiGraph-ECCCH/stratigraph-docs <https://github.com/StratiGraph-ECCCH/stratigraph-docs>`_
     - https://docs.stratigraph-eccch.eu
   * - The StratiGraph Academy
     - —
     - `StratiGraph-ECCCH/stratigraph-academy <https://github.com/StratiGraph-ECCCH/stratigraph-academy>`_
     - https://academy.stratigraph-eccch.eu

.. documentation-map:end
