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

class publication2014c_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class publication2014c_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class Labelled:

    pass
class publication2014c_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class publication2014c_PublicationSystem:

    pass
class Counted:

    pass
class publication2014c_Progress(Labelled):

    def __init__(self, percent: int, time: int, progress: "publication2014c_Paper" = None, Progress: "publication2014c_Paper" = None, publication2014c_Progress: "publication2014c_PublicationProcess" = None):
        self.percent = percent
        self.time = time
        self.progress = progress
        self.Progress = Progress
        self.publication2014c_Progress = publication2014c_Progress
        
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
        old_value = getattr(self, f"_publication2014c_Progress__Progress", None)
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
        old_value = getattr(self, f"_publication2014c_Progress__progress", None)
        self.__progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Paper29"):
                opp_val = getattr(old_value, "Paper29", None)
                if opp_val == self:
                    setattr(old_value, "Paper29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Paper29"):
                opp_val = getattr(value, "Paper29", None)
                setattr(value, "Paper29", self)

    @property
    def publication2014c_Progress(self):
        return self.__publication2014c_Progress

    @publication2014c_Progress.setter
    def publication2014c_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Progress__publication2014c_Progress", None)
        self.__publication2014c_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_PublicationProcess27"):
                opp_val = getattr(old_value, "publication2014c_PublicationProcess27", None)
                if opp_val == self:
                    setattr(old_value, "publication2014c_PublicationProcess27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_PublicationProcess27"):
                opp_val = getattr(value, "publication2014c_PublicationProcess27", None)
                setattr(value, "publication2014c_PublicationProcess27", self)

