<h1>API de Clientes e Produtos</h1>

Esta API foi desenvolvida utilizando basicamente:
```
    - Python 3.6
    - Django 2.1.12
    - Django Rest Framework 3.9.1
    - PostgreSQL 11.5
    - Redis 5.0.6
```


Comandos importantes para inicialização (utilizando docker-compose):

- Roda as migrations 
```
docker-compose run web./manage.py migrate 
```

- Cria Super Usuário
```
docker-compose run web ./manage.py createsuperuser --email <email> --username <username>
```

Sobre a autenticação da API, a mesma é feita através de um simples Token. As chamadas só poderão ser realizadas por um usuário cadastrado e com o token gerado, do contrário não será autorizado. A chamada para retornar o token de um usuário específico é:

__POST__ /api/token-auth/

Parâmetros: 
```
{
    "username": <username>,
    "password": <senha>
}
```

O Token deve ser passado como um Header da chamada, seguindo o seguinte padrão (exemplo curl):
```
curl -H "Authorization: Token <Token do Usuário>" 
```

Todos os endpoints de listagem possuem paginação, então caso queira uma página especifica, é só inserir "?page=x" ao final da url. As informações de número da página e total de páginas estarão no início do json de retorno. 

<h2>Endpoints:</h2>

<h3>Clientes</h3>

- <h4>Listar</h4>
__GET__ /api/client/


- <h4>Cadastrar</h4>
__POST__ /api/client/

Parâmetros:
```
{
    "name": <Nome do cliente>,
	"email": <Email do cliente>
}
```


- <h4>Recuperar</h4>
__GET__ /api/client/{id}



- <h4>Atualizar</h4>
__PUT__ /api/client/{id}

Parâmetros:
```
{
    "name": <Nome do cliente>,
    "email": <Email do cliente>
}
```


- <h4>Remover</h4>
__DELETE__ /api/client/{id}


Se tiverem quaisquer dúvidas podem entrar em contato comigo.
