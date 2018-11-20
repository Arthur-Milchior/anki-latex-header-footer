# Change the latex prefix and suffix of all note types

## Warning 
If you change prefix/suffix directly in a note type's option, this
modification will be lost the first time you use this add-on again.

## Rationale
After two years of using anki, mostly for mathematics, it never
occured that the latex configuration I use depends on the note type.

## Configuration
Use the add-on manager, select this add-on, and "config". Change the
value of configure "prefix" and "suffix" to choose for latex
prefix. (Don't edit directly meta.json, the add-on would not detect
it)

## Internal
Version 1 used two global configurations "latexPre" and
"latexPost". If they are found, they are deleted when anki start, and
replaced by configurations. 

## Advice
Using add-on [112201952](https://ankiweb.net/shared/info/112201952)
you can have new-line in your configuration. It would be more readable !

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   |Arthur Milchior <arthur@milchior.fr>
Based on    |Anki code by Damien Elmes <anki@ichi2.net>
License     |GNU AGPL, version 3 or later; http|//www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-latex-header-footer
Addon number| [1863928230](https://ankiweb.net/shared/info/1863928230)
