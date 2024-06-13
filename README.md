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

## Rodar backend no docker 

Configurar arquivo .env com as variáveis de ambiente.
    
```bash
docker build -t justai .
docker run -d -p 5000:5000 --env-file .env --name justai-container justai
```
## Teste
```bash
POST http://0.0.0.0:5000/just-ai/legal-advice
{
	"messages": [
		{
			"role": "user",
			"content": "Olá, bom dia, como você funciona?"
		},
			{
			"role": "system",
			"content": "Bom dia! Eu sou uma inteligência artificial da empresa JustAI, disponível para auxiliar com dúvidas jurídicas. Posso ajudar a esclarecer questões sobre diversos temas do direito e orientar sobre os próximos passos a serem tomados. Para começar, poderia me informar seu nome, idade e cidade? Assim, posso personalizar melhor a orientação para sua situação."
		},
		{
			"role": "user",
			"content": "LEGAL, sou vinicius tenho 22 anos e moro em poços de caldas"
		}
	]
}
```

## Frontend

### Instalação
```bash
npm install
```

### Execução
```bash
npm start
```

