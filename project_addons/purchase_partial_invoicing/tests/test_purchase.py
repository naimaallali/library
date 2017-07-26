# -*- coding: utf-8 -*-
from openerp.tests.common import TransactionCase
from psycopg2 import IntegrityError

class TestResPartner(TransactionCase):

    def setUp(self):
        super(TestResPartner, self).setUp()
        self.user=self.env.ref('base.user_root')

    def test_10_create_partner(self):
        """
        [Administrateur]
        Je crée un partenaire avec Nom=ALLALI et prénom=Naima.
        Je vérifie que le nom est ALLALI et le prénom est ALLALI.
        """
        vals={
            'name':'Naima',
        }

        partner=self.env['res.partner'].sudo(self.user).create(vals)
        self.assertEquals('Allali',partner.name, "nom erroné")
        self.assertEquals(True,partner._check_ean_key(1),"Test échoué")

    def test_20_create_partner(self):
        vals=dict(name='Naima')
        with self.assertRaise(IntegrityError):
            self.env['res.partner'].sudo(self.user).create(vals)
