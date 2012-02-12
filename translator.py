#/usr/bin/env python
enabledIcon = '\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\x00\x00\x20\x00\x00\x00\x20\x08\x06\x00\x00\x00\x73\x7a\x7a\xf4\x00\x00\x00\x01\x73\x52\x47\x42\x00\xae\xce\x1c\xe9\x00\x00\x00\x06\x62\x4b\x47\x44\x00\xff\x00\xff\x00\xff\xa0\xbd\xa7\x93\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7\x6f\xa8\x64\x00\x00\x00\x07\x74\x49\x4d\x45\x07\xdb\x01\x0c\x02\x00\x17\x43\xcc\x81\xed\x00\x00\x00\x6c\x49\x44\x41\x54\x58\xc3\xed\x97\xc1\x0e\xc0\x20\x08\x43\x2d\xd9\xff\xff\x72\xbd\x1b\x74\x19\x11\x59\x62\x39\x7a\xb0\x4f\xd2\x06\x04\xc9\x56\x59\xd6\x8a\x4b\x00\xe5\x00\x8f\x77\x08\x20\xcd\x99\x24\xb1\xec\x40\xa6\xb8\x77\xbf\x9d\x14\xf7\x74\x64\xc2\x7f\x01\x8c\x0e\x3d\x91\x04\x7b\x8b\x49\x76\x0c\x11\x19\x46\xab\xb4\x7c\x7d\x80\x4c\x28\x00\x01\x08\x40\x00\x02\x10\x40\x08\x60\x36\x72\x23\xbb\x44\xb8\x03\xbb\x16\x17\x5c\xff\x3b\xee\xb9\x17\x2a\x31\x76\x79\xd5\x35\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82'

disabledIcon = '\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\x00\x00\x20\x00\x00\x00\x20\x08\x06\x00\x00\x00\x73\x7a\x7a\xf4\x00\x00\x00\x01\x73\x52\x47\x42\x00\xae\xce\x1c\xe9\x00\x00\x00\x06\x62\x4b\x47\x44\x00\xff\x00\xff\x00\xff\xa0\xbd\xa7\x93\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7\x6f\xa8\x64\x00\x00\x00\x07\x74\x49\x4d\x45\x07\xdb\x01\x0c\x02\x00\x20\xfb\x71\x24\xe2\x00\x00\x00\xdc\x49\x44\x41\x54\x58\xc3\xc5\x96\xbd\x16\xc2\x30\x08\x46\x3f\x72\xba\xd4\x59\xb7\xfa\xfe\x0f\xa6\x5b\x9d\xed\x88\x53\x3d\xb5\xf9\x05\x03\x61\xca\x69\x86\x7b\x0b\x21\x81\x98\x19\xde\xf1\xa2\xcb\x63\x5f\x87\x91\x70\x77\x81\x33\xdc\x55\x20\x05\x77\x13\xc8\xc1\x01\x60\x4a\x7d\x24\xa2\x6e\x27\x73\xc5\xfc\xcc\xed\x5d\xf9\x7d\x0f\x23\xe1\x51\x09\xbc\xe0\x37\x6c\x8b\xe9\x19\x68\x85\x9b\x08\x48\xe0\xdd\x05\xa4\xf0\x48\x80\x99\xc9\x03\x7e\xe4\x44\x19\xd0\x48\x68\xe1\x00\x40\x9a\xc7\xe8\xd8\x2d\x2d\xad\x56\x8a\x60\xdd\xe7\xb5\x98\x7a\x83\x25\x70\x55\x06\x4a\xf7\xba\x14\x2e\x16\xa8\xc1\x73\xad\xd6\xa5\x04\x25\xb8\x06\x2c\xca\x80\x15\xbc\x49\xc0\x12\x5e\x15\xb0\x86\x17\x05\x3c\xe0\x59\x81\x12\x5c\xda\x66\x62\x01\x4f\x78\x24\xe0\x0d\xff\x11\x18\x01\xff\x0a\x8c\x82\x03\x00\xad\x98\x55\xf0\xd4\x00\xab\x99\x25\x82\xf6\xcf\xff\x99\x9e\xaa\x6f\x41\x6b\xda\x7b\x48\x04\xef\x9a\x9f\xe3\x03\xe0\xea\x83\xef\x9b\x29\x8c\x86\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82'


