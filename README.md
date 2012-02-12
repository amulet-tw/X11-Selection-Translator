## X11 Selection Translator

Select the text and show the result translated by Google immediately.

<img src="http://img132.imageshack.us/img132/3637/samplegx.png" />


Usage:
`python translator.py &`

Modify Translator.LANGPAIR to fit your need: <a href="http://code.google.com/intl/en/apis/language/translate/v1/getting_started.html#LangNameArray">LangNameArray</a>


It works like this:

QClipboard.selectionChanged.connect(showTranslation)

then shows a QLabel under the cursor.


### Tested dependencies:

* Python 2.7.1

* PyQt   4.8.2

