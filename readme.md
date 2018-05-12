

Projeto está localizado em: https://github.com/xaxa/desafio_estante_virtual.git


Utilizado:
- Python 3.5.2
- Django 2.0.5
- djangorestframework 3.8.2



-------
Atletas
-------

**Listagem de atletas**

**GET** /atleta/

**Visualização de atleta**

**GET** /atleta/[id]/

**Cadastro de Atleta**

**POST** /atleta/

atributos:
- nome CharField[150] (obrigatório)

exemplo content: 

    {
        "nome": "Carlos"
    }

**Edição de Atleta**

**PATCH** /atleta/[id]/

atributos:
- nome CharField[150] (obrigatório)

exemplo content: 

    {
        "nome": "Carlos Alves"
    }

**Deletar Atleta**

**DELETE** /atleta/[id]/

----------
Competição
----------

**Listagem de competicões**

**GET** /competicao/

**Visualização de competição com resultado**

**GET** /competicao/[id]/

**Cadastro de competição**

**POST** /competicao/

atributos:
- nome CharField[150] (obrigatório)
- quantidade_chances SmallInt (obrigatório)
- finalizada Boolean (default False)
- criterio_vencedor CharField[5] (obrigatório)
    podendo ser "maior" ou "menor"


exemplo content:

    {
        "nome": "100m rasos",
        "quantidade_chances": 1,
        "finalizada": false,
        "criterio_vencedor": "menor"
    }

**Edição de competição**

**PATCH** /competicao/[id]/

atributos:
- nome CharField[150] (obrigatório)
- quantidade_chances SmallInt (obrigatório)
- finalizada Boolean (default False)
- criterio_vencedor CharField[5] (obrigatório)
    podendo ser "maior" ou "menor"


exemplo content:

    {
        "nome": "100m Rasos",
        "quantidade_chances": 1,
        "finalizada": false,
        "criterio_vencedor": "menor"
    }

**Finalizar competição**

**PATCH** /competicao/[id]/finalizar/

**Deletar competição**

**DELETE** /competicao/[id]/

---------
Resultado
---------

**Cadastro de resultado:**

**POST** /resultado/

atributos:

- competicao [id de competicao] (obrigatório)
- atleta  [id de atleta] (obrigatório)
- valor DecimalField[max_digits=6, decimal_places=3] (obrigatório)
- unidade CharField[1] (obrigatório)
    podendo ser "s" ou "m"

exemplo content:

    {
        "competicao": 2,
        "atleta": 1,
        "valor": 9.157,
        "unidade": "s"
    }
