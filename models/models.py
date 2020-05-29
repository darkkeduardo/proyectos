# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api


class proyecto(models.Model):
    _name = 'proyecto.persona'
    _description = 'proyecto.persona'
    
    nombre = fields.Char()
    apellido = fields.Char()
    
    
    image = fields.Binary()

    
    # @api.model
    # def create(self, values):
    #     """
    #         Create a new record for a model ModelName
    #         @param values: provides a data for new record
    
    #         @return: returns a id of new record
    #     """
    #     # raise ValidationError('hola mundo')
    #     result = super(ModelName, self).create(values)
    
    #     return result
    


    # image_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    # image_128 = fields.Image("Image 128",  max_width=128, max_height=128, store=True)
    fecha_nacimiento = fields.Date(
        string='field_name',
        default=fields.Date.context_today,
    )
        

    grado_id = fields.Many2one(
        string='grado',
        comodel_name='proyecto.grado',
        ondelete='restrict',
    )
    
    
    reparto_id = fields.Many2one(
        string='reparto',
        comodel_name='proyecto.reparto',
        ondelete='restrict',
    )

    
    persona_habilitacion_ids = fields.Many2many(
        string='field_name',
        comodel_name='proyecto.habilitacion',
        relation='habilitaciones_persona_rel',
        column1='persona_id',
        column2='habilitacion_id',
    )

           
    # persona_habilitacion_ids = fields.Many2many(
    #     string='field_name',
    #     comodel_name='proyecto.persona',
    #     relation='habilitacions_persona_rel',
    #     column1='habilitacion_id',
    #     column2='persona_id',
    # )
    
    

    # fieldocambiadoxboton = fields.Char(
    #     string='fieldocambiadoxboton',
    # )
    
    

class grado(models.Model):
    _name = 'proyecto.grado'
    _description = 'proyecto.grado'

    
    name = fields.Char(
        string='Reparto',
    )
    




class reparto(models.Model):
    _name = 'proyecto.reparto'
    _description = 'proyecto.reparto'

    
    name = fields.Char(
        string='Reparto',
    )
    

class habilitacion(models.Model):
    _name = 'proyecto.habilitacion'
    _description = 'proyecto.habilitacion'

    
    name = fields.Char(
        string='Habilitacion',
    )
#
#

    
    habilitacion_persona_ids = fields.Many2many(
        string='Habilitacion',
        comodel_name='proyecto.persona',
        relation='habilitaciones_persona_rel',
        column1='habilitacion_id',
        column2='persona_id',
    )
     

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100


#PARA EL BOTON BUSCAR, MOSTRAMOS TODOS LOS REPARTOS ID<15
    # def BUSCAR(self):
    #     domain = [('id','<','15')]
    #     record = self.env['prueba1.reparto'].search(domain)
    #     concatenar = " "
    #     record[0].name="COAVNA"
    #     for valor in record:
    #         concatenar = concatenar + " " + str(valor.name) + " "

    # def limpiar(self):       
    #     self.ascenso= ""



