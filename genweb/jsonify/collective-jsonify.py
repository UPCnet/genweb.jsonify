# -*- coding: utf-8 -*-
from collective.jsonify.export import export_content as export_content_orig
from five import grok
from zope.interface import Interface


class ExportDexterity(grok.View):
    """Returns a list of paths of all items found by the catalog.
       This view return all elements from context called
    """
    grok.context(Interface)
    grok.name('export_dexterity')
    grok.require('cmf.ManagePortal')

    def render(self):
        if 'dir' not in self.request.form:
            raise ValueError("Mandatory parameter 'dir' was not specified")
        directory = self.request.form['dir']
        return export_content_orig(
            self.context,
            basedir=directory,  # export directory
            extra_skip_classname=['ATTopic']
        )
