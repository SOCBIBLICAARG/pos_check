# -*- coding: utf-8 -*-
import logging
import time

from openerp import tools
from openerp.osv import fields, osv

class account_check(osv.osv):
	_inherit = "account.check"

	_columns = {
	        'pos_order_id': fields.many2one('pos.order','POS Order'),
	        'voucher_id': fields.many2one('account.voucher', 'Voucher', readonly=True, required=False),
		}

account_check()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
