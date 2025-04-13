from pydantic import BaseModel
from typing import Optional, List
from model.player import Player
from schemas.game import *



class PlayerSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    game_player_id: int
    game_scheduling_id: int = 12
    player_name: str = 'vaguinho'
    player_email: str = 'vaguinho@gmail.com'


class PlayerSearchSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str = "Teste"


class ListPlayersSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    players:List[PlayerSchema]


def list_players(players: List[Player]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for player in players:
        result.append({
            "name": player.name,
            "email": player.email,
        })

    return {"players": result}


class PlayerViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    player_Id: int = 1
    name: str = "Zeca Urubu"
    email: str = "zecaurubu@gmail.com"
    # game_list: List[GameSchema]


class PlayerDeleteSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    name: str

def detail_player(player: Player):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "player_id": player.game_player_id,
        "name": player.player_name,
        "email": player.player_email,
        "game_scheduling_id": player.game_scheduling_id
    }
