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

class PlaceHolder:

    pass
class publication_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class publication_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class publication_PlaceHolder(ABC):

    pass
class Labelled:

    pass
class publication_PlaceHolderRn(PlaceHolder):

    pass
class publication_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class publication_PublicationSystem:

    pass
class publication_PlaceHolderRs(PlaceHolder):

    pass
class publication_Review(Labelled):

    pass
class publication_Write(Labelled):

    pass
class Counted:

    pass
class publication_Progress(Labelled):

    def __init__(self, percent: int, time: int, Progress: "publication_Paper" = None, progress: "publication_Paper" = None, publication_Progress: "publication_PublicationProcess" = None):
        self.percent = percent
        self.time = time
        self.Progress = Progress
        self.progress = progress
        self.publication_Progress = publication_Progress
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def percent(self) -> int:
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent

    @property
    def Progress(self):
        return self.__Progress

    @Progress.setter
    def Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Progress__Progress", None)
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

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Progress__progress", None)
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
    def publication_Progress(self):
        return self.__publication_Progress

    @publication_Progress.setter
    def publication_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Progress__publication_Progress", None)
        self.__publication_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PublicationProcess35"):
                opp_val = getattr(old_value, "publication_PublicationProcess35", None)
                if opp_val == self:
                    setattr(old_value, "publication_PublicationProcess35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PublicationProcess35"):
                opp_val = getattr(value, "publication_PublicationProcess35", None)
                setattr(value, "publication_PublicationProcess35", self)

