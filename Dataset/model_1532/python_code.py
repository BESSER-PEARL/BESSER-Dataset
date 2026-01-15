from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class research_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class research_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class research_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Counted:

    pass
class Labelled:

    pass
class research_Collaboration:

    def __init__(self, ratio: int, research_Collaboration: "research_Researcher" = None, research_Collaboration58: "research_Paper" = None):
        self.ratio = ratio
        self.research_Collaboration = research_Collaboration
        self.research_Collaboration58 = research_Collaboration58
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def research_Collaboration(self):
        return self.__research_Collaboration

    @research_Collaboration.setter
    def research_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Collaboration__research_Collaboration", None)
        self.__research_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Researcher10"):
                opp_val = getattr(old_value, "research_Researcher10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Researcher10"):
                opp_val = getattr(value, "research_Researcher10", None)
                if opp_val is None:
                    setattr(value, "research_Researcher10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research_Collaboration58(self):
        return self.__research_Collaboration58

    @research_Collaboration58.setter
    def research_Collaboration58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Collaboration__research_Collaboration58", None)
        self.__research_Collaboration58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Paper59"):
                opp_val = getattr(old_value, "research_Paper59", None)
                if opp_val == self:
                    setattr(old_value, "research_Paper59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Paper59"):
                opp_val = getattr(value, "research_Paper59", None)
                setattr(value, "research_Paper59", self)

class research_Skill:

    def __init__(self, description: str, research_Skill: "research_Researcher" = None):
        self.description = description
        self.research_Skill = research_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research_Skill(self):
        return self.__research_Skill

    @research_Skill.setter
    def research_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Skill__research_Skill", None)
        self.__research_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Researcher6"):
                opp_val = getattr(old_value, "research_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Researcher6"):
                opp_val = getattr(value, "research_Researcher6", None)
                if opp_val is None:
                    setattr(value, "research_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research_PaperKeyword:

    def __init__(self, weight: int, research_PaperKeyword: "research_Paper" = None, research_PaperKeyword55: "research_Keyword" = None):
        self.weight = weight
        self.research_PaperKeyword = research_PaperKeyword
        self.research_PaperKeyword55 = research_PaperKeyword55
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def research_PaperKeyword(self):
        return self.__research_PaperKeyword

    @research_PaperKeyword.setter
    def research_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_PaperKeyword__research_PaperKeyword", None)
        self.__research_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Paper15"):
                opp_val = getattr(old_value, "research_Paper15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Paper15"):
                opp_val = getattr(value, "research_Paper15", None)
                if opp_val is None:
                    setattr(value, "research_Paper15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research_PaperKeyword55(self):
        return self.__research_PaperKeyword55

    @research_PaperKeyword55.setter
    def research_PaperKeyword55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_PaperKeyword__research_PaperKeyword55", None)
        self.__research_PaperKeyword55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Keyword56"):
                opp_val = getattr(old_value, "research_Keyword56", None)
                if opp_val == self:
                    setattr(old_value, "research_Keyword56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Keyword56"):
                opp_val = getattr(value, "research_Keyword56", None)
                setattr(value, "research_Keyword56", self)

class research_Progress(Labelled):

    def __init__(self, percent: int, Progress: "research_Paper" = None, research_Progress: "research_PublicationProcess" = None, progress: "research_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.research_Progress = research_Progress
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
        old_value = getattr(self, f"_research_Progress__progress", None)
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

    @property
    def Progress(self):
        return self.__Progress

    @Progress.setter
    def Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Progress__Progress", None)
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
    def research_Progress(self):
        return self.__research_Progress

    @research_Progress.setter
    def research_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Progress__research_Progress", None)
        self.__research_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_PublicationProcess22"):
                opp_val = getattr(old_value, "research_PublicationProcess22", None)
                if opp_val == self:
                    setattr(old_value, "research_PublicationProcess22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_PublicationProcess22"):
                opp_val = getattr(value, "research_PublicationProcess22", None)
                setattr(value, "research_PublicationProcess22", self)

class research_Phase:

    def __init__(self, name: str, research_Phase: "research_PublicationProcess" = None):
        self.name = name
        self.research_Phase = research_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research_Phase(self):
        return self.__research_Phase

    @research_Phase.setter
    def research_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Phase__research_Phase", None)
        self.__research_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_PublicationProcess"):
                opp_val = getattr(old_value, "research_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_PublicationProcess"):
                opp_val = getattr(value, "research_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "research_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class research_KnowledgeManager(Named):

    pass
class research_Paper(Named):

    pass
class research_ReviewNote(Named):

    def __init__(self, content: str, research_ReviewNote: "research_Paragraph" = None, research_ReviewNote30: "research_Review" = None):
        self.content = content
        self.research_ReviewNote = research_ReviewNote
        self.research_ReviewNote30 = research_ReviewNote30
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research_ReviewNote(self):
        return self.__research_ReviewNote

    @research_ReviewNote.setter
    def research_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_ReviewNote__research_ReviewNote", None)
        self.__research_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Paragraph20"):
                opp_val = getattr(old_value, "research_Paragraph20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Paragraph20"):
                opp_val = getattr(value, "research_Paragraph20", None)
                if opp_val is None:
                    setattr(value, "research_Paragraph20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research_ReviewNote30(self):
        return self.__research_ReviewNote30

    @research_ReviewNote30.setter
    def research_ReviewNote30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_ReviewNote__research_ReviewNote30", None)
        self.__research_ReviewNote30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Review29"):
                opp_val = getattr(old_value, "research_Review29", None)
                if opp_val == self:
                    setattr(old_value, "research_Review29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Review29"):
                opp_val = getattr(value, "research_Review29", None)
                setattr(value, "research_Review29", self)

class research_PublicationSystem(Named):

    pass
class research_Paragraph(Named, Counted):

    def __init__(self, content: str, research_Paragraph: "research_Paper" = None, research_Paragraph20: set["research_ReviewNote"] = None, research_Paragraph27: "research_Write" = None):
        self.content = content
        self.research_Paragraph = research_Paragraph
        self.research_Paragraph20 = research_Paragraph20 if research_Paragraph20 is not None else set()
        self.research_Paragraph27 = research_Paragraph27
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research_Paragraph20(self):
        return self.__research_Paragraph20

    @research_Paragraph20.setter
    def research_Paragraph20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Paragraph__research_Paragraph20", None)
        self.__research_Paragraph20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research_ReviewNote"):
                    opp_val = getattr(item, "research_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "research_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research_ReviewNote"):
                    opp_val = getattr(item, "research_ReviewNote", None)
                    
                    setattr(item, "research_ReviewNote", self)
                    

    @property
    def research_Paragraph27(self):
        return self.__research_Paragraph27

    @research_Paragraph27.setter
    def research_Paragraph27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Paragraph__research_Paragraph27", None)
        self.__research_Paragraph27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Write26"):
                opp_val = getattr(old_value, "research_Write26", None)
                if opp_val == self:
                    setattr(old_value, "research_Write26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Write26"):
                opp_val = getattr(value, "research_Write26", None)
                setattr(value, "research_Write26", self)

    @property
    def research_Paragraph(self):
        return self.__research_Paragraph

    @research_Paragraph.setter
    def research_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Paragraph__research_Paragraph", None)
        self.__research_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Paper"):
                opp_val = getattr(old_value, "research_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Paper"):
                opp_val = getattr(value, "research_Paper", None)
                if opp_val is None:
                    setattr(value, "research_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research_Position(Named):

    def __init__(self, description: str, research_Position: "research_Researcher" = None, research_Position45: "research_PublicationSystem" = None, research_Position48: "research_Position" = None, research_Position46: "research_Position" = None):
        self.description = description
        self.research_Position = research_Position
        self.research_Position45 = research_Position45
        self.research_Position48 = research_Position48
        self.research_Position46 = research_Position46
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research_Position(self):
        return self.__research_Position

    @research_Position.setter
    def research_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Position__research_Position", None)
        self.__research_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Researcher8"):
                opp_val = getattr(old_value, "research_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "research_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Researcher8"):
                opp_val = getattr(value, "research_Researcher8", None)
                setattr(value, "research_Researcher8", self)

    @property
    def research_Position48(self):
        return self.__research_Position48

    @research_Position48.setter
    def research_Position48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Position__research_Position48", None)
        self.__research_Position48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Position46"):
                opp_val = getattr(old_value, "research_Position46", None)
                if opp_val == self:
                    setattr(old_value, "research_Position46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Position46"):
                opp_val = getattr(value, "research_Position46", None)
                setattr(value, "research_Position46", self)

    @property
    def research_Position46(self):
        return self.__research_Position46

    @research_Position46.setter
    def research_Position46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Position__research_Position46", None)
        self.__research_Position46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Position48"):
                opp_val = getattr(old_value, "research_Position48", None)
                if opp_val == self:
                    setattr(old_value, "research_Position48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Position48"):
                opp_val = getattr(value, "research_Position48", None)
                setattr(value, "research_Position48", self)

    @property
    def research_Position45(self):
        return self.__research_Position45

    @research_Position45.setter
    def research_Position45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Position__research_Position45", None)
        self.__research_Position45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_PublicationSystem44"):
                opp_val = getattr(old_value, "research_PublicationSystem44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_PublicationSystem44"):
                opp_val = getattr(value, "research_PublicationSystem44", None)
                if opp_val is None:
                    setattr(value, "research_PublicationSystem44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research_Keyword(Named):

    def __init__(self, description: str, research_Keyword53: "research_KnowledgeManager" = None, research_Keyword56: "research_PaperKeyword" = None, research_Keyword: set["research_Paper"] = None):
        self.description = description
        self.research_Keyword53 = research_Keyword53
        self.research_Keyword56 = research_Keyword56
        self.research_Keyword = research_Keyword if research_Keyword is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research_Keyword(self):
        return self.__research_Keyword

    @research_Keyword.setter
    def research_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Keyword__research_Keyword", None)
        self.__research_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research_Paper50"):
                    opp_val = getattr(item, "research_Paper50", None)
                    
                    if opp_val == self:
                        setattr(item, "research_Paper50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research_Paper50"):
                    opp_val = getattr(item, "research_Paper50", None)
                    
                    setattr(item, "research_Paper50", self)
                    

    @property
    def research_Keyword53(self):
        return self.__research_Keyword53

    @research_Keyword53.setter
    def research_Keyword53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Keyword__research_Keyword53", None)
        self.__research_Keyword53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_KnowledgeManager52"):
                opp_val = getattr(old_value, "research_KnowledgeManager52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_KnowledgeManager52"):
                opp_val = getattr(value, "research_KnowledgeManager52", None)
                if opp_val is None:
                    setattr(value, "research_KnowledgeManager52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research_Keyword56(self):
        return self.__research_Keyword56

    @research_Keyword56.setter
    def research_Keyword56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Keyword__research_Keyword56", None)
        self.__research_Keyword56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_PaperKeyword55"):
                opp_val = getattr(old_value, "research_PaperKeyword55", None)
                if opp_val == self:
                    setattr(old_value, "research_PaperKeyword55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_PaperKeyword55"):
                opp_val = getattr(value, "research_PaperKeyword55", None)
                setattr(value, "research_PaperKeyword55", self)

class research_PublicationStructure(Named):

    pass
class research_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, research_PublicationProcess: set["research_Phase"] = None, research_PublicationProcess22: "research_Progress" = None, research_PublicationProcess39: "research_PublicationSystem" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.research_PublicationProcess = research_PublicationProcess if research_PublicationProcess is not None else set()
        self.research_PublicationProcess22 = research_PublicationProcess22
        self.research_PublicationProcess39 = research_PublicationProcess39
        
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
    def research_PublicationProcess39(self):
        return self.__research_PublicationProcess39

    @research_PublicationProcess39.setter
    def research_PublicationProcess39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_PublicationProcess__research_PublicationProcess39", None)
        self.__research_PublicationProcess39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_PublicationSystem"):
                opp_val = getattr(old_value, "research_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "research_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_PublicationSystem"):
                opp_val = getattr(value, "research_PublicationSystem", None)
                setattr(value, "research_PublicationSystem", self)

    @property
    def research_PublicationProcess(self):
        return self.__research_PublicationProcess

    @research_PublicationProcess.setter
    def research_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_PublicationProcess__research_PublicationProcess", None)
        self.__research_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research_Phase"):
                    opp_val = getattr(item, "research_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "research_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research_Phase"):
                    opp_val = getattr(item, "research_Phase", None)
                    
                    setattr(item, "research_Phase", self)
                    

    @property
    def research_PublicationProcess22(self):
        return self.__research_PublicationProcess22

    @research_PublicationProcess22.setter
    def research_PublicationProcess22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_PublicationProcess__research_PublicationProcess22", None)
        self.__research_PublicationProcess22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Progress"):
                opp_val = getattr(old_value, "research_Progress", None)
                if opp_val == self:
                    setattr(old_value, "research_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Progress"):
                opp_val = getattr(value, "research_Progress", None)
                setattr(value, "research_Progress", self)

class research_Review(Labelled):

    def __init__(self, date: date, research_Review: "research_Researcher" = None, research_Review29: "research_ReviewNote" = None):
        self.date = date
        self.research_Review = research_Review
        self.research_Review29 = research_Review29
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def research_Review(self):
        return self.__research_Review

    @research_Review.setter
    def research_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Review__research_Review", None)
        self.__research_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Researcher3"):
                opp_val = getattr(old_value, "research_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Researcher3"):
                opp_val = getattr(value, "research_Researcher3", None)
                if opp_val is None:
                    setattr(value, "research_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research_Review29(self):
        return self.__research_Review29

    @research_Review29.setter
    def research_Review29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Review__research_Review29", None)
        self.__research_Review29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_ReviewNote30"):
                opp_val = getattr(old_value, "research_ReviewNote30", None)
                if opp_val == self:
                    setattr(old_value, "research_ReviewNote30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_ReviewNote30"):
                opp_val = getattr(value, "research_ReviewNote30", None)
                setattr(value, "research_ReviewNote30", self)

class research_Write(Labelled):

    def __init__(self, timeSpent: int, research_Write: "research_Researcher" = None, research_Write26: "research_Paragraph" = None):
        self.timeSpent = timeSpent
        self.research_Write = research_Write
        self.research_Write26 = research_Write26
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def research_Write26(self):
        return self.__research_Write26

    @research_Write26.setter
    def research_Write26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Write__research_Write26", None)
        self.__research_Write26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Paragraph27"):
                opp_val = getattr(old_value, "research_Paragraph27", None)
                if opp_val == self:
                    setattr(old_value, "research_Paragraph27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Paragraph27"):
                opp_val = getattr(value, "research_Paragraph27", None)
                setattr(value, "research_Paragraph27", self)

    @property
    def research_Write(self):
        return self.__research_Write

    @research_Write.setter
    def research_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Write__research_Write", None)
        self.__research_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Researcher"):
                opp_val = getattr(old_value, "research_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Researcher"):
                opp_val = getattr(value, "research_Researcher", None)
                if opp_val is None:
                    setattr(value, "research_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research_Researcher:

    def __init__(self, name: str, forName: str, research_Researcher: set["research_Write"] = None, research_Researcher3: set["research_Review"] = None, Researcher: "research_Paper" = None, authors: set["research_Paper"] = None, research_Researcher6: set["research_Skill"] = None, research_Researcher8: "research_Position" = None, research_Researcher10: set["research_Collaboration"] = None, research_Researcher32: "research_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.research_Researcher = research_Researcher if research_Researcher is not None else set()
        self.research_Researcher3 = research_Researcher3 if research_Researcher3 is not None else set()
        self.Researcher = Researcher
        self.authors = authors if authors is not None else set()
        self.research_Researcher6 = research_Researcher6 if research_Researcher6 is not None else set()
        self.research_Researcher8 = research_Researcher8
        self.research_Researcher10 = research_Researcher10 if research_Researcher10 is not None else set()
        self.research_Researcher32 = research_Researcher32
        
    @property
    def forName(self) -> str:
        return self.__forName

    @forName.setter
    def forName(self, forName: str):
        self.__forName = forName

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
        old_value = getattr(self, f"_research_Researcher__Researcher", None)
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
    def research_Researcher32(self):
        return self.__research_Researcher32

    @research_Researcher32.setter
    def research_Researcher32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Researcher__research_Researcher32", None)
        self.__research_Researcher32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_PublicationStructure"):
                opp_val = getattr(old_value, "research_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_PublicationStructure"):
                opp_val = getattr(value, "research_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "research_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research_Researcher6(self):
        return self.__research_Researcher6

    @research_Researcher6.setter
    def research_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Researcher__research_Researcher6", None)
        self.__research_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research_Skill"):
                    opp_val = getattr(item, "research_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "research_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research_Skill"):
                    opp_val = getattr(item, "research_Skill", None)
                    
                    setattr(item, "research_Skill", self)
                    

    @property
    def research_Researcher3(self):
        return self.__research_Researcher3

    @research_Researcher3.setter
    def research_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Researcher__research_Researcher3", None)
        self.__research_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research_Review"):
                    opp_val = getattr(item, "research_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "research_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research_Review"):
                    opp_val = getattr(item, "research_Review", None)
                    
                    setattr(item, "research_Review", self)
                    

    @property
    def research_Researcher10(self):
        return self.__research_Researcher10

    @research_Researcher10.setter
    def research_Researcher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Researcher__research_Researcher10", None)
        self.__research_Researcher10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research_Collaboration"):
                    opp_val = getattr(item, "research_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "research_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research_Collaboration"):
                    opp_val = getattr(item, "research_Collaboration", None)
                    
                    setattr(item, "research_Collaboration", self)
                    

    @property
    def research_Researcher8(self):
        return self.__research_Researcher8

    @research_Researcher8.setter
    def research_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Researcher__research_Researcher8", None)
        self.__research_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_Position"):
                opp_val = getattr(old_value, "research_Position", None)
                if opp_val == self:
                    setattr(old_value, "research_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_Position"):
                opp_val = getattr(value, "research_Position", None)
                setattr(value, "research_Position", self)

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Researcher__authors", None)
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
    def research_Researcher(self):
        return self.__research_Researcher

    @research_Researcher.setter
    def research_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_Researcher__research_Researcher", None)
        self.__research_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research_Write"):
                    opp_val = getattr(item, "research_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "research_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research_Write"):
                    opp_val = getattr(item, "research_Write", None)
                    
                    setattr(item, "research_Write", self)
                    