class publication2014c_Researcher:

    def __init__(self, name: str, forName: str, position: str, publication2014c_Researcher: set["publication2014c_Write"] = None, publication2014c_Researcher18: set["publication2014c_Review"] = None, authors: set["publication2014c_Paper"] = None, Researcher: "publication2014c_PublicationPhase" = None, neededPerson: set["publication2014c_PublicationPhase"] = None, Researcher23: "publication2014c_Paper" = None, publication2014c_Researcher37: "publication2014c_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.position = position
        self.publication2014c_Researcher = publication2014c_Researcher if publication2014c_Researcher is not None else set()
        self.publication2014c_Researcher18 = publication2014c_Researcher18 if publication2014c_Researcher18 is not None else set()
        self.authors = authors if authors is not None else set()
        self.Researcher = Researcher
        self.neededPerson = neededPerson if neededPerson is not None else set()
        self.Researcher23 = Researcher23
        self.publication2014c_Researcher37 = publication2014c_Researcher37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def neededPerson(self):
        return self.__neededPerson

    @neededPerson.setter
    def neededPerson(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Researcher__neededPerson", None)
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
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Researcher__authors", None)
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
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Researcher__Researcher", None)
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
    def publication2014c_Researcher(self):
        return self.__publication2014c_Researcher

    @publication2014c_Researcher.setter
    def publication2014c_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Researcher__publication2014c_Researcher", None)
        self.__publication2014c_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014c_Write"):
                    opp_val = getattr(item, "publication2014c_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014c_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014c_Write"):
                    opp_val = getattr(item, "publication2014c_Write", None)
                    
                    setattr(item, "publication2014c_Write", self)
                    

    @property
    def publication2014c_Researcher18(self):
        return self.__publication2014c_Researcher18

    @publication2014c_Researcher18.setter
    def publication2014c_Researcher18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Researcher__publication2014c_Researcher18", None)
        self.__publication2014c_Researcher18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014c_Review"):
                    opp_val = getattr(item, "publication2014c_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014c_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014c_Review"):
                    opp_val = getattr(item, "publication2014c_Review", None)
                    
                    setattr(item, "publication2014c_Review", self)
                    

    @property
    def publication2014c_Researcher37(self):
        return self.__publication2014c_Researcher37

    @publication2014c_Researcher37.setter
    def publication2014c_Researcher37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Researcher__publication2014c_Researcher37", None)
        self.__publication2014c_Researcher37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_PublicationStructure"):
                opp_val = getattr(old_value, "publication2014c_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_PublicationStructure"):
                opp_val = getattr(value, "publication2014c_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "publication2014c_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Researcher23(self):
        return self.__Researcher23

    @Researcher23.setter
    def Researcher23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Researcher__Researcher23", None)
        self.__Researcher23 = value
        
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

class publication2014c_Review(Labelled):

    pass
class publication2014c_Write(Labelled):

    pass
class publication2014c_Rule:

    def __init__(self, text: str, key: str, publication2014c_Rule: "publication2014c_PublicationProcess" = None, publication2014c_Rule8: "publication2014c_PublicationPhase" = None):
        self.text = text
        self.key = key
        self.publication2014c_Rule = publication2014c_Rule
        self.publication2014c_Rule8 = publication2014c_Rule8
        
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
    def publication2014c_Rule8(self):
        return self.__publication2014c_Rule8

    @publication2014c_Rule8.setter
    def publication2014c_Rule8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Rule__publication2014c_Rule8", None)
        self.__publication2014c_Rule8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_PublicationPhase7"):
                opp_val = getattr(old_value, "publication2014c_PublicationPhase7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_PublicationPhase7"):
                opp_val = getattr(value, "publication2014c_PublicationPhase7", None)
                if opp_val is None:
                    setattr(value, "publication2014c_PublicationPhase7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication2014c_Rule(self):
        return self.__publication2014c_Rule

    @publication2014c_Rule.setter
    def publication2014c_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Rule__publication2014c_Rule", None)
        self.__publication2014c_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_PublicationProcess2"):
                opp_val = getattr(old_value, "publication2014c_PublicationProcess2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_PublicationProcess2"):
                opp_val = getattr(value, "publication2014c_PublicationProcess2", None)
                if opp_val is None:
                    setattr(value, "publication2014c_PublicationProcess2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication2014c_PublicationPhase:

    def __init__(self, name: str, minTime: int, maxTime: int, publication2014c_PublicationPhase4: set["publication2014c_Sequence"] = None, publication2014c_PublicationPhase: "publication2014c_PublicationProcess" = None, phaseParticipation: set["publication2014c_Researcher"] = None, publication2014c_PublicationPhase7: set["publication2014c_Rule"] = None, publication2014c_PublicationPhase11: "publication2014c_Sequence" = None, publication2014c_PublicationPhase14: "publication2014c_Sequence" = None, PublicationPhase: "publication2014c_Researcher" = None):
        self.name = name
        self.minTime = minTime
        self.maxTime = maxTime
        self.publication2014c_PublicationPhase4 = publication2014c_PublicationPhase4 if publication2014c_PublicationPhase4 is not None else set()
        self.publication2014c_PublicationPhase = publication2014c_PublicationPhase
        self.phaseParticipation = phaseParticipation if phaseParticipation is not None else set()
        self.publication2014c_PublicationPhase7 = publication2014c_PublicationPhase7 if publication2014c_PublicationPhase7 is not None else set()
        self.publication2014c_PublicationPhase11 = publication2014c_PublicationPhase11
        self.publication2014c_PublicationPhase14 = publication2014c_PublicationPhase14
        self.PublicationPhase = PublicationPhase
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PublicationPhase(self):
        return self.__PublicationPhase

    @PublicationPhase.setter
    def PublicationPhase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_PublicationPhase__PublicationPhase", None)
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
    def publication2014c_PublicationPhase(self):
        return self.__publication2014c_PublicationPhase

    @publication2014c_PublicationPhase.setter
    def publication2014c_PublicationPhase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_PublicationPhase__publication2014c_PublicationPhase", None)
        self.__publication2014c_PublicationPhase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_PublicationProcess"):
                opp_val = getattr(old_value, "publication2014c_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_PublicationProcess"):
                opp_val = getattr(value, "publication2014c_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "publication2014c_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication2014c_PublicationPhase4(self):
        return self.__publication2014c_PublicationPhase4

    @publication2014c_PublicationPhase4.setter
    def publication2014c_PublicationPhase4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_PublicationPhase__publication2014c_PublicationPhase4", None)
        self.__publication2014c_PublicationPhase4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014c_Sequence"):
                    opp_val = getattr(item, "publication2014c_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014c_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014c_Sequence"):
                    opp_val = getattr(item, "publication2014c_Sequence", None)
                    
                    setattr(item, "publication2014c_Sequence", self)
                    

    @property
    def phaseParticipation(self):
        return self.__phaseParticipation

    @phaseParticipation.setter
    def phaseParticipation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_PublicationPhase__phaseParticipation", None)
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
    def publication2014c_PublicationPhase7(self):
        return self.__publication2014c_PublicationPhase7

    @publication2014c_PublicationPhase7.setter
    def publication2014c_PublicationPhase7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_PublicationPhase__publication2014c_PublicationPhase7", None)
        self.__publication2014c_PublicationPhase7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014c_Rule8"):
                    opp_val = getattr(item, "publication2014c_Rule8", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014c_Rule8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014c_Rule8"):
                    opp_val = getattr(item, "publication2014c_Rule8", None)
                    
                    setattr(item, "publication2014c_Rule8", self)
                    

    @property
    def publication2014c_PublicationPhase14(self):
        return self.__publication2014c_PublicationPhase14

    @publication2014c_PublicationPhase14.setter
    def publication2014c_PublicationPhase14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_PublicationPhase__publication2014c_PublicationPhase14", None)
        self.__publication2014c_PublicationPhase14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_Sequence13"):
                opp_val = getattr(old_value, "publication2014c_Sequence13", None)
                if opp_val == self:
                    setattr(old_value, "publication2014c_Sequence13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_Sequence13"):
                opp_val = getattr(value, "publication2014c_Sequence13", None)
                setattr(value, "publication2014c_Sequence13", self)

    @property
    def publication2014c_PublicationPhase11(self):
        return self.__publication2014c_PublicationPhase11

    @publication2014c_PublicationPhase11.setter
    def publication2014c_PublicationPhase11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_PublicationPhase__publication2014c_PublicationPhase11", None)
        self.__publication2014c_PublicationPhase11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_Sequence10"):
                opp_val = getattr(old_value, "publication2014c_Sequence10", None)
                if opp_val == self:
                    setattr(old_value, "publication2014c_Sequence10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_Sequence10"):
                opp_val = getattr(value, "publication2014c_Sequence10", None)
                setattr(value, "publication2014c_Sequence10", self)

class Named:

    pass
class publication2014c_Paragraph(Counted, Named):

    def __init__(self, content: str, publication2014c_Paragraph32: "publication2014c_Write" = None, publication2014c_Paragraph: "publication2014c_Paper" = None, publication2014c_Paragraph25: set["publication2014c_ReviewNote"] = None):
        self.content = content
        self.publication2014c_Paragraph32 = publication2014c_Paragraph32
        self.publication2014c_Paragraph = publication2014c_Paragraph
        self.publication2014c_Paragraph25 = publication2014c_Paragraph25 if publication2014c_Paragraph25 is not None else set()
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication2014c_Paragraph25(self):
        return self.__publication2014c_Paragraph25

    @publication2014c_Paragraph25.setter
    def publication2014c_Paragraph25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Paragraph__publication2014c_Paragraph25", None)
        self.__publication2014c_Paragraph25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014c_ReviewNote"):
                    opp_val = getattr(item, "publication2014c_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014c_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014c_ReviewNote"):
                    opp_val = getattr(item, "publication2014c_ReviewNote", None)
                    
                    setattr(item, "publication2014c_ReviewNote", self)
                    

    @property
    def publication2014c_Paragraph32(self):
        return self.__publication2014c_Paragraph32

    @publication2014c_Paragraph32.setter
    def publication2014c_Paragraph32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Paragraph__publication2014c_Paragraph32", None)
        self.__publication2014c_Paragraph32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_Write31"):
                opp_val = getattr(old_value, "publication2014c_Write31", None)
                if opp_val == self:
                    setattr(old_value, "publication2014c_Write31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_Write31"):
                opp_val = getattr(value, "publication2014c_Write31", None)
                setattr(value, "publication2014c_Write31", self)

    @property
    def publication2014c_Paragraph(self):
        return self.__publication2014c_Paragraph

    @publication2014c_Paragraph.setter
    def publication2014c_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Paragraph__publication2014c_Paragraph", None)
        self.__publication2014c_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_Paper"):
                opp_val = getattr(old_value, "publication2014c_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_Paper"):
                opp_val = getattr(value, "publication2014c_Paper", None)
                if opp_val is None:
                    setattr(value, "publication2014c_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication2014c_PublicationStructure(Named):

    pass
class publication2014c_Paper(Named):

    pass
class publication2014c_ReviewNote(Named):

    def __init__(self, content: str, publication2014c_ReviewNote35: "publication2014c_Review" = None, publication2014c_ReviewNote: "publication2014c_Paragraph" = None):
        self.content = content
        self.publication2014c_ReviewNote35 = publication2014c_ReviewNote35
        self.publication2014c_ReviewNote = publication2014c_ReviewNote
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication2014c_ReviewNote35(self):
        return self.__publication2014c_ReviewNote35

    @publication2014c_ReviewNote35.setter
    def publication2014c_ReviewNote35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_ReviewNote__publication2014c_ReviewNote35", None)
        self.__publication2014c_ReviewNote35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_Review34"):
                opp_val = getattr(old_value, "publication2014c_Review34", None)
                if opp_val == self:
                    setattr(old_value, "publication2014c_Review34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_Review34"):
                opp_val = getattr(value, "publication2014c_Review34", None)
                setattr(value, "publication2014c_Review34", self)

    @property
    def publication2014c_ReviewNote(self):
        return self.__publication2014c_ReviewNote

    @publication2014c_ReviewNote.setter
    def publication2014c_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_ReviewNote__publication2014c_ReviewNote", None)
        self.__publication2014c_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_Paragraph25"):
                opp_val = getattr(old_value, "publication2014c_Paragraph25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_Paragraph25"):
                opp_val = getattr(value, "publication2014c_Paragraph25", None)
                if opp_val is None:
                    setattr(value, "publication2014c_Paragraph25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication2014c_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, publication2014c_PublicationProcess: set["publication2014c_PublicationPhase"] = None, publication2014c_PublicationProcess2: set["publication2014c_Rule"] = None, publication2014c_PublicationProcess42: "publication2014c_PublicationSystem" = None, publication2014c_PublicationProcess27: "publication2014c_Progress" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.publication2014c_PublicationProcess = publication2014c_PublicationProcess if publication2014c_PublicationProcess is not None else set()
        self.publication2014c_PublicationProcess2 = publication2014c_PublicationProcess2 if publication2014c_PublicationProcess2 is not None else set()
        self.publication2014c_PublicationProcess42 = publication2014c_PublicationProcess42
        self.publication2014c_PublicationProcess27 = publication2014c_PublicationProcess27
        
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
    def publication2014c_PublicationProcess(self):
        return self.__publication2014c_PublicationProcess

    @publication2014c_PublicationProcess.setter
    def publication2014c_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_PublicationProcess__publication2014c_PublicationProcess", None)
        self.__publication2014c_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014c_PublicationPhase"):
                    opp_val = getattr(item, "publication2014c_PublicationPhase", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014c_PublicationPhase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014c_PublicationPhase"):
                    opp_val = getattr(item, "publication2014c_PublicationPhase", None)
                    
                    setattr(item, "publication2014c_PublicationPhase", self)
                    

    @property
    def publication2014c_PublicationProcess27(self):
        return self.__publication2014c_PublicationProcess27

    @publication2014c_PublicationProcess27.setter
    def publication2014c_PublicationProcess27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_PublicationProcess__publication2014c_PublicationProcess27", None)
        self.__publication2014c_PublicationProcess27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_Progress"):
                opp_val = getattr(old_value, "publication2014c_Progress", None)
                if opp_val == self:
                    setattr(old_value, "publication2014c_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_Progress"):
                opp_val = getattr(value, "publication2014c_Progress", None)
                setattr(value, "publication2014c_Progress", self)

    @property
    def publication2014c_PublicationProcess42(self):
        return self.__publication2014c_PublicationProcess42

    @publication2014c_PublicationProcess42.setter
    def publication2014c_PublicationProcess42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_PublicationProcess__publication2014c_PublicationProcess42", None)
        self.__publication2014c_PublicationProcess42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_PublicationSystem"):
                opp_val = getattr(old_value, "publication2014c_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "publication2014c_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_PublicationSystem"):
                opp_val = getattr(value, "publication2014c_PublicationSystem", None)
                setattr(value, "publication2014c_PublicationSystem", self)

    @property
    def publication2014c_PublicationProcess2(self):
        return self.__publication2014c_PublicationProcess2

    @publication2014c_PublicationProcess2.setter
    def publication2014c_PublicationProcess2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_PublicationProcess__publication2014c_PublicationProcess2", None)
        self.__publication2014c_PublicationProcess2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014c_Rule"):
                    opp_val = getattr(item, "publication2014c_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014c_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014c_Rule"):
                    opp_val = getattr(item, "publication2014c_Rule", None)
                    
                    setattr(item, "publication2014c_Rule", self)
                    

class publication2014c_Sequence:

    def __init__(self, sequenceType: str, publication2014c_Sequence: "publication2014c_PublicationPhase" = None, publication2014c_Sequence10: "publication2014c_PublicationPhase" = None, publication2014c_Sequence13: "publication2014c_PublicationPhase" = None):
        self.sequenceType = sequenceType
        self.publication2014c_Sequence = publication2014c_Sequence
        self.publication2014c_Sequence10 = publication2014c_Sequence10
        self.publication2014c_Sequence13 = publication2014c_Sequence13
        
    @property
    def sequenceType(self) -> str:
        return self.__sequenceType

    @sequenceType.setter
    def sequenceType(self, sequenceType: str):
        self.__sequenceType = sequenceType

    @property
    def publication2014c_Sequence10(self):
        return self.__publication2014c_Sequence10

    @publication2014c_Sequence10.setter
    def publication2014c_Sequence10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Sequence__publication2014c_Sequence10", None)
        self.__publication2014c_Sequence10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_PublicationPhase11"):
                opp_val = getattr(old_value, "publication2014c_PublicationPhase11", None)
                if opp_val == self:
                    setattr(old_value, "publication2014c_PublicationPhase11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_PublicationPhase11"):
                opp_val = getattr(value, "publication2014c_PublicationPhase11", None)
                setattr(value, "publication2014c_PublicationPhase11", self)

    @property
    def publication2014c_Sequence(self):
        return self.__publication2014c_Sequence

    @publication2014c_Sequence.setter
    def publication2014c_Sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Sequence__publication2014c_Sequence", None)
        self.__publication2014c_Sequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_PublicationPhase4"):
                opp_val = getattr(old_value, "publication2014c_PublicationPhase4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_PublicationPhase4"):
                opp_val = getattr(value, "publication2014c_PublicationPhase4", None)
                if opp_val is None:
                    setattr(value, "publication2014c_PublicationPhase4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication2014c_Sequence13(self):
        return self.__publication2014c_Sequence13

    @publication2014c_Sequence13.setter
    def publication2014c_Sequence13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014c_Sequence__publication2014c_Sequence13", None)
        self.__publication2014c_Sequence13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014c_PublicationPhase14"):
                opp_val = getattr(old_value, "publication2014c_PublicationPhase14", None)
                if opp_val == self:
                    setattr(old_value, "publication2014c_PublicationPhase14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014c_PublicationPhase14"):
                opp_val = getattr(value, "publication2014c_PublicationPhase14", None)
                setattr(value, "publication2014c_PublicationPhase14", self)
