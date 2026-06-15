# 🍔 API REST - Sistema Delivery

API REST desenvolvida com Django REST Framework para gerenciamento de usuários, estabelecimentos, produtos, pedidos e endereços em um sistema de delivery.

## 🚀 Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- Swagger (drf-yasg)

---

## 📦 Instalação

Clone o projeto:

```bash
git clone <url-do-repositorio>
```

Acesse a pasta:

```bash
cd API-RestFull---Sistema-Delivery-UC-SD--main
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

---

## 🌐 Endereço da API

Servidor local:

```http
http://127.0.0.1:8000/
```

---

# 📚 Documentação

## Swagger

```http
http://127.0.0.1:8000/swagger/
```

## ReDoc

```http
http://127.0.0.1:8000/redoc/
```

---

# 🔗 Endpoints

## Usuários

| Método | Endpoint |
|----------|----------|
| GET | /users/ |
| POST | /users/ |
| GET | /users/{id}/ |
| PUT | /users/{id}/ |
| DELETE | /users/{id}/ |

---

## Estabelecimentos

| Método | Endpoint |
|----------|----------|
| GET | /estabelecimentos/ |
| POST | /estabelecimentos/ |
| GET | /estabelecimentos/{id}/ |
| PUT | /estabelecimentos/{id}/ |
| DELETE | /estabelecimentos/{id}/ |

---

## Produtos

| Método | Endpoint |
|----------|----------|
| GET | /produtos/ |
| POST | /produtos/ |
| GET | /produtos/{id}/ |
| PUT | /produtos/{id}/ |
| DELETE | /produtos/{id}/ |

---

## Pedidos

| Método | Endpoint |
|----------|----------|
| GET | /pedidos/ |
| POST | /pedidos/ |
| GET | /pedidos/{id}/ |
| PUT | /pedidos/{id}/ |
| DELETE | /pedidos/{id}/ |

---

## Endereços

| Método | Endpoint |
|----------|----------|
| GET | /enderecos/ |
| POST | /enderecos/ |
| GET | /enderecos/{id}/ |
| PUT | /enderecos/{id}/ |
| DELETE | /enderecos/{id}/ |

---

## Listas

| Método | Endpoint |
|----------|----------|
| GET | /listas/ |
| POST | /listas/ |
| GET | /listas/{id}/ |
| PUT | /listas/{id}/ |
| DELETE | /listas/{id}/ |

---

# 🔍 Consultas Específicas

## Listas por Usuário

```http
GET /users/{id}/listas/
```

## Listas por Estabelecimento

```http
GET /estabelecimentos/{id}/listas/
```

## Listas por Produto

```http
GET /produtos/{id}/listas/
```

## Listas por Pedido

```http
GET /pedidos/{id}/listas/
```

## Listas por Endereço

```http
GET /enderecos/{id}/listas/
```

---

# 📊 Estrutura do Projeto

```text
delivery/
├── models.py
├── serializers.py
├── views.py
├── migrations/

config/
├── settings.py
├── urls.py