.. toctree::
   :maxdepth: 2
   :caption: Contents:

Using the SO CLI
================
This is a tutorial about how to use the CLI. This tutorial is specific to Linux/WSL
and macOS. Any help for Windows is welcome.

Installing
----------
Assuming that you have `Python
<https://python.org>`_ (3.6 or newer required due to F-strings), including PyInstaller and everything in
`the SO CLI requirements.txt
<https://github.com/Tyler887/so/blob/main/requirements.txt>`_, you **can** install ``so``
by using this command (works for and executes BASH):

.. code-block:: shell

   bash -c "$(curl -fsSL https://raw.githubusercontent.com/Tyler887/so/main/install.sh)"

This command may install Python if it is missing.

If you are unable to execute this command, copy and paste the installation script
from `Stack Apps
<https://stackapps.com/questions/9375/placeholder-stackoverflow-cli>`_.

Setting up
----------
The SO CLI uses the Stack Exchange API, which requires you to approve
the SO CLI when you try to use it.

If you run SO CLI without authenticating to the API, this error
will appear:

.. code-block::
   
   (x) Error: Please authenticate to the API using: so login
       The Stack Overflow CLI uses the Stack Exchange API, so you need
       to login to use the SO CLI.
       
       If you do not have a Stack Overflow account, you can safely
       remove this program from your system: sudo rm /usr/bin/so

So run ``so login``. If you moved to another account or just deleted your
Stack Overflow profile, you need to run ``so logout`` to remove the app from
your SEN account.

Using it
--------
``so`` or ``so help`` will list commands.

``so feed <type>`` allows you to view the RSS feed of questions/answers. It
is useful to check this out everyday so you can answer questions that still
do not                      have                     an             answer.

For more info, refer to the rest of the docs.
