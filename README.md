# Sistema de recomendação de jogos STEAM com Inteligencia Artificial


## Descrição

Sempre que vamos a um centro comercial para comprar um novo par de sapatos ou roupas, encontramos uma pessoa dedicada que nos ajuda com o tipo de produtos que devemos comprar de acordo com as nossas preferências e simplifica o nosso trabalho. Em palavras simples, ele é um sistema de recomendação. Mas neste mundo moderno tudo está online, e há tanto conteúdo na internet, há milhões de vídeos no Youtube e milhões de produtos na Amazon, o que dificulta a escolha do usuário. Aí vem o sistema de recomendação que simplifica a vida do usuário ao recomendar o próximo vídeo para assistir ou um produto similar para comprar.

Um sistema de recomendação é um código inteligente o suficiente para entender as preferências do usuário e recomendar coisas de acordo com seu interesse, o objetivo é aumentar a lucratividade. Por exemplo, Youtube e NetFlix querem que você passe mais tempo em sua plataforma, por isso, recomendam os vídeos com base nas preferências do usuário. A Amazon quer que você compre produtos em seu site para que eles possam ter mais lucro.

## Tipos de sistema de recomendação

1. **Baseado em popularidade:** Recomendar os principais produtos de seu site para todos os usuários. Este método não levará em consideração o interesse do usuário. Por exemplo, a seção Tendências no Youtube, os 250 melhores filmes do IMDB.

2. **Baseado em conteúdo:** Isso se baseia na semelhança entre os produtos. Por exemplo, se um usuário assistiu a um filme e gostou, ele poderá gostar de assistir a filmes semelhantes no futuro. Isso pode ser baseado no gênero, ator, atriz ou diretor.

3. **Filtragem colaborativa:** Isso se baseia na semelhança dos usuários. Por exemplo, se as pessoas A e B assistiram e gostaram do filme M, a seguir, se a pessoa A assistir ao filme Z e gostar, podemos recomendar o filme Z para a pessoa B, já que A e B são usuários semelhantes.


## Funcionalidades

1. **Recomendação Personalizada de Jogos:** Este sistema oferece recomendações personalizadas de jogos da plataforma Steam, utilizando técnicas avançadas de aprendizado de máquina (ML) e filtragem colaborativa. Os usuários podem inserir o nome de um jogo específico ou explorar opções disponíveis em um menu para receber sugestões adaptadas às suas preferências individuais.

2. **Análise de Preferências do Usuário:** O sistema analisa as preferências do usuário, bem como as características dos jogos, para identificar padrões e oferecer recomendações precisas e relevantes. Isso permite uma experiência de recomendação mais refinada e personalizada para cada usuário.

3. **Cosine Similarity:** Esse projeto usa o algoritimo de **Similaridade Sosseno** para calcular a similaridade entre os perfis de jogos e as preferências do usuário. A similaridade cosseno é uma medida que avalia a proximidade entre dois vetores, neste caso, os vetores representativos dos jogos e as preferências do usuário.

## Instalação PIP

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/RenatoDev4/recommendation_system.git

2. **Instale as dependências:**

   ```bash
   pip install pipenv
   pipenv install

3. **Configuração do Modelo de Linguagem da OpenAI:** Obtenha as credenciais ou chave de API da OpenAI e configure-as e configure-as como uma váriavel de ambiente.

4. **Execute o projeto:**

   ```bash
   streamlit run src/steam_recommendations.py



## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para discutir novas funcionalidades, relatar bugs ou enviar um pull request.
