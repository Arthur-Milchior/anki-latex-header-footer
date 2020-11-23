# Copyright: 2020 ijgnd
#            Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html


from aqt import mw
from aqt.models import Models
from aqt.qt import (
    QCheckBox,
    QTabWidget,
    QStackedWidget,
    QWidget,
    QVBoxLayout,
)
from aqt.utils import askUser
from aqt.gui_hooks import (
    models_advanced_will_show
)
from anki.hooks import wrap


def changeLaTeX(latexsvg, header, footer):
    for m in mw.col.models.all():
        m['latexsvg'] = latexsvg
        m['latexPre'] = header
        m['latexPost'] = footer
        mw.col.models.save(m)


def adjust_dialog(dialog):
    global apply_to_all
    apply_to_all = QCheckBox("Apply these settings to all models?")
    # TODO use something nicer
    for c in dialog.children():
        if isinstance(c, QTabWidget):
            for d in c.children():
                if isinstance(d, QStackedWidget):
                    for e in d.children():
                        if isinstance(e, QWidget):
                            for f in e.children():
                                if isinstance(f, QVBoxLayout):
                                    f.addWidget(apply_to_all)
models_advanced_will_show.append(adjust_dialog)


def onAdvanced(self):
    global apply_to_all
    if apply_to_all.isChecked():
        if askUser("Write these values for the header/footer to ALL notetypes?"):
            nt = self.current_notetype()
            changeLaTeX(nt["latexsvg"],
                        nt["latexPre"], 
                        nt["latexPost"])
Models.onAdvanced = wrap(Models.onAdvanced, onAdvanced)
