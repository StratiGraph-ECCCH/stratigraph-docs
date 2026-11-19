StratiGraph documentation
=========================

The landing project of ``docs.stratigraph-eccch.eu``: one address for the manuals of
the StratiGraph tools, each of which lives beside its own code and is published here
as a subproject.

- the node and its catalogue — ``stratigraph-server`` → ``/node/``
- the field assistant — ``stratigraph-stratifield`` → ``/field/``
- the recording templates — ``stratigraph-templates`` → ``/templates/``

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
