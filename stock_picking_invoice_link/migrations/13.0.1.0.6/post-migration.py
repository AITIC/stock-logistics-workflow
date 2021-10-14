# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields
from odoo import SUPERUSER_ID


def update_invoice_picking(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})
    order = env['sale.order'].browse(4944)
    moves = env['stock.move']
    for line in order.order_line:
        moves += line.get_stock_moves_link_invoice()
        moves = moves.filtered(
            lambda m: not m.invoice_line_ids
        )
    invoice_line = env['account.move.line'].browse(44895)
    invoice_line.move_line_ids = moves
    invoice = env['account.move'].browse(17549)
    invoice._compute_picking_ids()


def migrate(cr, version):
    update_invoice_picking(cr)
