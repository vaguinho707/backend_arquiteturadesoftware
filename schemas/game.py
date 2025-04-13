from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from schemas.player import PlayerSchema
from model.game import Game



class GameSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    id: int
    label: str 
    # created_by: int = 13
    creation_date: datetime = datetime.now()
    cost: float 
    location: str 
    game_date: datetime 
    duration_minutes: int 


class GameSearchSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    id: int

class ListGamesSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    games:List[GameSchema]


def list_games(games: List[Game]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for game in games:
        result.append({
            "id": game.game_scheduling_id,
            "label": game.label,
            # "created_by": game.created_by,
            "creation_date": game.creation_date,
            "cost": game.cost,
            "location": game.location,
            "game_date": game.game_date,
            "duration_minutes": game.duration_minutes,
        })

    return {"games": result}


class GameViewSchema(BaseModel):
    """ Define como um game será retornado.
    """
    label: str = "Peladix teste"
    # created_by: int = 13
    creation_date: datetime = datetime(1990,7,7)
    cost: float = 100.00 
    location: str = "Colégio Batista teste"
    game_date: datetime = datetime(2024,7,7)
    duration_minutes: int = 60
    # players_registered: List[PlayerSchema]


class GameDeleteSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome: str

def detail_game(game: Game):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
            "id": game.game_scheduling_id,
            "label": game.label,
            # "created_by": game.created_by,
            "creation_date": game.creation_date,
            "cost": game.cost,
            "location": game.location,
            "game_date": game.game_date,
            "duration_minutes": game.duration_minutes,
            # "players_registered": game.players_registered
    }
