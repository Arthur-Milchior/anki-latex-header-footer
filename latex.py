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
from anki.hooks import addHook
from aqt import mw
from aqt.qt import *
from aqt.utils import  showWarning


userOption = mw.addonManager.getConfig(__name__)
def changeLaTeX(prefix=None, suffix = None):
    """Set prefix and postfix in argument to every models"""
    models = list(mw.col.models.models.values())
    for (var,name,modelName) in [
            (suffix,"suffix","latexPost"),
            (prefix,"prefix","latexPre")]:
        if var is not None:
            userOption[name]=var
            for model in models:
                model[modelName] = var
    mw.addonManager.writeConfig(__name__,userOption)
    mw.col.flush()

def updateV1toV2():
    for conf, option in [("latexPre","prefix"),("latexPost","suffix")]: 
        if conf in  mw.col.conf:
            userOption[option]=mw.col.conf[conf]
            del mw.col.conf[conf]
    mw.addonManager.writeConfig(__name__,userOption)

    
addHook("profileLoaded",updateV1toV2)

def onChange(config):
    if "prefix" not in config:
        showWarning("The prefix configuration is missing. It won't be changed in note's type. Please edit add-ons again and add prefix in it.")
        prefix=None
    else:
        prefix=config["prefix"]
    if "suffix" not in config:
        showWarning("The suffix configuration is missing. It won't be changed in note's type. Please edit add-ons again and add suffix in it.")
        suffix=None
    else:
        suffix=config["suffix"]
    changeLaTeX(prefix=prefix, suffix=suffix)
        
        
mw.addonManager.setConfigUpdatedAction(__name__,onChange)
