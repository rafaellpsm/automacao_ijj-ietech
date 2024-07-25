





# What does the code do? 
The Code is made for the website made available by the Joga Junto institute
- [Website Link](https://projetofinal.jogajuntoinstituto.org)

On the website, you can create an account, log in, add products, such as clothes, shoes, accessories and product filters.

The Automation Code enters the website, registers a fake account, using **Faker**, stores the values ​​in a variable and applies them to the login page, entering the *Products* Home page, it adds a product, filling out the form and searching using the search button.

## How to Use the code
### ***Steps***
1. [Install Python (LTS)](https://www.python.org/downloads/)
---

2. In the code terminal install:

-       pip install behave
-       pip install selenium
-       pip install faker
-       pip install requests
---

3. In the code terminal:
+   Run:
+       python -m venv venv
---

4. Open Windows PowerShell as administrator
- Run:
+     Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

+     Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
+ Enter the option (YES): [ Y ]
---
5. In the code terminal:
+   Run:
+       .\venv\Scripts\Activate.ps1
---
6. In the code terminal:
+   Run:
+       behave

###

# O que o código faz?
O Código é feito para o site disponibilizado pelo instituto Joga Junto
- [Link do Site](https://projetofinal.jogajuntoinstituto.org)

No site você pode criar uma conta, fazer login, adicionar produtos, como roupas, sapatos e acessórios; e filtrar produtos.

O Código de Automação entra no site, cadastra uma conta falsa, usando **Faker**, armazena os valores em uma variável e aplica na página de login, entrando na página inicial, *Produtos*, adiciona um produto, preenchendo o formulário e o pesquisando usando o botão de pesquisa.

## Como usar o Código
### ***Passos***
1. [Instalar o Python (LTS)](https://www.python.org/downloads/)
---

2. No terminal do código, instale:

-       pip install behave
-       pip install selenium
-       pip install faker
-       pip install requests
---

3. No terminal do código:
+   Execute:
+       python -m venv venv
---

4. Open Windows PowerShell as administrator
- Execute:
+     Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

+     Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
+ Digite a opção (SIM): [ S ]
---
5. No terminal do código:
+   Execute:
+       .\venv\Scripts\Activate.ps1
---
6. No terminal do código:
+   Execute:
+       behave