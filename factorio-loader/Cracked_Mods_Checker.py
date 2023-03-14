import urllib.request
from xml.dom import minidom

class CrackedMods:

    def get_mods(self):

        self.url = 'https://factorio-launcher-mods.storage.googleapis.com/'
        self.webFile = urllib.request.urlopen(self.url)
        self.data = self.webFile.read()
        self.dom = minidom.parseString(self.data)
        self.dom.normalize()

        self.elements = self.dom.getElementsByTagName("Contents")

        self.cracked_mods = []

        for node in self.elements:
            for child in node.childNodes:
                if child.tagName == 'Key':
                    value = str(child.firstChild.data.replace(',','.'))
                    self.cracked_mods.append(value)

        return self.cracked_mods
