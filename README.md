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
    "username": <Username>,
    "password": <Senha>
}
```

O Token deve ser passado como um Header da chamada, seguindo o seguinte padrão (exemplo curl):
```
curl -H "Authorization: Token <Token do Usuário>" 
```

Todos os endpoints de listagem possuem paginação, então caso queira uma página especifica, é só inserir "?page=x" ao final da url. As informações sobre outras páginas estarão no início do json de retorno. 

Algumas observações:

    - Tentei focar nos principais endpoints pedidos no teste, assim, para algumas operações não disponíveis em chamadas da API, como o cadastro de produtos (em decorrência também de necessitar de uma imagem para cadastro) e a criação de reviews, utilizei e recomendo a utilização do shell e do admin do Django:

    Comando Sheel 
    ```
    django-admin.py shell
    ```

    Link Admin
    ``` 
    /admin
    ```

    - Utilizei o Redis para cache e melhor performance da API em algumas chamadas, através de dois métodos diferentes. Para os clientes implementei um cache manual, que sempre é atualizado quando ocorrem alterações no banco de dados. Para os produtos utilizei o cache padrão do Django, que é feito por tempo (a configuração do mesmo pode ser feita no * *settings.py* *);

<h1>Endpoints:</h1>

<h2>Clientes</h2>

- <h3>Listar</h3>
__GET__ /api/client/


- <h3>Cadastrar</h3>
__POST__ /api/client/

Parâmetros:
```
{
    "name": <Nome do cliente>,
	"email": <Email do cliente>
}
```


- <h3>Detalhar</h3>
__GET__ /api/client/{id}


- <h3>Atualizar</h3>
__PUT__ /api/client/{id}

Parâmetros:
```
{
    "name": <Nome do cliente>,
    "email": <Email do cliente>
}
```


- <h3>Remover</h3>
__DELETE__ /api/client/{id}



<h2>Produtos Favoritos do Cliente</h2>

- <h3>Listar</h3>
__GET__ /api/client/{id}/product-list/


- <h3>Adicionar</h3>
__POST__ /api/client/{id}/product-list/

Parâmetros:
```
{
    "product_id": <Id do produto que deve ser adicionado à lista>
}
```


<h2>Produtos</h2>

- <h3>Listar</h3>
__GET__ /api/product/


- <h3>Detalhar</h3>
__GET__ /api/product/{id}

Se tiverem quaisquer dúvidas podem entrar em contato comigo.