class publication_Sequence:

    def __init__(self, sequenceType: str, publication_Sequence12: "publication_PublicationPhase" = None, publication_Sequence15: "publication_PublicationPhase" = None, publication_Sequence: "publication_PublicationPhase" = None):
        self.sequenceType = sequenceType
        self.publication_Sequence12 = publication_Sequence12
        self.publication_Sequence15 = publication_Sequence15
        self.publication_Sequence = publication_Sequence
        
    @property
    def sequenceType(self) -> str:
        return self.__sequenceType

    @sequenceType.setter
    def sequenceType(self, sequenceType: str):
        self.__sequenceType = sequenceType

    @property
    def publication_Sequence15(self):
        return self.__publication_Sequence15

    @publication_Sequence15.setter
    def publication_Sequence15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Sequence__publication_Sequence15", None)
        self.__publication_Sequence15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PublicationPhase16"):
                opp_val = getattr(old_value, "publication_PublicationPhase16", None)
                if opp_val == self:
                    setattr(old_value, "publication_PublicationPhase16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PublicationPhase16"):
                opp_val = getattr(value, "publication_PublicationPhase16", None)
                setattr(value, "publication_PublicationPhase16", self)

    @property
    def publication_Sequence12(self):
        return self.__publication_Sequence12

    @publication_Sequence12.setter
    def publication_Sequence12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Sequence__publication_Sequence12", None)
        self.__publication_Sequence12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PublicationPhase13"):
                opp_val = getattr(old_value, "publication_PublicationPhase13", None)
                if opp_val == self:
                    setattr(old_value, "publication_PublicationPhase13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PublicationPhase13"):
                opp_val = getattr(value, "publication_PublicationPhase13", None)
                setattr(value, "publication_PublicationPhase13", self)

    @property
    def publication_Sequence(self):
        return self.__publication_Sequence

    @publication_Sequence.setter
    def publication_Sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Sequence__publication_Sequence", None)
        self.__publication_Sequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PublicationPhase4"):
                opp_val = getattr(old_value, "publication_PublicationPhase4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PublicationPhase4"):
                opp_val = getattr(value, "publication_PublicationPhase4", None)
                if opp_val is None:
                    setattr(value, "publication_PublicationPhase4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication_Rule:

    def __init__(self, text: str, key: str, publication_Rule8: "publication_PublicationPhase" = None, publication_Rule18: "publication_PlaceHolderRule" = None, publication_Rule: "publication_PublicationProcess" = None):
        self.text = text
        self.key = key
        self.publication_Rule8 = publication_Rule8
        self.publication_Rule18 = publication_Rule18
        self.publication_Rule = publication_Rule
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def publication_Rule8(self):
        return self.__publication_Rule8

    @publication_Rule8.setter
    def publication_Rule8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Rule__publication_Rule8", None)
        self.__publication_Rule8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PublicationPhase7"):
                opp_val = getattr(old_value, "publication_PublicationPhase7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PublicationPhase7"):
                opp_val = getattr(value, "publication_PublicationPhase7", None)
                if opp_val is None:
                    setattr(value, "publication_PublicationPhase7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication_Rule(self):
        return self.__publication_Rule

    @publication_Rule.setter
    def publication_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Rule__publication_Rule", None)
        self.__publication_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PublicationProcess2"):
                opp_val = getattr(old_value, "publication_PublicationProcess2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PublicationProcess2"):
                opp_val = getattr(value, "publication_PublicationProcess2", None)
                if opp_val is None:
                    setattr(value, "publication_PublicationProcess2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication_Rule18(self):
        return self.__publication_Rule18

    @publication_Rule18.setter
    def publication_Rule18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Rule__publication_Rule18", None)
        self.__publication_Rule18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PlaceHolderRule"):
                opp_val = getattr(old_value, "publication_PlaceHolderRule", None)
                if opp_val == self:
                    setattr(old_value, "publication_PlaceHolderRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PlaceHolderRule"):
                opp_val = getattr(value, "publication_PlaceHolderRule", None)
                setattr(value, "publication_PlaceHolderRule", self)

class publication_PlaceHolderRule(PlaceHolder):

    pass
class publication_PlaceHolderPP(PlaceHolder):

    pass
class publication_Researcher:

    def __init__(self, name: str, forName: str, position: str, Researcher: "publication_PublicationPhase" = None, neededPerson: set["publication_PublicationPhase"] = None, Researcher29: "publication_Paper" = None, publication_Researcher: set["publication_Write"] = None, publication_Researcher22: set["publication_Review"] = None, authors: set["publication_Paper"] = None, publication_Researcher25: "publication_PlaceHolderRs" = None, publication_Researcher45: "publication_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.position = position
        self.Researcher = Researcher
        self.neededPerson = neededPerson if neededPerson is not None else set()
        self.Researcher29 = Researcher29
        self.publication_Researcher = publication_Researcher if publication_Researcher is not None else set()
        self.publication_Researcher22 = publication_Researcher22 if publication_Researcher22 is not None else set()
        self.authors = authors if authors is not None else set()
        self.publication_Researcher25 = publication_Researcher25
        self.publication_Researcher45 = publication_Researcher45
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def forName(self) -> str:
        return self.__forName

    @forName.setter
    def forName(self, forName: str):
        self.__forName = forName

    @property
    def publication_Researcher25(self):
        return self.__publication_Researcher25

    @publication_Researcher25.setter
    def publication_Researcher25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Researcher__publication_Researcher25", None)
        self.__publication_Researcher25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PlaceHolderRs"):
                opp_val = getattr(old_value, "publication_PlaceHolderRs", None)
                if opp_val == self:
                    setattr(old_value, "publication_PlaceHolderRs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PlaceHolderRs"):
                opp_val = getattr(value, "publication_PlaceHolderRs", None)
                setattr(value, "publication_PlaceHolderRs", self)

    @property
    def Researcher29(self):
        return self.__Researcher29

    @Researcher29.setter
    def Researcher29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Researcher__Researcher29", None)
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

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Researcher__Researcher", None)
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
    def neededPerson(self):
        return self.__neededPerson

    @neededPerson.setter
    def neededPerson(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Researcher__neededPerson", None)
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
    def publication_Researcher22(self):
        return self.__publication_Researcher22

    @publication_Researcher22.setter
    def publication_Researcher22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Researcher__publication_Researcher22", None)
        self.__publication_Researcher22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication_Review"):
                    opp_val = getattr(item, "publication_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "publication_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication_Review"):
                    opp_val = getattr(item, "publication_Review", None)
                    
                    setattr(item, "publication_Review", self)
                    

    @property
    def publication_Researcher45(self):
        return self.__publication_Researcher45

    @publication_Researcher45.setter
    def publication_Researcher45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Researcher__publication_Researcher45", None)
        self.__publication_Researcher45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PublicationStructure"):
                opp_val = getattr(old_value, "publication_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PublicationStructure"):
                opp_val = getattr(value, "publication_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "publication_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Researcher__authors", None)
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
    def publication_Researcher(self):
        return self.__publication_Researcher

    @publication_Researcher.setter
    def publication_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Researcher__publication_Researcher", None)
        self.__publication_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication_Write"):
                    opp_val = getattr(item, "publication_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "publication_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication_Write"):
                    opp_val = getattr(item, "publication_Write", None)
                    
                    setattr(item, "publication_Write", self)
                    

class publication_PublicationPhase:

    def __init__(self, maxTime: int, name: str, minTime: int, publication_PublicationPhase: "publication_PublicationProcess" = None, phaseParticipation: set["publication_Researcher"] = None, publication_PublicationPhase7: set["publication_Rule"] = None, publication_PublicationPhase10: "publication_PlaceHolderPP" = None, publication_PublicationPhase13: "publication_Sequence" = None, publication_PublicationPhase16: "publication_Sequence" = None, PublicationPhase: "publication_Researcher" = None, publication_PublicationPhase4: set["publication_Sequence"] = None):
        self.maxTime = maxTime
        self.name = name
        self.minTime = minTime
        self.publication_PublicationPhase = publication_PublicationPhase
        self.phaseParticipation = phaseParticipation if phaseParticipation is not None else set()
        self.publication_PublicationPhase7 = publication_PublicationPhase7 if publication_PublicationPhase7 is not None else set()
        self.publication_PublicationPhase10 = publication_PublicationPhase10
        self.publication_PublicationPhase13 = publication_PublicationPhase13
        self.publication_PublicationPhase16 = publication_PublicationPhase16
        self.PublicationPhase = PublicationPhase
        self.publication_PublicationPhase4 = publication_PublicationPhase4 if publication_PublicationPhase4 is not None else set()
        
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
    def minTime(self) -> int:
        return self.__minTime

    @minTime.setter
    def minTime(self, minTime: int):
        self.__minTime = minTime

    @property
    def publication_PublicationPhase7(self):
        return self.__publication_PublicationPhase7

    @publication_PublicationPhase7.setter
    def publication_PublicationPhase7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_PublicationPhase__publication_PublicationPhase7", None)
        self.__publication_PublicationPhase7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication_Rule8"):
                    opp_val = getattr(item, "publication_Rule8", None)
                    
                    if opp_val == self:
                        setattr(item, "publication_Rule8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication_Rule8"):
                    opp_val = getattr(item, "publication_Rule8", None)
                    
                    setattr(item, "publication_Rule8", self)
                    

    @property
    def phaseParticipation(self):
        return self.__phaseParticipation

    @phaseParticipation.setter
    def phaseParticipation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_PublicationPhase__phaseParticipation", None)
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
    def PublicationPhase(self):
        return self.__PublicationPhase

    @PublicationPhase.setter
    def PublicationPhase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_PublicationPhase__PublicationPhase", None)
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
    def publication_PublicationPhase16(self):
        return self.__publication_PublicationPhase16

    @publication_PublicationPhase16.setter
    def publication_PublicationPhase16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_PublicationPhase__publication_PublicationPhase16", None)
        self.__publication_PublicationPhase16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_Sequence15"):
                opp_val = getattr(old_value, "publication_Sequence15", None)
                if opp_val == self:
                    setattr(old_value, "publication_Sequence15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_Sequence15"):
                opp_val = getattr(value, "publication_Sequence15", None)
                setattr(value, "publication_Sequence15", self)

    @property
    def publication_PublicationPhase10(self):
        return self.__publication_PublicationPhase10

    @publication_PublicationPhase10.setter
    def publication_PublicationPhase10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_PublicationPhase__publication_PublicationPhase10", None)
        self.__publication_PublicationPhase10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PlaceHolderPP"):
                opp_val = getattr(old_value, "publication_PlaceHolderPP", None)
                if opp_val == self:
                    setattr(old_value, "publication_PlaceHolderPP", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PlaceHolderPP"):
                opp_val = getattr(value, "publication_PlaceHolderPP", None)
                setattr(value, "publication_PlaceHolderPP", self)

    @property
    def publication_PublicationPhase(self):
        return self.__publication_PublicationPhase

    @publication_PublicationPhase.setter
    def publication_PublicationPhase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_PublicationPhase__publication_PublicationPhase", None)
        self.__publication_PublicationPhase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PublicationProcess"):
                opp_val = getattr(old_value, "publication_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PublicationProcess"):
                opp_val = getattr(value, "publication_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "publication_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication_PublicationPhase4(self):
        return self.__publication_PublicationPhase4

    @publication_PublicationPhase4.setter
    def publication_PublicationPhase4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_PublicationPhase__publication_PublicationPhase4", None)
        self.__publication_PublicationPhase4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication_Sequence"):
                    opp_val = getattr(item, "publication_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "publication_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication_Sequence"):
                    opp_val = getattr(item, "publication_Sequence", None)
                    
                    setattr(item, "publication_Sequence", self)
                    

    @property
    def publication_PublicationPhase13(self):
        return self.__publication_PublicationPhase13

    @publication_PublicationPhase13.setter
    def publication_PublicationPhase13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_PublicationPhase__publication_PublicationPhase13", None)
        self.__publication_PublicationPhase13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_Sequence12"):
                opp_val = getattr(old_value, "publication_Sequence12", None)
                if opp_val == self:
                    setattr(old_value, "publication_Sequence12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_Sequence12"):
                opp_val = getattr(value, "publication_Sequence12", None)
                setattr(value, "publication_Sequence12", self)

class Named:

    pass
class publication_Paper(Named):

    pass
class publication_ReviewNote(Named):

    def __init__(self, content: str, publication_ReviewNote: "publication_Paragraph" = None, publication_ReviewNote43: "publication_Review" = None, publication_ReviewNote33: "publication_PlaceHolderRn" = None):
        self.content = content
        self.publication_ReviewNote = publication_ReviewNote
        self.publication_ReviewNote43 = publication_ReviewNote43
        self.publication_ReviewNote33 = publication_ReviewNote33
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication_ReviewNote(self):
        return self.__publication_ReviewNote

    @publication_ReviewNote.setter
    def publication_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_ReviewNote__publication_ReviewNote", None)
        self.__publication_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_Paragraph31"):
                opp_val = getattr(old_value, "publication_Paragraph31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_Paragraph31"):
                opp_val = getattr(value, "publication_Paragraph31", None)
                if opp_val is None:
                    setattr(value, "publication_Paragraph31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication_ReviewNote43(self):
        return self.__publication_ReviewNote43

    @publication_ReviewNote43.setter
    def publication_ReviewNote43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_ReviewNote__publication_ReviewNote43", None)
        self.__publication_ReviewNote43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_Review42"):
                opp_val = getattr(old_value, "publication_Review42", None)
                if opp_val == self:
                    setattr(old_value, "publication_Review42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_Review42"):
                opp_val = getattr(value, "publication_Review42", None)
                setattr(value, "publication_Review42", self)

    @property
    def publication_ReviewNote33(self):
        return self.__publication_ReviewNote33

    @publication_ReviewNote33.setter
    def publication_ReviewNote33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_ReviewNote__publication_ReviewNote33", None)
        self.__publication_ReviewNote33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PlaceHolderRn"):
                opp_val = getattr(old_value, "publication_PlaceHolderRn", None)
                if opp_val == self:
                    setattr(old_value, "publication_PlaceHolderRn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PlaceHolderRn"):
                opp_val = getattr(value, "publication_PlaceHolderRn", None)
                setattr(value, "publication_PlaceHolderRn", self)

class publication_Paragraph(Named, Counted):

    def __init__(self, content: str, publication_Paragraph: "publication_Paper" = None, publication_Paragraph31: set["publication_ReviewNote"] = None, publication_Paragraph40: "publication_Write" = None):
        self.content = content
        self.publication_Paragraph = publication_Paragraph
        self.publication_Paragraph31 = publication_Paragraph31 if publication_Paragraph31 is not None else set()
        self.publication_Paragraph40 = publication_Paragraph40
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication_Paragraph40(self):
        return self.__publication_Paragraph40

    @publication_Paragraph40.setter
    def publication_Paragraph40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Paragraph__publication_Paragraph40", None)
        self.__publication_Paragraph40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_Write39"):
                opp_val = getattr(old_value, "publication_Write39", None)
                if opp_val == self:
                    setattr(old_value, "publication_Write39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_Write39"):
                opp_val = getattr(value, "publication_Write39", None)
                setattr(value, "publication_Write39", self)

    @property
    def publication_Paragraph31(self):
        return self.__publication_Paragraph31

    @publication_Paragraph31.setter
    def publication_Paragraph31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Paragraph__publication_Paragraph31", None)
        self.__publication_Paragraph31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication_ReviewNote"):
                    opp_val = getattr(item, "publication_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "publication_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication_ReviewNote"):
                    opp_val = getattr(item, "publication_ReviewNote", None)
                    
                    setattr(item, "publication_ReviewNote", self)
                    

    @property
    def publication_Paragraph(self):
        return self.__publication_Paragraph

    @publication_Paragraph.setter
    def publication_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Paragraph__publication_Paragraph", None)
        self.__publication_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_Paper"):
                opp_val = getattr(old_value, "publication_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_Paper"):
                opp_val = getattr(value, "publication_Paper", None)
                if opp_val is None:
                    setattr(value, "publication_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication_PublicationStructure(Named):

    pass
class publication_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, publication_PublicationProcess: set["publication_PublicationPhase"] = None, publication_PublicationProcess2: set["publication_Rule"] = None, publication_PublicationProcess50: "publication_PublicationSystem" = None, publication_PublicationProcess35: "publication_Progress" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.publication_PublicationProcess = publication_PublicationProcess if publication_PublicationProcess is not None else set()
        self.publication_PublicationProcess2 = publication_PublicationProcess2 if publication_PublicationProcess2 is not None else set()
        self.publication_PublicationProcess50 = publication_PublicationProcess50
        self.publication_PublicationProcess35 = publication_PublicationProcess35
        
    @property
    def maxTime(self) -> int:
        return self.__maxTime

    @maxTime.setter
    def maxTime(self, maxTime: int):
        self.__maxTime = maxTime

    @property
    def minTime(self) -> int:
        return self.__minTime

    @minTime.setter
    def minTime(self, minTime: int):
        self.__minTime = minTime

    @property
    def publication_PublicationProcess35(self):
        return self.__publication_PublicationProcess35

    @publication_PublicationProcess35.setter
    def publication_PublicationProcess35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_PublicationProcess__publication_PublicationProcess35", None)
        self.__publication_PublicationProcess35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_Progress"):
                opp_val = getattr(old_value, "publication_Progress", None)
                if opp_val == self:
                    setattr(old_value, "publication_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_Progress"):
                opp_val = getattr(value, "publication_Progress", None)
                setattr(value, "publication_Progress", self)

    @property
    def publication_PublicationProcess2(self):
        return self.__publication_PublicationProcess2

    @publication_PublicationProcess2.setter
    def publication_PublicationProcess2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_PublicationProcess__publication_PublicationProcess2", None)
        self.__publication_PublicationProcess2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication_Rule"):
                    opp_val = getattr(item, "publication_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "publication_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication_Rule"):
                    opp_val = getattr(item, "publication_Rule", None)
                    
                    setattr(item, "publication_Rule", self)
                    

    @property
    def publication_PublicationProcess(self):
        return self.__publication_PublicationProcess

    @publication_PublicationProcess.setter
    def publication_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_PublicationProcess__publication_PublicationProcess", None)
        self.__publication_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication_PublicationPhase"):
                    opp_val = getattr(item, "publication_PublicationPhase", None)
                    
                    if opp_val == self:
                        setattr(item, "publication_PublicationPhase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication_PublicationPhase"):
                    opp_val = getattr(item, "publication_PublicationPhase", None)
                    
                    setattr(item, "publication_PublicationPhase", self)
                    

    @property
    def publication_PublicationProcess50(self):
        return self.__publication_PublicationProcess50

    @publication_PublicationProcess50.setter
    def publication_PublicationProcess50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_PublicationProcess__publication_PublicationProcess50", None)
        self.__publication_PublicationProcess50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_PublicationSystem"):
                opp_val = getattr(old_value, "publication_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "publication_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_PublicationSystem"):
                opp_val = getattr(value, "publication_PublicationSystem", None)
                setattr(value, "publication_PublicationSystem", self)
