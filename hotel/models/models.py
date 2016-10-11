# -*- coding: utf-8 -*-

from openerp.osv import fields, osv


class reg_hotel(osv.osv):
     _name = 'reg.hotel'
     _rec_name='nombre'
     
     _columns={
        'nombre':fields.char('Nombre del cliente',size=50,required=True,help='Nombre del Cliente'),
        'cuantas habitaciones':fields.integer('cuantas habitaciones',size=10,required=True,help='Numero de habitaciones'),
        'Forma de pago':fields.char('Forma de pago ',size=10,required=True,help='debito credito efectivo'),
        'ci':fields.integer('Cedula del cliente',required=True,help='Nombre del Consejo Comunal'),
        'fecha':fields.datetime('Fecha',size=20,help='fecha de rejistro'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...')
        }
        
     _defaults={
        'active':True,
        'nombre':''
        }
     
