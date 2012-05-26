==============
python-acapela
==============

:Author: Arezqui Belaid
:Description: Python wrapper for text-to-speech synthesis with Acapela



python-acapela - Python Acapela Library
=======================================

python-acapela is a library to produce text-to-speech file using `Acapela`_ web services.

.. _Acapela: http://acapela-vaas.com/


Quickstart
==========

::

   import acapela
   engine = acapela.init()
   engine.say('Greetings!')
   engine.say('How are you today?')
   engine.runAndWait()


Features
--------

* Produce text to speech in different languages, see list of languages supported :
  http://www.acapela-vaas.com/ReleasedDocumentation/voices_list.php

* Support different type of audio quality 22Hk, 8Hk

* Provide different voices gender and different intonation


Installation
------------

You can install, upgrade, uninstall python-acapela.py with these commands::

  $ sudo pip install python-acapela
  $ sudo pip install --upgrade python-acapela
  $ sudo pip uninstall python-acapela

Or if you don't have `pip`::

  $ sudo easy_install python-acapela


Example usage and output
------------------------

::

  $ python-acapela 'I feel like I’m taking crazy pills!' -l en
  


Feedback
--------

Your feedback is more than welcome. Write email to
areski@gmail.com or post bugs and feature requests on github:

http://github.com/areski/python-acapela/issues

Source download
---------------

The source code is currently available on github. Fork away!

http://github.com/areski/python-acapela
