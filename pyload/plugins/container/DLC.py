# -*- coding: utf-8 -*-
import re
import xml.dom.minidom
from builtins import _

import Cryptodome.Cipher.AES
from pyload.plugins.internal.container import Container
from pyload.plugins.utils import decode, encode


class DLC(Container):
    __name__ = "DLC"
    __type__ = "container"
    __version__ = "0.32"
    __status__ = "testing"

    __pattern__ = r"(.+\.dlc|[\w\+^_]+==[\w\+^_/]+==)$"
    __config__ = [
        ("activated", "bool", "Activated", True),
        ("use_premium", "bool", "Use premium account if available", True),
        (
            "folder_per_package",
            "Default;Yes;No",
            "Create folder for each package",
            "Default",
        ),
    ]

    __description__ = """DLC container decrypter plugin"""
    __license__ = "GPLv3"
    __authors__ = [
        ("RaNaN", "RaNaN@pyload.net"),
        ("spoob", "spoob@pyload.net"),
        ("mkaay", "mkaay@mkaay.de"),
        ("Schnusch", "Schnusch@users.noreply.github.com"),
        ("Walter Purcaro", "vuolter@gmail.com"),
        ("GammaC0de", "nitzo2001[AT]yahoo[DOT]com"),
    ]

    KEY = "cb99b5cbc24db398"
    IV = "9bc24cb995cb8db3"
    API_URL = "http://service.jdownloader.org/dlcrypt/service.php?srcType=dlc&destType=pylo&data={}"

    def decrypt(self, pyfile):
        fs_filename = encode(pyfile.url)
        with open(fs_filename) as dlc:
            data = dlc.read().strip()

        data += "=" * (-len(data) % 4)

        dlc_key = data[-88:]
        dlc_data = data[:-88].decode("base64")
        dlc_content = self.load(self.API_URL.format(dlc_key))

        try:
            rc = (
                re.search(r"<rc>(.+)</rc>", dlc_content, re.S)
                .group(1)
                .decode("base64")[:16]
            )

        except AttributeError:
            self.fail(_("Container is corrupted"))

        key = iv = Cryptodome.Cipher.AES.new(
            self.KEY, Cryptodome.Cipher.AES.MODE_CBC, self.IV
        ).decrypt(rc)

        self.data = (
            Cryptodome.Cipher.AES.new(key, Cryptodome.Cipher.AES.MODE_CBC, iv)
            .decrypt(dlc_data)
            .decode("base64")
        )

        self.packages = [
            (name or pyfile.name, links, name or pyfile.name)
            for name, links in self.get_packages()
        ]

    def get_packages(self):
        root = xml.dom.minidom.parseString(self.data).documentElement
        content = root.getElementsByTagName("content")[0]
        return self.parse_packages(content)

    def parse_packages(self, startNode):
        return [
            (decode(node.getAttribute("name")).decode("base64"), self.parse_links(node))
            for node in startNode.getElementsByTagName("package")
        ]

    def parse_links(self, startNode):
        return [
            node.getElementsByTagName("url")[0].firstChild.data.decode("base64")
            for node in startNode.getElementsByTagName("file")
        ]
