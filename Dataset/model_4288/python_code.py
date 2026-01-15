from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Position(Enum):
    attackDamageCarry = "attackDamageCarry"
    support = "support"
    midLane = "midLane"
    topLane = "topLane"
    jungle = "jungle"
class GroupStageType(Enum):
    league = "league"
    worldsPlayIn = "worldsPlayIn"
    worldsGroup = "worldsGroup"
    riftRivalsGroup = "riftRivalsGroup"
    msiPlayIn = "msiPlayIn"
    msiGroup = "msiGroup"
    allStarsGroup = "allStarsGroup"
class TournamentType(Enum):
    worlds = "worlds"
    regionals = "regionals"
    allStars = "allStars"
    promotion = "promotion"
    midSeasonInvitational = "midSeasonInvitational"
    riftRivals = "riftRivals"
    playOff = "playOff"
class CapacityType(Enum):
    positioning = "positioning"
    stressManagement = "stressManagement"
    playmakingMechanics = "playmakingMechanics"
    escapeMechanics = "escapeMechanics"
    patience = "patience"
    farm = "farm"
    steal = "steal"
    splitPush = "splitPush"
    teamPlay = "teamPlay"
    aggressivity = "aggressivity"
    leadership = "leadership"
    draft = "draft"
    pathing = "pathing"
    awareness = "awareness"
    experience = "experience"
    objectivePlay = "objectivePlay"
    metaGame = "metaGame"
class Season(Enum):
    spring = "spring"
    summer = "summer"
class MatchType(Enum):
    quarterFinal = "quarterFinal"
    singleRoundElimination = "singleRoundElimination"
    group = "group"
    final = "final"
    semiFinal = "semiFinal"


############################################
# Definition of Classes
############################################

class eSport_Root:

    pass
class eSport_Group:

    pass
