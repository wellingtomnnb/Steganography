# Steganography API
Uma API simples construída com FastAPI que utiliza técnicas de **esteganografia** para realizar transliterações e inserções de caracteres invisíveis em textos. Este projeto foi desenvolvido para demonstrar a funcionalidade de esteganografia em texto, que podem ser aplicadas em diferentes cenários, como:

<details>
<summary>Exemplos</summary>

* **Ofuscação de senhas:** Substituir caracteres por equivalentes visuais dificulta ataques de keylogging ou brute force.

* **Proteção de conteúdo em redes sociais:** Evitar que publicações com palavras sensíveis sejam removidas automaticamente por algoritmos de moderação.

* **Marcação de textos para direitos autorais:** Inserir caracteres invisíveis em textos ou documentos digitais para identificar plágios ou cópias.

* **Evitar indexação de textos por motores de busca:** Prevenir que textos sejam indexados corretamente ao modificar caracteres com transliteração ou caracteres invisíveis.

* **Esconder mensagens em textos:** Utilizar caracteres invisíveis para criar esteganografia textual, escondendo informações em mensagens aparentemente normais.

* **Manipulação de textos para sistemas de reconhecimento óptico (OCR):** Tornar textos digitalizados mais difíceis de serem lidos por OCR, alterando a composição dos caracteres.

* **Proteção contra scraping de dados:** Empresas que querem evitar que seus sites sejam extraídos por bots podem usar caracteres invisíveis ou transliteração para tornar o conteúdo menos acessível.

* **Ofuscação de conteúdo para aprendizado de máquinas:** Enganar modelos de machine learning que analisam texto ao utilizar caracteres invisíveis ou semelhantes.

* **Evitar edição automática de documentos:** Inserir caracteres invisíveis em documentos digitais para prevenir que editores automáticos ou softwares de revisão alterem trechos específicos.

</details>

## Estrutura do Projeto
```
/app 
  ├── init.py 
  ├── api.py 
  ├── main.py 
/data 
  └── lexico.csv 
Dockerfile 
docker-compose.yml
```


## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework para construção da API.
- **Pandas**: Para manipulação de dados.
- **Docker**: Para containerização da aplicação.

## Requisitos

- Python 3.9 ou superior
- Docker e Docker Compose

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/wellingtomnnb/Steganography
   cd Steganography
2. Crie e inicie os contêineres com Docker Compose:
   ```bash
    docker-compose up --build
## Uso
Após iniciar os contêineres, a API estará disponível em http://localhost:8000. Você pode usar ferramentas como Postman ou CURL para interagir com a API.

### Endpoints
*Prefixo: /v1/*
* **POST /steganography**
  * Descrição: Translitera um texto e inserir caracteres invisíveis.
  * Corpo da Requisição:
    ```bash
    { "text": "Texto para ser transliterado." }
  * Resposta:
    ```bash
    { "text": "Texto para ser transliterado." } 

## Contribuição
Sinta-se à vontade para enviar um pull request ou abrir uma issue se encontrar algum problema ou tiver sugestões para melhorias.
