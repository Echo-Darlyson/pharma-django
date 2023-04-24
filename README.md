<h1>About</h1>
<p>Projeto desenvolvido com o framework de Python, Django. O projeto é um site de farmácia que lista e cadastro os produtos, retornando e cadastrando nome, tarja, preço e se há necessidade de receita</p>

<h2>Como Executar o Projeto?</h2>

<ol>
  <li>Criar um ambiente virtual: <code>virtualenv venv</code></li>
  <li>Ativar ambiente virtual: <code>venv\Scripts\activate</code></li>
  <li>Instalar dependências: <code>pip install -r requirements.txt</code></li>
  <li>Dentro da pasta pharmadjango, rodar o comando: <code>python manage.py runserver</code></li>
  <li>Rodar o comando: <code>python manage.py migrate</code></li>
  <li>Acessar o endereço (listar os produtos): <b>localhost:8000/remedios/listamedicamentos</b></li>
  <li>Acessar o endereço (cadastrar os produtos): <b>localhost:8000/remedios/cadastramedicamentos</b></li>
</ol>
  
<h2>Como Acessar o Painel Administrativo?</h2>

<ol>
  <li>Rodar o seguinte comando: <code>python manage.py createsuperuser</code></li>
  <li>Cadastrar seu usuário e senha</li>
  <li>Acessar o endereço: <b>localhost:8080/admin</b> e logar com seu usuário e senha recém criados</li>
</ol>

<h2>Integrantes da Equipe</h2>
<ul>
  <li>Darlyson Rangel</li>
  <li>Davi Almeida</li>
  <li>Kalil Ribeiro</li>
  <li>Leonardo Carvalho</li>
  <li>Jean França</li>
</ul>
