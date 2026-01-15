from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class research101_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class research101_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class research101_Named(ABC):

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
class research101_PaperKeyword:

    def __init__(self, weight: int, research101_PaperKeyword: "research101_Paper" = None, research101_PaperKeyword55: "research101_Keyword" = None):
        self.weight = weight
        self.research101_PaperKeyword = research101_PaperKeyword
        self.research101_PaperKeyword55 = research101_PaperKeyword55
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def research101_PaperKeyword55(self):
        return self.__research101_PaperKeyword55

    @research101_PaperKeyword55.setter
    def research101_PaperKeyword55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_PaperKeyword__research101_PaperKeyword55", None)
        self.__research101_PaperKeyword55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Keyword56"):
                opp_val = getattr(old_value, "research101_Keyword56", None)
                if opp_val == self:
                    setattr(old_value, "research101_Keyword56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Keyword56"):
                opp_val = getattr(value, "research101_Keyword56", None)
                setattr(value, "research101_Keyword56", self)

    @property
    def research101_PaperKeyword(self):
        return self.__research101_PaperKeyword

    @research101_PaperKeyword.setter
    def research101_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_PaperKeyword__research101_PaperKeyword", None)
        self.__research101_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Paper15"):
                opp_val = getattr(old_value, "research101_Paper15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Paper15"):
                opp_val = getattr(value, "research101_Paper15", None)
                if opp_val is None:
                    setattr(value, "research101_Paper15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research101_Progress(Labelled):

    def __init__(self, percent: int, Progress: "research101_Paper" = None, progress: "research101_Paper" = None, research101_Progress: "research101_PublicationProcess" = None):
        self.percent = percent
        self.Progress = Progress
        self.progress = progress
        self.research101_Progress = research101_Progress
        
    @property
    def percent(self) -> int:
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent

    @property
    def research101_Progress(self):
        return self.__research101_Progress

    @research101_Progress.setter
    def research101_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Progress__research101_Progress", None)
        self.__research101_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_PublicationProcess22"):
                opp_val = getattr(old_value, "research101_PublicationProcess22", None)
                if opp_val == self:
                    setattr(old_value, "research101_PublicationProcess22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_PublicationProcess22"):
                opp_val = getattr(value, "research101_PublicationProcess22", None)
                setattr(value, "research101_PublicationProcess22", self)

    @property
    def Progress(self):
        return self.__Progress

    @Progress.setter
    def Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Progress__Progress", None)
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
        old_value = getattr(self, f"_research101_Progress__progress", None)
        self.__progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Paper24"):
                opp_val = getattr(old_value, "Paper24", None)
                if opp_val == self:
                    setattr(old_value, "Paper24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Paper24"):
                opp_val = getattr(value, "Paper24", None)
                setattr(value, "Paper24", self)

class Counted:

    pass
class research101_Skill:

    def __init__(self, description: str, research101_Skill: "research101_Researcher" = None):
        self.description = description
        self.research101_Skill = research101_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research101_Skill(self):
        return self.__research101_Skill

    @research101_Skill.setter
    def research101_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Skill__research101_Skill", None)
        self.__research101_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Researcher6"):
                opp_val = getattr(old_value, "research101_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Researcher6"):
                opp_val = getattr(value, "research101_Researcher6", None)
                if opp_val is None:
                    setattr(value, "research101_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research101_Review(Labelled):

    def __init__(self, date: date, research101_Review: "research101_Researcher" = None, research101_Review29: "research101_ReviewNote" = None):
        self.date = date
        self.research101_Review = research101_Review
        self.research101_Review29 = research101_Review29
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def research101_Review29(self):
        return self.__research101_Review29

    @research101_Review29.setter
    def research101_Review29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Review__research101_Review29", None)
        self.__research101_Review29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_ReviewNote30"):
                opp_val = getattr(old_value, "research101_ReviewNote30", None)
                if opp_val == self:
                    setattr(old_value, "research101_ReviewNote30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_ReviewNote30"):
                opp_val = getattr(value, "research101_ReviewNote30", None)
                setattr(value, "research101_ReviewNote30", self)

    @property
    def research101_Review(self):
        return self.__research101_Review

    @research101_Review.setter
    def research101_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Review__research101_Review", None)
        self.__research101_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Researcher3"):
                opp_val = getattr(old_value, "research101_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Researcher3"):
                opp_val = getattr(value, "research101_Researcher3", None)
                if opp_val is None:
                    setattr(value, "research101_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research101_Write(Labelled):

    def __init__(self, timeSpent: int, research101_Write: "research101_Researcher" = None, research101_Write26: "research101_Paragraph" = None):
        self.timeSpent = timeSpent
        self.research101_Write = research101_Write
        self.research101_Write26 = research101_Write26
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def research101_Write(self):
        return self.__research101_Write

    @research101_Write.setter
    def research101_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Write__research101_Write", None)
        self.__research101_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Researcher"):
                opp_val = getattr(old_value, "research101_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Researcher"):
                opp_val = getattr(value, "research101_Researcher", None)
                if opp_val is None:
                    setattr(value, "research101_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research101_Write26(self):
        return self.__research101_Write26

    @research101_Write26.setter
    def research101_Write26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Write__research101_Write26", None)
        self.__research101_Write26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Paragraph27"):
                opp_val = getattr(old_value, "research101_Paragraph27", None)
                if opp_val == self:
                    setattr(old_value, "research101_Paragraph27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Paragraph27"):
                opp_val = getattr(value, "research101_Paragraph27", None)
                setattr(value, "research101_Paragraph27", self)

class research101_Collaboration:

    def __init__(self, ratio: int, research101_Collaboration: "research101_Researcher" = None, research101_Collaboration58: "research101_Paper" = None):
        self.ratio = ratio
        self.research101_Collaboration = research101_Collaboration
        self.research101_Collaboration58 = research101_Collaboration58
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def research101_Collaboration58(self):
        return self.__research101_Collaboration58

    @research101_Collaboration58.setter
    def research101_Collaboration58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Collaboration__research101_Collaboration58", None)
        self.__research101_Collaboration58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Paper59"):
                opp_val = getattr(old_value, "research101_Paper59", None)
                if opp_val == self:
                    setattr(old_value, "research101_Paper59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Paper59"):
                opp_val = getattr(value, "research101_Paper59", None)
                setattr(value, "research101_Paper59", self)

    @property
    def research101_Collaboration(self):
        return self.__research101_Collaboration

    @research101_Collaboration.setter
    def research101_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Collaboration__research101_Collaboration", None)
        self.__research101_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Researcher10"):
                opp_val = getattr(old_value, "research101_Researcher10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Researcher10"):
                opp_val = getattr(value, "research101_Researcher10", None)
                if opp_val is None:
                    setattr(value, "research101_Researcher10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class research101_KnowledgeManager(Named):

    pass
class research101_Paper(Named):

    pass
class research101_PublicationStructure(Named):

    pass
class research101_ReviewNote(Named):

    def __init__(self, content: str, research101_ReviewNote: "research101_Paragraph" = None, research101_ReviewNote30: "research101_Review" = None):
        self.content = content
        self.research101_ReviewNote = research101_ReviewNote
        self.research101_ReviewNote30 = research101_ReviewNote30
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research101_ReviewNote30(self):
        return self.__research101_ReviewNote30

    @research101_ReviewNote30.setter
    def research101_ReviewNote30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_ReviewNote__research101_ReviewNote30", None)
        self.__research101_ReviewNote30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Review29"):
                opp_val = getattr(old_value, "research101_Review29", None)
                if opp_val == self:
                    setattr(old_value, "research101_Review29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Review29"):
                opp_val = getattr(value, "research101_Review29", None)
                setattr(value, "research101_Review29", self)

    @property
    def research101_ReviewNote(self):
        return self.__research101_ReviewNote

    @research101_ReviewNote.setter
    def research101_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_ReviewNote__research101_ReviewNote", None)
        self.__research101_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Paragraph20"):
                opp_val = getattr(old_value, "research101_Paragraph20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Paragraph20"):
                opp_val = getattr(value, "research101_Paragraph20", None)
                if opp_val is None:
                    setattr(value, "research101_Paragraph20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research101_Keyword(Named):

    def __init__(self, description: str, research101_Keyword: set["research101_Paper"] = None, research101_Keyword56: "research101_PaperKeyword" = None, research101_Keyword53: "research101_KnowledgeManager" = None):
        self.description = description
        self.research101_Keyword = research101_Keyword if research101_Keyword is not None else set()
        self.research101_Keyword56 = research101_Keyword56
        self.research101_Keyword53 = research101_Keyword53
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research101_Keyword(self):
        return self.__research101_Keyword

    @research101_Keyword.setter
    def research101_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Keyword__research101_Keyword", None)
        self.__research101_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research101_Paper50"):
                    opp_val = getattr(item, "research101_Paper50", None)
                    
                    if opp_val == self:
                        setattr(item, "research101_Paper50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research101_Paper50"):
                    opp_val = getattr(item, "research101_Paper50", None)
                    
                    setattr(item, "research101_Paper50", self)
                    

    @property
    def research101_Keyword56(self):
        return self.__research101_Keyword56

    @research101_Keyword56.setter
    def research101_Keyword56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Keyword__research101_Keyword56", None)
        self.__research101_Keyword56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_PaperKeyword55"):
                opp_val = getattr(old_value, "research101_PaperKeyword55", None)
                if opp_val == self:
                    setattr(old_value, "research101_PaperKeyword55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_PaperKeyword55"):
                opp_val = getattr(value, "research101_PaperKeyword55", None)
                setattr(value, "research101_PaperKeyword55", self)

    @property
    def research101_Keyword53(self):
        return self.__research101_Keyword53

    @research101_Keyword53.setter
    def research101_Keyword53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Keyword__research101_Keyword53", None)
        self.__research101_Keyword53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_KnowledgeManager52"):
                opp_val = getattr(old_value, "research101_KnowledgeManager52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_KnowledgeManager52"):
                opp_val = getattr(value, "research101_KnowledgeManager52", None)
                if opp_val is None:
                    setattr(value, "research101_KnowledgeManager52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research101_PublicationSystem(Named):

    pass
class research101_Paragraph(Named, Counted):

    def __init__(self, content: str, research101_Paragraph: "research101_Paper" = None, research101_Paragraph27: "research101_Write" = None, research101_Paragraph20: set["research101_ReviewNote"] = None):
        self.content = content
        self.research101_Paragraph = research101_Paragraph
        self.research101_Paragraph27 = research101_Paragraph27
        self.research101_Paragraph20 = research101_Paragraph20 if research101_Paragraph20 is not None else set()
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research101_Paragraph(self):
        return self.__research101_Paragraph

    @research101_Paragraph.setter
    def research101_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Paragraph__research101_Paragraph", None)
        self.__research101_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Paper"):
                opp_val = getattr(old_value, "research101_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Paper"):
                opp_val = getattr(value, "research101_Paper", None)
                if opp_val is None:
                    setattr(value, "research101_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research101_Paragraph20(self):
        return self.__research101_Paragraph20

    @research101_Paragraph20.setter
    def research101_Paragraph20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Paragraph__research101_Paragraph20", None)
        self.__research101_Paragraph20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research101_ReviewNote"):
                    opp_val = getattr(item, "research101_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "research101_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research101_ReviewNote"):
                    opp_val = getattr(item, "research101_ReviewNote", None)
                    
                    setattr(item, "research101_ReviewNote", self)
                    

    @property
    def research101_Paragraph27(self):
        return self.__research101_Paragraph27

    @research101_Paragraph27.setter
    def research101_Paragraph27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Paragraph__research101_Paragraph27", None)
        self.__research101_Paragraph27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Write26"):
                opp_val = getattr(old_value, "research101_Write26", None)
                if opp_val == self:
                    setattr(old_value, "research101_Write26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Write26"):
                opp_val = getattr(value, "research101_Write26", None)
                setattr(value, "research101_Write26", self)

class research101_Position(Named):

    def __init__(self, description: str, research101_Position: "research101_Researcher" = None, research101_Position45: "research101_PublicationSystem" = None, research101_Position48: "research101_Position" = None, research101_Position46: "research101_Position" = None):
        self.description = description
        self.research101_Position = research101_Position
        self.research101_Position45 = research101_Position45
        self.research101_Position48 = research101_Position48
        self.research101_Position46 = research101_Position46
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research101_Position48(self):
        return self.__research101_Position48

    @research101_Position48.setter
    def research101_Position48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Position__research101_Position48", None)
        self.__research101_Position48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Position46"):
                opp_val = getattr(old_value, "research101_Position46", None)
                if opp_val == self:
                    setattr(old_value, "research101_Position46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Position46"):
                opp_val = getattr(value, "research101_Position46", None)
                setattr(value, "research101_Position46", self)

    @property
    def research101_Position46(self):
        return self.__research101_Position46

    @research101_Position46.setter
    def research101_Position46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Position__research101_Position46", None)
        self.__research101_Position46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Position48"):
                opp_val = getattr(old_value, "research101_Position48", None)
                if opp_val == self:
                    setattr(old_value, "research101_Position48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Position48"):
                opp_val = getattr(value, "research101_Position48", None)
                setattr(value, "research101_Position48", self)

    @property
    def research101_Position45(self):
        return self.__research101_Position45

    @research101_Position45.setter
    def research101_Position45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Position__research101_Position45", None)
        self.__research101_Position45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_PublicationSystem44"):
                opp_val = getattr(old_value, "research101_PublicationSystem44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_PublicationSystem44"):
                opp_val = getattr(value, "research101_PublicationSystem44", None)
                if opp_val is None:
                    setattr(value, "research101_PublicationSystem44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research101_Position(self):
        return self.__research101_Position

    @research101_Position.setter
    def research101_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Position__research101_Position", None)
        self.__research101_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Researcher8"):
                opp_val = getattr(old_value, "research101_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "research101_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Researcher8"):
                opp_val = getattr(value, "research101_Researcher8", None)
                setattr(value, "research101_Researcher8", self)

class research101_PublicationProcess(Named):

    def __init__(self, maxTime: int, minTime: int, research101_PublicationProcess: set["research101_Phase"] = None, research101_PublicationProcess22: "research101_Progress" = None, research101_PublicationProcess39: "research101_PublicationSystem" = None):
        self.maxTime = maxTime
        self.minTime = minTime
        self.research101_PublicationProcess = research101_PublicationProcess if research101_PublicationProcess is not None else set()
        self.research101_PublicationProcess22 = research101_PublicationProcess22
        self.research101_PublicationProcess39 = research101_PublicationProcess39
        
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
    def research101_PublicationProcess22(self):
        return self.__research101_PublicationProcess22

    @research101_PublicationProcess22.setter
    def research101_PublicationProcess22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_PublicationProcess__research101_PublicationProcess22", None)
        self.__research101_PublicationProcess22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Progress"):
                opp_val = getattr(old_value, "research101_Progress", None)
                if opp_val == self:
                    setattr(old_value, "research101_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Progress"):
                opp_val = getattr(value, "research101_Progress", None)
                setattr(value, "research101_Progress", self)

    @property
    def research101_PublicationProcess39(self):
        return self.__research101_PublicationProcess39

    @research101_PublicationProcess39.setter
    def research101_PublicationProcess39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_PublicationProcess__research101_PublicationProcess39", None)
        self.__research101_PublicationProcess39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_PublicationSystem"):
                opp_val = getattr(old_value, "research101_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "research101_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_PublicationSystem"):
                opp_val = getattr(value, "research101_PublicationSystem", None)
                setattr(value, "research101_PublicationSystem", self)

    @property
    def research101_PublicationProcess(self):
        return self.__research101_PublicationProcess

    @research101_PublicationProcess.setter
    def research101_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_PublicationProcess__research101_PublicationProcess", None)
        self.__research101_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research101_Phase"):
                    opp_val = getattr(item, "research101_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "research101_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research101_Phase"):
                    opp_val = getattr(item, "research101_Phase", None)
                    
                    setattr(item, "research101_Phase", self)
                    

class research101_Researcher:

    def __init__(self, name: str, forName: str, research101_Researcher10: set["research101_Collaboration"] = None, research101_Researcher: set["research101_Write"] = None, research101_Researcher3: set["research101_Review"] = None, authors: set["research101_Paper"] = None, research101_Researcher6: set["research101_Skill"] = None, research101_Researcher8: "research101_Position" = None, Researcher: "research101_Paper" = None, research101_Researcher32: "research101_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.research101_Researcher10 = research101_Researcher10 if research101_Researcher10 is not None else set()
        self.research101_Researcher = research101_Researcher if research101_Researcher is not None else set()
        self.research101_Researcher3 = research101_Researcher3 if research101_Researcher3 is not None else set()
        self.authors = authors if authors is not None else set()
        self.research101_Researcher6 = research101_Researcher6 if research101_Researcher6 is not None else set()
        self.research101_Researcher8 = research101_Researcher8
        self.Researcher = Researcher
        self.research101_Researcher32 = research101_Researcher32
        
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
    def research101_Researcher3(self):
        return self.__research101_Researcher3

    @research101_Researcher3.setter
    def research101_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Researcher__research101_Researcher3", None)
        self.__research101_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research101_Review"):
                    opp_val = getattr(item, "research101_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "research101_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research101_Review"):
                    opp_val = getattr(item, "research101_Review", None)
                    
                    setattr(item, "research101_Review", self)
                    

    @property
    def research101_Researcher(self):
        return self.__research101_Researcher

    @research101_Researcher.setter
    def research101_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Researcher__research101_Researcher", None)
        self.__research101_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research101_Write"):
                    opp_val = getattr(item, "research101_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "research101_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research101_Write"):
                    opp_val = getattr(item, "research101_Write", None)
                    
                    setattr(item, "research101_Write", self)
                    

    @property
    def research101_Researcher6(self):
        return self.__research101_Researcher6

    @research101_Researcher6.setter
    def research101_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Researcher__research101_Researcher6", None)
        self.__research101_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research101_Skill"):
                    opp_val = getattr(item, "research101_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "research101_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research101_Skill"):
                    opp_val = getattr(item, "research101_Skill", None)
                    
                    setattr(item, "research101_Skill", self)
                    

    @property
    def research101_Researcher10(self):
        return self.__research101_Researcher10

    @research101_Researcher10.setter
    def research101_Researcher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Researcher__research101_Researcher10", None)
        self.__research101_Researcher10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research101_Collaboration"):
                    opp_val = getattr(item, "research101_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "research101_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research101_Collaboration"):
                    opp_val = getattr(item, "research101_Collaboration", None)
                    
                    setattr(item, "research101_Collaboration", self)
                    

    @property
    def research101_Researcher8(self):
        return self.__research101_Researcher8

    @research101_Researcher8.setter
    def research101_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Researcher__research101_Researcher8", None)
        self.__research101_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_Position"):
                opp_val = getattr(old_value, "research101_Position", None)
                if opp_val == self:
                    setattr(old_value, "research101_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_Position"):
                opp_val = getattr(value, "research101_Position", None)
                setattr(value, "research101_Position", self)

    @property
    def research101_Researcher32(self):
        return self.__research101_Researcher32

    @research101_Researcher32.setter
    def research101_Researcher32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Researcher__research101_Researcher32", None)
        self.__research101_Researcher32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_PublicationStructure"):
                opp_val = getattr(old_value, "research101_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_PublicationStructure"):
                opp_val = getattr(value, "research101_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "research101_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Researcher__authors", None)
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
        old_value = getattr(self, f"_research101_Researcher__Researcher", None)
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

class research101_Phase:

    def __init__(self, name: str, research101_Phase: "research101_PublicationProcess" = None):
        self.name = name
        self.research101_Phase = research101_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research101_Phase(self):
        return self.__research101_Phase

    @research101_Phase.setter
    def research101_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research101_Phase__research101_Phase", None)
        self.__research101_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research101_PublicationProcess"):
                opp_val = getattr(old_value, "research101_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research101_PublicationProcess"):
                opp_val = getattr(value, "research101_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "research101_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
