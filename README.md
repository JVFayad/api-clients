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
```
__POST__ /api/token-auth/

Parâmetros: 
    - username
    - senha
```

Todos os endpoints de listagem possuem paginação, então caso queira uma página especifica, é só inserir "?page=x" ao final da url. As informações de número da página e total de páginas estarão no início do json de retorno. 

Utilizei o Postman para testes, mas coloquei as chamadas com curl caso queiram utilizar (curl realizado no Windows).

<h2>Endpoints:</h2>

<h3>Comentar</h3>
<h5>
curl http://localhost:8000/api/comments/ --user joao.teste@gmail.com:senha -H "Content-type:application/json" -X POST -d @json.txt
</h5>

Conteúdo do arquivo json.txt (os comentários foram colocados para matéria de explicação dos parâmetros, não estão no arquivo original):
```
{
   "content":"Conteúdo",  // Conteúdo do comentário
   "type":"texto",        // Tipo do comentário
   "highlight_value":5,   // Valor de destaque (se não houver compra de destaque, passar 0)
   "post_id":1            // ID da postagem relacionada
}
```

<h3>Listar comentarios de um Usuário</h3>
<h5>
curl --user email:password -X GET http://localhost:8000/api/comments/user/{user_id}
</h5>

<h3>Listar comentários de uma Postagem</h3>
<h5>
curl --user email:password -X GET http://localhost:8000/api/comments/post/{post_id}
</h5>

<h3>Remover comentário</h3>
<h5>
curl --user email:password -X DELETE http://localhost:8000/api/comments/{comment_id}
</h5>

<h3>Listar notificações de um usuário</h3>
<h5>
curl --user email:password -X GET http://localhost:8000/api/notifications/user/{user_id}
</h5>

Se tiverem quaisquer dúvidas podem entrar em contato comigo.
