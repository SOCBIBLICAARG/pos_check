# -*- coding: utf-8 -*-
import logging
import time

from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _

class pos_session(osv.osv):
	_inherit = "pos.session"

	def wkf_action_closing_control(self, cr, uid, ids, context=None):
		for session_id in ids:
			order_ids = self.pool.get('pos.order').search(cr,uid,[('session_id','=',session_id)])
			for order_id in order_ids:
				check_ids = self.pool.get('account.check').search(cr,uid,[('pos_order_id','=',order_id),('state','=','draft')])
				for check_object in self.pool.get('account.check').browse(cr,uid,check_ids):
			                check_object.signal_workflow('draft_router')
	        return super(pos_session,self).wkf_action_closing_control(cr, uid, ids, context=context)

pos_session()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
