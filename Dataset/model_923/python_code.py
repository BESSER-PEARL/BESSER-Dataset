from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SequenceType(Enum):
    startToStart = "startToStart"
    finishToStart = "finishToStart"
    startToFinish = "startToFinish"
    finishToFinish = "finishToFinish"


############################################
# Definition of Classes
############################################

class revision_PlaceHolder(ABC):

    pass
class PlaceHolder:

    pass
class revision_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class revision_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class revision_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class revision_PublicationSystem:

    pass
class Labelled:

    pass
class revision_PlaceHolderRn(PlaceHolder):

    pass
class Counted:

    pass
class revision_Progress(Labelled):

    def __init__(self, percent: int, Progress: "revision_Paper" = None, revision_Progress: "revision_PublicationProcess" = None, progress: "revision_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.revision_Progress = revision_Progress
        self.progress = progress
        
    @property
    def percent(self) -> int:
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Progress__progress", None)
        self.__progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Paper37"):
                opp_val = getattr(old_value, "Paper37", None)
                if opp_val == self:
                    setattr(old_value, "Paper37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Paper37"):
                opp_val = getattr(value, "Paper37", None)
                setattr(value, "Paper37", self)

    @property
    def revision_Progress(self):
        return self.__revision_Progress

    @revision_Progress.setter
    def revision_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Progress__revision_Progress", None)
        self.__revision_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PublicationProcess35"):
                opp_val = getattr(old_value, "revision_PublicationProcess35", None)
                if opp_val == self:
                    setattr(old_value, "revision_PublicationProcess35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PublicationProcess35"):
                opp_val = getattr(value, "revision_PublicationProcess35", None)
                setattr(value, "revision_PublicationProcess35", self)

    @property
    def Progress(self):
        return self.__Progress

    @Progress.setter
    def Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Progress__Progress", None)
        self.__Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paper"):
                opp_val = getattr(old_value, "paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paper"):
                opp_val = getattr(value, "paper", None)
                if opp_val is None:
                    setattr(value, "paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class revision_PlaceHolderPP(PlaceHolder):

    pass
class revision_PlaceHolderRs(PlaceHolder):

    pass
class revision_Review(Labelled):

    pass
class revision_Write(Labelled):

    pass
class revision_PlaceHolderRule(PlaceHolder):

    pass
class revision_PublicationPhase:

    def __init__(self, name: str, minTime: int, maxTime: int, revision_PublicationPhase4: set["revision_Sequence"] = None, phaseParticipation: set["revision_Researcher"] = None, revision_PublicationPhase7: set["revision_Rule"] = None, revision_PublicationPhase: "revision_PublicationProcess" = None, revision_PublicationPhase13: "revision_Sequence" = None, revision_PublicationPhase16: "revision_Sequence" = None, PublicationPhase: "revision_Researcher" = None, revision_PublicationPhase10: "revision_PlaceHolderPP" = None):
        self.name = name
        self.minTime = minTime
        self.maxTime = maxTime
        self.revision_PublicationPhase4 = revision_PublicationPhase4 if revision_PublicationPhase4 is not None else set()
        self.phaseParticipation = phaseParticipation if phaseParticipation is not None else set()
        self.revision_PublicationPhase7 = revision_PublicationPhase7 if revision_PublicationPhase7 is not None else set()
        self.revision_PublicationPhase = revision_PublicationPhase
        self.revision_PublicationPhase13 = revision_PublicationPhase13
        self.revision_PublicationPhase16 = revision_PublicationPhase16
        self.PublicationPhase = PublicationPhase
        self.revision_PublicationPhase10 = revision_PublicationPhase10
        
    @property
    def minTime(self) -> int:
        return self.__minTime

    @minTime.setter
    def minTime(self, minTime: int):
        self.__minTime = minTime

    @property
    def maxTime(self) -> int:
        return self.__maxTime

    @maxTime.setter
    def maxTime(self, maxTime: int):
        self.__maxTime = maxTime

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phaseParticipation(self):
        return self.__phaseParticipation

    @phaseParticipation.setter
    def phaseParticipation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_PublicationPhase__phaseParticipation", None)
        self.__phaseParticipation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Researcher"):
                    opp_val = getattr(item, "Researcher", None)
                    
                    if opp_val == self:
                        setattr(item, "Researcher", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Researcher"):
                    opp_val = getattr(item, "Researcher", None)
                    
                    setattr(item, "Researcher", self)
                    

    @property
    def revision_PublicationPhase(self):
        return self.__revision_PublicationPhase

    @revision_PublicationPhase.setter
    def revision_PublicationPhase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_PublicationPhase__revision_PublicationPhase", None)
        self.__revision_PublicationPhase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PublicationProcess"):
                opp_val = getattr(old_value, "revision_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PublicationProcess"):
                opp_val = getattr(value, "revision_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "revision_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PublicationPhase(self):
        return self.__PublicationPhase

    @PublicationPhase.setter
    def PublicationPhase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_PublicationPhase__PublicationPhase", None)
        self.__PublicationPhase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "neededPerson"):
                opp_val = getattr(old_value, "neededPerson", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "neededPerson"):
                opp_val = getattr(value, "neededPerson", None)
                if opp_val is None:
                    setattr(value, "neededPerson", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def revision_PublicationPhase10(self):
        return self.__revision_PublicationPhase10

    @revision_PublicationPhase10.setter
    def revision_PublicationPhase10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_PublicationPhase__revision_PublicationPhase10", None)
        self.__revision_PublicationPhase10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PlaceHolderPP"):
                opp_val = getattr(old_value, "revision_PlaceHolderPP", None)
                if opp_val == self:
                    setattr(old_value, "revision_PlaceHolderPP", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PlaceHolderPP"):
                opp_val = getattr(value, "revision_PlaceHolderPP", None)
                setattr(value, "revision_PlaceHolderPP", self)

    @property
    def revision_PublicationPhase16(self):
        return self.__revision_PublicationPhase16

    @revision_PublicationPhase16.setter
    def revision_PublicationPhase16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_PublicationPhase__revision_PublicationPhase16", None)
        self.__revision_PublicationPhase16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_Sequence15"):
                opp_val = getattr(old_value, "revision_Sequence15", None)
                if opp_val == self:
                    setattr(old_value, "revision_Sequence15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_Sequence15"):
                opp_val = getattr(value, "revision_Sequence15", None)
                setattr(value, "revision_Sequence15", self)

    @property
    def revision_PublicationPhase7(self):
        return self.__revision_PublicationPhase7

    @revision_PublicationPhase7.setter
    def revision_PublicationPhase7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_PublicationPhase__revision_PublicationPhase7", None)
        self.__revision_PublicationPhase7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "revision_Rule8"):
                    opp_val = getattr(item, "revision_Rule8", None)
                    
                    if opp_val == self:
                        setattr(item, "revision_Rule8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "revision_Rule8"):
                    opp_val = getattr(item, "revision_Rule8", None)
                    
                    setattr(item, "revision_Rule8", self)
                    

    @property
    def revision_PublicationPhase4(self):
        return self.__revision_PublicationPhase4

    @revision_PublicationPhase4.setter
    def revision_PublicationPhase4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_PublicationPhase__revision_PublicationPhase4", None)
        self.__revision_PublicationPhase4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "revision_Sequence"):
                    opp_val = getattr(item, "revision_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "revision_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "revision_Sequence"):
                    opp_val = getattr(item, "revision_Sequence", None)
                    
                    setattr(item, "revision_Sequence", self)
                    

    @property
    def revision_PublicationPhase13(self):
        return self.__revision_PublicationPhase13

    @revision_PublicationPhase13.setter
    def revision_PublicationPhase13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_PublicationPhase__revision_PublicationPhase13", None)
        self.__revision_PublicationPhase13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_Sequence12"):
                opp_val = getattr(old_value, "revision_Sequence12", None)
                if opp_val == self:
                    setattr(old_value, "revision_Sequence12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_Sequence12"):
                opp_val = getattr(value, "revision_Sequence12", None)
                setattr(value, "revision_Sequence12", self)

class revision_Researcher:

    def __init__(self, name: str, forName: str, position: str, Researcher: "revision_PublicationPhase" = None, neededPerson: set["revision_PublicationPhase"] = None, revision_Researcher: set["revision_Write"] = None, revision_Researcher22: set["revision_Review"] = None, authors: set["revision_Paper"] = None, revision_Researcher25: "revision_PlaceHolderRs" = None, Researcher29: "revision_Paper" = None, revision_Researcher45: "revision_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.position = position
        self.Researcher = Researcher
        self.neededPerson = neededPerson if neededPerson is not None else set()
        self.revision_Researcher = revision_Researcher if revision_Researcher is not None else set()
        self.revision_Researcher22 = revision_Researcher22 if revision_Researcher22 is not None else set()
        self.authors = authors if authors is not None else set()
        self.revision_Researcher25 = revision_Researcher25
        self.Researcher29 = Researcher29
        self.revision_Researcher45 = revision_Researcher45
        
    @property
    def forName(self) -> str:
        return self.__forName

    @forName.setter
    def forName(self, forName: str):
        self.__forName = forName

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Researcher__Researcher", None)
        self.__Researcher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "phaseParticipation"):
                opp_val = getattr(old_value, "phaseParticipation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "phaseParticipation"):
                opp_val = getattr(value, "phaseParticipation", None)
                if opp_val is None:
                    setattr(value, "phaseParticipation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def revision_Researcher(self):
        return self.__revision_Researcher

    @revision_Researcher.setter
    def revision_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Researcher__revision_Researcher", None)
        self.__revision_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "revision_Write"):
                    opp_val = getattr(item, "revision_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "revision_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "revision_Write"):
                    opp_val = getattr(item, "revision_Write", None)
                    
                    setattr(item, "revision_Write", self)
                    

    @property
    def revision_Researcher25(self):
        return self.__revision_Researcher25

    @revision_Researcher25.setter
    def revision_Researcher25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Researcher__revision_Researcher25", None)
        self.__revision_Researcher25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PlaceHolderRs"):
                opp_val = getattr(old_value, "revision_PlaceHolderRs", None)
                if opp_val == self:
                    setattr(old_value, "revision_PlaceHolderRs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PlaceHolderRs"):
                opp_val = getattr(value, "revision_PlaceHolderRs", None)
                setattr(value, "revision_PlaceHolderRs", self)

    @property
    def neededPerson(self):
        return self.__neededPerson

    @neededPerson.setter
    def neededPerson(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Researcher__neededPerson", None)
        self.__neededPerson = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PublicationPhase"):
                    opp_val = getattr(item, "PublicationPhase", None)
                    
                    if opp_val == self:
                        setattr(item, "PublicationPhase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PublicationPhase"):
                    opp_val = getattr(item, "PublicationPhase", None)
                    
                    setattr(item, "PublicationPhase", self)
                    

    @property
    def revision_Researcher22(self):
        return self.__revision_Researcher22

    @revision_Researcher22.setter
    def revision_Researcher22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Researcher__revision_Researcher22", None)
        self.__revision_Researcher22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "revision_Review"):
                    opp_val = getattr(item, "revision_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "revision_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "revision_Review"):
                    opp_val = getattr(item, "revision_Review", None)
                    
                    setattr(item, "revision_Review", self)
                    

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Researcher__authors", None)
        self.__authors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Paper"):
                    opp_val = getattr(item, "Paper", None)
                    
                    if opp_val == self:
                        setattr(item, "Paper", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Paper"):
                    opp_val = getattr(item, "Paper", None)
                    
                    setattr(item, "Paper", self)
                    

    @property
    def revision_Researcher45(self):
        return self.__revision_Researcher45

    @revision_Researcher45.setter
    def revision_Researcher45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Researcher__revision_Researcher45", None)
        self.__revision_Researcher45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PublicationStructure"):
                opp_val = getattr(old_value, "revision_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PublicationStructure"):
                opp_val = getattr(value, "revision_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "revision_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Researcher29(self):
        return self.__Researcher29

    @Researcher29.setter
    def Researcher29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Researcher__Researcher29", None)
        self.__Researcher29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "papers"):
                opp_val = getattr(old_value, "papers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "papers"):
                opp_val = getattr(value, "papers", None)
                if opp_val is None:
                    setattr(value, "papers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class revision_Sequence:

    def __init__(self, sequenceType: str, revision_Sequence: "revision_PublicationPhase" = None, revision_Sequence12: "revision_PublicationPhase" = None, revision_Sequence15: "revision_PublicationPhase" = None):
        self.sequenceType = sequenceType
        self.revision_Sequence = revision_Sequence
        self.revision_Sequence12 = revision_Sequence12
        self.revision_Sequence15 = revision_Sequence15
        
    @property
    def sequenceType(self) -> str:
        return self.__sequenceType

    @sequenceType.setter
    def sequenceType(self, sequenceType: str):
        self.__sequenceType = sequenceType

    @property
    def revision_Sequence(self):
        return self.__revision_Sequence

    @revision_Sequence.setter
    def revision_Sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Sequence__revision_Sequence", None)
        self.__revision_Sequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PublicationPhase4"):
                opp_val = getattr(old_value, "revision_PublicationPhase4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PublicationPhase4"):
                opp_val = getattr(value, "revision_PublicationPhase4", None)
                if opp_val is None:
                    setattr(value, "revision_PublicationPhase4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def revision_Sequence15(self):
        return self.__revision_Sequence15

    @revision_Sequence15.setter
    def revision_Sequence15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Sequence__revision_Sequence15", None)
        self.__revision_Sequence15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PublicationPhase16"):
                opp_val = getattr(old_value, "revision_PublicationPhase16", None)
                if opp_val == self:
                    setattr(old_value, "revision_PublicationPhase16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PublicationPhase16"):
                opp_val = getattr(value, "revision_PublicationPhase16", None)
                setattr(value, "revision_PublicationPhase16", self)

    @property
    def revision_Sequence12(self):
        return self.__revision_Sequence12

    @revision_Sequence12.setter
    def revision_Sequence12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Sequence__revision_Sequence12", None)
        self.__revision_Sequence12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PublicationPhase13"):
                opp_val = getattr(old_value, "revision_PublicationPhase13", None)
                if opp_val == self:
                    setattr(old_value, "revision_PublicationPhase13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PublicationPhase13"):
                opp_val = getattr(value, "revision_PublicationPhase13", None)
                setattr(value, "revision_PublicationPhase13", self)

class revision_Rule:

    def __init__(self, text: str, key: str, revision_Rule: "revision_PublicationProcess" = None, revision_Rule8: "revision_PublicationPhase" = None, revision_Rule18: "revision_PlaceHolderRule" = None):
        self.text = text
        self.key = key
        self.revision_Rule = revision_Rule
        self.revision_Rule8 = revision_Rule8
        self.revision_Rule18 = revision_Rule18
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def revision_Rule(self):
        return self.__revision_Rule

    @revision_Rule.setter
    def revision_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Rule__revision_Rule", None)
        self.__revision_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PublicationProcess2"):
                opp_val = getattr(old_value, "revision_PublicationProcess2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PublicationProcess2"):
                opp_val = getattr(value, "revision_PublicationProcess2", None)
                if opp_val is None:
                    setattr(value, "revision_PublicationProcess2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def revision_Rule8(self):
        return self.__revision_Rule8

    @revision_Rule8.setter
    def revision_Rule8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Rule__revision_Rule8", None)
        self.__revision_Rule8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PublicationPhase7"):
                opp_val = getattr(old_value, "revision_PublicationPhase7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PublicationPhase7"):
                opp_val = getattr(value, "revision_PublicationPhase7", None)
                if opp_val is None:
                    setattr(value, "revision_PublicationPhase7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def revision_Rule18(self):
        return self.__revision_Rule18

    @revision_Rule18.setter
    def revision_Rule18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Rule__revision_Rule18", None)
        self.__revision_Rule18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PlaceHolderRule"):
                opp_val = getattr(old_value, "revision_PlaceHolderRule", None)
                if opp_val == self:
                    setattr(old_value, "revision_PlaceHolderRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PlaceHolderRule"):
                opp_val = getattr(value, "revision_PlaceHolderRule", None)
                setattr(value, "revision_PlaceHolderRule", self)

class Named:

    pass
class revision_Paragraph(Counted, Named):

    def __init__(self, content: str, revision_Paragraph31: set["revision_ReviewNote"] = None, revision_Paragraph40: "revision_Write" = None, revision_Paragraph: "revision_Paper" = None):
        self.content = content
        self.revision_Paragraph31 = revision_Paragraph31 if revision_Paragraph31 is not None else set()
        self.revision_Paragraph40 = revision_Paragraph40
        self.revision_Paragraph = revision_Paragraph
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def revision_Paragraph40(self):
        return self.__revision_Paragraph40

    @revision_Paragraph40.setter
    def revision_Paragraph40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Paragraph__revision_Paragraph40", None)
        self.__revision_Paragraph40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_Write39"):
                opp_val = getattr(old_value, "revision_Write39", None)
                if opp_val == self:
                    setattr(old_value, "revision_Write39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_Write39"):
                opp_val = getattr(value, "revision_Write39", None)
                setattr(value, "revision_Write39", self)

    @property
    def revision_Paragraph31(self):
        return self.__revision_Paragraph31

    @revision_Paragraph31.setter
    def revision_Paragraph31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Paragraph__revision_Paragraph31", None)
        self.__revision_Paragraph31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "revision_ReviewNote"):
                    opp_val = getattr(item, "revision_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "revision_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "revision_ReviewNote"):
                    opp_val = getattr(item, "revision_ReviewNote", None)
                    
                    setattr(item, "revision_ReviewNote", self)
                    

    @property
    def revision_Paragraph(self):
        return self.__revision_Paragraph

    @revision_Paragraph.setter
    def revision_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_Paragraph__revision_Paragraph", None)
        self.__revision_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_Paper"):
                opp_val = getattr(old_value, "revision_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_Paper"):
                opp_val = getattr(value, "revision_Paper", None)
                if opp_val is None:
                    setattr(value, "revision_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class revision_PublicationStructure(Named):

    pass
class revision_Paper(Named):

    pass
class revision_ReviewNote(Named):

    def __init__(self, content: str, revision_ReviewNote: "revision_Paragraph" = None, revision_ReviewNote33: "revision_PlaceHolderRn" = None, revision_ReviewNote43: "revision_Review" = None):
        self.content = content
        self.revision_ReviewNote = revision_ReviewNote
        self.revision_ReviewNote33 = revision_ReviewNote33
        self.revision_ReviewNote43 = revision_ReviewNote43
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def revision_ReviewNote33(self):
        return self.__revision_ReviewNote33

    @revision_ReviewNote33.setter
    def revision_ReviewNote33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_ReviewNote__revision_ReviewNote33", None)
        self.__revision_ReviewNote33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PlaceHolderRn"):
                opp_val = getattr(old_value, "revision_PlaceHolderRn", None)
                if opp_val == self:
                    setattr(old_value, "revision_PlaceHolderRn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PlaceHolderRn"):
                opp_val = getattr(value, "revision_PlaceHolderRn", None)
                setattr(value, "revision_PlaceHolderRn", self)

    @property
    def revision_ReviewNote43(self):
        return self.__revision_ReviewNote43

    @revision_ReviewNote43.setter
    def revision_ReviewNote43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_ReviewNote__revision_ReviewNote43", None)
        self.__revision_ReviewNote43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_Review42"):
                opp_val = getattr(old_value, "revision_Review42", None)
                if opp_val == self:
                    setattr(old_value, "revision_Review42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_Review42"):
                opp_val = getattr(value, "revision_Review42", None)
                setattr(value, "revision_Review42", self)

    @property
    def revision_ReviewNote(self):
        return self.__revision_ReviewNote

    @revision_ReviewNote.setter
    def revision_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_ReviewNote__revision_ReviewNote", None)
        self.__revision_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_Paragraph31"):
                opp_val = getattr(old_value, "revision_Paragraph31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_Paragraph31"):
                opp_val = getattr(value, "revision_Paragraph31", None)
                if opp_val is None:
                    setattr(value, "revision_Paragraph31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class revision_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, revision_PublicationProcess2: set["revision_Rule"] = None, revision_PublicationProcess: set["revision_PublicationPhase"] = None, revision_PublicationProcess35: "revision_Progress" = None, revision_PublicationProcess50: "revision_PublicationSystem" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.revision_PublicationProcess2 = revision_PublicationProcess2 if revision_PublicationProcess2 is not None else set()
        self.revision_PublicationProcess = revision_PublicationProcess if revision_PublicationProcess is not None else set()
        self.revision_PublicationProcess35 = revision_PublicationProcess35
        self.revision_PublicationProcess50 = revision_PublicationProcess50
        
    @property
    def minTime(self) -> int:
        return self.__minTime

    @minTime.setter
    def minTime(self, minTime: int):
        self.__minTime = minTime

    @property
    def maxTime(self) -> int:
        return self.__maxTime

    @maxTime.setter
    def maxTime(self, maxTime: int):
        self.__maxTime = maxTime

    @property
    def revision_PublicationProcess50(self):
        return self.__revision_PublicationProcess50

    @revision_PublicationProcess50.setter
    def revision_PublicationProcess50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_PublicationProcess__revision_PublicationProcess50", None)
        self.__revision_PublicationProcess50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_PublicationSystem"):
                opp_val = getattr(old_value, "revision_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "revision_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_PublicationSystem"):
                opp_val = getattr(value, "revision_PublicationSystem", None)
                setattr(value, "revision_PublicationSystem", self)

    @property
    def revision_PublicationProcess2(self):
        return self.__revision_PublicationProcess2

    @revision_PublicationProcess2.setter
    def revision_PublicationProcess2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_PublicationProcess__revision_PublicationProcess2", None)
        self.__revision_PublicationProcess2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "revision_Rule"):
                    opp_val = getattr(item, "revision_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "revision_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "revision_Rule"):
                    opp_val = getattr(item, "revision_Rule", None)
                    
                    setattr(item, "revision_Rule", self)
                    

    @property
    def revision_PublicationProcess(self):
        return self.__revision_PublicationProcess

    @revision_PublicationProcess.setter
    def revision_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_PublicationProcess__revision_PublicationProcess", None)
        self.__revision_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "revision_PublicationPhase"):
                    opp_val = getattr(item, "revision_PublicationPhase", None)
                    
                    if opp_val == self:
                        setattr(item, "revision_PublicationPhase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "revision_PublicationPhase"):
                    opp_val = getattr(item, "revision_PublicationPhase", None)
                    
                    setattr(item, "revision_PublicationPhase", self)
                    

    @property
    def revision_PublicationProcess35(self):
        return self.__revision_PublicationProcess35

    @revision_PublicationProcess35.setter
    def revision_PublicationProcess35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_revision_PublicationProcess__revision_PublicationProcess35", None)
        self.__revision_PublicationProcess35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revision_Progress"):
                opp_val = getattr(old_value, "revision_Progress", None)
                if opp_val == self:
                    setattr(old_value, "revision_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revision_Progress"):
                opp_val = getattr(value, "revision_Progress", None)
                setattr(value, "revision_Progress", self)
