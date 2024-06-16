# Projeto de Engenharia de Software - JustAI
## Seminarios III
### G6: Ferramentas para Democratização do Acesso à Justiça: Desenvolvimento de plataformas que ofereçam orientação jurídica básica e acessível, ajudando a população a entender seus direitos e como proceder em situações legais comuns.

### Desenvolverdores do projeto.
- [Kleberson Lima]
- [Jules Eloisio]
- [Vitor Granato]
- [Vinicius Assis]


## Backend

### Instalação

Instale o Python e o pip3 use o comando a baixo:  
```bash
sudo apt-get install python3 python3-pip
```

Entre na pasta backend e execute o comando a baixo: 

```bash
pip3 install -r requirements.txt
```
### Conf. Variaveis de ambiente:
Export variáveis de ambiente MAC/LINUX: 
- No terminal, na pasta backend, execute o comando:
```bash
export OPENAI_API_KEY=

```

- Para exportar no windows, abra o pesquisar, escreva por "Variaveis de Ambiente" > Avnçado > Em baixo "Variaveis de ambiente" > Variaveis do sistema > Novo > Coloque o nome da variavel "OPENAI_API_KEY" > {Sua chave da OPENAI} em Valor da variavel, e cliquem em "OK" > "OK".
- Feito esse passo, no terminal, na pasta backend execute o comando:
```bash
set OPENAI_API_KEY= {Sua chave da OPENAI}

```

### Execução
- Na pasta backend, execute:
  
```bash 
uvicorn app.app:app --host 0.0.0.0 --port 5555 --reload
```
Mensagem de sucesso: "INFO: Uvicorn running on http://0.0.0.0:5555 (Press CTRL+C to quit)"

## Caso escolha rodar no Docker:  
Configurar arquivo .env com as variáveis de ambiente.

```bash
docker build -t justai .
docker run -d -p 5000:5000 --env-file .env --name justai-container justai
```

## Faça o teste: 
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

### Instalação das dependencias: 
- Entra na pasta Frontend e execute:
```bash
npm install
```

### Execução da aplicação: 
- Ainda na pasta Frontend, de o seguinte comanod para aplicação rodar.
  
```bash
npm start
```

## Para execução já com as dependencias instaladas, siga o passo:

- Rode o comando das variaveis de ambiente na pasta backend;
- Rode o comando de execução do backend;
- Rode na pasta Frontend, a Execução da aplicação.


