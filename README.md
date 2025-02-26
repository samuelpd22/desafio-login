# 📌 Documentação da Aplicação Fidelity

## 📚 1. Visão Geral
A **Fidelity** é um sistema de autenticação de usuários, oferecendo funcionalidades de **login, registro e recuperação de senha**. O backend foi desenvolvido em **Django** com **PostgreSQL**, enquanto o frontend utiliza **Bootstrap** e **JavaScript** para uma interface responsiva.

## 🛠️ 2. Tecnologias Utilizadas
### Backend
- Django
- Django ORM
- PostgreSQL

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

### Segurança
- CSRF Token (Django)
- Hash de senha (Django Auth)

## ⚙️ 3. Requisitos
Para executar a aplicação corretamente, é necessário ter o **Docker** instalado em seu computador.

- [Instalar Docker](https://www.docker.com/get-started)

## 🏰 4. Arquitetura da Aplicação
A aplicação segue o padrão **MVC (Model-View-Controller)**:

### 📂 Backend (Django)
- **Models**: Definem as tabelas do banco de dados.
- **Views**: Gerenciam a lógica da aplicação.
- **Templates**: Responsáveis pela renderização das páginas HTML.

### 🎨 Frontend
- **Login e Registro**: Páginas interativas com **Bootstrap**.
- **Validação de Formulários**: Implementada via **JavaScript**.

## 🔄 5. Fluxos do Sistema

### 🔑 5.1 Fluxo de Login
1. Usuário acessa a página de login.
2. Informa e-mail e senha.
3. O sistema valida os dados e autentica o usuário.
4. **Se houver erro**, exibe uma mensagem.
5. **Se correto**, redireciona para o menu principal.

### 📝 5.2 Fluxo de Registro
1. Usuário acessa a página de registro.
2. Preenche nome, e-mail e senha.
3. O sistema valida e cria a conta.
4. **Se sucesso**, redireciona para a tela de login.
5. **Se erro**, exibe mensagem.

## 🖥️ 6. Telas do Sistema

### 🏠 6.1 Tela de Login
- Campo de **e-mail** e **senha**.
- Botão para **exibir senha**.
- Link para **"Esqueceu a senha?"** (Função não implementada).

### 🆕 6.2 Tela de Registro
- Formulário para cadastro de novo usuário.
- Botão de **confirmação**.



## 🛠️ 7. Como Executar a Aplicação no Docker

### 📥 7.1 Clonando o Repositório
```sh
git clone https://github.com/samuelpd22/desafio-login.git
cd desafio-login
```

### 🏗️ 7.2 Construindo e Subindo os Containers
```sh
docker-compose up --build
```
Isso iniciará dois containers:
- `db`: Servidor PostgreSQL.
- `api`: Aplicação Django.

### 🌍 7.3 Acessando a Aplicação
Acesse no navegador: [http://localhost:8000](http://localhost:8000)

Para verificar os containers em execução:
```sh
docker ps
```

Caso precise acessar o banco de dados manualmente:
```sh
docker exec -it postgres_container psql -U myuser -d mydatabase
```

Se precisar rodar migrações manualmente:
```sh
docker exec -it django_api python manage.py migrate
```

## 🗄️ 8. Banco de Dados

### 📑 Tabelas Principais:
#### **Usuários**
| Campo           | Tipo        |
|---------------|------------|
| id           | UUID (PK)   |
| nome         | String      |
| email        | String      |
| senha_hash   | String      |
| data_criacao | Timestamp   |

## 📌 9. Considerações Finais
Essa documentação fornece uma visão geral sobre a arquitetura e funcionamento da aplicação **Fidelity**. Podemos expandi-la com **diagramas** e **detalhes técnicos adicionais** conforme necessário. 🚀

