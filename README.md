# Previdencia

## Overview

**Este é um repositorio de um sistema de previdencia, este projeto utiliza a documentação openAPI**

    Ex: http://localhost:8000/docs

## Pré-requisitos
- Python 3.10 
- (Opcional) pipenv

## Instruções para executar o projeto
**Para executar esse projeto é necessário a instalação de algumas dependências:**

### (Opção 1) Intalar as dependências pelo requirements.txt
- Caso não tenha o pip seguir tutorial do link abaixo
    [pip doc](https://pip.pypa.io/en/stable/installation/)

**Utilizar o comando abaixo:**
        
        pip install -r requirements.txt

**Após instalação o projeto poderá ser executado com o comando abaixo (terminal):**

        uvicorn main:app

### (Opção 2) Para executar o script utilizando um virtualenv primeiro deve-se o pipenv


**Para instalar o pipenv executar o comando abaixo:**
        
        pip install pipenv

**Para criar seu virtualenv execute:**
        
        pipenv --python 3.10.6

**Para entrar em seu virtualenv execute:**
        
        pipenv shell

**Para executar a instalação das dependências que estão no Pipfile pode-se usar o comando**

        pipenv install --dev

**E para executar o projeto basta usar o comando:**

        uvicorn main:app

**(Observação) Para sair do virtualenv basta usar o comando:**

        exit

### (Opção 3) Para executar o script utilizando docker:


**Fazer build do Dockerfile:**
        
        docker build -t "previdencia:Dockerfile" . 

**Executar a imagem docker criada:**

        docker run previdencia:Dockerfile
