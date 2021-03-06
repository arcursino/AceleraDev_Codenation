## Requisitos

Você precisará de Python 3 e pip. É altamente recomendado utilizar ambientes virtuais
com o virtualenv e o arquivo `requirements.txt` para instalar os pacotes dependências
do desafio:

```bash
$ pip3 install virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Windows

```bash
> pip3 install virtualenv
> virtualenv ..\venv -p python3
> ..\venv\Scripts\activate
> pip install -r requirements.txt
```

Para rodar o Streamlit:
```bash
> streamlit run *nome_do_arquivo*.py
```


Quando finalizado, você pode desativar o ambiente virtual do virtualenv com:

```bash
$ deactivate
```

Para quem usa Docker

```bash
$ make start
```
Para parar o Docker

```bash
$ docker ps
$ docker stop "container"
```