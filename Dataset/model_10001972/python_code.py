from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ScoreType(Enum):
    pass

############################################
# Definition of Classes
############################################










class BowlingGame:

    def __init__(self, attempts: str, scoreType: ScoreType, previousGame: Game, nextGames: str):
        self.attempts = attempts
        self.scoreType = scoreType
        self.previousGame = previousGame
        self.nextGames = nextGames
        
        pass
    @property
    def attempts(self):
        return self.__attempts
    @attempts.setter
    def attempts(self, attempts: str):
        self.__attempts = attempts

    @property
    def previousGame(self):
        return self.__previousGame
    @previousGame.setter
    def previousGame(self, previousGame: Game):
        self.__previousGame = previousGame

    @property
    def nextGames(self):
        return self.__nextGames
    @nextGames.setter
    def nextGames(self, nextGames: str):
        self.__nextGames = nextGames

    @property
    def scoreType(self):
        return self.__scoreType
    @scoreType.setter
    def scoreType(self, scoreType: ScoreType):
        self.__scoreType = scoreType



class Importer_Interface:

    pass


class Result:

    def __init__(self, player: str, score: int):
        self.player = player
        self.score = score
        
        pass
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player: str):
        self.__player = player



class InitialData:

    def __init__(self, playerName: str, points: str):
        self.playerName = playerName
        self.points = points
        
        pass
    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points: str):
        self.__points = points

    @property
    def playerName(self):
        return self.__playerName
    @playerName.setter
    def playerName(self, playerName: str):
        self.__playerName = playerName



class FileImporter:

    def __init__(self, INITIAL_DATAFILE: str):
        self.INITIAL_DATAFILE = INITIAL_DATAFILE
        
        pass
    @property
    def INITIAL_DATAFILE(self):
        return self.__INITIAL_DATAFILE
    @INITIAL_DATAFILE.setter
    def INITIAL_DATAFILE(self, INITIAL_DATAFILE: str):
        self.__INITIAL_DATAFILE = INITIAL_DATAFILE



class Attempt:

    def __init__(self, number: int, points: int):
        self.number = number
        self.points = points
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points: int):
        self.__points = points



class Game:

    def __init__(self, number: int, score: int):
        self.number = number
        self.score = score
        
        pass
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number



class Player:

    def __init__(self, name: str, totalScore: int, games: Game):
        self.name = name
        self.totalScore = totalScore
        self.games = games
        
        pass
    @property
    def games(self):
        return self.__games
    @games.setter
    def games(self, games: Game):
        self.__games = games

    @property
    def totalScore(self):
        return self.__totalScore
    @totalScore.setter
    def totalScore(self, totalScore: int):
        self.__totalScore = totalScore

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Match:

    def __init__(self, date: str, name: str, players: str, winner: Result):
        self.date = date
        self.name = name
        self.players = players
        self.winner = winner
        
        pass
    @property
    def winner(self):
        return self.__winner
    @winner.setter
    def winner(self, winner: Result):
        self.__winner = winner

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: str):
        self.__players = players

