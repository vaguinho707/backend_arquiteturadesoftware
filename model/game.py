from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
# from typing import Union

from model.player import Player
from model import Base


class Game(Base):
    __tablename__ = 'game_scheduling'

    game_scheduling_id = Column(Integer, primary_key=True)
    label = Column(String(100))
    # created_by = Column(Integer)
    creation_date = Column(DateTime, default=datetime.now())
    cost = Column(Float)
    location =Column(String(100))
    game_date = Column(DateTime)
    duration_minutes = Column(Integer)

    def __init__(self, game_scheduling_id: Integer, label: str, creation_date: datetime,cost: float, location: str, game_date: datetime, duration_minutes: int):
        """
        Cria uma pelada. 

        Arguments:
            texto: o texto de um comentário.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        # self.game_scheduling_id = game_scheduling_id
        self.label = label
        # self.created_by = created_by
        self.creation_date = creation_date
        self.cost = cost
        self.location = location
        self.game_date = game_date
        self.duration_minutes = duration_minutes



