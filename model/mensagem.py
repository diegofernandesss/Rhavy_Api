from flask_restful import fields 

mensagem_fields = {
  'descricao': fields.String,
  'codigo': fields.String
}

class Mensagem():
  def __init__(self, descricao, codigo):
    self.descricao = descricao
    self.codigo = codigo