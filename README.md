Copyright: Arthur Milchior arthur@milchior.fr
License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
Feel free to contribute to this code on https://github.com/Arthur-Milchior/anki-latex-header-footer
Add-on number 1863928230

This add-on allow to change the latex prefix and suffix only once,
using the add-on manager.

Note that if you change prefix/suffix directly in a note type's option,
this modification will be lost the first time you use this add-on again.

#Rationale
After two years of using anki, mostly for mathematics, it never
occured that the latex configuration I use depends on the note type.

#Configuration
Use the add-on manager, and configure "prefix" and "suffix" to choose
for latex prefix. (Don't edit directly meta.json, the add-on would not
detect it)

#Internal
Version 1 used two global configurations "latexPre" and
"latexPost". If they are found, they are deleted when anki start, and
replaced by configurations. 