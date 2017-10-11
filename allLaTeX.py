"""Copyright: Arthur Milchior arthur@milchior.fr
License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
Feel free to contribute to this code on https://github.com/Arthur-Milchior/anki-latex-header-footer


Change the LaTeX of every note type.

In my usage, there is no reason to have distinct header, and its a
pain to edit every footer when I realize I do need a package. Hence this simple addon.
I'm too lazy to figure out how to have a multiline text editor, so here it is.

To use:

1) Open the main browser
2) Select "change LaTeX" 
3) Enter the LaTeX header
4) Enter the LaTeX footer

"""
import aqt
from aqt import mw
from aqt.qt import *
from aqt.utils import getText, tooltip, askUserDialog


def test(s):
    return s and isinstance(s, basestring)

def changeLaTeX(latexPre=None, latexPost = None):
    models = list(mw.col.models.models.values())
    if not test(latexPre):
        if  'latexPre' in mw.col.conf :
            latexPre = mw.col.conf['latexPre']
    if not test(latexPre):
        model = models[0]
        if 'latexPre' in model:
            latexPre = model['latexPre']

    (latexPre,ret)=getText("LaTeX header",default=latexPre)
    if test(latexPre) and ret:
        mw.col.conf['latexPre']= latexPre
        for model in models:
            model['latexPre'] = latexPre


    models = list(mw.col.models.models.values())
    if not test(latexPost):
        if  'latexPost' in mw.col.conf :
            latexPost = mw.col.conf['latexPost']
    if not test(latexPost):
        model = models[0]
        if 'latexPost' in model:
            latexPost = model['latexPost']

    (latexPost,ret_)=getText("LaTeX footer",default=latexPost)
    if test(latexPost) and ret_:
        mw.col.conf['latexPost']= latexPost
        for model in models:
            model['latexPost'] = latexPost

    if ret or ret_:
        mw.col.flush()

def launch():
    changeLaTeX ()
action = QAction(aqt.mw)
action.setText("Latex Head/foot")
mw.form.menuTools.addAction(action)
action.triggered.connect(launch)