class eSport_Match:

    def __init__(self, loserWins: int, type: str, Match: "eSport_Team" = None, Match44: "eSport_Team" = None, Match60: "eSport_Group" = None, matchs: "eSport_Group" = None, matchs51: "eSport_FinalStage" = None, matchsWon: "eSport_Team" = None, matchsLost: "eSport_Team" = None, Match72: "eSport_FinalStage" = None):
        self.loserWins = loserWins
        self.type = type
        self.Match = Match
        self.Match44 = Match44
        self.Match60 = Match60
        self.matchs = matchs
        self.matchs51 = matchs51
        self.matchsWon = matchsWon
        self.matchsLost = matchsLost
        self.Match72 = Match72
        
    @property
    def loserWins(self) -> int:
        return self.__loserWins

    @loserWins.setter
    def loserWins(self, loserWins: int):
        self.__loserWins = loserWins

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Match60(self):
        return self.__Match60

    @Match60.setter
    def Match60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Match__Match60", None)
        self.__Match60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group"):
                opp_val = getattr(old_value, "group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group"):
                opp_val = getattr(value, "group", None)
                if opp_val is None:
                    setattr(value, "group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Match72(self):
        return self.__Match72

    @Match72.setter
    def Match72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Match__Match72", None)
        self.__Match72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finalstage"):
                opp_val = getattr(old_value, "finalstage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finalstage"):
                opp_val = getattr(value, "finalstage", None)
                if opp_val is None:
                    setattr(value, "finalstage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Match44(self):
        return self.__Match44

    @Match44.setter
    def Match44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Match__Match44", None)
        self.__Match44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teamLoser"):
                opp_val = getattr(old_value, "teamLoser", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teamLoser"):
                opp_val = getattr(value, "teamLoser", None)
                if opp_val is None:
                    setattr(value, "teamLoser", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def matchs51(self):
        return self.__matchs51

    @matchs51.setter
    def matchs51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Match__matchs51", None)
        self.__matchs51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FinalStage52"):
                opp_val = getattr(old_value, "FinalStage52", None)
                if opp_val == self:
                    setattr(old_value, "FinalStage52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FinalStage52"):
                opp_val = getattr(value, "FinalStage52", None)
                setattr(value, "FinalStage52", self)

    @property
    def matchsLost(self):
        return self.__matchsLost

    @matchsLost.setter
    def matchsLost(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Match__matchsLost", None)
        self.__matchsLost = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Team56"):
                opp_val = getattr(old_value, "Team56", None)
                if opp_val == self:
                    setattr(old_value, "Team56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Team56"):
                opp_val = getattr(value, "Team56", None)
                setattr(value, "Team56", self)

    @property
    def matchsWon(self):
        return self.__matchsWon

    @matchsWon.setter
    def matchsWon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Match__matchsWon", None)
        self.__matchsWon = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Team54"):
                opp_val = getattr(old_value, "Team54", None)
                if opp_val == self:
                    setattr(old_value, "Team54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Team54"):
                opp_val = getattr(value, "Team54", None)
                setattr(value, "Team54", self)

    @property
    def Match(self):
        return self.__Match

    @Match.setter
    def Match(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Match__Match", None)
        self.__Match = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teamWinner"):
                opp_val = getattr(old_value, "teamWinner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teamWinner"):
                opp_val = getattr(value, "teamWinner", None)
                if opp_val is None:
                    setattr(value, "teamWinner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def matchs(self):
        return self.__matchs

    @matchs.setter
    def matchs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Match__matchs", None)
        self.__matchs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Group49"):
                opp_val = getattr(old_value, "Group49", None)
                if opp_val == self:
                    setattr(old_value, "Group49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Group49"):
                opp_val = getattr(value, "Group49", None)
                setattr(value, "Group49", self)

class eSport_League:

    def __init__(self, year: int, season: str, name: str, size: int, leagues: "eSport_Zone" = None, league: "eSport_GroupStage" = None, leagueFrom: set["eSport_Qualification"] = None, League: "eSport_Zone" = None, League70: "eSport_GroupStage" = None, eSport_League: "eSport_Root" = None, League84: "eSport_Qualification" = None):
        self.year = year
        self.season = season
        self.name = name
        self.size = size
        self.leagues = leagues
        self.league = league
        self.leagueFrom = leagueFrom if leagueFrom is not None else set()
        self.League = League
        self.League70 = League70
        self.eSport_League = eSport_League
        self.League84 = League84
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def season(self) -> str:
        return self.__season

    @season.setter
    def season(self, season: str):
        self.__season = season

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def League70(self):
        return self.__League70

    @League70.setter
    def League70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_League__League70", None)
        self.__League70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groupstage69"):
                opp_val = getattr(old_value, "groupstage69", None)
                if opp_val == self:
                    setattr(old_value, "groupstage69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groupstage69"):
                opp_val = getattr(value, "groupstage69", None)
                setattr(value, "groupstage69", self)

    @property
    def eSport_League(self):
        return self.__eSport_League

    @eSport_League.setter
    def eSport_League(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_League__eSport_League", None)
        self.__eSport_League = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSport_Root89"):
                opp_val = getattr(old_value, "eSport_Root89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSport_Root89"):
                opp_val = getattr(value, "eSport_Root89", None)
                if opp_val is None:
                    setattr(value, "eSport_Root89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def league(self):
        return self.__league

    @league.setter
    def league(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_League__league", None)
        self.__league = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GroupStage15"):
                opp_val = getattr(old_value, "GroupStage15", None)
                if opp_val == self:
                    setattr(old_value, "GroupStage15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GroupStage15"):
                opp_val = getattr(value, "GroupStage15", None)
                setattr(value, "GroupStage15", self)

    @property
    def League84(self):
        return self.__League84

    @League84.setter
    def League84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_League__League84", None)
        self.__League84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualifiesFor83"):
                opp_val = getattr(old_value, "qualifiesFor83", None)
                if opp_val == self:
                    setattr(old_value, "qualifiesFor83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualifiesFor83"):
                opp_val = getattr(value, "qualifiesFor83", None)
                setattr(value, "qualifiesFor83", self)

    @property
    def leagues(self):
        return self.__leagues

    @leagues.setter
    def leagues(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_League__leagues", None)
        self.__leagues = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Zone13"):
                opp_val = getattr(old_value, "Zone13", None)
                if opp_val == self:
                    setattr(old_value, "Zone13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Zone13"):
                opp_val = getattr(value, "Zone13", None)
                setattr(value, "Zone13", self)

    @property
    def leagueFrom(self):
        return self.__leagueFrom

    @leagueFrom.setter
    def leagueFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_League__leagueFrom", None)
        self.__leagueFrom = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Qualification17"):
                    opp_val = getattr(item, "Qualification17", None)
                    
                    if opp_val == self:
                        setattr(item, "Qualification17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Qualification17"):
                    opp_val = getattr(item, "Qualification17", None)
                    
                    setattr(item, "Qualification17", self)
                    

    @property
    def League(self):
        return self.__League

    @League.setter
    def League(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_League__League", None)
        self.__League = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zone"):
                opp_val = getattr(old_value, "zone", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zone"):
                opp_val = getattr(value, "zone", None)
                if opp_val is None:
                    setattr(value, "zone", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eSport_Qualification:

    def __init__(self, name: str, Qualification17: "eSport_League" = None, Qualification: "eSport_Tournament" = None, Qualification11: "eSport_Tournament" = None, eSport_Qualification: "eSport_Root" = None, qualifiesFor: "eSport_Tournament" = None, qualifiesFrom: "eSport_Tournament" = None, qualifiesFor83: "eSport_League" = None):
        self.name = name
        self.Qualification17 = Qualification17
        self.Qualification = Qualification
        self.Qualification11 = Qualification11
        self.eSport_Qualification = eSport_Qualification
        self.qualifiesFor = qualifiesFor
        self.qualifiesFrom = qualifiesFrom
        self.qualifiesFor83 = qualifiesFor83
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def qualifiesFrom(self):
        return self.__qualifiesFrom

    @qualifiesFrom.setter
    def qualifiesFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Qualification__qualifiesFrom", None)
        self.__qualifiesFrom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tournament81"):
                opp_val = getattr(old_value, "Tournament81", None)
                if opp_val == self:
                    setattr(old_value, "Tournament81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tournament81"):
                opp_val = getattr(value, "Tournament81", None)
                setattr(value, "Tournament81", self)

    @property
    def Qualification(self):
        return self.__Qualification

    @Qualification.setter
    def Qualification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Qualification__Qualification", None)
        self.__Qualification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tournamentFrom"):
                opp_val = getattr(old_value, "tournamentFrom", None)
                if opp_val == self:
                    setattr(old_value, "tournamentFrom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tournamentFrom"):
                opp_val = getattr(value, "tournamentFrom", None)
                setattr(value, "tournamentFrom", self)

    @property
    def Qualification17(self):
        return self.__Qualification17

    @Qualification17.setter
    def Qualification17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Qualification__Qualification17", None)
        self.__Qualification17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leagueFrom"):
                opp_val = getattr(old_value, "leagueFrom", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leagueFrom"):
                opp_val = getattr(value, "leagueFrom", None)
                if opp_val is None:
                    setattr(value, "leagueFrom", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eSport_Qualification(self):
        return self.__eSport_Qualification

    @eSport_Qualification.setter
    def eSport_Qualification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Qualification__eSport_Qualification", None)
        self.__eSport_Qualification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSport_Root96"):
                opp_val = getattr(old_value, "eSport_Root96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSport_Root96"):
                opp_val = getattr(value, "eSport_Root96", None)
                if opp_val is None:
                    setattr(value, "eSport_Root96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Qualification11(self):
        return self.__Qualification11

    @Qualification11.setter
    def Qualification11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Qualification__Qualification11", None)
        self.__Qualification11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tournamentTo"):
                opp_val = getattr(old_value, "tournamentTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tournamentTo"):
                opp_val = getattr(value, "tournamentTo", None)
                if opp_val is None:
                    setattr(value, "tournamentTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qualifiesFor83(self):
        return self.__qualifiesFor83

    @qualifiesFor83.setter
    def qualifiesFor83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Qualification__qualifiesFor83", None)
        self.__qualifiesFor83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "League84"):
                opp_val = getattr(old_value, "League84", None)
                if opp_val == self:
                    setattr(old_value, "League84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "League84"):
                opp_val = getattr(value, "League84", None)
                setattr(value, "League84", self)

    @property
    def qualifiesFor(self):
        return self.__qualifiesFor

    @qualifiesFor.setter
    def qualifiesFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Qualification__qualifiesFor", None)
        self.__qualifiesFor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tournament79"):
                opp_val = getattr(old_value, "Tournament79", None)
                if opp_val == self:
                    setattr(old_value, "Tournament79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tournament79"):
                opp_val = getattr(value, "Tournament79", None)
                setattr(value, "Tournament79", self)

class eSport_GroupStage:

    def __init__(self, type: str, maxNbGames: int, meetingsInSameGroup: int, meetingsWithOtherGroups: int, GroupStage15: "eSport_League" = None, GroupStage: "eSport_Tournament" = None, GroupStage58: "eSport_Group" = None, groupstage: set["eSport_Group"] = None, groupstages: "eSport_Tournament" = None, groupstage69: "eSport_League" = None):
        self.type = type
        self.maxNbGames = maxNbGames
        self.meetingsInSameGroup = meetingsInSameGroup
        self.meetingsWithOtherGroups = meetingsWithOtherGroups
        self.GroupStage15 = GroupStage15
        self.GroupStage = GroupStage
        self.GroupStage58 = GroupStage58
        self.groupstage = groupstage if groupstage is not None else set()
        self.groupstages = groupstages
        self.groupstage69 = groupstage69
        
    @property
    def meetingsWithOtherGroups(self) -> int:
        return self.__meetingsWithOtherGroups

    @meetingsWithOtherGroups.setter
    def meetingsWithOtherGroups(self, meetingsWithOtherGroups: int):
        self.__meetingsWithOtherGroups = meetingsWithOtherGroups

    @property
    def maxNbGames(self) -> int:
        return self.__maxNbGames

    @maxNbGames.setter
    def maxNbGames(self, maxNbGames: int):
        self.__maxNbGames = maxNbGames

    @property
    def meetingsInSameGroup(self) -> int:
        return self.__meetingsInSameGroup

    @meetingsInSameGroup.setter
    def meetingsInSameGroup(self, meetingsInSameGroup: int):
        self.__meetingsInSameGroup = meetingsInSameGroup

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def GroupStage58(self):
        return self.__GroupStage58

    @GroupStage58.setter
    def GroupStage58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_GroupStage__GroupStage58", None)
        self.__GroupStage58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groups"):
                opp_val = getattr(old_value, "groups", None)
                if opp_val == self:
                    setattr(old_value, "groups", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groups"):
                opp_val = getattr(value, "groups", None)
                setattr(value, "groups", self)

    @property
    def GroupStage(self):
        return self.__GroupStage

    @GroupStage.setter
    def GroupStage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_GroupStage__GroupStage", None)
        self.__GroupStage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tournament8"):
                opp_val = getattr(old_value, "tournament8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tournament8"):
                opp_val = getattr(value, "tournament8", None)
                if opp_val is None:
                    setattr(value, "tournament8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def groupstage(self):
        return self.__groupstage

    @groupstage.setter
    def groupstage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_GroupStage__groupstage", None)
        self.__groupstage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Group65"):
                    opp_val = getattr(item, "Group65", None)
                    
                    if opp_val == self:
                        setattr(item, "Group65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Group65"):
                    opp_val = getattr(item, "Group65", None)
                    
                    setattr(item, "Group65", self)
                    

    @property
    def groupstages(self):
        return self.__groupstages

    @groupstages.setter
    def groupstages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_GroupStage__groupstages", None)
        self.__groupstages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tournament67"):
                opp_val = getattr(old_value, "Tournament67", None)
                if opp_val == self:
                    setattr(old_value, "Tournament67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tournament67"):
                opp_val = getattr(value, "Tournament67", None)
                setattr(value, "Tournament67", self)

    @property
    def groupstage69(self):
        return self.__groupstage69

    @groupstage69.setter
    def groupstage69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_GroupStage__groupstage69", None)
        self.__groupstage69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "League70"):
                opp_val = getattr(old_value, "League70", None)
                if opp_val == self:
                    setattr(old_value, "League70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "League70"):
                opp_val = getattr(value, "League70", None)
                setattr(value, "League70", self)

    @property
    def GroupStage15(self):
        return self.__GroupStage15

    @GroupStage15.setter
    def GroupStage15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_GroupStage__GroupStage15", None)
        self.__GroupStage15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "league"):
                opp_val = getattr(old_value, "league", None)
                if opp_val == self:
                    setattr(old_value, "league", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "league"):
                opp_val = getattr(value, "league", None)
                setattr(value, "league", self)

class eSport_FinalStage:

    def __init__(self, maxNbGames: int, FinalStage: "eSport_Tournament" = None, FinalStage47: "eSport_Team" = None, FinalStage52: "eSport_Match" = None, finalstage: set["eSport_Match"] = None, finalstages: "eSport_Tournament" = None, finalstages76: set["eSport_Team"] = None):
        self.maxNbGames = maxNbGames
        self.FinalStage = FinalStage
        self.FinalStage47 = FinalStage47
        self.FinalStage52 = FinalStage52
        self.finalstage = finalstage if finalstage is not None else set()
        self.finalstages = finalstages
        self.finalstages76 = finalstages76 if finalstages76 is not None else set()
        
    @property
    def maxNbGames(self) -> int:
        return self.__maxNbGames

    @maxNbGames.setter
    def maxNbGames(self, maxNbGames: int):
        self.__maxNbGames = maxNbGames

    @property
    def FinalStage(self):
        return self.__FinalStage

    @FinalStage.setter
    def FinalStage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_FinalStage__FinalStage", None)
        self.__FinalStage = value
        
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
    def FinalStage52(self):
        return self.__FinalStage52

    @FinalStage52.setter
    def FinalStage52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_FinalStage__FinalStage52", None)
        self.__FinalStage52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "matchs51"):
                opp_val = getattr(old_value, "matchs51", None)
                if opp_val == self:
                    setattr(old_value, "matchs51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "matchs51"):
                opp_val = getattr(value, "matchs51", None)
                setattr(value, "matchs51", self)

    @property
    def finalstage(self):
        return self.__finalstage

    @finalstage.setter
    def finalstage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_FinalStage__finalstage", None)
        self.__finalstage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Match72"):
                    opp_val = getattr(item, "Match72", None)
                    
                    if opp_val == self:
                        setattr(item, "Match72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Match72"):
                    opp_val = getattr(item, "Match72", None)
                    
                    setattr(item, "Match72", self)
                    

    @property
    def finalstages76(self):
        return self.__finalstages76

    @finalstages76.setter
    def finalstages76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_FinalStage__finalstages76", None)
        self.__finalstages76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Team77"):
                    opp_val = getattr(item, "Team77", None)
                    
                    if opp_val == self:
                        setattr(item, "Team77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Team77"):
                    opp_val = getattr(item, "Team77", None)
                    
                    setattr(item, "Team77", self)
                    

    @property
    def FinalStage47(self):
        return self.__FinalStage47

    @FinalStage47.setter
    def FinalStage47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_FinalStage__FinalStage47", None)
        self.__FinalStage47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teams46"):
                opp_val = getattr(old_value, "teams46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teams46"):
                opp_val = getattr(value, "teams46", None)
                if opp_val is None:
                    setattr(value, "teams46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def finalstages(self):
        return self.__finalstages

    @finalstages.setter
    def finalstages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_FinalStage__finalstages", None)
        self.__finalstages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tournament74"):
                opp_val = getattr(old_value, "Tournament74", None)
                if opp_val == self:
                    setattr(old_value, "Tournament74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tournament74"):
                opp_val = getattr(value, "Tournament74", None)
                setattr(value, "Tournament74", self)

class eSport_Zone:

    def __init__(self, name: str, Zone13: "eSport_League" = None, Zone: "eSport_Tournament" = None, Zone24: "eSport_Country" = None, allowedZones: set["eSport_Tournament"] = None, zone: set["eSport_League"] = None, zone30: set["eSport_Country"] = None, zone33: set["eSport_Team"] = None, Zone39: "eSport_Team" = None, eSport_Zone: "eSport_Root" = None):
        self.name = name
        self.Zone13 = Zone13
        self.Zone = Zone
        self.Zone24 = Zone24
        self.allowedZones = allowedZones if allowedZones is not None else set()
        self.zone = zone if zone is not None else set()
        self.zone30 = zone30 if zone30 is not None else set()
        self.zone33 = zone33 if zone33 is not None else set()
        self.Zone39 = Zone39
        self.eSport_Zone = eSport_Zone
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Zone13(self):
        return self.__Zone13

    @Zone13.setter
    def Zone13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Zone__Zone13", None)
        self.__Zone13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leagues"):
                opp_val = getattr(old_value, "leagues", None)
                if opp_val == self:
                    setattr(old_value, "leagues", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leagues"):
                opp_val = getattr(value, "leagues", None)
                setattr(value, "leagues", self)

    @property
    def allowedZones(self):
        return self.__allowedZones

    @allowedZones.setter
    def allowedZones(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Zone__allowedZones", None)
        self.__allowedZones = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tournament27"):
                    opp_val = getattr(item, "Tournament27", None)
                    
                    if opp_val == self:
                        setattr(item, "Tournament27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tournament27"):
                    opp_val = getattr(item, "Tournament27", None)
                    
                    setattr(item, "Tournament27", self)
                    

    @property
    def Zone24(self):
        return self.__Zone24

    @Zone24.setter
    def Zone24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Zone__Zone24", None)
        self.__Zone24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "countries23"):
                opp_val = getattr(old_value, "countries23", None)
                if opp_val == self:
                    setattr(old_value, "countries23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "countries23"):
                opp_val = getattr(value, "countries23", None)
                setattr(value, "countries23", self)

    @property
    def zone30(self):
        return self.__zone30

    @zone30.setter
    def zone30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Zone__zone30", None)
        self.__zone30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Country31"):
                    opp_val = getattr(item, "Country31", None)
                    
                    if opp_val == self:
                        setattr(item, "Country31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Country31"):
                    opp_val = getattr(item, "Country31", None)
                    
                    setattr(item, "Country31", self)
                    

    @property
    def zone33(self):
        return self.__zone33

    @zone33.setter
    def zone33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Zone__zone33", None)
        self.__zone33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Team34"):
                    opp_val = getattr(item, "Team34", None)
                    
                    if opp_val == self:
                        setattr(item, "Team34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Team34"):
                    opp_val = getattr(item, "Team34", None)
                    
                    setattr(item, "Team34", self)
                    

    @property
    def Zone(self):
        return self.__Zone

    @Zone.setter
    def Zone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Zone__Zone", None)
        self.__Zone = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tournaments5"):
                opp_val = getattr(old_value, "tournaments5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tournaments5"):
                opp_val = getattr(value, "tournaments5", None)
                if opp_val is None:
                    setattr(value, "tournaments5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Zone39(self):
        return self.__Zone39

    @Zone39.setter
    def Zone39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Zone__Zone39", None)
        self.__Zone39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teams"):
                opp_val = getattr(old_value, "teams", None)
                if opp_val == self:
                    setattr(old_value, "teams", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teams"):
                opp_val = getattr(value, "teams", None)
                setattr(value, "teams", self)

    @property
    def zone(self):
        return self.__zone

    @zone.setter
    def zone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Zone__zone", None)
        self.__zone = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "League"):
                    opp_val = getattr(item, "League", None)
                    
                    if opp_val == self:
                        setattr(item, "League", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "League"):
                    opp_val = getattr(item, "League", None)
                    
                    setattr(item, "League", self)
                    

    @property
    def eSport_Zone(self):
        return self.__eSport_Zone

    @eSport_Zone.setter
    def eSport_Zone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Zone__eSport_Zone", None)
        self.__eSport_Zone = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSport_Root"):
                opp_val = getattr(old_value, "eSport_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSport_Root"):
                opp_val = getattr(value, "eSport_Root", None)
                if opp_val is None:
                    setattr(value, "eSport_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eSport_Country:

    def __init__(self, name: str, Country19: "eSport_Person" = None, Country: "eSport_Tournament" = None, countries: set["eSport_Tournament"] = None, countries23: "eSport_Zone" = None, country: set["eSport_Person"] = None, Country31: "eSport_Zone" = None, eSport_Country: "eSport_Root" = None):
        self.name = name
        self.Country19 = Country19
        self.Country = Country
        self.countries = countries if countries is not None else set()
        self.countries23 = countries23
        self.country = country if country is not None else set()
        self.Country31 = Country31
        self.eSport_Country = eSport_Country
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Country__country", None)
        self.__country = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def Country19(self):
        return self.__Country19

    @Country19.setter
    def Country19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Country__Country19", None)
        self.__Country19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persons"):
                opp_val = getattr(old_value, "persons", None)
                if opp_val == self:
                    setattr(old_value, "persons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persons"):
                opp_val = getattr(value, "persons", None)
                setattr(value, "persons", self)

    @property
    def countries(self):
        return self.__countries

    @countries.setter
    def countries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Country__countries", None)
        self.__countries = value if value is not None else set()
        
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
    def Country(self):
        return self.__Country

    @Country.setter
    def Country(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Country__Country", None)
        self.__Country = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tournaments"):
                opp_val = getattr(old_value, "tournaments", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tournaments"):
                opp_val = getattr(value, "tournaments", None)
                if opp_val is None:
                    setattr(value, "tournaments", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def countries23(self):
        return self.__countries23

    @countries23.setter
    def countries23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Country__countries23", None)
        self.__countries23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Zone24"):
                opp_val = getattr(old_value, "Zone24", None)
                if opp_val == self:
                    setattr(old_value, "Zone24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Zone24"):
                opp_val = getattr(value, "Zone24", None)
                setattr(value, "Zone24", self)

    @property
    def Country31(self):
        return self.__Country31

    @Country31.setter
    def Country31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Country__Country31", None)
        self.__Country31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zone30"):
                opp_val = getattr(old_value, "zone30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zone30"):
                opp_val = getattr(value, "zone30", None)
                if opp_val is None:
                    setattr(value, "zone30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eSport_Country(self):
        return self.__eSport_Country

    @eSport_Country.setter
    def eSport_Country(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Country__eSport_Country", None)
        self.__eSport_Country = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSport_Root98"):
                opp_val = getattr(old_value, "eSport_Root98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSport_Root98"):
                opp_val = getattr(value, "eSport_Root98", None)
                if opp_val is None:
                    setattr(value, "eSport_Root98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eSport_Tournament:

    def __init__(self, name: str, size: int, type: str, year: int, tournaments: set["eSport_Country"] = None, tournaments5: set["eSport_Zone"] = None, tournament: set["eSport_FinalStage"] = None, tournament8: set["eSport_GroupStage"] = None, tournamentFrom: "eSport_Qualification" = None, tournamentTo: set["eSport_Qualification"] = None, Tournament: "eSport_Country" = None, Tournament27: "eSport_Zone" = None, Tournament67: "eSport_GroupStage" = None, eSport_Tournament: "eSport_Root" = None, Tournament74: "eSport_FinalStage" = None, Tournament79: "eSport_Qualification" = None, Tournament81: "eSport_Qualification" = None):
        self.name = name
        self.size = size
        self.type = type
        self.year = year
        self.tournaments = tournaments if tournaments is not None else set()
        self.tournaments5 = tournaments5 if tournaments5 is not None else set()
        self.tournament = tournament if tournament is not None else set()
        self.tournament8 = tournament8 if tournament8 is not None else set()
        self.tournamentFrom = tournamentFrom
        self.tournamentTo = tournamentTo if tournamentTo is not None else set()
        self.Tournament = Tournament
        self.Tournament27 = Tournament27
        self.Tournament67 = Tournament67
        self.eSport_Tournament = eSport_Tournament
        self.Tournament74 = Tournament74
        self.Tournament79 = Tournament79
        self.Tournament81 = Tournament81
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def tournamentTo(self):
        return self.__tournamentTo

    @tournamentTo.setter
    def tournamentTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__tournamentTo", None)
        self.__tournamentTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Qualification11"):
                    opp_val = getattr(item, "Qualification11", None)
                    
                    if opp_val == self:
                        setattr(item, "Qualification11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Qualification11"):
                    opp_val = getattr(item, "Qualification11", None)
                    
                    setattr(item, "Qualification11", self)
                    

    @property
    def Tournament81(self):
        return self.__Tournament81

    @Tournament81.setter
    def Tournament81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__Tournament81", None)
        self.__Tournament81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualifiesFrom"):
                opp_val = getattr(old_value, "qualifiesFrom", None)
                if opp_val == self:
                    setattr(old_value, "qualifiesFrom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualifiesFrom"):
                opp_val = getattr(value, "qualifiesFrom", None)
                setattr(value, "qualifiesFrom", self)

    @property
    def tournaments(self):
        return self.__tournaments

    @tournaments.setter
    def tournaments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__tournaments", None)
        self.__tournaments = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Country"):
                    opp_val = getattr(item, "Country", None)
                    
                    if opp_val == self:
                        setattr(item, "Country", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Country"):
                    opp_val = getattr(item, "Country", None)
                    
                    setattr(item, "Country", self)
                    

    @property
    def eSport_Tournament(self):
        return self.__eSport_Tournament

    @eSport_Tournament.setter
    def eSport_Tournament(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__eSport_Tournament", None)
        self.__eSport_Tournament = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSport_Root87"):
                opp_val = getattr(old_value, "eSport_Root87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSport_Root87"):
                opp_val = getattr(value, "eSport_Root87", None)
                if opp_val is None:
                    setattr(value, "eSport_Root87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Tournament67(self):
        return self.__Tournament67

    @Tournament67.setter
    def Tournament67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__Tournament67", None)
        self.__Tournament67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groupstages"):
                opp_val = getattr(old_value, "groupstages", None)
                if opp_val == self:
                    setattr(old_value, "groupstages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groupstages"):
                opp_val = getattr(value, "groupstages", None)
                setattr(value, "groupstages", self)

    @property
    def Tournament(self):
        return self.__Tournament

    @Tournament.setter
    def Tournament(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__Tournament", None)
        self.__Tournament = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "countries"):
                opp_val = getattr(old_value, "countries", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "countries"):
                opp_val = getattr(value, "countries", None)
                if opp_val is None:
                    setattr(value, "countries", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Tournament74(self):
        return self.__Tournament74

    @Tournament74.setter
    def Tournament74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__Tournament74", None)
        self.__Tournament74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finalstages"):
                opp_val = getattr(old_value, "finalstages", None)
                if opp_val == self:
                    setattr(old_value, "finalstages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finalstages"):
                opp_val = getattr(value, "finalstages", None)
                setattr(value, "finalstages", self)

    @property
    def tournament(self):
        return self.__tournament

    @tournament.setter
    def tournament(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__tournament", None)
        self.__tournament = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FinalStage"):
                    opp_val = getattr(item, "FinalStage", None)
                    
                    if opp_val == self:
                        setattr(item, "FinalStage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FinalStage"):
                    opp_val = getattr(item, "FinalStage", None)
                    
                    setattr(item, "FinalStage", self)
                    

    @property
    def Tournament79(self):
        return self.__Tournament79

    @Tournament79.setter
    def Tournament79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__Tournament79", None)
        self.__Tournament79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualifiesFor"):
                opp_val = getattr(old_value, "qualifiesFor", None)
                if opp_val == self:
                    setattr(old_value, "qualifiesFor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualifiesFor"):
                opp_val = getattr(value, "qualifiesFor", None)
                setattr(value, "qualifiesFor", self)

    @property
    def tournamentFrom(self):
        return self.__tournamentFrom

    @tournamentFrom.setter
    def tournamentFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__tournamentFrom", None)
        self.__tournamentFrom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Qualification"):
                opp_val = getattr(old_value, "Qualification", None)
                if opp_val == self:
                    setattr(old_value, "Qualification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Qualification"):
                opp_val = getattr(value, "Qualification", None)
                setattr(value, "Qualification", self)

    @property
    def tournaments5(self):
        return self.__tournaments5

    @tournaments5.setter
    def tournaments5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__tournaments5", None)
        self.__tournaments5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Zone"):
                    opp_val = getattr(item, "Zone", None)
                    
                    if opp_val == self:
                        setattr(item, "Zone", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Zone"):
                    opp_val = getattr(item, "Zone", None)
                    
                    setattr(item, "Zone", self)
                    

    @property
    def tournament8(self):
        return self.__tournament8

    @tournament8.setter
    def tournament8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__tournament8", None)
        self.__tournament8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GroupStage"):
                    opp_val = getattr(item, "GroupStage", None)
                    
                    if opp_val == self:
                        setattr(item, "GroupStage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GroupStage"):
                    opp_val = getattr(item, "GroupStage", None)
                    
                    setattr(item, "GroupStage", self)
                    

    @property
    def Tournament27(self):
        return self.__Tournament27

    @Tournament27.setter
    def Tournament27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Tournament__Tournament27", None)
        self.__Tournament27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "allowedZones"):
                opp_val = getattr(old_value, "allowedZones", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "allowedZones"):
                opp_val = getattr(value, "allowedZones", None)
                if opp_val is None:
                    setattr(value, "allowedZones", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eSport_Person(ABC):

    def __init__(self, name: str, age: int, description: str, persons: "eSport_Country" = None, eSport_Person: set["eSport_Capacity"] = None, Person: "eSport_Country" = None, eSport_Person94: "eSport_Root" = None):
        self.name = name
        self.age = age
        self.description = description
        self.persons = persons
        self.eSport_Person = eSport_Person if eSport_Person is not None else set()
        self.Person = Person
        self.eSport_Person94 = eSport_Person94
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "country"):
                opp_val = getattr(old_value, "country", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "country"):
                opp_val = getattr(value, "country", None)
                if opp_val is None:
                    setattr(value, "country", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Person__persons", None)
        self.__persons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Country19"):
                opp_val = getattr(old_value, "Country19", None)
                if opp_val == self:
                    setattr(old_value, "Country19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Country19"):
                opp_val = getattr(value, "Country19", None)
                setattr(value, "Country19", self)

    @property
    def eSport_Person(self):
        return self.__eSport_Person

    @eSport_Person.setter
    def eSport_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Person__eSport_Person", None)
        self.__eSport_Person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eSport_Capacity"):
                    opp_val = getattr(item, "eSport_Capacity", None)
                    
                    if opp_val == self:
                        setattr(item, "eSport_Capacity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eSport_Capacity"):
                    opp_val = getattr(item, "eSport_Capacity", None)
                    
                    setattr(item, "eSport_Capacity", self)
                    

    @property
    def eSport_Person94(self):
        return self.__eSport_Person94

    @eSport_Person94.setter
    def eSport_Person94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Person__eSport_Person94", None)
        self.__eSport_Person94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSport_Root93"):
                opp_val = getattr(old_value, "eSport_Root93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSport_Root93"):
                opp_val = getattr(value, "eSport_Root93", None)
                if opp_val is None:
                    setattr(value, "eSport_Root93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eSport_Capacity:

    def __init__(self, type: str, value: int, eSport_Capacity: "eSport_Person" = None):
        self.type = type
        self.value = value
        self.eSport_Capacity = eSport_Capacity
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def eSport_Capacity(self):
        return self.__eSport_Capacity

    @eSport_Capacity.setter
    def eSport_Capacity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Capacity__eSport_Capacity", None)
        self.__eSport_Capacity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSport_Person"):
                opp_val = getattr(old_value, "eSport_Person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSport_Person"):
                opp_val = getattr(value, "eSport_Person", None)
                if opp_val is None:
                    setattr(value, "eSport_Person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eSport_Team:

    def __init__(self, championshipPoints: int, name: str, Team: "eSport_Player" = None, Team2: "eSport_Coach" = None, teamWinner: set["eSport_Match"] = None, teamLoser: set["eSport_Match"] = None, teams46: set["eSport_FinalStage"] = None, Team34: "eSport_Zone" = None, team: set["eSport_Player"] = None, team37: "eSport_Coach" = None, teams: "eSport_Zone" = None, teams41: set["eSport_Group"] = None, Team63: "eSport_Group" = None, Team54: "eSport_Match" = None, Team56: "eSport_Match" = None, eSport_Team: "eSport_Root" = None, Team77: "eSport_FinalStage" = None):
        self.championshipPoints = championshipPoints
        self.name = name
        self.Team = Team
        self.Team2 = Team2
        self.teamWinner = teamWinner if teamWinner is not None else set()
        self.teamLoser = teamLoser if teamLoser is not None else set()
        self.teams46 = teams46 if teams46 is not None else set()
        self.Team34 = Team34
        self.team = team if team is not None else set()
        self.team37 = team37
        self.teams = teams
        self.teams41 = teams41 if teams41 is not None else set()
        self.Team63 = Team63
        self.Team54 = Team54
        self.Team56 = Team56
        self.eSport_Team = eSport_Team
        self.Team77 = Team77
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def championshipPoints(self) -> int:
        return self.__championshipPoints

    @championshipPoints.setter
    def championshipPoints(self, championshipPoints: int):
        self.__championshipPoints = championshipPoints

    @property
    def teamLoser(self):
        return self.__teamLoser

    @teamLoser.setter
    def teamLoser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__teamLoser", None)
        self.__teamLoser = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Match44"):
                    opp_val = getattr(item, "Match44", None)
                    
                    if opp_val == self:
                        setattr(item, "Match44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Match44"):
                    opp_val = getattr(item, "Match44", None)
                    
                    setattr(item, "Match44", self)
                    

    @property
    def Team54(self):
        return self.__Team54

    @Team54.setter
    def Team54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__Team54", None)
        self.__Team54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "matchsWon"):
                opp_val = getattr(old_value, "matchsWon", None)
                if opp_val == self:
                    setattr(old_value, "matchsWon", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "matchsWon"):
                opp_val = getattr(value, "matchsWon", None)
                setattr(value, "matchsWon", self)

    @property
    def teams46(self):
        return self.__teams46

    @teams46.setter
    def teams46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__teams46", None)
        self.__teams46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FinalStage47"):
                    opp_val = getattr(item, "FinalStage47", None)
                    
                    if opp_val == self:
                        setattr(item, "FinalStage47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FinalStage47"):
                    opp_val = getattr(item, "FinalStage47", None)
                    
                    setattr(item, "FinalStage47", self)
                    

    @property
    def teams41(self):
        return self.__teams41

    @teams41.setter
    def teams41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__teams41", None)
        self.__teams41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    if opp_val == self:
                        setattr(item, "Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    setattr(item, "Group", self)
                    

    @property
    def team37(self):
        return self.__team37

    @team37.setter
    def team37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__team37", None)
        self.__team37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Coach"):
                opp_val = getattr(old_value, "Coach", None)
                if opp_val == self:
                    setattr(old_value, "Coach", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Coach"):
                opp_val = getattr(value, "Coach", None)
                setattr(value, "Coach", self)

    @property
    def teamWinner(self):
        return self.__teamWinner

    @teamWinner.setter
    def teamWinner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__teamWinner", None)
        self.__teamWinner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Match"):
                    opp_val = getattr(item, "Match", None)
                    
                    if opp_val == self:
                        setattr(item, "Match", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Match"):
                    opp_val = getattr(item, "Match", None)
                    
                    setattr(item, "Match", self)
                    

    @property
    def Team63(self):
        return self.__Team63

    @Team63.setter
    def Team63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__Team63", None)
        self.__Team63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groups62"):
                opp_val = getattr(old_value, "groups62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groups62"):
                opp_val = getattr(value, "groups62", None)
                if opp_val is None:
                    setattr(value, "groups62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eSport_Team(self):
        return self.__eSport_Team

    @eSport_Team.setter
    def eSport_Team(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__eSport_Team", None)
        self.__eSport_Team = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSport_Root91"):
                opp_val = getattr(old_value, "eSport_Root91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSport_Root91"):
                opp_val = getattr(value, "eSport_Root91", None)
                if opp_val is None:
                    setattr(value, "eSport_Root91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Team77(self):
        return self.__Team77

    @Team77.setter
    def Team77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__Team77", None)
        self.__Team77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finalstages76"):
                opp_val = getattr(old_value, "finalstages76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finalstages76"):
                opp_val = getattr(value, "finalstages76", None)
                if opp_val is None:
                    setattr(value, "finalstages76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def teams(self):
        return self.__teams

    @teams.setter
    def teams(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__teams", None)
        self.__teams = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Zone39"):
                opp_val = getattr(old_value, "Zone39", None)
                if opp_val == self:
                    setattr(old_value, "Zone39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Zone39"):
                opp_val = getattr(value, "Zone39", None)
                setattr(value, "Zone39", self)

    @property
    def Team56(self):
        return self.__Team56

    @Team56.setter
    def Team56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__Team56", None)
        self.__Team56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "matchsLost"):
                opp_val = getattr(old_value, "matchsLost", None)
                if opp_val == self:
                    setattr(old_value, "matchsLost", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "matchsLost"):
                opp_val = getattr(value, "matchsLost", None)
                setattr(value, "matchsLost", self)

    @property
    def Team(self):
        return self.__Team

    @Team.setter
    def Team(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__Team", None)
        self.__Team = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players"):
                opp_val = getattr(old_value, "players", None)
                if opp_val == self:
                    setattr(old_value, "players", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players"):
                opp_val = getattr(value, "players", None)
                setattr(value, "players", self)

    @property
    def Team2(self):
        return self.__Team2

    @Team2.setter
    def Team2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__Team2", None)
        self.__Team2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coach"):
                opp_val = getattr(old_value, "coach", None)
                if opp_val == self:
                    setattr(old_value, "coach", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coach"):
                opp_val = getattr(value, "coach", None)
                setattr(value, "coach", self)

    @property
    def Team34(self):
        return self.__Team34

    @Team34.setter
    def Team34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__Team34", None)
        self.__Team34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zone33"):
                opp_val = getattr(old_value, "zone33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zone33"):
                opp_val = getattr(value, "zone33", None)
                if opp_val is None:
                    setattr(value, "zone33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Team__team", None)
        self.__team = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Player"):
                    opp_val = getattr(item, "Player", None)
                    
                    if opp_val == self:
                        setattr(item, "Player", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Player"):
                    opp_val = getattr(item, "Player", None)
                    
                    setattr(item, "Player", self)
                    

class Person:

    pass
class eSport_Coach(Person):

    pass
class eSport_Player(Person):

    def __init__(self, position: str, players: "eSport_Team" = None, Player: "eSport_Team" = None):
        self.position = position
        self.players = players
        self.Player = Player
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def Player(self):
        return self.__Player

    @Player.setter
    def Player(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Player__Player", None)
        self.__Player = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "team"):
                opp_val = getattr(old_value, "team", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "team"):
                opp_val = getattr(value, "team", None)
                if opp_val is None:
                    setattr(value, "team", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eSport_Player__players", None)
        self.__players = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Team"):
                opp_val = getattr(old_value, "Team", None)
                if opp_val == self:
                    setattr(old_value, "Team", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Team"):
                opp_val = getattr(value, "Team", None)
                setattr(value, "Team", self)
