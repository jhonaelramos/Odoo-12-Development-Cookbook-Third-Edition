# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import date, datetime
import logging
#import qrcode

#try:
#    import cStringIO as StringIO
#except ImportError:
#    import StringIO
	
from uuid import uuid4
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class HrEmployee(models.Model):
    _inherit = 'hr.employee'