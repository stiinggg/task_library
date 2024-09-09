# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InheritLibraryBook(models.Model):
    _inherit = "library.book"

    # Relational Fields
    author_id = fields.Many2one('res.partner', required=True)
    category_id = fields.Many2one('library.book.category')
    