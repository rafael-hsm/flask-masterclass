# flask-masterclass
Anotações do curso Flask Masterclass - Desenvolvendo aplicações web com python
### Dicas
Comando para instalar a opção de rodar o HTTP diretamente no terminal.
```
sudo apt-get install httpie
```

## Ambiente
Instalar a extensão Test UI
Better Jinja
Bootstrap 5

## Bibliotecas
Serão informadas no arquivo requirements.in

## Boostrap com flask
Instalando a biblioteca mais recomendada
```python
pip install 
```

## SQLAlchemy
Criar variável db onde chamamos o SQLAlchemy
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlcyemy(app)
```
Comando para criar o banco de dados
```
flask shell
from nome_arquivo_app import db
```
No console digite:
```
db.create_all()
```

**Para adicionar um usuario pelo terminal flask (password passado de forma simples):**
```
from nome_arquivo_com_app import db, User
user = User()
user.name = "Rafael Meireles"
user.email = "rafa@ey.com.br"
user.password = rafa12345
db.session.add(user)
db.session.commit()
```

## Login e Autenticação
Lembre de inicializar a classe e aplicar ao app, importar o login_required também.
UserMixin é um compilado de configurações padrões que o flask exige, é só para agilizar o processo.

```python
from flask_login import LoginManager, UserMixin, login_required


login_manager = LoginManager()
login_manager.init_app(app)
```

Para criar um hash no password e para checar use o seguinte
```python
from werkzeug.security import generate_password_hash, check_password_hash
user.password = generate_password_hash(request.form['password'])
```