# -*- coding: utf-8 -*-
import logging
import time

from openerp import tools
from openerp.osv import fields, osv

class account_journal(osv.osv):
	_inherit = "account.journal"

	_columns = {
	        'check_in_pos': fields.boolean('Checks in Point of Sales'),
		}

account_journal()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
