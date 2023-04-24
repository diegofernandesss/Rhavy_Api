from flask_restful import reqparse, marshal, marshal_with, Resource
from model.pessoa import Pessoa, pessoa_fields
from model.mensagem import Mensagem, mensagem_fields
from helpers.database import db
from helpers.logger import logger
from model.endereco import Endereco

parser = reqparse.RequestParser()
parser.add_argument('nome', type=str, help='Problema na conversão do nome!')
parser.add_argument('email', type=str, help='Problema na conversão do email!')


class PessoaResource(Resource):
    @marshal_with(pessoa_fields)
    def get(self):
      pessoas = Pessoa.query.all()
      return (pessoas, 200)

    @marshal_with(pessoa_fields)  
    def post(self):
        args = parser.parse_args()
        nome = args['nome']
        email = args['email']
        
        pessoa = Pessoa(nome, email)

        db.session.add(pessoa)
        db.session.commit()

        return pessoa, 201

class PessoasResource(Resource):

  def get(self, pessoa_id):
    logger.info("Identificado de pessoa: " + pessoa_id)
    pessoa = Pessoa.query.filter_by(id=pessoa_id).first()

    if (pessoa is not None):
      return marshal(pessoa, pessoa_fields), 200
    else:
      mensagem = Mensagem('Pessoa não encontrada', 1)
      return marshal(mensagem, mensagem_fields), 404

  def put(self, pessoa_id):

    args = parser.parse_args()
    nome = args['nome']
    email = args['email']

    pessoa = Pessoa.query.get(pessoa_id)

    if pessoa is not None:
      pessoa.nome = nome
      pessoa.email = email

      db.session.add(pessoa)
      db.session.commit()

      return marshal(pessoa, pessoa_fields), 200
    else:
      mensagem = Mensagem('Pessoa não encontrada', 1)
      return marshal(mensagem, mensagem_fields), 404