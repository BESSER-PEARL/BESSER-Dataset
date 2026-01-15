from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class HowOut(Enum):
    Bowled = "Bowled"
    Caught = "Caught"
    Lbw = "Lbw"
    Run_Out = "Run_Out"
    Stumped = "Stumped"
class BallType(Enum):
    three_runs = "three_runs"
    four_runs = "four_runs"
    six_runs = "six_runs"
    dot_ball = "dot_ball"
    one_run = "one_run"
    two_runs = "two_runs"
class ExtraType(Enum):
    Wide = "Wide"
    NoBall = "NoBall"
    Bye = "Bye"
    LegBye = "LegBye"


############################################
# Definition of Classes
############################################

class Ball:

    pass
class model_ExtraBall(Ball):

    def __init__(self, extraType: str, isValidBall: str):
        self.extraType = extraType
        self.isValidBall = isValidBall
        
    @property
    def isValidBall(self) -> str:
        return self.__isValidBall

    @isValidBall.setter
    def isValidBall(self, isValidBall: str):
        self.__isValidBall = isValidBall

    @property
    def extraType(self) -> str:
        return self.__extraType

    @extraType.setter
    def extraType(self, extraType: str):
        self.__extraType = extraType

class model_WicketBall(Ball):

    def __init__(self, howOut: str, WicketBall: "model_Player" = None, model_WicketBall: "model_Player" = None, wicketball: "model_Player" = None):
        self.howOut = howOut
        self.WicketBall = WicketBall
        self.model_WicketBall = model_WicketBall
        self.wicketball = wicketball
        
    @property
    def howOut(self) -> str:
        return self.__howOut

    @howOut.setter
    def howOut(self, howOut: str):
        self.__howOut = howOut

    @property
    def WicketBall(self):
        return self.__WicketBall

    @WicketBall.setter
    def WicketBall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_WicketBall__WicketBall", None)
        self.__WicketBall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playerOut"):
                opp_val = getattr(old_value, "playerOut", None)
                if opp_val == self:
                    setattr(old_value, "playerOut", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playerOut"):
                opp_val = getattr(value, "playerOut", None)
                setattr(value, "playerOut", self)

    @property
    def wicketball(self):
        return self.__wicketball

    @wicketball.setter
    def wicketball(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_WicketBall__wicketball", None)
        self.__wicketball = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Player30"):
                opp_val = getattr(old_value, "Player30", None)
                if opp_val == self:
                    setattr(old_value, "Player30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Player30"):
                opp_val = getattr(value, "Player30", None)
                setattr(value, "Player30", self)

    @property
    def model_WicketBall(self):
        return self.__model_WicketBall

    @model_WicketBall.setter
    def model_WicketBall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_WicketBall__model_WicketBall", None)
        self.__model_WicketBall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Player28"):
                opp_val = getattr(old_value, "model_Player28", None)
                if opp_val == self:
                    setattr(old_value, "model_Player28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Player28"):
                opp_val = getattr(value, "model_Player28", None)
                setattr(value, "model_Player28", self)

class model_Innings:

    def __init__(self, noOvers: int, total: int, wicketsDown: int, overCount: str, Summary: str, innings: set["model_Over"] = None, model_Innings5: "model_Team" = None, model_Innings8: "model_Team" = None, model_Innings11: "model_Player" = None, model_Innings13: "model_Player" = None, model_Innings: "model_Game" = None, Innings: "model_Over" = None):
        self.noOvers = noOvers
        self.total = total
        self.wicketsDown = wicketsDown
        self.overCount = overCount
        self.Summary = Summary
        self.innings = innings if innings is not None else set()
        self.model_Innings5 = model_Innings5
        self.model_Innings8 = model_Innings8
        self.model_Innings11 = model_Innings11
        self.model_Innings13 = model_Innings13
        self.model_Innings = model_Innings
        self.Innings = Innings
        
    @property
    def wicketsDown(self) -> int:
        return self.__wicketsDown

    @wicketsDown.setter
    def wicketsDown(self, wicketsDown: int):
        self.__wicketsDown = wicketsDown

    @property
    def Summary(self) -> str:
        return self.__Summary

    @Summary.setter
    def Summary(self, Summary: str):
        self.__Summary = Summary

    @property
    def total(self) -> int:
        return self.__total

    @total.setter
    def total(self, total: int):
        self.__total = total

    @property
    def noOvers(self) -> int:
        return self.__noOvers

    @noOvers.setter
    def noOvers(self, noOvers: int):
        self.__noOvers = noOvers

    @property
    def overCount(self) -> str:
        return self.__overCount

    @overCount.setter
    def overCount(self, overCount: str):
        self.__overCount = overCount

    @property
    def model_Innings(self):
        return self.__model_Innings

    @model_Innings.setter
    def model_Innings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Innings__model_Innings", None)
        self.__model_Innings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Game"):
                opp_val = getattr(old_value, "model_Game", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Game"):
                opp_val = getattr(value, "model_Game", None)
                if opp_val is None:
                    setattr(value, "model_Game", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Innings11(self):
        return self.__model_Innings11

    @model_Innings11.setter
    def model_Innings11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Innings__model_Innings11", None)
        self.__model_Innings11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Player"):
                opp_val = getattr(old_value, "model_Player", None)
                if opp_val == self:
                    setattr(old_value, "model_Player", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Player"):
                opp_val = getattr(value, "model_Player", None)
                setattr(value, "model_Player", self)

    @property
    def model_Innings8(self):
        return self.__model_Innings8

    @model_Innings8.setter
    def model_Innings8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Innings__model_Innings8", None)
        self.__model_Innings8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Team9"):
                opp_val = getattr(old_value, "model_Team9", None)
                if opp_val == self:
                    setattr(old_value, "model_Team9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Team9"):
                opp_val = getattr(value, "model_Team9", None)
                setattr(value, "model_Team9", self)

    @property
    def model_Innings13(self):
        return self.__model_Innings13

    @model_Innings13.setter
    def model_Innings13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Innings__model_Innings13", None)
        self.__model_Innings13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Player14"):
                opp_val = getattr(old_value, "model_Player14", None)
                if opp_val == self:
                    setattr(old_value, "model_Player14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Player14"):
                opp_val = getattr(value, "model_Player14", None)
                setattr(value, "model_Player14", self)

    @property
    def innings(self):
        return self.__innings

    @innings.setter
    def innings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Innings__innings", None)
        self.__innings = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Over"):
                    opp_val = getattr(item, "Over", None)
                    
                    if opp_val == self:
                        setattr(item, "Over", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Over"):
                    opp_val = getattr(item, "Over", None)
                    
                    setattr(item, "Over", self)
                    

    @property
    def model_Innings5(self):
        return self.__model_Innings5

    @model_Innings5.setter
    def model_Innings5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Innings__model_Innings5", None)
        self.__model_Innings5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Team6"):
                opp_val = getattr(old_value, "model_Team6", None)
                if opp_val == self:
                    setattr(old_value, "model_Team6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Team6"):
                opp_val = getattr(value, "model_Team6", None)
                setattr(value, "model_Team6", self)

    @property
    def Innings(self):
        return self.__Innings

    @Innings.setter
    def Innings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Innings__Innings", None)
        self.__Innings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "overs"):
                opp_val = getattr(old_value, "overs", None)
                if opp_val == self:
                    setattr(old_value, "overs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "overs"):
                opp_val = getattr(value, "overs", None)
                setattr(value, "overs", self)

    def bowlBall(self):
        # TODO: Implement bowlBall method
        pass

    def newOver(self, bowler: str) -> str:
        # TODO: Implement newOver method
        pass

class model_Game:

    def __init__(self, date: date, venue: str, model_Game2: set["model_Team"] = None, model_Game: set["model_Innings"] = None):
        self.date = date
        self.venue = venue
        self.model_Game2 = model_Game2 if model_Game2 is not None else set()
        self.model_Game = model_Game if model_Game is not None else set()
        
    @property
    def venue(self) -> str:
        return self.__venue

    @venue.setter
    def venue(self, venue: str):
        self.__venue = venue

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def model_Game2(self):
        return self.__model_Game2

    @model_Game2.setter
    def model_Game2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Game__model_Game2", None)
        self.__model_Game2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Team"):
                    opp_val = getattr(item, "model_Team", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Team", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Team"):
                    opp_val = getattr(item, "model_Team", None)
                    
                    setattr(item, "model_Team", self)
                    

    @property
    def model_Game(self):
        return self.__model_Game

    @model_Game.setter
    def model_Game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Game__model_Game", None)
        self.__model_Game = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Innings"):
                    opp_val = getattr(item, "model_Innings", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Innings", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Innings"):
                    opp_val = getattr(item, "model_Innings", None)
                    
                    setattr(item, "model_Innings", self)
                    

class model_Ball:

    def __init__(self, runs: str, runValue: int, switchEnds: str, model_Ball: "model_Over" = None, Ball: "model_Player" = None, ballsFaced: "model_Player" = None):
        self.runs = runs
        self.runValue = runValue
        self.switchEnds = switchEnds
        self.model_Ball = model_Ball
        self.Ball = Ball
        self.ballsFaced = ballsFaced
        
    @property
    def runValue(self) -> int:
        return self.__runValue

    @runValue.setter
    def runValue(self, runValue: int):
        self.__runValue = runValue

    @property
    def runs(self) -> str:
        return self.__runs

    @runs.setter
    def runs(self, runs: str):
        self.__runs = runs

    @property
    def switchEnds(self) -> str:
        return self.__switchEnds

    @switchEnds.setter
    def switchEnds(self, switchEnds: str):
        self.__switchEnds = switchEnds

    @property
    def model_Ball(self):
        return self.__model_Ball

    @model_Ball.setter
    def model_Ball(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Ball__model_Ball", None)
        self.__model_Ball = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Over"):
                opp_val = getattr(old_value, "model_Over", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Over"):
                opp_val = getattr(value, "model_Over", None)
                if opp_val is None:
                    setattr(value, "model_Over", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Ball(self):
        return self.__Ball

    @Ball.setter
    def Ball(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Ball__Ball", None)
        self.__Ball = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "batsman"):
                opp_val = getattr(old_value, "batsman", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "batsman"):
                opp_val = getattr(value, "batsman", None)
                if opp_val is None:
                    setattr(value, "batsman", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ballsFaced(self):
        return self.__ballsFaced

    @ballsFaced.setter
    def ballsFaced(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Ball__ballsFaced", None)
        self.__ballsFaced = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Player19"):
                opp_val = getattr(old_value, "Player19", None)
                if opp_val == self:
                    setattr(old_value, "Player19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Player19"):
                opp_val = getattr(value, "Player19", None)
                setattr(value, "Player19", self)

class model_Player:

    def __init__(self, name: str, runsScored: int, noOversBowled: str, noBallsFaced: int, howOut: str, model_Player: "model_Innings" = None, model_Player14: "model_Innings" = None, batsman: set["model_Ball"] = None, bowler: set["model_Over"] = None, playerOut: "model_WicketBall" = None, model_Player26: "model_Team" = None, model_Player28: "model_WicketBall" = None, Player30: "model_WicketBall" = None, Player: "model_Over" = None, Player19: "model_Ball" = None):
        self.name = name
        self.runsScored = runsScored
        self.noOversBowled = noOversBowled
        self.noBallsFaced = noBallsFaced
        self.howOut = howOut
        self.model_Player = model_Player
        self.model_Player14 = model_Player14
        self.batsman = batsman if batsman is not None else set()
        self.bowler = bowler if bowler is not None else set()
        self.playerOut = playerOut
        self.model_Player26 = model_Player26
        self.model_Player28 = model_Player28
        self.Player30 = Player30
        self.Player = Player
        self.Player19 = Player19
        
    @property
    def howOut(self) -> str:
        return self.__howOut

    @howOut.setter
    def howOut(self, howOut: str):
        self.__howOut = howOut

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def runsScored(self) -> int:
        return self.__runsScored

    @runsScored.setter
    def runsScored(self, runsScored: int):
        self.__runsScored = runsScored

    @property
    def noBallsFaced(self) -> int:
        return self.__noBallsFaced

    @noBallsFaced.setter
    def noBallsFaced(self, noBallsFaced: int):
        self.__noBallsFaced = noBallsFaced

    @property
    def noOversBowled(self) -> str:
        return self.__noOversBowled

    @noOversBowled.setter
    def noOversBowled(self, noOversBowled: str):
        self.__noOversBowled = noOversBowled

    @property
    def model_Player26(self):
        return self.__model_Player26

    @model_Player26.setter
    def model_Player26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Player__model_Player26", None)
        self.__model_Player26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Team25"):
                opp_val = getattr(old_value, "model_Team25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Team25"):
                opp_val = getattr(value, "model_Team25", None)
                if opp_val is None:
                    setattr(value, "model_Team25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def batsman(self):
        return self.__batsman

    @batsman.setter
    def batsman(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Player__batsman", None)
        self.__batsman = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ball"):
                    opp_val = getattr(item, "Ball", None)
                    
                    if opp_val == self:
                        setattr(item, "Ball", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ball"):
                    opp_val = getattr(item, "Ball", None)
                    
                    setattr(item, "Ball", self)
                    

    @property
    def model_Player28(self):
        return self.__model_Player28

    @model_Player28.setter
    def model_Player28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Player__model_Player28", None)
        self.__model_Player28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_WicketBall"):
                opp_val = getattr(old_value, "model_WicketBall", None)
                if opp_val == self:
                    setattr(old_value, "model_WicketBall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_WicketBall"):
                opp_val = getattr(value, "model_WicketBall", None)
                setattr(value, "model_WicketBall", self)

    @property
    def model_Player(self):
        return self.__model_Player

    @model_Player.setter
    def model_Player(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Player__model_Player", None)
        self.__model_Player = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Innings11"):
                opp_val = getattr(old_value, "model_Innings11", None)
                if opp_val == self:
                    setattr(old_value, "model_Innings11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Innings11"):
                opp_val = getattr(value, "model_Innings11", None)
                setattr(value, "model_Innings11", self)

    @property
    def bowler(self):
        return self.__bowler

    @bowler.setter
    def bowler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Player__bowler", None)
        self.__bowler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Over22"):
                    opp_val = getattr(item, "Over22", None)
                    
                    if opp_val == self:
                        setattr(item, "Over22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Over22"):
                    opp_val = getattr(item, "Over22", None)
                    
                    setattr(item, "Over22", self)
                    

    @property
    def Player30(self):
        return self.__Player30

    @Player30.setter
    def Player30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Player__Player30", None)
        self.__Player30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wicketball"):
                opp_val = getattr(old_value, "wicketball", None)
                if opp_val == self:
                    setattr(old_value, "wicketball", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wicketball"):
                opp_val = getattr(value, "wicketball", None)
                setattr(value, "wicketball", self)

    @property
    def Player(self):
        return self.__Player

    @Player.setter
    def Player(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Player__Player", None)
        self.__Player = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oversBowled"):
                opp_val = getattr(old_value, "oversBowled", None)
                if opp_val == self:
                    setattr(old_value, "oversBowled", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oversBowled"):
                opp_val = getattr(value, "oversBowled", None)
                setattr(value, "oversBowled", self)

    @property
    def playerOut(self):
        return self.__playerOut

    @playerOut.setter
    def playerOut(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Player__playerOut", None)
        self.__playerOut = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WicketBall"):
                opp_val = getattr(old_value, "WicketBall", None)
                if opp_val == self:
                    setattr(old_value, "WicketBall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WicketBall"):
                opp_val = getattr(value, "WicketBall", None)
                setattr(value, "WicketBall", self)

    @property
    def Player19(self):
        return self.__Player19

    @Player19.setter
    def Player19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Player__Player19", None)
        self.__Player19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ballsFaced"):
                opp_val = getattr(old_value, "ballsFaced", None)
                if opp_val == self:
                    setattr(old_value, "ballsFaced", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ballsFaced"):
                opp_val = getattr(value, "ballsFaced", None)
                setattr(value, "ballsFaced", self)

    @property
    def model_Player14(self):
        return self.__model_Player14

    @model_Player14.setter
    def model_Player14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Player__model_Player14", None)
        self.__model_Player14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Innings13"):
                opp_val = getattr(old_value, "model_Innings13", None)
                if opp_val == self:
                    setattr(old_value, "model_Innings13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Innings13"):
                opp_val = getattr(value, "model_Innings13", None)
                setattr(value, "model_Innings13", self)

class model_Over:

    def __init__(self, runs: int, BALLS_IN_OVER: int, validBalls: int, isComplete: bool, Over: "model_Innings" = None, model_Over: set["model_Ball"] = None, Over22: "model_Player" = None, overs: "model_Innings" = None, oversBowled: "model_Player" = None):
        self.runs = runs
        self.BALLS_IN_OVER = BALLS_IN_OVER
        self.validBalls = validBalls
        self.isComplete = isComplete
        self.Over = Over
        self.model_Over = model_Over if model_Over is not None else set()
        self.Over22 = Over22
        self.overs = overs
        self.oversBowled = oversBowled
        
    @property
    def validBalls(self) -> int:
        return self.__validBalls

    @validBalls.setter
    def validBalls(self, validBalls: int):
        self.__validBalls = validBalls

    @property
    def isComplete(self) -> bool:
        return self.__isComplete

    @isComplete.setter
    def isComplete(self, isComplete: bool):
        self.__isComplete = isComplete

    @property
    def runs(self) -> int:
        return self.__runs

    @runs.setter
    def runs(self, runs: int):
        self.__runs = runs

    @property
    def BALLS_IN_OVER(self) -> int:
        return self.__BALLS_IN_OVER

    @BALLS_IN_OVER.setter
    def BALLS_IN_OVER(self, BALLS_IN_OVER: int):
        self.__BALLS_IN_OVER = BALLS_IN_OVER

    @property
    def Over22(self):
        return self.__Over22

    @Over22.setter
    def Over22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Over__Over22", None)
        self.__Over22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowler"):
                opp_val = getattr(old_value, "bowler", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowler"):
                opp_val = getattr(value, "bowler", None)
                if opp_val is None:
                    setattr(value, "bowler", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oversBowled(self):
        return self.__oversBowled

    @oversBowled.setter
    def oversBowled(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Over__oversBowled", None)
        self.__oversBowled = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Player"):
                opp_val = getattr(old_value, "Player", None)
                if opp_val == self:
                    setattr(old_value, "Player", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Player"):
                opp_val = getattr(value, "Player", None)
                setattr(value, "Player", self)

    @property
    def Over(self):
        return self.__Over

    @Over.setter
    def Over(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Over__Over", None)
        self.__Over = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "innings"):
                opp_val = getattr(old_value, "innings", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "innings"):
                opp_val = getattr(value, "innings", None)
                if opp_val is None:
                    setattr(value, "innings", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def overs(self):
        return self.__overs

    @overs.setter
    def overs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Over__overs", None)
        self.__overs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Innings"):
                opp_val = getattr(old_value, "Innings", None)
                if opp_val == self:
                    setattr(old_value, "Innings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Innings"):
                opp_val = getattr(value, "Innings", None)
                setattr(value, "Innings", self)

    @property
    def model_Over(self):
        return self.__model_Over

    @model_Over.setter
    def model_Over(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Over__model_Over", None)
        self.__model_Over = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Ball"):
                    opp_val = getattr(item, "model_Ball", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Ball", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Ball"):
                    opp_val = getattr(item, "model_Ball", None)
                    
                    setattr(item, "model_Ball", self)
                    

class model_Team:

    def __init__(self, name: str, model_Team: "model_Game" = None, model_Team6: "model_Innings" = None, model_Team9: "model_Innings" = None, model_Team25: set["model_Player"] = None):
        self.name = name
        self.model_Team = model_Team
        self.model_Team6 = model_Team6
        self.model_Team9 = model_Team9
        self.model_Team25 = model_Team25 if model_Team25 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Team6(self):
        return self.__model_Team6

    @model_Team6.setter
    def model_Team6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Team__model_Team6", None)
        self.__model_Team6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Innings5"):
                opp_val = getattr(old_value, "model_Innings5", None)
                if opp_val == self:
                    setattr(old_value, "model_Innings5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Innings5"):
                opp_val = getattr(value, "model_Innings5", None)
                setattr(value, "model_Innings5", self)

    @property
    def model_Team25(self):
        return self.__model_Team25

    @model_Team25.setter
    def model_Team25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Team__model_Team25", None)
        self.__model_Team25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Player26"):
                    opp_val = getattr(item, "model_Player26", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Player26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Player26"):
                    opp_val = getattr(item, "model_Player26", None)
                    
                    setattr(item, "model_Player26", self)
                    

    @property
    def model_Team9(self):
        return self.__model_Team9

    @model_Team9.setter
    def model_Team9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Team__model_Team9", None)
        self.__model_Team9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Innings8"):
                opp_val = getattr(old_value, "model_Innings8", None)
                if opp_val == self:
                    setattr(old_value, "model_Innings8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Innings8"):
                opp_val = getattr(value, "model_Innings8", None)
                setattr(value, "model_Innings8", self)

    @property
    def model_Team(self):
        return self.__model_Team

    @model_Team.setter
    def model_Team(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Team__model_Team", None)
        self.__model_Team = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Game2"):
                opp_val = getattr(old_value, "model_Game2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Game2"):
                opp_val = getattr(value, "model_Game2", None)
                if opp_val is None:
                    setattr(value, "model_Game2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
