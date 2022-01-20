#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) 2022  Rui Figueira
# This extension makes it easier to get things such as text to show up properly in Fritzing,
# by converting all objects to paths and saving as <DocumentName>_fritzing.svg
#
"""
This extension will pre-process a vector image by applying the operations:
'EditSelectAllInAllLayers' and 'ObjectToPath'
before calling the dialog File->Save As....
"""

import inkex
import os
from inkex.base import TempDirMixin
from inkex.command import inkscape_command
from inkex import load_svg
from inkex.command import write_svg

class FritzingExport(TempDirMixin, inkex.EffectExtension):
    def effect(self):
        tempDocument = load_svg(inkscape_command(
            self.svg,
            verbs=['EditSelectAllInAllLayers', 'EditUnlinkClone', 'ObjectToPath'],
        ))

        tempDocumentPath = os.path.splitext(self.document_path())[0] + "_fritzing.svg"
        if os.path.exists(tempDocumentPath):
            os.remove(tempDocumentPath)
        write_svg(tempDocument, tempDocumentPath)

if __name__ == '__main__':
    FritzingExport().run()

