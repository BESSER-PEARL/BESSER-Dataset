from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class tp4_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class tp4_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class tp4_Named(ABC):

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
class Counted:

    pass
class tp4_Review(Labelled):

    def __init__(self, date: date, tp4_Review: "tp4_Researcher" = None, tp4_Review24: "tp4_ReviewNote" = None):
        self.date = date
        self.tp4_Review = tp4_Review
        self.tp4_Review24 = tp4_Review24
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def tp4_Review(self):
        return self.__tp4_Review

    @tp4_Review.setter
    def tp4_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Review__tp4_Review", None)
        self.__tp4_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Researcher3"):
                opp_val = getattr(old_value, "tp4_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Researcher3"):
                opp_val = getattr(value, "tp4_Researcher3", None)
                if opp_val is None:
                    setattr(value, "tp4_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp4_Review24(self):
        return self.__tp4_Review24

    @tp4_Review24.setter
    def tp4_Review24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Review__tp4_Review24", None)
        self.__tp4_Review24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_ReviewNote25"):
                opp_val = getattr(old_value, "tp4_ReviewNote25", None)
                if opp_val == self:
                    setattr(old_value, "tp4_ReviewNote25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_ReviewNote25"):
                opp_val = getattr(value, "tp4_ReviewNote25", None)
                setattr(value, "tp4_ReviewNote25", self)

class tp4_Progress(Labelled):

    def __init__(self, percent: int, Progress: "tp4_Paper" = None, tp4_Progress: "tp4_PublicationProcess" = None, progress: "tp4_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.tp4_Progress = tp4_Progress
        self.progress = progress
        
    @property
    def percent(self) -> int:
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent

    @property
    def tp4_Progress(self):
        return self.__tp4_Progress

    @tp4_Progress.setter
    def tp4_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Progress__tp4_Progress", None)
        self.__tp4_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_PublicationProcess17"):
                opp_val = getattr(old_value, "tp4_PublicationProcess17", None)
                if opp_val == self:
                    setattr(old_value, "tp4_PublicationProcess17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_PublicationProcess17"):
                opp_val = getattr(value, "tp4_PublicationProcess17", None)
                setattr(value, "tp4_PublicationProcess17", self)

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Progress__progress", None)
        self.__progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Paper19"):
                opp_val = getattr(old_value, "Paper19", None)
                if opp_val == self:
                    setattr(old_value, "Paper19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Paper19"):
                opp_val = getattr(value, "Paper19", None)
                setattr(value, "Paper19", self)

    @property
    def Progress(self):
        return self.__Progress

    @Progress.setter
    def Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Progress__Progress", None)
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

class tp4_Skill:

    def __init__(self, description: str, tp4_Skill: "tp4_Researcher" = None):
        self.description = description
        self.tp4_Skill = tp4_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def tp4_Skill(self):
        return self.__tp4_Skill

    @tp4_Skill.setter
    def tp4_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Skill__tp4_Skill", None)
        self.__tp4_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Researcher6"):
                opp_val = getattr(old_value, "tp4_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Researcher6"):
                opp_val = getattr(value, "tp4_Researcher6", None)
                if opp_val is None:
                    setattr(value, "tp4_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tp4_Write(Labelled):

    def __init__(self, timeSpent: int, tp4_Write: "tp4_Researcher" = None, tp4_Write21: "tp4_Paragraph" = None):
        self.timeSpent = timeSpent
        self.tp4_Write = tp4_Write
        self.tp4_Write21 = tp4_Write21
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def tp4_Write(self):
        return self.__tp4_Write

    @tp4_Write.setter
    def tp4_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Write__tp4_Write", None)
        self.__tp4_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Researcher"):
                opp_val = getattr(old_value, "tp4_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Researcher"):
                opp_val = getattr(value, "tp4_Researcher", None)
                if opp_val is None:
                    setattr(value, "tp4_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp4_Write21(self):
        return self.__tp4_Write21

    @tp4_Write21.setter
    def tp4_Write21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Write__tp4_Write21", None)
        self.__tp4_Write21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Paragraph22"):
                opp_val = getattr(old_value, "tp4_Paragraph22", None)
                if opp_val == self:
                    setattr(old_value, "tp4_Paragraph22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Paragraph22"):
                opp_val = getattr(value, "tp4_Paragraph22", None)
                setattr(value, "tp4_Paragraph22", self)

class tp4_Researcher:

    def __init__(self, name: str, forName: str, tp4_Researcher6: set["tp4_Skill"] = None, tp4_Researcher8: "tp4_Position" = None, tp4_Researcher: set["tp4_Write"] = None, tp4_Researcher3: set["tp4_Review"] = None, authors: set["tp4_Paper"] = None, Researcher: "tp4_Paper" = None, tp4_Researcher27: "tp4_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.tp4_Researcher6 = tp4_Researcher6 if tp4_Researcher6 is not None else set()
        self.tp4_Researcher8 = tp4_Researcher8
        self.tp4_Researcher = tp4_Researcher if tp4_Researcher is not None else set()
        self.tp4_Researcher3 = tp4_Researcher3 if tp4_Researcher3 is not None else set()
        self.authors = authors if authors is not None else set()
        self.Researcher = Researcher
        self.tp4_Researcher27 = tp4_Researcher27
        
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
    def tp4_Researcher(self):
        return self.__tp4_Researcher

    @tp4_Researcher.setter
    def tp4_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Researcher__tp4_Researcher", None)
        self.__tp4_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp4_Write"):
                    opp_val = getattr(item, "tp4_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "tp4_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp4_Write"):
                    opp_val = getattr(item, "tp4_Write", None)
                    
                    setattr(item, "tp4_Write", self)
                    

    @property
    def tp4_Researcher6(self):
        return self.__tp4_Researcher6

    @tp4_Researcher6.setter
    def tp4_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Researcher__tp4_Researcher6", None)
        self.__tp4_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp4_Skill"):
                    opp_val = getattr(item, "tp4_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "tp4_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp4_Skill"):
                    opp_val = getattr(item, "tp4_Skill", None)
                    
                    setattr(item, "tp4_Skill", self)
                    

    @property
    def tp4_Researcher8(self):
        return self.__tp4_Researcher8

    @tp4_Researcher8.setter
    def tp4_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Researcher__tp4_Researcher8", None)
        self.__tp4_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Position"):
                opp_val = getattr(old_value, "tp4_Position", None)
                if opp_val == self:
                    setattr(old_value, "tp4_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Position"):
                opp_val = getattr(value, "tp4_Position", None)
                setattr(value, "tp4_Position", self)

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Researcher__Researcher", None)
        self.__Researcher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "res_papers"):
                opp_val = getattr(old_value, "res_papers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "res_papers"):
                opp_val = getattr(value, "res_papers", None)
                if opp_val is None:
                    setattr(value, "res_papers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp4_Researcher3(self):
        return self.__tp4_Researcher3

    @tp4_Researcher3.setter
    def tp4_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Researcher__tp4_Researcher3", None)
        self.__tp4_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp4_Review"):
                    opp_val = getattr(item, "tp4_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "tp4_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp4_Review"):
                    opp_val = getattr(item, "tp4_Review", None)
                    
                    setattr(item, "tp4_Review", self)
                    

    @property
    def tp4_Researcher27(self):
        return self.__tp4_Researcher27

    @tp4_Researcher27.setter
    def tp4_Researcher27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Researcher__tp4_Researcher27", None)
        self.__tp4_Researcher27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_PublicationStructure"):
                opp_val = getattr(old_value, "tp4_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_PublicationStructure"):
                opp_val = getattr(value, "tp4_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "tp4_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Researcher__authors", None)
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
                    

class tp4_Phases:

    def __init__(self, name: str, tp4_Phases: "tp4_PublicationProcess" = None):
        self.name = name
        self.tp4_Phases = tp4_Phases
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tp4_Phases(self):
        return self.__tp4_Phases

    @tp4_Phases.setter
    def tp4_Phases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Phases__tp4_Phases", None)
        self.__tp4_Phases = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_PublicationProcess"):
                opp_val = getattr(old_value, "tp4_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_PublicationProcess"):
                opp_val = getattr(value, "tp4_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "tp4_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class tp4_PublicationSystem(Named):

    pass
class tp4_Paper(Named):

    pass
class tp4_PublicationStructure(Named):

    pass
class tp4_ReviewNote(Named):

    def __init__(self, content: str, tp4_ReviewNote: "tp4_Paragraph" = None, tp4_ReviewNote25: "tp4_Review" = None):
        self.content = content
        self.tp4_ReviewNote = tp4_ReviewNote
        self.tp4_ReviewNote25 = tp4_ReviewNote25
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def tp4_ReviewNote(self):
        return self.__tp4_ReviewNote

    @tp4_ReviewNote.setter
    def tp4_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_ReviewNote__tp4_ReviewNote", None)
        self.__tp4_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Paragraph15"):
                opp_val = getattr(old_value, "tp4_Paragraph15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Paragraph15"):
                opp_val = getattr(value, "tp4_Paragraph15", None)
                if opp_val is None:
                    setattr(value, "tp4_Paragraph15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp4_ReviewNote25(self):
        return self.__tp4_ReviewNote25

    @tp4_ReviewNote25.setter
    def tp4_ReviewNote25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_ReviewNote__tp4_ReviewNote25", None)
        self.__tp4_ReviewNote25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Review24"):
                opp_val = getattr(old_value, "tp4_Review24", None)
                if opp_val == self:
                    setattr(old_value, "tp4_Review24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Review24"):
                opp_val = getattr(value, "tp4_Review24", None)
                setattr(value, "tp4_Review24", self)

class tp4_Position(Named):

    def __init__(self, description: str, tp4_Position: "tp4_Researcher" = None, tp4_Position38: "tp4_PublicationSystem" = None, tp4_Position44: "tp4_Position" = None, tp4_Position42: "tp4_Position" = None):
        self.description = description
        self.tp4_Position = tp4_Position
        self.tp4_Position38 = tp4_Position38
        self.tp4_Position44 = tp4_Position44
        self.tp4_Position42 = tp4_Position42
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def tp4_Position44(self):
        return self.__tp4_Position44

    @tp4_Position44.setter
    def tp4_Position44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Position__tp4_Position44", None)
        self.__tp4_Position44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Position42"):
                opp_val = getattr(old_value, "tp4_Position42", None)
                if opp_val == self:
                    setattr(old_value, "tp4_Position42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Position42"):
                opp_val = getattr(value, "tp4_Position42", None)
                setattr(value, "tp4_Position42", self)

    @property
    def tp4_Position42(self):
        return self.__tp4_Position42

    @tp4_Position42.setter
    def tp4_Position42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Position__tp4_Position42", None)
        self.__tp4_Position42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Position44"):
                opp_val = getattr(old_value, "tp4_Position44", None)
                if opp_val == self:
                    setattr(old_value, "tp4_Position44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Position44"):
                opp_val = getattr(value, "tp4_Position44", None)
                setattr(value, "tp4_Position44", self)

    @property
    def tp4_Position(self):
        return self.__tp4_Position

    @tp4_Position.setter
    def tp4_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Position__tp4_Position", None)
        self.__tp4_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Researcher8"):
                opp_val = getattr(old_value, "tp4_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "tp4_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Researcher8"):
                opp_val = getattr(value, "tp4_Researcher8", None)
                setattr(value, "tp4_Researcher8", self)

    @property
    def tp4_Position38(self):
        return self.__tp4_Position38

    @tp4_Position38.setter
    def tp4_Position38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Position__tp4_Position38", None)
        self.__tp4_Position38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_PublicationSystem37"):
                opp_val = getattr(old_value, "tp4_PublicationSystem37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_PublicationSystem37"):
                opp_val = getattr(value, "tp4_PublicationSystem37", None)
                if opp_val is None:
                    setattr(value, "tp4_PublicationSystem37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tp4_Paragraph(Named, Counted):

    def __init__(self, content: str, tp4_Paragraph: "tp4_Paper" = None, tp4_Paragraph15: set["tp4_ReviewNote"] = None, tp4_Paragraph22: "tp4_Write" = None):
        self.content = content
        self.tp4_Paragraph = tp4_Paragraph
        self.tp4_Paragraph15 = tp4_Paragraph15 if tp4_Paragraph15 is not None else set()
        self.tp4_Paragraph22 = tp4_Paragraph22
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def tp4_Paragraph22(self):
        return self.__tp4_Paragraph22

    @tp4_Paragraph22.setter
    def tp4_Paragraph22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Paragraph__tp4_Paragraph22", None)
        self.__tp4_Paragraph22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Write21"):
                opp_val = getattr(old_value, "tp4_Write21", None)
                if opp_val == self:
                    setattr(old_value, "tp4_Write21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Write21"):
                opp_val = getattr(value, "tp4_Write21", None)
                setattr(value, "tp4_Write21", self)

    @property
    def tp4_Paragraph(self):
        return self.__tp4_Paragraph

    @tp4_Paragraph.setter
    def tp4_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Paragraph__tp4_Paragraph", None)
        self.__tp4_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Paper"):
                opp_val = getattr(old_value, "tp4_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Paper"):
                opp_val = getattr(value, "tp4_Paper", None)
                if opp_val is None:
                    setattr(value, "tp4_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp4_Paragraph15(self):
        return self.__tp4_Paragraph15

    @tp4_Paragraph15.setter
    def tp4_Paragraph15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Paragraph__tp4_Paragraph15", None)
        self.__tp4_Paragraph15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp4_ReviewNote"):
                    opp_val = getattr(item, "tp4_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "tp4_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp4_ReviewNote"):
                    opp_val = getattr(item, "tp4_ReviewNote", None)
                    
                    setattr(item, "tp4_ReviewNote", self)
                    

class tp4_Keyword(Named):

    def __init__(self, description: str, tp4_Keyword: "tp4_Paper" = None, tp4_Keyword41: "tp4_PublicationSystem" = None):
        self.description = description
        self.tp4_Keyword = tp4_Keyword
        self.tp4_Keyword41 = tp4_Keyword41
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def tp4_Keyword(self):
        return self.__tp4_Keyword

    @tp4_Keyword.setter
    def tp4_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Keyword__tp4_Keyword", None)
        self.__tp4_Keyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Paper13"):
                opp_val = getattr(old_value, "tp4_Paper13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Paper13"):
                opp_val = getattr(value, "tp4_Paper13", None)
                if opp_val is None:
                    setattr(value, "tp4_Paper13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp4_Keyword41(self):
        return self.__tp4_Keyword41

    @tp4_Keyword41.setter
    def tp4_Keyword41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_Keyword__tp4_Keyword41", None)
        self.__tp4_Keyword41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_PublicationSystem40"):
                opp_val = getattr(old_value, "tp4_PublicationSystem40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_PublicationSystem40"):
                opp_val = getattr(value, "tp4_PublicationSystem40", None)
                if opp_val is None:
                    setattr(value, "tp4_PublicationSystem40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tp4_PublicationProcess(Named):

    def __init__(self, maxTime: int, minTime: int, tp4_PublicationProcess: set["tp4_Phases"] = None, tp4_PublicationProcess17: "tp4_Progress" = None, tp4_PublicationProcess32: "tp4_PublicationSystem" = None):
        self.maxTime = maxTime
        self.minTime = minTime
        self.tp4_PublicationProcess = tp4_PublicationProcess if tp4_PublicationProcess is not None else set()
        self.tp4_PublicationProcess17 = tp4_PublicationProcess17
        self.tp4_PublicationProcess32 = tp4_PublicationProcess32
        
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
    def tp4_PublicationProcess(self):
        return self.__tp4_PublicationProcess

    @tp4_PublicationProcess.setter
    def tp4_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_PublicationProcess__tp4_PublicationProcess", None)
        self.__tp4_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp4_Phases"):
                    opp_val = getattr(item, "tp4_Phases", None)
                    
                    if opp_val == self:
                        setattr(item, "tp4_Phases", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp4_Phases"):
                    opp_val = getattr(item, "tp4_Phases", None)
                    
                    setattr(item, "tp4_Phases", self)
                    

    @property
    def tp4_PublicationProcess17(self):
        return self.__tp4_PublicationProcess17

    @tp4_PublicationProcess17.setter
    def tp4_PublicationProcess17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_PublicationProcess__tp4_PublicationProcess17", None)
        self.__tp4_PublicationProcess17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_Progress"):
                opp_val = getattr(old_value, "tp4_Progress", None)
                if opp_val == self:
                    setattr(old_value, "tp4_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_Progress"):
                opp_val = getattr(value, "tp4_Progress", None)
                setattr(value, "tp4_Progress", self)

    @property
    def tp4_PublicationProcess32(self):
        return self.__tp4_PublicationProcess32

    @tp4_PublicationProcess32.setter
    def tp4_PublicationProcess32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp4_PublicationProcess__tp4_PublicationProcess32", None)
        self.__tp4_PublicationProcess32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp4_PublicationSystem"):
                opp_val = getattr(old_value, "tp4_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "tp4_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp4_PublicationSystem"):
                opp_val = getattr(value, "tp4_PublicationSystem", None)
                setattr(value, "tp4_PublicationSystem", self)
