# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Library Book Category"
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The name must be unique.')
    ]

    # Default Field
    name = fields.Char(required=True, unique=True)
    
