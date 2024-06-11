# Projeto de Engenharia de Software
## Seminarios III
### G6: Ferramentas para Democratização do Acesso à Justiça: Desenvolvimento de plataformas que ofereçam orientação jurídica básica e acessível, ajudando a população a entender seus direitos e como proceder em situações legais comuns.

### Integrantes
- [Kleberson]
- [Jules]
- [Vitor]
- [Vinicius Assis]


## Backend

### Instalação

Instale o Python e o pip3.
```bash
sudo apt-get install python3 python3-pip
```

Entre na pasta backend e execute o comando:

```bash
pip3 install -r requirements.txt
```

Export variáveis de ambiente
```bash
export OPENAI_API_KEY=
```

### Execução

```bash 
uvicorn app.app:app --host 0.0.0.0 --port 5555 --reload
```

mensagem: "INFO: Uvicorn running on http://0.0.0.0:5555 (Press CTRL+C to quit)"

## Frontend

### Instalação
```bash
npm install
```

### Execução
```bash
npm start
```

