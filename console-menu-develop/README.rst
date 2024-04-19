|Build Status|\ |Documentation Status|

console-menu
============

A simple Python menu-based UI system for terminal applications.
Perfect for those times when you need a menu-driven program, but don’t want the
overhead or learning curve of a full-fledged GUI framework.

Derived from the curses-menu project, but with curses dependency removed.

http://console-menu.readthedocs.org/en/latest/

.. image:: https://raw.githubusercontent.com/aegirhall/console-menu/develop/images/console-menu_screenshot1.png

.. image:: https://raw.githubusercontent.com/aegirhall/console-menu/develop/images/console-menu_screenshot2.png

.. image:: https://raw.githubusercontent.com/aegirhall/console-menu/develop/images/console-menu_screenshot3.png

.. image:: https://raw.githubusercontent.com/aegirhall/console-menu/develop/images/console-menu_screenshot4.png

Installation
~~~~~~~~~~~~

Tested on Python 3.7 - 3.11, as well as pypy and pypy 3.

Installation can be performed by running pip

.. code:: shell

   pip install console-menu

Usage
-----

It's designed to be pretty simple to use. Here's an example

.. code:: python

    # Import the necessary packages
    from consolemenu import *
    from consolemenu.items import *

    # Create the menu
    menu = ConsoleMenu("Title", "Subtitle")

    # Create some items

    # MenuItem is the base class for all items, it doesn't do anything when selected
    menu_item = MenuItem("Menu Item")

    # A FunctionItem runs a Python function when selected
    function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

    # A CommandItem runs a console command
    command_item = CommandItem("Run a console command",  "touch hello.txt")

    # A SelectionMenu constructs a menu from a list of strings
    selection_menu = SelectionMenu(["item1", "item2", "item3"])

    # A SubmenuItem lets you add a menu (the selection_menu above, for example)
    # as a submenu of another menu
    submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

    # Once we're done creating them, we just add the items to the menu
    menu.append_item(menu_item)
    menu.append_item(function_item)
    menu.append_item(command_item)
    menu.append_item(submenu_item)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()

.. |Build Status| image:: https://github.com/aegirhall/console-menu/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/aegirhall/console-menu/actions/workflows/ci.yml
.. |Documentation Status| image:: https://readthedocs.org/projects/console-menu/badge/?version=latest
   :target: http://console-menu.readthedocs.org/en/latest/?badge=latest

Development
-----------

.. code:: shell

   pip install -r requirements-docs.txt
   pip install -v -e .
   pytest
