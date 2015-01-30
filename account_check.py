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

        def _get_pos_voucher_id(self, cr, uid, context=None):
		voucher_id = self.pool.get('account.voucher').search(cr,uid,[('name','=','PAGO REFERENCIA CHEQUES POS')])
		if not voucher_id:
			return 1
		else:
	        	return voucher_id[0]
	
	_defaults = {
		'voucher_id': _get_pos_voucher_id,
		}


account_check()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
