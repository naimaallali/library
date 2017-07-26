# -*- coding: utf-8 -*-
import odoo
from odoo import api, fields, models
from odoo.addons.website.models.website import slug
from odoo import exceptions


class ResUsers(models.Model):

    _inherit='res.users'

    # message=fields.Char('message',required=True)
    categ_validator_ids=fields.One2many('res.categories','user_id')
    categ_reader_ids=fields.One2many('res.categories','user_id')

class categories(models.Model):

    _name="res.categories"

    name=fields.Char('nom de catégorie',required=True)
    is_validator=fields.Boolean('valideur')
    is_reader=fields.Boolean('lecteur')
    user_id=fields.Many2one('res.users')