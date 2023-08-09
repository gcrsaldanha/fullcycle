# Notes

> Disclaimer: use `{"username": "admin", "password": "123456}` for authentication.

I wasn't able to make the custom JWT work yet (to use `email` instead of `username`).


# Running on Docker

```bash
docker-compose build
docker-compose up
```


# Running on host

```bash
pip install -r requirements.txt
DJANGO_SETTINGS_MODULE=stock_system.dev_settings ./runserver.sh
```

```bash
# django shell
DJANGO_SETTINGS_MODULE=stock_system.dev_settings python manage.py shell 
```


# Running tests

```bash
pip install -r requirements.txt
pytest
```


> Copiado de https://github.com/codeedu-tests/fullcycle-tutor-python-test/blob/main/README.md

# Teste para tutor/desenvolvedor Python

## Descrição

O projeto consiste na criação de um sistema de estoque de produtos

## Tecnologias e requisitos

* Back-end - Python (Pode ser usado qualquer lib ou framework)
* Docker para orquestar o ambiente da aplicação
* Banco de dados MySQL

## Contexto do sistema

Usuários poderão cadastrar produtos e dar entrada/saída no estoque. O cadastro de produtos serão categorizados.
Somente usuários autenticados poderão manipular o sistema.

## Design do sistema

### Back-end - Python

Você deve criar uma API Rest que terá os seguintes endpoints:

* POST /auth - Gera um token JWT para autenticação (usuário e senha deverão ser fixo: admin@user.com e 123456. Se a credential não for valida, a API deverá retornar um erro. O tempo de vida de um token será de 5 min).
```json
{
    "email": "admin@user.com",
    "password": "123456"
}
```
* POST /auth/refresh - Renova o token de acesso atual por mais 5 min, será gerado um novo token. Se o token de acesso não for válido, a API deverá retornar um erro.
```json
{
    "access_token": "xxxxx.yyyyy.zzzzz"
}
```
* GET /categories - Listagem de categorias
```json
[
    {
        "id": 1,
        "name": "Category 1"
    },
    {
        "id": 2,
        "name": "Category 2"
    }
]
```
* POST /categories - Criação de categorias (se o nome não for passado, a API deverá informar um erro)
```json
{
    "name": "Awesome category"
}
```
* POST /products - Criação de um produto (se o nome não for passado ou a categoria não existir, a API deverá informar um erro)
```json
{
    "name": "Foo product",
    "category_id": 123
}
```
* GET /products?page=1 - Listar produtos (A listagem de produtos terá paginação com no máximo 15 registros por página)
```json
{
    "data": [
       {
            "id": 1,
            "name": "Product 1",
            "quantity": 120,
            "category_id": 1,
            "category_name": "Categoria 1"
        },
        {
            "id": 1,
            "name": "Product 2",
            "quantity": 60,
            "category_id": 2,
            "category_name": "Categoria 2"
        }
    ],
    "meta": {
        "page": 1
    }
}
```
* GET /products/:id - Mostrar um produto (Se o produto não existir, a API deve retornar um erro)
```json
{
    "id": 1,
    "name": "Product 1",
    "quantity": 120,
    "category_id": 1,
    "category_name": "Categoria 1"
}
```
* POST /inventory/add - Dar entrada de mais quantidades de um produto no estoque
```json
{
    "product_id": 1,
    "quantity": 1,
}
```
* POST /inventory/sub - Dar saída de mais quantidades de um produto no estoque (Se o produto não existir ou se o estoque do produto menos a quantidade a ser retirada for < 0, a API deve retornar um erro)
```json
{
    "product_id": 2,
    "quantity": 1,
}
```

Sempre quando uma entrada ou saída for realizada, deve-se registrar isto e também atualizar o estoque do produto.

Crie dados falsos para categorias e produtos. Crie pelo menos 5 categorias e 150 produtos já previamente cadastrados no banco de dados.

Criar a aplicação usando testes automatizados será um grande diferencial.

## Docker

Crie as duas aplicações montando-as com Docker de forma que ao fazer `docker-compose up` seja possível testar todo o ambiente. 
O Docker deve levantar back-end, front-end, banco de dados.


## Vídeo-aula

Você deverá gravar 4 aulas, cada aula não deve passar de 25 min. Aulas deverão ser gravadas com a utilização de câmera.

Duas aulas deverão ser codificando alguma parte do sistema (de sua escolha) no ato da aula. 

Duas aulas deverão explicar alguma parte do sistema já criado, o objetivo da aula será focar na explicação da implementação e explicar os motivos desta implementação.

Explique com clareza o que será desenvolvido, monte sua didática para que um aluno consiga entende-la facilmente.

## Entrega

Entregue o projeto em um repositório Git remoto (as 4 aulas deverão estar presentes no repositório, renderize-as em baixa qualidade) e disponibilize o link.
