# -*- coding: utf-8 -*
import jinja2
import json
import textwrap
import subprocess


def kreiraj_uplatnicu(podaci):
    """
    Prima podatke u JSON formatu i vraća sadržaj PDF datoteke
    """
    podaci = json.loads(podaci)

    def sredi_znakove(value):
        rjecnik = {u'š': u'scaron', u'Š': u'Scaron',
                   u'ž': u'zcaron', u'Ž': u'Zcaron',
                   u'đ': u'dcroat', u'Đ': u'Dcroat',
                   u'ć': u'cacute', u'Ć': u'Cacute',
                   u'č': u'ccaron', u'Č': u'Ccaron'}

        for k, v in rjecnik.iteritems():
            value = value.replace(k, u') show /%s glyphshow (' % v)

        return value

    jinja = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"))
    jinja.filters['sredi_znakove'] = sredi_znakove

    template = jinja.get_template("uplatnica.tpl")

    podaci['opis'] = map(sredi_znakove, textwrap.wrap(podaci['opis_placanja'], 28))
    podaci['textwrap'] = textwrap

    gs = subprocess.Popen(['gs', '-sOutputFile=-', '-sDEVICE=pdfwrite',
                           '-dPDFSETTINGS=/prepress', '-dHaveTrueTypes=true',
                           '-dEmbedAllFonts=true', '-dSubsetFonts=true', '-'],
                           stdout=subprocess.PIPE, stdin=subprocess.PIPE)

    izlaz, greska = gs.communicate(template.render(podaci).encode('utf-8'))
    return izlaz
