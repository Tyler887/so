.. toctree::
   :maxdepth: 2
   :caption: Contents:

Using the SO CLI
================
This is a tutorial about how to use the CLI. This tutorial is specific to GNU/Linux (including WSL)
and macOS, including BSD descendants. Any help for Windows is welcome.

Installing
----------
It's easy to install ``so``. However, the way to install it depends on your OS.

.. tab:: macOS, *BSD or GNU/Linux (Unix-like)
   
   .. warning::
      
      Stack Overflow CLI is not tested on macOS or *BSD, only on GNU/Linux and Windows.
   
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

.. tab:: Windows
   
   .. warning::
      
      SO CLI is not yet avaliable via Windows Package Manager. If popularity grows, I'll submit
      SO CLI to the Microsoft WinGet community repository for review when the project
      is ready to be avaliable to the public.
   
   To install ``so``, launch PowerShell (recommended Windows Powershell 5.1 or
   PowerShell 7) and run:
   
   .. code-block:: powershell
      
      Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://github.com/Tyler887/so/raw/main/install.ps1')

Using it
--------
.. warning::

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

  So run ``so login``. Already logged in? If you moved to another account or just deleted your
  Stack Overflow profile, you need to run ``so logout`` to remove the app from
  your SEN account.

``so`` or ``so help`` will list commands.

``so feed <type>`` allows you to view the RSS feed of questions/answers. It
is useful to check this out everyday so you can answer questions that still
do not                      have                     an             answer.

For more info, refer to the rest of the docs.
