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


__version__ = '1.1'

import sys
import os.path

if sys.version_info < (3,0):
    import urllib as request
    parse = request
    import urllib2
    for method in dir(urllib2):
        setattr(request, method, getattr(urllib2, method))
    import cookielib as cookiejar
    
else:
    from http import cookiejar
    from urllib import parse, request


ACCOUNT_LOGIN = 'EVAL_XXXX'
APPLICATION_LOGIN = 'EVAL_XXXXXXX'
APPLICATION_PASSWORD = 'XXXXXXXX'

SERVICE_URL = 'http://vaas.acapela-group.com/Services/Synthesizer'
QUALITY = '22k' # 22k, 8k, 8ka, 8kmu
TTS_ENGINE = 'ACAPELA'
DIRECTORY = '/tmp/'


class Acapela(object):

    #Properties
    TTS_ENGINE = None
    ACCOUNT_LOGIN = None
    APPLICATION_LOGIN = None
    APPLICATION_PASSWORD = None
    SERVICE_URL = None
    QUALITY = None
    DIRECTORY = ''
    
    #Available voices list
    #http://www.acapela-vaas.com/ReleasedDocumentation/voices_list.php
    langs  = {
        'ES': {
            'W': {
                'NORMAL': 'ines',
            },
            'M': {
                'NORMAL': 'antonio',
            }
        },
        'BR': {
            'W': {
                'NORMAL': 'marcia',
            },
        },
        'EN': {
            'W': {
                'NORMAL': 'lucy',
            },
            'M': {
                'NORMAL': 'graham',
            },
        },
        'US': {
            'W': {
                'NORMAL': 'laura',
            },
            'M': {
                'NORMAL': 'heather',
            },
        },
        'FR': {
            'W': {
                'NORMAL': 'alice',
            },
            'M': {
                'NORMAL': 'antoine',
            },
        },
        'PT': {
            'W': {
                'NORMAL': 'marcia',
            },
        },
    }
    data = {}
    filename = None
    
    def __init__(self, tts_engine, account_login, application_login, application_password, service_url, quality, directory=''):
        """construct Acapela TTS"""
        self.TTS_ENGINE = tts_engine
        self.ACCOUNT_LOGIN = account_login
        self.APPLICATION_LOGIN = application_login
        self.APPLICATION_PASSWORD = application_password
        self.SERVICE_URL = service_url
        self.QUALITY = quality
        self.DIRECTORY = directory
    
    def prepare(self, text, lang, gender, intonation):
        """Prepare Acapela TTS"""
        lang = lang.upper()
        concatkey = "%s-%s-%s-%s" % (text, lang, gender, intonation)
        key =  self.TTS_ENGINE + '' + str(hash(concatkey))
        try:
            req_voice = self.langs[lang][gender][intonation] + self.QUALITY
        except:
            req_voice = 'lucy22k'
        
        self.data = {
            'cl_env': 'FLASH_AS_3.0',
            'req_snd_id': key,
            'cl_login': self.ACCOUNT_LOGIN,
            'cl_vers': '1-30',
            'req_err_as_id3': 'yes',
            'req_voice': req_voice,
            'cl_app': self.APPLICATION_LOGIN,
            'prot_vers': '2',
            'cl_pwd': self.APPLICATION_PASSWORD,
            'req_asw_type': 'STREAM',
        }
        self.filename = "%s-%s.mp3" % (key, lang)
        self.data['req_text'] = '\\vct=100\\ \\spd=160\\ %s' % text.encode("utf-8")
        
    def run(self):
        """run will call acapela API and and produce audio"""
        #check if file exists
        if os.path.isfile(self.DIRECTORY + self.filename):
            return self.filename
        else:
            encdata = parse.urlencode(self.data)
            request.urlretrieve(self.SERVICE_URL, self.DIRECTORY + self.filename, data=encdata)
            return self.filename
        
        

def test_acapela():


    #Construct
    tts_acapela = Acapela(TTS_ENGINE, ACCOUNT_LOGIN, APPLICATION_LOGIN, APPLICATION_PASSWORD, SERVICE_URL, QUALITY, DIRECTORY)    

    #General settings for test
    gender = 'W'
    intonation = 'NORMAL'
    
    #Spanish
    lang = 'ES'
    text = u"Newfies-Dialer es una aplicación de transmisión de voz diseñado y construido para automatizar la entrega de las llamadas telefónicas interactivas a contactos, clientes y público en general."
    tts_acapela.prepare(text, lang, gender, intonation)
    output_filename = tts_acapela.run()
    print "Recorded TTS to %s" % output_filename
    sys.exit()
    
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
    #_main()
    test_acapela()
    

