from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class InvitationEventType(Enum):
    GENERATED = "GENERATED"
    CHANGED = "CHANGED"
class InvitationReply(Enum):
    NO_REPLY = "NO_REPLY"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"


############################################
# Definition of Classes
############################################

class DescribedEntity:

    pass
class pokerleague_PrizeMoneyRuleSet(DescribedEntity):

    pass
class pokerleague_Tournament(DescribedEntity):

    def __init__(self, tournamentStart: str, tournamentEnd: str, minPlayers: int, maxPlayers: int, defaultBuyIn: int, tournamentAnnouncementLead: int, tournamentInvitationClosure: int, tournamentInvitationContact: str, Tournament: "pokerleague_Competition" = None, tournament: set["pokerleague_Invitation"] = None, tournaments: "pokerleague_Competition" = None, tournament14: set["pokerleague_Game"] = None, Tournament16: "pokerleague_Invitation" = None, pokerleague_Tournament: "pokerleague_PrizeMoneyRuleSet" = None, Tournament23: "pokerleague_Game" = None):
        self.tournamentStart = tournamentStart
        self.tournamentEnd = tournamentEnd
        self.minPlayers = minPlayers
        self.maxPlayers = maxPlayers
        self.defaultBuyIn = defaultBuyIn
        self.tournamentAnnouncementLead = tournamentAnnouncementLead
        self.tournamentInvitationClosure = tournamentInvitationClosure
        self.tournamentInvitationContact = tournamentInvitationContact
        self.Tournament = Tournament
        self.tournament = tournament if tournament is not None else set()
        self.tournaments = tournaments
        self.tournament14 = tournament14 if tournament14 is not None else set()
        self.Tournament16 = Tournament16
        self.pokerleague_Tournament = pokerleague_Tournament
        self.Tournament23 = Tournament23
        
    @property
    def tournamentInvitationClosure(self) -> int:
        return self.__tournamentInvitationClosure

    @tournamentInvitationClosure.setter
    def tournamentInvitationClosure(self, tournamentInvitationClosure: int):
        self.__tournamentInvitationClosure = tournamentInvitationClosure

    @property
    def defaultBuyIn(self) -> int:
        return self.__defaultBuyIn

    @defaultBuyIn.setter
    def defaultBuyIn(self, defaultBuyIn: int):
        self.__defaultBuyIn = defaultBuyIn

    @property
    def tournamentEnd(self) -> str:
        return self.__tournamentEnd

    @tournamentEnd.setter
    def tournamentEnd(self, tournamentEnd: str):
        self.__tournamentEnd = tournamentEnd

    @property
    def tournamentInvitationContact(self) -> str:
        return self.__tournamentInvitationContact

    @tournamentInvitationContact.setter
    def tournamentInvitationContact(self, tournamentInvitationContact: str):
        self.__tournamentInvitationContact = tournamentInvitationContact

    @property
    def minPlayers(self) -> int:
        return self.__minPlayers

    @minPlayers.setter
    def minPlayers(self, minPlayers: int):
        self.__minPlayers = minPlayers

    @property
    def tournamentAnnouncementLead(self) -> int:
        return self.__tournamentAnnouncementLead

    @tournamentAnnouncementLead.setter
    def tournamentAnnouncementLead(self, tournamentAnnouncementLead: int):
        self.__tournamentAnnouncementLead = tournamentAnnouncementLead

    @property
    def tournamentStart(self) -> str:
        return self.__tournamentStart

    @tournamentStart.setter
    def tournamentStart(self, tournamentStart: str):
        self.__tournamentStart = tournamentStart

    @property
    def maxPlayers(self) -> int:
        return self.__maxPlayers

    @maxPlayers.setter
    def maxPlayers(self, maxPlayers: int):
        self.__maxPlayers = maxPlayers

    @property
    def tournament(self):
        return self.__tournament

    @tournament.setter
    def tournament(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Tournament__tournament", None)
        self.__tournament = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Invitation"):
                    opp_val = getattr(item, "Invitation", None)
                    
                    if opp_val == self:
                        setattr(item, "Invitation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Invitation"):
                    opp_val = getattr(item, "Invitation", None)
                    
                    setattr(item, "Invitation", self)
                    

    @property
    def Tournament(self):
        return self.__Tournament

    @Tournament.setter
    def Tournament(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Tournament__Tournament", None)
        self.__Tournament = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "competition"):
                opp_val = getattr(old_value, "competition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "competition"):
                opp_val = getattr(value, "competition", None)
                if opp_val is None:
                    setattr(value, "competition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Tournament23(self):
        return self.__Tournament23

    @Tournament23.setter
    def Tournament23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Tournament__Tournament23", None)
        self.__Tournament23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "games"):
                opp_val = getattr(old_value, "games", None)
                if opp_val == self:
                    setattr(old_value, "games", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "games"):
                opp_val = getattr(value, "games", None)
                setattr(value, "games", self)

    @property
    def tournaments(self):
        return self.__tournaments

    @tournaments.setter
    def tournaments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Tournament__tournaments", None)
        self.__tournaments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Competition"):
                opp_val = getattr(old_value, "Competition", None)
                if opp_val == self:
                    setattr(old_value, "Competition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Competition"):
                opp_val = getattr(value, "Competition", None)
                setattr(value, "Competition", self)

    @property
    def Tournament16(self):
        return self.__Tournament16

    @Tournament16.setter
    def Tournament16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Tournament__Tournament16", None)
        self.__Tournament16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invitations"):
                opp_val = getattr(old_value, "invitations", None)
                if opp_val == self:
                    setattr(old_value, "invitations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invitations"):
                opp_val = getattr(value, "invitations", None)
                setattr(value, "invitations", self)

    @property
    def tournament14(self):
        return self.__tournament14

    @tournament14.setter
    def tournament14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Tournament__tournament14", None)
        self.__tournament14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Game"):
                    opp_val = getattr(item, "Game", None)
                    
                    if opp_val == self:
                        setattr(item, "Game", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Game"):
                    opp_val = getattr(item, "Game", None)
                    
                    setattr(item, "Game", self)
                    

    @property
    def pokerleague_Tournament(self):
        return self.__pokerleague_Tournament

    @pokerleague_Tournament.setter
    def pokerleague_Tournament(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Tournament__pokerleague_Tournament", None)
        self.__pokerleague_Tournament = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pokerleague_PrizeMoneyRuleSet10"):
                opp_val = getattr(old_value, "pokerleague_PrizeMoneyRuleSet10", None)
                if opp_val == self:
                    setattr(old_value, "pokerleague_PrizeMoneyRuleSet10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pokerleague_PrizeMoneyRuleSet10"):
                opp_val = getattr(value, "pokerleague_PrizeMoneyRuleSet10", None)
                setattr(value, "pokerleague_PrizeMoneyRuleSet10", self)

class pokerleague_Competition(DescribedEntity):

    def __init__(self, startDate: date, endDate: date, minimalAttendance: int, defaultBuyIn: int, defaultMinPlayers: int, defaultMaxPlayers: int, defaultTournamentAnnouncementLead: int, defaultTournamentInvitationClosure: int, defaultTournamentInvitationContact: str, pokerleague_Competition: "pokerleague_PrizeMoneyRuleSet" = None, competition: set["pokerleague_Tournament"] = None, pokerleague_Competition8: set["pokerleague_Player"] = None, Competition: "pokerleague_Tournament" = None):
        self.startDate = startDate
        self.endDate = endDate
        self.minimalAttendance = minimalAttendance
        self.defaultBuyIn = defaultBuyIn
        self.defaultMinPlayers = defaultMinPlayers
        self.defaultMaxPlayers = defaultMaxPlayers
        self.defaultTournamentAnnouncementLead = defaultTournamentAnnouncementLead
        self.defaultTournamentInvitationClosure = defaultTournamentInvitationClosure
        self.defaultTournamentInvitationContact = defaultTournamentInvitationContact
        self.pokerleague_Competition = pokerleague_Competition
        self.competition = competition if competition is not None else set()
        self.pokerleague_Competition8 = pokerleague_Competition8 if pokerleague_Competition8 is not None else set()
        self.Competition = Competition
        
    @property
    def defaultBuyIn(self) -> int:
        return self.__defaultBuyIn

    @defaultBuyIn.setter
    def defaultBuyIn(self, defaultBuyIn: int):
        self.__defaultBuyIn = defaultBuyIn

    @property
    def defaultTournamentInvitationClosure(self) -> int:
        return self.__defaultTournamentInvitationClosure

    @defaultTournamentInvitationClosure.setter
    def defaultTournamentInvitationClosure(self, defaultTournamentInvitationClosure: int):
        self.__defaultTournamentInvitationClosure = defaultTournamentInvitationClosure

    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def minimalAttendance(self) -> int:
        return self.__minimalAttendance

    @minimalAttendance.setter
    def minimalAttendance(self, minimalAttendance: int):
        self.__minimalAttendance = minimalAttendance

    @property
    def defaultMaxPlayers(self) -> int:
        return self.__defaultMaxPlayers

    @defaultMaxPlayers.setter
    def defaultMaxPlayers(self, defaultMaxPlayers: int):
        self.__defaultMaxPlayers = defaultMaxPlayers

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def defaultMinPlayers(self) -> int:
        return self.__defaultMinPlayers

    @defaultMinPlayers.setter
    def defaultMinPlayers(self, defaultMinPlayers: int):
        self.__defaultMinPlayers = defaultMinPlayers

    @property
    def defaultTournamentAnnouncementLead(self) -> int:
        return self.__defaultTournamentAnnouncementLead

    @defaultTournamentAnnouncementLead.setter
    def defaultTournamentAnnouncementLead(self, defaultTournamentAnnouncementLead: int):
        self.__defaultTournamentAnnouncementLead = defaultTournamentAnnouncementLead

    @property
    def defaultTournamentInvitationContact(self) -> str:
        return self.__defaultTournamentInvitationContact

    @defaultTournamentInvitationContact.setter
    def defaultTournamentInvitationContact(self, defaultTournamentInvitationContact: str):
        self.__defaultTournamentInvitationContact = defaultTournamentInvitationContact

    @property
    def pokerleague_Competition8(self):
        return self.__pokerleague_Competition8

    @pokerleague_Competition8.setter
    def pokerleague_Competition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Competition__pokerleague_Competition8", None)
        self.__pokerleague_Competition8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pokerleague_Player"):
                    opp_val = getattr(item, "pokerleague_Player", None)
                    
                    if opp_val == self:
                        setattr(item, "pokerleague_Player", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pokerleague_Player"):
                    opp_val = getattr(item, "pokerleague_Player", None)
                    
                    setattr(item, "pokerleague_Player", self)
                    

    @property
    def competition(self):
        return self.__competition

    @competition.setter
    def competition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Competition__competition", None)
        self.__competition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tournament"):
                    opp_val = getattr(item, "Tournament", None)
                    
                    if opp_val == self:
                        setattr(item, "Tournament", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tournament"):
                    opp_val = getattr(item, "Tournament", None)
                    
                    setattr(item, "Tournament", self)
                    

    @property
    def pokerleague_Competition(self):
        return self.__pokerleague_Competition

    @pokerleague_Competition.setter
    def pokerleague_Competition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Competition__pokerleague_Competition", None)
        self.__pokerleague_Competition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pokerleague_PrizeMoneyRuleSet"):
                opp_val = getattr(old_value, "pokerleague_PrizeMoneyRuleSet", None)
                if opp_val == self:
                    setattr(old_value, "pokerleague_PrizeMoneyRuleSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pokerleague_PrizeMoneyRuleSet"):
                opp_val = getattr(value, "pokerleague_PrizeMoneyRuleSet", None)
                setattr(value, "pokerleague_PrizeMoneyRuleSet", self)

    @property
    def Competition(self):
        return self.__Competition

    @Competition.setter
    def Competition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Competition__Competition", None)
        self.__Competition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tournaments"):
                opp_val = getattr(old_value, "tournaments", None)
                if opp_val == self:
                    setattr(old_value, "tournaments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tournaments"):
                opp_val = getattr(value, "tournaments", None)
                setattr(value, "tournaments", self)

class Serializable:

    pass
class pokerleague_DataStructureVersion(Serializable):

    def __init__(self, id: int, currentVersion: str):
        self.id = id
        self.currentVersion = currentVersion
        
    @property
    def currentVersion(self) -> str:
        return self.__currentVersion

    @currentVersion.setter
    def currentVersion(self, currentVersion: str):
        self.__currentVersion = currentVersion

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class pokerleague_Serializable(ABC):

    pass
class IdentifiableEntity:

    pass
class pokerleague_Game(IdentifiableEntity):

    def __init__(self, buyIn: int, ordinal: int, Game: "pokerleague_Tournament" = None, pokerleague_Game: "pokerleague_PrizeMoneyRuleSet" = None, game: set["pokerleague_PlayerInGame"] = None, Game30: "pokerleague_PlayerInGame" = None, games: "pokerleague_Tournament" = None):
        self.buyIn = buyIn
        self.ordinal = ordinal
        self.Game = Game
        self.pokerleague_Game = pokerleague_Game
        self.game = game if game is not None else set()
        self.Game30 = Game30
        self.games = games
        
    @property
    def buyIn(self) -> int:
        return self.__buyIn

    @buyIn.setter
    def buyIn(self, buyIn: int):
        self.__buyIn = buyIn

    @property
    def ordinal(self) -> int:
        return self.__ordinal

    @ordinal.setter
    def ordinal(self, ordinal: int):
        self.__ordinal = ordinal

    @property
    def Game(self):
        return self.__Game

    @Game.setter
    def Game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Game__Game", None)
        self.__Game = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tournament14"):
                opp_val = getattr(old_value, "tournament14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tournament14"):
                opp_val = getattr(value, "tournament14", None)
                if opp_val is None:
                    setattr(value, "tournament14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pokerleague_Game(self):
        return self.__pokerleague_Game

    @pokerleague_Game.setter
    def pokerleague_Game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Game__pokerleague_Game", None)
        self.__pokerleague_Game = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pokerleague_PrizeMoneyRuleSet25"):
                opp_val = getattr(old_value, "pokerleague_PrizeMoneyRuleSet25", None)
                if opp_val == self:
                    setattr(old_value, "pokerleague_PrizeMoneyRuleSet25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pokerleague_PrizeMoneyRuleSet25"):
                opp_val = getattr(value, "pokerleague_PrizeMoneyRuleSet25", None)
                setattr(value, "pokerleague_PrizeMoneyRuleSet25", self)

    @property
    def game(self):
        return self.__game

    @game.setter
    def game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Game__game", None)
        self.__game = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PlayerInGame"):
                    opp_val = getattr(item, "PlayerInGame", None)
                    
                    if opp_val == self:
                        setattr(item, "PlayerInGame", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PlayerInGame"):
                    opp_val = getattr(item, "PlayerInGame", None)
                    
                    setattr(item, "PlayerInGame", self)
                    

    @property
    def Game30(self):
        return self.__Game30

    @Game30.setter
    def Game30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Game__Game30", None)
        self.__Game30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playersInGame"):
                opp_val = getattr(old_value, "playersInGame", None)
                if opp_val == self:
                    setattr(old_value, "playersInGame", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playersInGame"):
                opp_val = getattr(value, "playersInGame", None)
                setattr(value, "playersInGame", self)

    @property
    def games(self):
        return self.__games

    @games.setter
    def games(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Game__games", None)
        self.__games = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tournament23"):
                opp_val = getattr(old_value, "Tournament23", None)
                if opp_val == self:
                    setattr(old_value, "Tournament23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tournament23"):
                opp_val = getattr(value, "Tournament23", None)
                setattr(value, "Tournament23", self)

class pokerleague_InvitationEvent(IdentifiableEntity):

    def __init__(self, eventTime: str, eventType: str, sent: bool, InvitationEvent: "pokerleague_Invitation" = None, events: "pokerleague_Invitation" = None):
        self.eventTime = eventTime
        self.eventType = eventType
        self.sent = sent
        self.InvitationEvent = InvitationEvent
        self.events = events
        
    @property
    def sent(self) -> bool:
        return self.__sent

    @sent.setter
    def sent(self, sent: bool):
        self.__sent = sent

    @property
    def eventType(self) -> str:
        return self.__eventType

    @eventType.setter
    def eventType(self, eventType: str):
        self.__eventType = eventType

    @property
    def eventTime(self) -> str:
        return self.__eventTime

    @eventTime.setter
    def eventTime(self, eventTime: str):
        self.__eventTime = eventTime

    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_InvitationEvent__events", None)
        self.__events = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Invitation21"):
                opp_val = getattr(old_value, "Invitation21", None)
                if opp_val == self:
                    setattr(old_value, "Invitation21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Invitation21"):
                opp_val = getattr(value, "Invitation21", None)
                setattr(value, "Invitation21", self)

    @property
    def InvitationEvent(self):
        return self.__InvitationEvent

    @InvitationEvent.setter
    def InvitationEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_InvitationEvent__InvitationEvent", None)
        self.__InvitationEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invitation"):
                opp_val = getattr(old_value, "invitation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invitation"):
                opp_val = getattr(value, "invitation", None)
                if opp_val is None:
                    setattr(value, "invitation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pokerleague_Player(IdentifiableEntity):

    def __init__(self, active: bool, nick: str, firstName: str, lastName: str, emailAddress: str, pokerleague_Player: "pokerleague_Competition" = None, pokerleague_Player18: "pokerleague_Invitation" = None, pokerleague_Player28: "pokerleague_PlayerInGame" = None):
        self.active = active
        self.nick = nick
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.pokerleague_Player = pokerleague_Player
        self.pokerleague_Player18 = pokerleague_Player18
        self.pokerleague_Player28 = pokerleague_Player28
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def nick(self) -> str:
        return self.__nick

    @nick.setter
    def nick(self, nick: str):
        self.__nick = nick

    @property
    def emailAddress(self) -> str:
        return self.__emailAddress

    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def pokerleague_Player(self):
        return self.__pokerleague_Player

    @pokerleague_Player.setter
    def pokerleague_Player(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Player__pokerleague_Player", None)
        self.__pokerleague_Player = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pokerleague_Competition8"):
                opp_val = getattr(old_value, "pokerleague_Competition8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pokerleague_Competition8"):
                opp_val = getattr(value, "pokerleague_Competition8", None)
                if opp_val is None:
                    setattr(value, "pokerleague_Competition8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pokerleague_Player28(self):
        return self.__pokerleague_Player28

    @pokerleague_Player28.setter
    def pokerleague_Player28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Player__pokerleague_Player28", None)
        self.__pokerleague_Player28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pokerleague_PlayerInGame"):
                opp_val = getattr(old_value, "pokerleague_PlayerInGame", None)
                if opp_val == self:
                    setattr(old_value, "pokerleague_PlayerInGame", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pokerleague_PlayerInGame"):
                opp_val = getattr(value, "pokerleague_PlayerInGame", None)
                setattr(value, "pokerleague_PlayerInGame", self)

    @property
    def pokerleague_Player18(self):
        return self.__pokerleague_Player18

    @pokerleague_Player18.setter
    def pokerleague_Player18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Player__pokerleague_Player18", None)
        self.__pokerleague_Player18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pokerleague_Invitation"):
                opp_val = getattr(old_value, "pokerleague_Invitation", None)
                if opp_val == self:
                    setattr(old_value, "pokerleague_Invitation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pokerleague_Invitation"):
                opp_val = getattr(value, "pokerleague_Invitation", None)
                setattr(value, "pokerleague_Invitation", self)

class pokerleague_Invitation(IdentifiableEntity):

    def __init__(self, reply: str, ordinal: int, uuid: str, Invitation: "pokerleague_Tournament" = None, invitations: "pokerleague_Tournament" = None, pokerleague_Invitation: "pokerleague_Player" = None, invitation: set["pokerleague_InvitationEvent"] = None, Invitation21: "pokerleague_InvitationEvent" = None):
        self.reply = reply
        self.ordinal = ordinal
        self.uuid = uuid
        self.Invitation = Invitation
        self.invitations = invitations
        self.pokerleague_Invitation = pokerleague_Invitation
        self.invitation = invitation if invitation is not None else set()
        self.Invitation21 = Invitation21
        
    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

    @property
    def reply(self) -> str:
        return self.__reply

    @reply.setter
    def reply(self, reply: str):
        self.__reply = reply

    @property
    def ordinal(self) -> int:
        return self.__ordinal

    @ordinal.setter
    def ordinal(self, ordinal: int):
        self.__ordinal = ordinal

    @property
    def Invitation21(self):
        return self.__Invitation21

    @Invitation21.setter
    def Invitation21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Invitation__Invitation21", None)
        self.__Invitation21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events"):
                opp_val = getattr(old_value, "events", None)
                if opp_val == self:
                    setattr(old_value, "events", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events"):
                opp_val = getattr(value, "events", None)
                setattr(value, "events", self)

    @property
    def Invitation(self):
        return self.__Invitation

    @Invitation.setter
    def Invitation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Invitation__Invitation", None)
        self.__Invitation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tournament"):
                opp_val = getattr(old_value, "tournament", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tournament"):
                opp_val = getattr(value, "tournament", None)
                if opp_val is None:
                    setattr(value, "tournament", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def invitation(self):
        return self.__invitation

    @invitation.setter
    def invitation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Invitation__invitation", None)
        self.__invitation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InvitationEvent"):
                    opp_val = getattr(item, "InvitationEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "InvitationEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InvitationEvent"):
                    opp_val = getattr(item, "InvitationEvent", None)
                    
                    setattr(item, "InvitationEvent", self)
                    

    @property
    def invitations(self):
        return self.__invitations

    @invitations.setter
    def invitations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Invitation__invitations", None)
        self.__invitations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tournament16"):
                opp_val = getattr(old_value, "Tournament16", None)
                if opp_val == self:
                    setattr(old_value, "Tournament16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tournament16"):
                opp_val = getattr(value, "Tournament16", None)
                setattr(value, "Tournament16", self)

    @property
    def pokerleague_Invitation(self):
        return self.__pokerleague_Invitation

    @pokerleague_Invitation.setter
    def pokerleague_Invitation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_Invitation__pokerleague_Invitation", None)
        self.__pokerleague_Invitation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pokerleague_Player18"):
                opp_val = getattr(old_value, "pokerleague_Player18", None)
                if opp_val == self:
                    setattr(old_value, "pokerleague_Player18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pokerleague_Player18"):
                opp_val = getattr(value, "pokerleague_Player18", None)
                setattr(value, "pokerleague_Player18", self)

class pokerleague_PrizeMoneyRule(IdentifiableEntity):

    def __init__(self, numberOfPlayers: int, prizeMoneyRules: "pokerleague_PrizeMoneyRuleSet" = None, prizeMoneyRule: set["pokerleague_PrizeMoneyFormula"] = None, PrizeMoneyRule4: "pokerleague_PrizeMoneyFormula" = None, PrizeMoneyRule: "pokerleague_PrizeMoneyRuleSet" = None):
        self.numberOfPlayers = numberOfPlayers
        self.prizeMoneyRules = prizeMoneyRules
        self.prizeMoneyRule = prizeMoneyRule if prizeMoneyRule is not None else set()
        self.PrizeMoneyRule4 = PrizeMoneyRule4
        self.PrizeMoneyRule = PrizeMoneyRule
        
    @property
    def numberOfPlayers(self) -> int:
        return self.__numberOfPlayers

    @numberOfPlayers.setter
    def numberOfPlayers(self, numberOfPlayers: int):
        self.__numberOfPlayers = numberOfPlayers

    @property
    def PrizeMoneyRule4(self):
        return self.__PrizeMoneyRule4

    @PrizeMoneyRule4.setter
    def PrizeMoneyRule4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_PrizeMoneyRule__PrizeMoneyRule4", None)
        self.__PrizeMoneyRule4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prizeMoneyFormulas"):
                opp_val = getattr(old_value, "prizeMoneyFormulas", None)
                if opp_val == self:
                    setattr(old_value, "prizeMoneyFormulas", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prizeMoneyFormulas"):
                opp_val = getattr(value, "prizeMoneyFormulas", None)
                setattr(value, "prizeMoneyFormulas", self)

    @property
    def prizeMoneyRule(self):
        return self.__prizeMoneyRule

    @prizeMoneyRule.setter
    def prizeMoneyRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_PrizeMoneyRule__prizeMoneyRule", None)
        self.__prizeMoneyRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PrizeMoneyFormula"):
                    opp_val = getattr(item, "PrizeMoneyFormula", None)
                    
                    if opp_val == self:
                        setattr(item, "PrizeMoneyFormula", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PrizeMoneyFormula"):
                    opp_val = getattr(item, "PrizeMoneyFormula", None)
                    
                    setattr(item, "PrizeMoneyFormula", self)
                    

    @property
    def prizeMoneyRules(self):
        return self.__prizeMoneyRules

    @prizeMoneyRules.setter
    def prizeMoneyRules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_PrizeMoneyRule__prizeMoneyRules", None)
        self.__prizeMoneyRules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrizeMoneyRuleSet"):
                opp_val = getattr(old_value, "PrizeMoneyRuleSet", None)
                if opp_val == self:
                    setattr(old_value, "PrizeMoneyRuleSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrizeMoneyRuleSet"):
                opp_val = getattr(value, "PrizeMoneyRuleSet", None)
                setattr(value, "PrizeMoneyRuleSet", self)

    @property
    def PrizeMoneyRule(self):
        return self.__PrizeMoneyRule

    @PrizeMoneyRule.setter
    def PrizeMoneyRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_PrizeMoneyRule__PrizeMoneyRule", None)
        self.__PrizeMoneyRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prizeMoneyRuleSet"):
                opp_val = getattr(old_value, "prizeMoneyRuleSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prizeMoneyRuleSet"):
                opp_val = getattr(value, "prizeMoneyRuleSet", None)
                if opp_val is None:
                    setattr(value, "prizeMoneyRuleSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pokerleague_PlayerInGame(IdentifiableEntity):

    def __init__(self, rank: int, PlayerInGame: "pokerleague_Game" = None, pokerleague_PlayerInGame: "pokerleague_Player" = None, playersInGame: "pokerleague_Game" = None):
        self.rank = rank
        self.PlayerInGame = PlayerInGame
        self.pokerleague_PlayerInGame = pokerleague_PlayerInGame
        self.playersInGame = playersInGame
        
    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def PlayerInGame(self):
        return self.__PlayerInGame

    @PlayerInGame.setter
    def PlayerInGame(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_PlayerInGame__PlayerInGame", None)
        self.__PlayerInGame = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game"):
                opp_val = getattr(old_value, "game", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game"):
                opp_val = getattr(value, "game", None)
                if opp_val is None:
                    setattr(value, "game", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def playersInGame(self):
        return self.__playersInGame

    @playersInGame.setter
    def playersInGame(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_PlayerInGame__playersInGame", None)
        self.__playersInGame = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Game30"):
                opp_val = getattr(old_value, "Game30", None)
                if opp_val == self:
                    setattr(old_value, "Game30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Game30"):
                opp_val = getattr(value, "Game30", None)
                setattr(value, "Game30", self)

    @property
    def pokerleague_PlayerInGame(self):
        return self.__pokerleague_PlayerInGame

    @pokerleague_PlayerInGame.setter
    def pokerleague_PlayerInGame(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_PlayerInGame__pokerleague_PlayerInGame", None)
        self.__pokerleague_PlayerInGame = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pokerleague_Player28"):
                opp_val = getattr(old_value, "pokerleague_Player28", None)
                if opp_val == self:
                    setattr(old_value, "pokerleague_Player28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pokerleague_Player28"):
                opp_val = getattr(value, "pokerleague_Player28", None)
                setattr(value, "pokerleague_Player28", self)

class pokerleague_PrizeMoneyFormula(IdentifiableEntity):

    def __init__(self, rank: int, relativePrizeMoney: int, PrizeMoneyFormula: "pokerleague_PrizeMoneyRule" = None, prizeMoneyFormulas: "pokerleague_PrizeMoneyRule" = None):
        self.rank = rank
        self.relativePrizeMoney = relativePrizeMoney
        self.PrizeMoneyFormula = PrizeMoneyFormula
        self.prizeMoneyFormulas = prizeMoneyFormulas
        
    @property
    def relativePrizeMoney(self) -> int:
        return self.__relativePrizeMoney

    @relativePrizeMoney.setter
    def relativePrizeMoney(self, relativePrizeMoney: int):
        self.__relativePrizeMoney = relativePrizeMoney

    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def prizeMoneyFormulas(self):
        return self.__prizeMoneyFormulas

    @prizeMoneyFormulas.setter
    def prizeMoneyFormulas(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_PrizeMoneyFormula__prizeMoneyFormulas", None)
        self.__prizeMoneyFormulas = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrizeMoneyRule4"):
                opp_val = getattr(old_value, "PrizeMoneyRule4", None)
                if opp_val == self:
                    setattr(old_value, "PrizeMoneyRule4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrizeMoneyRule4"):
                opp_val = getattr(value, "PrizeMoneyRule4", None)
                setattr(value, "PrizeMoneyRule4", self)

    @property
    def PrizeMoneyFormula(self):
        return self.__PrizeMoneyFormula

    @PrizeMoneyFormula.setter
    def PrizeMoneyFormula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pokerleague_PrizeMoneyFormula__PrizeMoneyFormula", None)
        self.__PrizeMoneyFormula = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prizeMoneyRule"):
                opp_val = getattr(old_value, "prizeMoneyRule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prizeMoneyRule"):
                opp_val = getattr(value, "prizeMoneyRule", None)
                if opp_val is None:
                    setattr(value, "prizeMoneyRule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pokerleague_DescribedEntity(IdentifiableEntity):

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class pokerleague_IdentifiableEntity(Serializable):

    def __init__(self, id: int, proxy: bool, obsolete: bool):
        self.id = id
        self.proxy = proxy
        self.obsolete = obsolete
        
    @property
    def obsolete(self) -> bool:
        return self.__obsolete

    @obsolete.setter
    def obsolete(self, obsolete: bool):
        self.__obsolete = obsolete

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def proxy(self) -> bool:
        return self.__proxy

    @proxy.setter
    def proxy(self, proxy: bool):
        self.__proxy = proxy

class pokerleague_Settings(Serializable):

    def __init__(self, id: int, adminPassword: str, defaultTimeZone: str, smtpHost: str, smtpPort: str, smtpUser: str, smtpPassword: str, smtpFrom: str, urlBase: str):
        self.id = id
        self.adminPassword = adminPassword
        self.defaultTimeZone = defaultTimeZone
        self.smtpHost = smtpHost
        self.smtpPort = smtpPort
        self.smtpUser = smtpUser
        self.smtpPassword = smtpPassword
        self.smtpFrom = smtpFrom
        self.urlBase = urlBase
        
    @property
    def adminPassword(self) -> str:
        return self.__adminPassword

    @adminPassword.setter
    def adminPassword(self, adminPassword: str):
        self.__adminPassword = adminPassword

    @property
    def smtpUser(self) -> str:
        return self.__smtpUser

    @smtpUser.setter
    def smtpUser(self, smtpUser: str):
        self.__smtpUser = smtpUser

    @property
    def defaultTimeZone(self) -> str:
        return self.__defaultTimeZone

    @defaultTimeZone.setter
    def defaultTimeZone(self, defaultTimeZone: str):
        self.__defaultTimeZone = defaultTimeZone

    @property
    def smtpPassword(self) -> str:
        return self.__smtpPassword

    @smtpPassword.setter
    def smtpPassword(self, smtpPassword: str):
        self.__smtpPassword = smtpPassword

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def urlBase(self) -> str:
        return self.__urlBase

    @urlBase.setter
    def urlBase(self, urlBase: str):
        self.__urlBase = urlBase

    @property
    def smtpPort(self) -> str:
        return self.__smtpPort

    @smtpPort.setter
    def smtpPort(self, smtpPort: str):
        self.__smtpPort = smtpPort

    @property
    def smtpFrom(self) -> str:
        return self.__smtpFrom

    @smtpFrom.setter
    def smtpFrom(self, smtpFrom: str):
        self.__smtpFrom = smtpFrom

    @property
    def smtpHost(self) -> str:
        return self.__smtpHost

    @smtpHost.setter
    def smtpHost(self, smtpHost: str):
        self.__smtpHost = smtpHost

class pokerleague_DataVersion(Serializable):

    def __init__(self, id: int, currentVersion: str):
        self.id = id
        self.currentVersion = currentVersion
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def currentVersion(self) -> str:
        return self.__currentVersion

    @currentVersion.setter
    def currentVersion(self, currentVersion: str):
        self.__currentVersion = currentVersion
