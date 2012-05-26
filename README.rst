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
    
    ACCOUNT_LOGIN = 'EVAL_XXXX'
    APPLICATION_LOGIN = 'EVAL_XXXXXXX'
    APPLICATION_PASSWORD = 'XXXXXXXX'
    SERVICE_URL = 'http://vaas.acapela-group.com/Services/Synthesizer'
    
    tts_acapela = acapela.Acapela(ACCOUNT_LOGIN, APPLICATION_LOGIN, APPLICATION_PASSWORD, SERVICE_URL, '22k', '/tmp/')    
    tts_acapela.prepare(text=u"Hola! Buenos días", lang='ES', gender='W', intonation='NORMAL')
    output_filename = tts_acapela.run()
    
    print "Recorded TTS to %s" % output_filename


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
