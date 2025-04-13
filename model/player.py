from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base
from model.game import *


class Player(Base):
    __tablename__ = 'game_players'

    game_player_id = Column(Integer, primary_key=True)
    game_scheduling_id = Column(Integer, primary_key=True)
    player_name =Column(String(100))
    player_email = Column(String(100))

    # games = relationship("Game")


    def __init__(self, game_player_id: Integer, player_name: String,player_email: String, game_scheduling_id: Integer):
        """
        Cria uma pelada. 

        Arguments:
            texto: o texto de um comentário.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        self.game_player_id = game_player_id
        self.game_scheduling_id = game_scheduling_id
        self.player_email = player_email
        self.player_name = player_name

    # def add_player(self, game: Game):
    #     """ Adiciona um novo comentário ao Produto
    #     """
    #     self.games.append(game)