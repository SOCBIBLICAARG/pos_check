# -*- coding: utf-8 -*-
import logging
import time

from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _

class pos_order(osv.osv):
	_inherit = "pos.order"

	_columns = {
	        'received_third_check_ids': fields.one2many('account.check','pos_order_id', 'Third Checks', domain=[('type','=','third')], context={'default_type':'third','from_voucher':False}, required=False ),
		}


        def _check_payment_method_check(self, cr, uid, ids, context=None):
                account_check_obj = self.pool.get('account.check')
                statement_obj = self.pool.get('account.bank.statement.line')
		return_value = False
		check_amount = 0
		statement_amount = 0
                for obj in self.browse(cr,uid,ids,context=context):
			if not obj.statement_ids:
				return True
			for statement in statement_obj.browse(cr,uid,obj.statement_ids):
				if statement.journal_id.type == 'third':
					return_value = True
					statement_amount = statement.amount
					break
			for check in account_check_obj.browse(cr,uid,obj.received_third_check_ids):
				check_amount += check.amount
			if check_amount != statement_amount:
				return_value = False
                return return_value

        _constraints = [
                (_check_payment_method_check, 'Payment method does not support checks. Check the checks amount.', ['received_third_check_ids']),
                ]


pos_order()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
