==============
python-acapela
==============

:Author: Arezqui Belaid
:Description: Python wrapper for text-to-speech synthesis with Acapela
:Company: Developed by Star2Billing http://www.star2billing.com


Python Acapela Wrapper
======================

python-acapela is a library to produce a text-to-speech file using `Acapela`_ web services.

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

* Support different type of audio quality 22Hz, 8Hz

* Provide voices of different gender and intonation


Installation
------------

Install, upgrade and uninstall python-acapela.py with these commands::

  $ sudo pip install python-acapela
  $ sudo pip install --upgrade python-acapela
  $ sudo pip uninstall python-acapela

Or if you don't have `pip`::

  $ sudo easy_install python-acapela


Example usage and output
------------------------

::

  $ Usage: python-acapela -acclogin <accountlogin> -applogin <applicationlogin> -p <password> -t <text> [-q <quality>] [-d <directory>] [-url <service_url>] [-h]
  
  $ Output : Recorded TTS to /tmp/ACAPELA-8895934760117809679-ES.mp3


Feedback
--------

Your feedback is more than welcome. Write email to
areski@gmail.com or post bugs and feature requests on github:

http://github.com/areski/python-acapela/issues


Extra information
-----------------

Newfies-Dialer, an open source Auto Dialer software, uses this module to synthetize audio files being play to the end-user.
Further information about Newfies-Dialer can be found at http://www.newfies-dialer.org

This module is built and supported by Star2Billing : http://www.star2billing.com

Similar library in Ruby : https://github.com/mheld/acapela-ruby


Source download
---------------

The source code is currently available on github. Fork away!

http://github.com/areski/python-acapela