import json
import sys
import urllib
import urllib2
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtTest import *


class Translator(QWidget):
    LANGPAIR = 'en|zh-TW'
    TRANSLATE_DELAY = 300
    TRANSLATE_TIMEOUT = 1  # second
    DISPLAY_TIME_LENGTH = 2000
    URL = 'http://ajax.googleapis.com/ajax/services/language/translate'

    def __init__(self, parent=None):
        super(Translator, self).__init__(parent)

        self.enabled = False
        
        self.clipboard = QApplication.clipboard()
        if not self.clipboard.supportsSelection():
            QMessageBox.critical(self, 'Aborted',
                                 'Clipboard Selection is not supported')
            sys.exit(1)
            
        self.clipboard.selectionChanged.connect(self.translate_)
        
        if not QSystemTrayIcon.isSystemTrayAvailable():
            QMessageBox.critical(self, 'Aborted',
                                 'SystemTray is not available')
            sys.exit(1)

        self.initialResource()
        self.createTrayIcon()
        
        self.label = QLabel()
        # truncate window decorator and border
        self.label.setWindowFlags(Qt.SplashScreen)

        self.timer = QTimer()  # for closing label automatically
        self.timer.setSingleShot(True)
        self.timer.setInterval(self.DISPLAY_TIME_LENGTH)
        self.timer.timeout.connect(self.label.close)
        
    def translate_(self):
        if not self.enabled:
            return

        # process only if the cursor hasn't moved away after a while
        self.prev_pos = QCursor.pos()
        QTest.qSleep(self.TRANSLATE_DELAY)
        point = QCursor.pos() - self.prev_pos
        if point.manhattanLength() > 10:
            return

        self.timer.stop()
        self.label.close()
        
        text = self.parseSelection()
        if not text:
            return

        self.clipboard.blockSignals(True)
        
        translation = self.translateText(text)
        print translation

        if translation == text:  # translation failed
            translation = 'WTF!?'
        self.displayLabel(translation)
        
        self.clipboard.blockSignals(False)

    def parseSelection(self):
        text = ''
        try:
            text = str(self.clipboard.text(QClipboard.Selection).trimmed())
        except UnicodeEncodeError:
            pass
        return text
        
    def translateText(self, text):
        params = urllib.urlencode({'v': '1.0', 'q': text,
                                   'langpair': self.LANGPAIR})
        try:
            content = urllib2.urlopen(self.URL, params,
                                      self.TRANSLATE_TIMEOUT).read()
            result = json.loads(content)
        except (IOError, TypeError):
            return 'Timeout...'

        if result['responseStatus'] == 200:
            return result['responseData']['translatedText']

    def displayLabel(self, text):
        self.label.setText(text)
        # offset the label a little bit
        self.label.move(QCursor.pos() + QPoint(2, 2))
        QApplication.processEvents()  # for redrawing label text immediately
        self.label.show()
        self.timer.start()

    def toggleEnabled(self, reason):
        if reason == QSystemTrayIcon.Context:
            return

        self.enabled = not self.enabled
        if self.enabled:
            self.trayIcon.setIcon(self.enabledIcon)
        else:
            self.trayIcon.setIcon(self.disabledIcon)
            
        toolTip = 'Click to %s translation' % \
                  ('enable', 'disable')[self.enabled]
        self.trayIcon.setToolTip(toolTip)
        
    def createTrayIcon(self):
        quitAction = QAction(self.tr('&Quit'), self)
        quitAction.triggered.connect(qApp.quit)
        menu = QMenu(self)
        menu.addAction(quitAction)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(menu)
        self.trayIcon.activated.connect(self.toggleEnabled)
        self.toggleEnabled(QSystemTrayIcon.Trigger)
        self.trayIcon.show()

    def initialResource(self):
        pixmap = QPixmap()
        pixmap.loadFromData(enabledIcon)
        self.enabledIcon = QIcon(pixmap)
        pixmap = QPixmap()
        pixmap.loadFromData(disabledIcon)
        self.disabledIcon = QIcon(pixmap)


def main():
    app = QApplication(sys.argv)
    translator = Translator()
    return app.exec_()


if __name__ == '__main__':
    main()

