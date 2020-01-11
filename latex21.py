# Copyright: 2020 ijgnd
#            Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import aqt
from aqt.models import Models
from aqt.qt import *
from aqt.utils import restoreGeom, saveGeom, tooltip, askUser


def changeLaTeX(latexsvg, header, footer):
    for m in aqt.mw.col.models.all():
        m['latexsvg'] = latexsvg
        m['latexPre'] = header
        m['latexPost'] = footer
    aqt.mw.col.flush()


def onAdvanced(self):
    d = QDialog(self)
    frm = aqt.forms.modelopts.Ui_Dialog()
    frm.setupUi(d)
    ### mod start
    apply_to_all = QCheckBox("Apply these settings to all models?")
    frm.verticalLayout.addWidget(apply_to_all)   #  must be run after setupUi since everything is defined in setupUi ...
    ### mod end
    frm.latexsvg.setChecked(self.model.get("latexsvg", False))
    frm.latexHeader.setText(self.model['latexPre'])
    frm.latexFooter.setText(self.model['latexPost'])
    d.setWindowTitle(_("Options for %s") % self.model['name'])
    frm.buttonBox.helpRequested.connect(lambda: openHelp("latex"))
    restoreGeom(d, "modelopts")
    d.exec_()
    saveGeom(d, "modelopts")
    self.model['latexsvg'] = frm.latexsvg.isChecked()
    self.model['latexPre'] = str(frm.latexHeader.toPlainText())
    self.model['latexPost'] = str(frm.latexFooter.toPlainText())
    ### mod start
    if apply_to_all.isChecked():
        if askUser("Write these values for the header/footer to ALL notetypes?"):
            changeLaTeX(self.model['latexsvg'], self.model['latexPre'], self.model['latexPost'])
Models.onAdvanced = onAdvanced
