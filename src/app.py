import pickle
from typing import List

import numpy as np
import streamlit as st


def steam_recommend() -> None:
    """
    Function for generating a recommendation system for Steam games.
    It sets up the page configuration and sidebar information, as well as
    loading and processing the necessary data for recommendations and displaying
    the most highly rated games on the Steam platform.

    Returns:
    --------
    None
    """

    st.set_page_config(
        page_title="Sistema de Recomendação - STEAM", page_icon="🎮", layout="wide"
    )

    st.sidebar.image("./img/steam.jpg")
    st.sidebar.header("Sobre o desenvolvedor")
    nome = "Renato Moraes"
    titulo = "Cientista de Dados"
    linkedin_url = "https://linkedin.com/in/renato-moraes-11b546272"
    github_url = "https://github.com/RenatoDev4"
    github_projeto = "https://github.com/RenatoDev4/recommendation_system"

    st.sidebar.text(f"Nome: {nome}")
    st.sidebar.text(f"Cargo: {titulo}")
    st.sidebar.header("Redes sociais")
    st.sidebar.markdown(
        f"**[LinkedIn]({linkedin_url})** | **[GitHub]({github_url})**"
    )  # noqa
    st.sidebar.header("GitHub do projeto")
    st.sidebar.markdown(f"**[Link]({github_projeto})**")

    st.sidebar.markdown("***")

    st.sidebar.header("Sobre o Projeto")
    st.sidebar.info(
        "Este sistema oferece recomendações personalizadas de jogos da plataforma Steam, utilizando técnicas de aprendizado de máquina (ML). Os usuários podem inserir o nome de um jogo específico ou explorar opções disponíveis em um menu para receber sugestões adaptadas às suas preferências individuais."
    )

    popular_games = pickle.load(open("./data/popular_games.pkl", "rb"))
    pt = pickle.load(open("./data/pt.pkl", "rb"))
    similarity_scores = pickle.load(open("./data/similarity_scores.pkl", "rb"))
    game_title = list(pt.index.values)

    game_name = (list(popular_games["titulo"].values),)
    image = (list(popular_games["img_url"].values),)
    votes = (list(popular_games["total_avaliacao"].values),)
    rating = (list(popular_games["media_avaliacao"].values),)
    url = (list(popular_games["url"].values),)

    def recommend(user_input: str) -> List[List[str]]:
        """
        Returns a list of recommended items based on the user input.

        Parameters:
            user_input (str): The user input for which recommendations are to be made.

        Returns:
            list: A list of recommended items, each item containing various details such as title, image URL, URL, media rating, and total rating.
        """
        index = np.where(pt.index == user_input)[0][0]
        similar_items = sorted(
            list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True
        )[1:5]

        data = []
        for i in similar_items:
            item = []
            temp_df = popular_games[popular_games["titulo"] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates("titulo")["titulo"].values))
            item.extend(list(temp_df.drop_duplicates("titulo")["img_url"].values))
            item.extend(list(temp_df.drop_duplicates("titulo")["url"].values))
            item.extend(
                list(temp_df.drop_duplicates("titulo")["media_avaliacao"].values)
            )
            item.extend(
                list(temp_df.drop_duplicates("titulo")["total_avaliacao"].values)
            )

            data.append(item)

        return data

    st.title("Sistema de recomendação de jogos - STEAM")
    user_input = st.selectbox(
        "Por favor, digite o nome de um jogo ou selecione uma opção do menu para receber uma recomendação.",
        game_title,
    )

    if st.button("Mostrar Recomendação"):
        st.markdown("___")
        st.header("Recomendação para o jogo: {}".format(user_input))
        try:
            data = recommend(user_input)

            cols = st.columns(4)
            for c in range(len(cols)):
                with cols[c]:
                    st.markdown(
                        f'<a href="{data[c][2]}"><img src="{data[c][1]}" style="max-width:100%;"></a>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f"<span style='font-size:20px'>{data[c][0]}</span>",
                        unsafe_allow_html=True,
                    )
                    st.write("Positive ratio:", data[c][3])
                    st.write("Total de reviews:", data[c][4])
        except IndexError:
            st.error(
                "Ah, parece que este jogo é meio exclusivo quando se trata de recomendações 😅. Não encontramos muitas sugestões por aqui, mas fique tranquilo! Existem tantos outros jogos incríveis esperando para serem descobertos 😎"
            )

    st.markdown("___")

    st.title("Os jogos mais bem avaliados no universo Steam")

    num_games = 40
    num_cols = 4

    for i in range(num_games):
        if i % num_cols == 0:
            cols = st.columns(num_cols)
        with cols[i % num_cols]:
            st.markdown(
                f'<a href="{url[0][i]}"><img src="{image[0][i]}" style="max-width:100%;"></a>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<span style='font-size:20px'>{game_name[0][i]}</span>",
                unsafe_allow_html=True,
            )
            st.write("Positive ratio:", rating[0][i])
            st.write("Total de reviews:", votes[0][i])
