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

class publication2014_PlaceHolder(ABC):

    pass
class PlaceHolder:

    pass
class publication2014_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class publication2014_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class publication2014_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Labelled:

    pass
class publication2014_PlaceHolderRn(PlaceHolder):

    pass
class publication2014_PublicationSystem:

    pass
class publication2014_Review(Labelled):

    pass
class publication2014_Write(Labelled):

    pass
class publication2014_PlaceHolderRule(PlaceHolder):

    pass
class Counted:

    pass
class publication2014_Progress(Labelled):

    def __init__(self, percent: int, time: int, Progress: "publication2014_Paper" = None, publication2014_Progress: "publication2014_PublicationProcess" = None, progress: "publication2014_Paper" = None):
        self.percent = percent
        self.time = time
        self.Progress = Progress
        self.publication2014_Progress = publication2014_Progress
        self.progress = progress
        
    @property
    def percent(self) -> int:
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent

    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Progress__progress", None)
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
    def publication2014_Progress(self):
        return self.__publication2014_Progress

    @publication2014_Progress.setter
    def publication2014_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Progress__publication2014_Progress", None)
        self.__publication2014_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PublicationProcess35"):
                opp_val = getattr(old_value, "publication2014_PublicationProcess35", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_PublicationProcess35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PublicationProcess35"):
                opp_val = getattr(value, "publication2014_PublicationProcess35", None)
                setattr(value, "publication2014_PublicationProcess35", self)

    @property
    def Progress(self):
        return self.__Progress

    @Progress.setter
    def Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Progress__Progress", None)
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

class publication2014_PlaceHolderRs(PlaceHolder):

    pass
class publication2014_Sequence:

    def __init__(self, sequenceType: str, publication2014_Sequence12: "publication2014_PublicationPhase" = None, publication2014_Sequence15: "publication2014_PublicationPhase" = None, publication2014_Sequence: "publication2014_PublicationPhase" = None):
        self.sequenceType = sequenceType
        self.publication2014_Sequence12 = publication2014_Sequence12
        self.publication2014_Sequence15 = publication2014_Sequence15
        self.publication2014_Sequence = publication2014_Sequence
        
    @property
    def sequenceType(self) -> str:
        return self.__sequenceType

    @sequenceType.setter
    def sequenceType(self, sequenceType: str):
        self.__sequenceType = sequenceType

    @property
    def publication2014_Sequence(self):
        return self.__publication2014_Sequence

    @publication2014_Sequence.setter
    def publication2014_Sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Sequence__publication2014_Sequence", None)
        self.__publication2014_Sequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PublicationPhase4"):
                opp_val = getattr(old_value, "publication2014_PublicationPhase4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PublicationPhase4"):
                opp_val = getattr(value, "publication2014_PublicationPhase4", None)
                if opp_val is None:
                    setattr(value, "publication2014_PublicationPhase4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication2014_Sequence12(self):
        return self.__publication2014_Sequence12

    @publication2014_Sequence12.setter
    def publication2014_Sequence12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Sequence__publication2014_Sequence12", None)
        self.__publication2014_Sequence12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PublicationPhase13"):
                opp_val = getattr(old_value, "publication2014_PublicationPhase13", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_PublicationPhase13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PublicationPhase13"):
                opp_val = getattr(value, "publication2014_PublicationPhase13", None)
                setattr(value, "publication2014_PublicationPhase13", self)

    @property
    def publication2014_Sequence15(self):
        return self.__publication2014_Sequence15

    @publication2014_Sequence15.setter
    def publication2014_Sequence15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Sequence__publication2014_Sequence15", None)
        self.__publication2014_Sequence15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PublicationPhase16"):
                opp_val = getattr(old_value, "publication2014_PublicationPhase16", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_PublicationPhase16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PublicationPhase16"):
                opp_val = getattr(value, "publication2014_PublicationPhase16", None)
                setattr(value, "publication2014_PublicationPhase16", self)

class publication2014_Rule:

    def __init__(self, text: str, key: str, publication2014_Rule8: "publication2014_PublicationPhase" = None, publication2014_Rule: "publication2014_PublicationProcess" = None, publication2014_Rule18: "publication2014_PlaceHolderRule" = None):
        self.text = text
        self.key = key
        self.publication2014_Rule8 = publication2014_Rule8
        self.publication2014_Rule = publication2014_Rule
        self.publication2014_Rule18 = publication2014_Rule18
        
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
    def publication2014_Rule18(self):
        return self.__publication2014_Rule18

    @publication2014_Rule18.setter
    def publication2014_Rule18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Rule__publication2014_Rule18", None)
        self.__publication2014_Rule18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PlaceHolderRule"):
                opp_val = getattr(old_value, "publication2014_PlaceHolderRule", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_PlaceHolderRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PlaceHolderRule"):
                opp_val = getattr(value, "publication2014_PlaceHolderRule", None)
                setattr(value, "publication2014_PlaceHolderRule", self)

    @property
    def publication2014_Rule(self):
        return self.__publication2014_Rule

    @publication2014_Rule.setter
    def publication2014_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Rule__publication2014_Rule", None)
        self.__publication2014_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PublicationProcess2"):
                opp_val = getattr(old_value, "publication2014_PublicationProcess2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PublicationProcess2"):
                opp_val = getattr(value, "publication2014_PublicationProcess2", None)
                if opp_val is None:
                    setattr(value, "publication2014_PublicationProcess2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication2014_Rule8(self):
        return self.__publication2014_Rule8

    @publication2014_Rule8.setter
    def publication2014_Rule8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Rule__publication2014_Rule8", None)
        self.__publication2014_Rule8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PublicationPhase7"):
                opp_val = getattr(old_value, "publication2014_PublicationPhase7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PublicationPhase7"):
                opp_val = getattr(value, "publication2014_PublicationPhase7", None)
                if opp_val is None:
                    setattr(value, "publication2014_PublicationPhase7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication2014_PublicationPhase:

    def __init__(self, minTime: int, maxTime: int, name: str, phaseParticipation: set["publication2014_Researcher"] = None, publication2014_PublicationPhase7: set["publication2014_Rule"] = None, publication2014_PublicationPhase10: "publication2014_PlaceHolderPP" = None, publication2014_PublicationPhase13: "publication2014_Sequence" = None, publication2014_PublicationPhase16: "publication2014_Sequence" = None, publication2014_PublicationPhase: "publication2014_PublicationProcess" = None, publication2014_PublicationPhase4: set["publication2014_Sequence"] = None, PublicationPhase: "publication2014_Researcher" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.name = name
        self.phaseParticipation = phaseParticipation if phaseParticipation is not None else set()
        self.publication2014_PublicationPhase7 = publication2014_PublicationPhase7 if publication2014_PublicationPhase7 is not None else set()
        self.publication2014_PublicationPhase10 = publication2014_PublicationPhase10
        self.publication2014_PublicationPhase13 = publication2014_PublicationPhase13
        self.publication2014_PublicationPhase16 = publication2014_PublicationPhase16
        self.publication2014_PublicationPhase = publication2014_PublicationPhase
        self.publication2014_PublicationPhase4 = publication2014_PublicationPhase4 if publication2014_PublicationPhase4 is not None else set()
        self.PublicationPhase = PublicationPhase
        
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
    def publication2014_PublicationPhase(self):
        return self.__publication2014_PublicationPhase

    @publication2014_PublicationPhase.setter
    def publication2014_PublicationPhase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_PublicationPhase__publication2014_PublicationPhase", None)
        self.__publication2014_PublicationPhase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PublicationProcess"):
                opp_val = getattr(old_value, "publication2014_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PublicationProcess"):
                opp_val = getattr(value, "publication2014_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "publication2014_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def phaseParticipation(self):
        return self.__phaseParticipation

    @phaseParticipation.setter
    def phaseParticipation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_PublicationPhase__phaseParticipation", None)
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
        old_value = getattr(self, f"_publication2014_PublicationPhase__PublicationPhase", None)
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
    def publication2014_PublicationPhase4(self):
        return self.__publication2014_PublicationPhase4

    @publication2014_PublicationPhase4.setter
    def publication2014_PublicationPhase4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_PublicationPhase__publication2014_PublicationPhase4", None)
        self.__publication2014_PublicationPhase4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014_Sequence"):
                    opp_val = getattr(item, "publication2014_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014_Sequence"):
                    opp_val = getattr(item, "publication2014_Sequence", None)
                    
                    setattr(item, "publication2014_Sequence", self)
                    

    @property
    def publication2014_PublicationPhase16(self):
        return self.__publication2014_PublicationPhase16

    @publication2014_PublicationPhase16.setter
    def publication2014_PublicationPhase16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_PublicationPhase__publication2014_PublicationPhase16", None)
        self.__publication2014_PublicationPhase16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_Sequence15"):
                opp_val = getattr(old_value, "publication2014_Sequence15", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_Sequence15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_Sequence15"):
                opp_val = getattr(value, "publication2014_Sequence15", None)
                setattr(value, "publication2014_Sequence15", self)

    @property
    def publication2014_PublicationPhase10(self):
        return self.__publication2014_PublicationPhase10

    @publication2014_PublicationPhase10.setter
    def publication2014_PublicationPhase10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_PublicationPhase__publication2014_PublicationPhase10", None)
        self.__publication2014_PublicationPhase10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PlaceHolderPP"):
                opp_val = getattr(old_value, "publication2014_PlaceHolderPP", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_PlaceHolderPP", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PlaceHolderPP"):
                opp_val = getattr(value, "publication2014_PlaceHolderPP", None)
                setattr(value, "publication2014_PlaceHolderPP", self)

    @property
    def publication2014_PublicationPhase7(self):
        return self.__publication2014_PublicationPhase7

    @publication2014_PublicationPhase7.setter
    def publication2014_PublicationPhase7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_PublicationPhase__publication2014_PublicationPhase7", None)
        self.__publication2014_PublicationPhase7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014_Rule8"):
                    opp_val = getattr(item, "publication2014_Rule8", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014_Rule8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014_Rule8"):
                    opp_val = getattr(item, "publication2014_Rule8", None)
                    
                    setattr(item, "publication2014_Rule8", self)
                    

    @property
    def publication2014_PublicationPhase13(self):
        return self.__publication2014_PublicationPhase13

    @publication2014_PublicationPhase13.setter
    def publication2014_PublicationPhase13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_PublicationPhase__publication2014_PublicationPhase13", None)
        self.__publication2014_PublicationPhase13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_Sequence12"):
                opp_val = getattr(old_value, "publication2014_Sequence12", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_Sequence12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_Sequence12"):
                opp_val = getattr(value, "publication2014_Sequence12", None)
                setattr(value, "publication2014_Sequence12", self)

class Named:

    pass
class publication2014_ReviewNote(Named):

    def __init__(self, content: str, publication2014_ReviewNote: "publication2014_Paragraph" = None, publication2014_ReviewNote33: "publication2014_PlaceHolderRn" = None, publication2014_ReviewNote43: "publication2014_Review" = None):
        self.content = content
        self.publication2014_ReviewNote = publication2014_ReviewNote
        self.publication2014_ReviewNote33 = publication2014_ReviewNote33
        self.publication2014_ReviewNote43 = publication2014_ReviewNote43
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication2014_ReviewNote33(self):
        return self.__publication2014_ReviewNote33

    @publication2014_ReviewNote33.setter
    def publication2014_ReviewNote33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_ReviewNote__publication2014_ReviewNote33", None)
        self.__publication2014_ReviewNote33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PlaceHolderRn"):
                opp_val = getattr(old_value, "publication2014_PlaceHolderRn", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_PlaceHolderRn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PlaceHolderRn"):
                opp_val = getattr(value, "publication2014_PlaceHolderRn", None)
                setattr(value, "publication2014_PlaceHolderRn", self)

    @property
    def publication2014_ReviewNote(self):
        return self.__publication2014_ReviewNote

    @publication2014_ReviewNote.setter
    def publication2014_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_ReviewNote__publication2014_ReviewNote", None)
        self.__publication2014_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_Paragraph31"):
                opp_val = getattr(old_value, "publication2014_Paragraph31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_Paragraph31"):
                opp_val = getattr(value, "publication2014_Paragraph31", None)
                if opp_val is None:
                    setattr(value, "publication2014_Paragraph31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication2014_ReviewNote43(self):
        return self.__publication2014_ReviewNote43

    @publication2014_ReviewNote43.setter
    def publication2014_ReviewNote43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_ReviewNote__publication2014_ReviewNote43", None)
        self.__publication2014_ReviewNote43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_Review42"):
                opp_val = getattr(old_value, "publication2014_Review42", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_Review42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_Review42"):
                opp_val = getattr(value, "publication2014_Review42", None)
                setattr(value, "publication2014_Review42", self)

class publication2014_Paper(Named):

    pass
class publication2014_PublicationStructure(Named):

    pass
class publication2014_Paragraph(Named, Counted):

    def __init__(self, content: str, publication2014_Paragraph: "publication2014_Paper" = None, publication2014_Paragraph31: set["publication2014_ReviewNote"] = None, publication2014_Paragraph40: "publication2014_Write" = None):
        self.content = content
        self.publication2014_Paragraph = publication2014_Paragraph
        self.publication2014_Paragraph31 = publication2014_Paragraph31 if publication2014_Paragraph31 is not None else set()
        self.publication2014_Paragraph40 = publication2014_Paragraph40
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication2014_Paragraph31(self):
        return self.__publication2014_Paragraph31

    @publication2014_Paragraph31.setter
    def publication2014_Paragraph31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Paragraph__publication2014_Paragraph31", None)
        self.__publication2014_Paragraph31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014_ReviewNote"):
                    opp_val = getattr(item, "publication2014_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014_ReviewNote"):
                    opp_val = getattr(item, "publication2014_ReviewNote", None)
                    
                    setattr(item, "publication2014_ReviewNote", self)
                    

    @property
    def publication2014_Paragraph40(self):
        return self.__publication2014_Paragraph40

    @publication2014_Paragraph40.setter
    def publication2014_Paragraph40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Paragraph__publication2014_Paragraph40", None)
        self.__publication2014_Paragraph40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_Write39"):
                opp_val = getattr(old_value, "publication2014_Write39", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_Write39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_Write39"):
                opp_val = getattr(value, "publication2014_Write39", None)
                setattr(value, "publication2014_Write39", self)

    @property
    def publication2014_Paragraph(self):
        return self.__publication2014_Paragraph

    @publication2014_Paragraph.setter
    def publication2014_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Paragraph__publication2014_Paragraph", None)
        self.__publication2014_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_Paper"):
                opp_val = getattr(old_value, "publication2014_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_Paper"):
                opp_val = getattr(value, "publication2014_Paper", None)
                if opp_val is None:
                    setattr(value, "publication2014_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication2014_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, publication2014_PublicationProcess: set["publication2014_PublicationPhase"] = None, publication2014_PublicationProcess2: set["publication2014_Rule"] = None, publication2014_PublicationProcess50: "publication2014_PublicationSystem" = None, publication2014_PublicationProcess35: "publication2014_Progress" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.publication2014_PublicationProcess = publication2014_PublicationProcess if publication2014_PublicationProcess is not None else set()
        self.publication2014_PublicationProcess2 = publication2014_PublicationProcess2 if publication2014_PublicationProcess2 is not None else set()
        self.publication2014_PublicationProcess50 = publication2014_PublicationProcess50
        self.publication2014_PublicationProcess35 = publication2014_PublicationProcess35
        
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
    def publication2014_PublicationProcess(self):
        return self.__publication2014_PublicationProcess

    @publication2014_PublicationProcess.setter
    def publication2014_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_PublicationProcess__publication2014_PublicationProcess", None)
        self.__publication2014_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014_PublicationPhase"):
                    opp_val = getattr(item, "publication2014_PublicationPhase", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014_PublicationPhase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014_PublicationPhase"):
                    opp_val = getattr(item, "publication2014_PublicationPhase", None)
                    
                    setattr(item, "publication2014_PublicationPhase", self)
                    

    @property
    def publication2014_PublicationProcess50(self):
        return self.__publication2014_PublicationProcess50

    @publication2014_PublicationProcess50.setter
    def publication2014_PublicationProcess50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_PublicationProcess__publication2014_PublicationProcess50", None)
        self.__publication2014_PublicationProcess50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PublicationSystem"):
                opp_val = getattr(old_value, "publication2014_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PublicationSystem"):
                opp_val = getattr(value, "publication2014_PublicationSystem", None)
                setattr(value, "publication2014_PublicationSystem", self)

    @property
    def publication2014_PublicationProcess2(self):
        return self.__publication2014_PublicationProcess2

    @publication2014_PublicationProcess2.setter
    def publication2014_PublicationProcess2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_PublicationProcess__publication2014_PublicationProcess2", None)
        self.__publication2014_PublicationProcess2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014_Rule"):
                    opp_val = getattr(item, "publication2014_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014_Rule"):
                    opp_val = getattr(item, "publication2014_Rule", None)
                    
                    setattr(item, "publication2014_Rule", self)
                    

    @property
    def publication2014_PublicationProcess35(self):
        return self.__publication2014_PublicationProcess35

    @publication2014_PublicationProcess35.setter
    def publication2014_PublicationProcess35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_PublicationProcess__publication2014_PublicationProcess35", None)
        self.__publication2014_PublicationProcess35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_Progress"):
                opp_val = getattr(old_value, "publication2014_Progress", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_Progress"):
                opp_val = getattr(value, "publication2014_Progress", None)
                setattr(value, "publication2014_Progress", self)

class publication2014_PlaceHolderPP(PlaceHolder):

    pass
class publication2014_Researcher:

    def __init__(self, name: str, forName: str, position: str, Researcher: "publication2014_PublicationPhase" = None, publication2014_Researcher25: "publication2014_PlaceHolderRs" = None, Researcher29: "publication2014_Paper" = None, neededPerson: set["publication2014_PublicationPhase"] = None, publication2014_Researcher: set["publication2014_Write"] = None, publication2014_Researcher22: set["publication2014_Review"] = None, authors: set["publication2014_Paper"] = None, publication2014_Researcher45: "publication2014_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.position = position
        self.Researcher = Researcher
        self.publication2014_Researcher25 = publication2014_Researcher25
        self.Researcher29 = Researcher29
        self.neededPerson = neededPerson if neededPerson is not None else set()
        self.publication2014_Researcher = publication2014_Researcher if publication2014_Researcher is not None else set()
        self.publication2014_Researcher22 = publication2014_Researcher22 if publication2014_Researcher22 is not None else set()
        self.authors = authors if authors is not None else set()
        self.publication2014_Researcher45 = publication2014_Researcher45
        
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
    def forName(self) -> str:
        return self.__forName

    @forName.setter
    def forName(self, forName: str):
        self.__forName = forName

    @property
    def publication2014_Researcher25(self):
        return self.__publication2014_Researcher25

    @publication2014_Researcher25.setter
    def publication2014_Researcher25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Researcher__publication2014_Researcher25", None)
        self.__publication2014_Researcher25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PlaceHolderRs"):
                opp_val = getattr(old_value, "publication2014_PlaceHolderRs", None)
                if opp_val == self:
                    setattr(old_value, "publication2014_PlaceHolderRs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PlaceHolderRs"):
                opp_val = getattr(value, "publication2014_PlaceHolderRs", None)
                setattr(value, "publication2014_PlaceHolderRs", self)

    @property
    def publication2014_Researcher22(self):
        return self.__publication2014_Researcher22

    @publication2014_Researcher22.setter
    def publication2014_Researcher22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Researcher__publication2014_Researcher22", None)
        self.__publication2014_Researcher22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014_Review"):
                    opp_val = getattr(item, "publication2014_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014_Review"):
                    opp_val = getattr(item, "publication2014_Review", None)
                    
                    setattr(item, "publication2014_Review", self)
                    

    @property
    def Researcher29(self):
        return self.__Researcher29

    @Researcher29.setter
    def Researcher29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Researcher__Researcher29", None)
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
        old_value = getattr(self, f"_publication2014_Researcher__Researcher", None)
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
    def publication2014_Researcher45(self):
        return self.__publication2014_Researcher45

    @publication2014_Researcher45.setter
    def publication2014_Researcher45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Researcher__publication2014_Researcher45", None)
        self.__publication2014_Researcher45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication2014_PublicationStructure"):
                opp_val = getattr(old_value, "publication2014_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication2014_PublicationStructure"):
                opp_val = getattr(value, "publication2014_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "publication2014_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Researcher__authors", None)
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
    def neededPerson(self):
        return self.__neededPerson

    @neededPerson.setter
    def neededPerson(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Researcher__neededPerson", None)
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
    def publication2014_Researcher(self):
        return self.__publication2014_Researcher

    @publication2014_Researcher.setter
    def publication2014_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication2014_Researcher__publication2014_Researcher", None)
        self.__publication2014_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication2014_Write"):
                    opp_val = getattr(item, "publication2014_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "publication2014_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication2014_Write"):
                    opp_val = getattr(item, "publication2014_Write", None)
                    
                    setattr(item, "publication2014_Write", self)
                    
