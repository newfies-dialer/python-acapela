#!/usr/bin/env python
# -*- coding: utf-8 -*-
# acapela.py - Python wrapper for text-to-speech synthesis with Acapela
# Copyright (C) 2012 Arezqui Belaid <areski@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import acapela

ACCOUNT_LOGIN = 'EVAL_XXXX'
APPLICATION_LOGIN = 'EVAL_XXXXXXX'
APPLICATION_PASSWORD = 'XXXXXXXX'

SERVICE_URL = 'http://vaas.acapela-group.com/Services/Synthesizer'
QUALITY = '22k' # 22k, 8k, 8ka, 8kmu
TTS_ENGINE = 'ACAPELA'
DIRECTORY = '/tmp/'


def test_acapela():
    """
    Function to test text to speech
    """

    #Construct
    tts_acapela = acapela.Acapela(TTS_ENGINE, ACCOUNT_LOGIN, APPLICATION_LOGIN, APPLICATION_PASSWORD, SERVICE_URL, QUALITY, DIRECTORY)    

    #General settings for test
    gender = 'W'
    intonation = 'NORMAL'
    
    #Spanish
    lang = 'ES'
    text = u"Newfies-Dialer es una aplicación de transmisión de voz diseñado y construido para automatizar la entrega de las llamadas telefónicas interactivas a contactos, clientes y público en general."
    tts_acapela.prepare(text, lang, gender, intonation)
    output_filename = tts_acapela.run()
    print "Recorded TTS to %s" % output_filename
    
    #Portuguese
    lang = 'BR'
    text = u"Newfies-Dialer é um aplicativo de transmissão de voz projetada e construída para automatizar a entrega de telefonemas interativos para contatos, clientes e público em geral."
    tts_acapela.prepare(text, lang, gender, intonation)
    output_filename = tts_acapela.run()
    print "Recorded TTS to %s" % output_filename
    
    #French
    lang = 'FR'
    text = u"Newfies-Dialer est une application de diffusion vocale conçu et construit pour automatiser la livraison des appels téléphoniques interactifs à des contacts, des clients et le public en général."
    tts_acapela.prepare(text, lang, gender, intonation)
    output_filename = tts_acapela.run()
    print "Recorded TTS to %s" % output_filename
    
    #English
    lang = 'EN'
    text = "Newfies-Dialer is a voice broadcast application designed and built to automate the delivery of interactive phone calls to contacts, clients and the general public."
    tts_acapela.prepare(text, lang, gender, intonation)
    output_filename = tts_acapela.run()
    print "Recorded TTS to %s" % output_filename
    
    

if __name__ == '__main__':
    test_acapela()
    

