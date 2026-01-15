from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class research15_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class research15_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class research15_Named(ABC):

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
class research15_PaperKeyword:

    def __init__(self, weight: int, research15_PaperKeyword: "research15_Paper" = None, research15_PaperKeyword55: "research15_Keyword" = None):
        self.weight = weight
        self.research15_PaperKeyword = research15_PaperKeyword
        self.research15_PaperKeyword55 = research15_PaperKeyword55
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def research15_PaperKeyword(self):
        return self.__research15_PaperKeyword

    @research15_PaperKeyword.setter
    def research15_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_PaperKeyword__research15_PaperKeyword", None)
        self.__research15_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Paper15"):
                opp_val = getattr(old_value, "research15_Paper15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Paper15"):
                opp_val = getattr(value, "research15_Paper15", None)
                if opp_val is None:
                    setattr(value, "research15_Paper15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research15_PaperKeyword55(self):
        return self.__research15_PaperKeyword55

    @research15_PaperKeyword55.setter
    def research15_PaperKeyword55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_PaperKeyword__research15_PaperKeyword55", None)
        self.__research15_PaperKeyword55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Keyword56"):
                opp_val = getattr(old_value, "research15_Keyword56", None)
                if opp_val == self:
                    setattr(old_value, "research15_Keyword56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Keyword56"):
                opp_val = getattr(value, "research15_Keyword56", None)
                setattr(value, "research15_Keyword56", self)

class research15_Progress(Labelled):

    def __init__(self, percent: int, Progress: "research15_Paper" = None, research15_Progress: "research15_PublicationProcess" = None, progress: "research15_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.research15_Progress = research15_Progress
        self.progress = progress
        
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
        old_value = getattr(self, f"_research15_Progress__Progress", None)
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
        old_value = getattr(self, f"_research15_Progress__progress", None)
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
    def research15_Progress(self):
        return self.__research15_Progress

    @research15_Progress.setter
    def research15_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Progress__research15_Progress", None)
        self.__research15_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_PublicationProcess22"):
                opp_val = getattr(old_value, "research15_PublicationProcess22", None)
                if opp_val == self:
                    setattr(old_value, "research15_PublicationProcess22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_PublicationProcess22"):
                opp_val = getattr(value, "research15_PublicationProcess22", None)
                setattr(value, "research15_PublicationProcess22", self)

class research15_Collaboration:

    def __init__(self, ratio: int, research15_Collaboration: "research15_Researcher" = None, research15_Collaboration58: "research15_Paper" = None):
        self.ratio = ratio
        self.research15_Collaboration = research15_Collaboration
        self.research15_Collaboration58 = research15_Collaboration58
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def research15_Collaboration(self):
        return self.__research15_Collaboration

    @research15_Collaboration.setter
    def research15_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Collaboration__research15_Collaboration", None)
        self.__research15_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Researcher10"):
                opp_val = getattr(old_value, "research15_Researcher10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Researcher10"):
                opp_val = getattr(value, "research15_Researcher10", None)
                if opp_val is None:
                    setattr(value, "research15_Researcher10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research15_Collaboration58(self):
        return self.__research15_Collaboration58

    @research15_Collaboration58.setter
    def research15_Collaboration58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Collaboration__research15_Collaboration58", None)
        self.__research15_Collaboration58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Paper59"):
                opp_val = getattr(old_value, "research15_Paper59", None)
                if opp_val == self:
                    setattr(old_value, "research15_Paper59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Paper59"):
                opp_val = getattr(value, "research15_Paper59", None)
                setattr(value, "research15_Paper59", self)

class Counted:

    pass
class research15_Review(Labelled):

    def __init__(self, date: date, research15_Review: "research15_Researcher" = None, research15_Review29: "research15_ReviewNote" = None):
        self.date = date
        self.research15_Review = research15_Review
        self.research15_Review29 = research15_Review29
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def research15_Review(self):
        return self.__research15_Review

    @research15_Review.setter
    def research15_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Review__research15_Review", None)
        self.__research15_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Researcher3"):
                opp_val = getattr(old_value, "research15_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Researcher3"):
                opp_val = getattr(value, "research15_Researcher3", None)
                if opp_val is None:
                    setattr(value, "research15_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research15_Review29(self):
        return self.__research15_Review29

    @research15_Review29.setter
    def research15_Review29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Review__research15_Review29", None)
        self.__research15_Review29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_ReviewNote30"):
                opp_val = getattr(old_value, "research15_ReviewNote30", None)
                if opp_val == self:
                    setattr(old_value, "research15_ReviewNote30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_ReviewNote30"):
                opp_val = getattr(value, "research15_ReviewNote30", None)
                setattr(value, "research15_ReviewNote30", self)

class research15_Write(Labelled):

    def __init__(self, timeSpent: int, research15_Write: "research15_Researcher" = None, research15_Write26: "research15_Paragraph" = None):
        self.timeSpent = timeSpent
        self.research15_Write = research15_Write
        self.research15_Write26 = research15_Write26
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def research15_Write(self):
        return self.__research15_Write

    @research15_Write.setter
    def research15_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Write__research15_Write", None)
        self.__research15_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Researcher"):
                opp_val = getattr(old_value, "research15_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Researcher"):
                opp_val = getattr(value, "research15_Researcher", None)
                if opp_val is None:
                    setattr(value, "research15_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research15_Write26(self):
        return self.__research15_Write26

    @research15_Write26.setter
    def research15_Write26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Write__research15_Write26", None)
        self.__research15_Write26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Paragraph27"):
                opp_val = getattr(old_value, "research15_Paragraph27", None)
                if opp_val == self:
                    setattr(old_value, "research15_Paragraph27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Paragraph27"):
                opp_val = getattr(value, "research15_Paragraph27", None)
                setattr(value, "research15_Paragraph27", self)

class research15_Researcher:

    def __init__(self, name: str, forName: str, authors: set["research15_Paper"] = None, research15_Researcher6: set["research15_Skill"] = None, research15_Researcher: set["research15_Write"] = None, research15_Researcher3: set["research15_Review"] = None, research15_Researcher8: "research15_Position" = None, research15_Researcher10: set["research15_Collaboration"] = None, Researcher: "research15_Paper" = None, research15_Researcher32: "research15_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.authors = authors if authors is not None else set()
        self.research15_Researcher6 = research15_Researcher6 if research15_Researcher6 is not None else set()
        self.research15_Researcher = research15_Researcher if research15_Researcher is not None else set()
        self.research15_Researcher3 = research15_Researcher3 if research15_Researcher3 is not None else set()
        self.research15_Researcher8 = research15_Researcher8
        self.research15_Researcher10 = research15_Researcher10 if research15_Researcher10 is not None else set()
        self.Researcher = Researcher
        self.research15_Researcher32 = research15_Researcher32
        
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
    def research15_Researcher6(self):
        return self.__research15_Researcher6

    @research15_Researcher6.setter
    def research15_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Researcher__research15_Researcher6", None)
        self.__research15_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research15_Skill"):
                    opp_val = getattr(item, "research15_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "research15_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research15_Skill"):
                    opp_val = getattr(item, "research15_Skill", None)
                    
                    setattr(item, "research15_Skill", self)
                    

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Researcher__authors", None)
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
    def research15_Researcher32(self):
        return self.__research15_Researcher32

    @research15_Researcher32.setter
    def research15_Researcher32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Researcher__research15_Researcher32", None)
        self.__research15_Researcher32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_PublicationStructure"):
                opp_val = getattr(old_value, "research15_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_PublicationStructure"):
                opp_val = getattr(value, "research15_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "research15_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Researcher__Researcher", None)
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
    def research15_Researcher8(self):
        return self.__research15_Researcher8

    @research15_Researcher8.setter
    def research15_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Researcher__research15_Researcher8", None)
        self.__research15_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Position"):
                opp_val = getattr(old_value, "research15_Position", None)
                if opp_val == self:
                    setattr(old_value, "research15_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Position"):
                opp_val = getattr(value, "research15_Position", None)
                setattr(value, "research15_Position", self)

    @property
    def research15_Researcher10(self):
        return self.__research15_Researcher10

    @research15_Researcher10.setter
    def research15_Researcher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Researcher__research15_Researcher10", None)
        self.__research15_Researcher10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research15_Collaboration"):
                    opp_val = getattr(item, "research15_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "research15_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research15_Collaboration"):
                    opp_val = getattr(item, "research15_Collaboration", None)
                    
                    setattr(item, "research15_Collaboration", self)
                    

    @property
    def research15_Researcher(self):
        return self.__research15_Researcher

    @research15_Researcher.setter
    def research15_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Researcher__research15_Researcher", None)
        self.__research15_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research15_Write"):
                    opp_val = getattr(item, "research15_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "research15_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research15_Write"):
                    opp_val = getattr(item, "research15_Write", None)
                    
                    setattr(item, "research15_Write", self)
                    

    @property
    def research15_Researcher3(self):
        return self.__research15_Researcher3

    @research15_Researcher3.setter
    def research15_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Researcher__research15_Researcher3", None)
        self.__research15_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research15_Review"):
                    opp_val = getattr(item, "research15_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "research15_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research15_Review"):
                    opp_val = getattr(item, "research15_Review", None)
                    
                    setattr(item, "research15_Review", self)
                    

class research15_Skill:

    def __init__(self, description: str, research15_Skill: "research15_Researcher" = None):
        self.description = description
        self.research15_Skill = research15_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research15_Skill(self):
        return self.__research15_Skill

    @research15_Skill.setter
    def research15_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Skill__research15_Skill", None)
        self.__research15_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Researcher6"):
                opp_val = getattr(old_value, "research15_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Researcher6"):
                opp_val = getattr(value, "research15_Researcher6", None)
                if opp_val is None:
                    setattr(value, "research15_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class research15_KnowledgeManager(Named):

    pass
class research15_Keyword(Named):

    def __init__(self, description: str, research15_Keyword: set["research15_Paper"] = None, research15_Keyword53: "research15_KnowledgeManager" = None, research15_Keyword56: "research15_PaperKeyword" = None):
        self.description = description
        self.research15_Keyword = research15_Keyword if research15_Keyword is not None else set()
        self.research15_Keyword53 = research15_Keyword53
        self.research15_Keyword56 = research15_Keyword56
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research15_Keyword(self):
        return self.__research15_Keyword

    @research15_Keyword.setter
    def research15_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Keyword__research15_Keyword", None)
        self.__research15_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research15_Paper50"):
                    opp_val = getattr(item, "research15_Paper50", None)
                    
                    if opp_val == self:
                        setattr(item, "research15_Paper50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research15_Paper50"):
                    opp_val = getattr(item, "research15_Paper50", None)
                    
                    setattr(item, "research15_Paper50", self)
                    

    @property
    def research15_Keyword53(self):
        return self.__research15_Keyword53

    @research15_Keyword53.setter
    def research15_Keyword53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Keyword__research15_Keyword53", None)
        self.__research15_Keyword53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_KnowledgeManager52"):
                opp_val = getattr(old_value, "research15_KnowledgeManager52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_KnowledgeManager52"):
                opp_val = getattr(value, "research15_KnowledgeManager52", None)
                if opp_val is None:
                    setattr(value, "research15_KnowledgeManager52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research15_Keyword56(self):
        return self.__research15_Keyword56

    @research15_Keyword56.setter
    def research15_Keyword56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Keyword__research15_Keyword56", None)
        self.__research15_Keyword56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_PaperKeyword55"):
                opp_val = getattr(old_value, "research15_PaperKeyword55", None)
                if opp_val == self:
                    setattr(old_value, "research15_PaperKeyword55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_PaperKeyword55"):
                opp_val = getattr(value, "research15_PaperKeyword55", None)
                setattr(value, "research15_PaperKeyword55", self)

class research15_ReviewNote(Named):

    def __init__(self, content: str, research15_ReviewNote: "research15_Paragraph" = None, research15_ReviewNote30: "research15_Review" = None):
        self.content = content
        self.research15_ReviewNote = research15_ReviewNote
        self.research15_ReviewNote30 = research15_ReviewNote30
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research15_ReviewNote(self):
        return self.__research15_ReviewNote

    @research15_ReviewNote.setter
    def research15_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_ReviewNote__research15_ReviewNote", None)
        self.__research15_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Paragraph20"):
                opp_val = getattr(old_value, "research15_Paragraph20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Paragraph20"):
                opp_val = getattr(value, "research15_Paragraph20", None)
                if opp_val is None:
                    setattr(value, "research15_Paragraph20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research15_ReviewNote30(self):
        return self.__research15_ReviewNote30

    @research15_ReviewNote30.setter
    def research15_ReviewNote30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_ReviewNote__research15_ReviewNote30", None)
        self.__research15_ReviewNote30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Review29"):
                opp_val = getattr(old_value, "research15_Review29", None)
                if opp_val == self:
                    setattr(old_value, "research15_Review29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Review29"):
                opp_val = getattr(value, "research15_Review29", None)
                setattr(value, "research15_Review29", self)

class research15_Paragraph(Counted, Named):

    def __init__(self, content: str, research15_Paragraph: "research15_Paper" = None, research15_Paragraph27: "research15_Write" = None, research15_Paragraph20: set["research15_ReviewNote"] = None):
        self.content = content
        self.research15_Paragraph = research15_Paragraph
        self.research15_Paragraph27 = research15_Paragraph27
        self.research15_Paragraph20 = research15_Paragraph20 if research15_Paragraph20 is not None else set()
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research15_Paragraph20(self):
        return self.__research15_Paragraph20

    @research15_Paragraph20.setter
    def research15_Paragraph20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Paragraph__research15_Paragraph20", None)
        self.__research15_Paragraph20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research15_ReviewNote"):
                    opp_val = getattr(item, "research15_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "research15_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research15_ReviewNote"):
                    opp_val = getattr(item, "research15_ReviewNote", None)
                    
                    setattr(item, "research15_ReviewNote", self)
                    

    @property
    def research15_Paragraph27(self):
        return self.__research15_Paragraph27

    @research15_Paragraph27.setter
    def research15_Paragraph27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Paragraph__research15_Paragraph27", None)
        self.__research15_Paragraph27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Write26"):
                opp_val = getattr(old_value, "research15_Write26", None)
                if opp_val == self:
                    setattr(old_value, "research15_Write26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Write26"):
                opp_val = getattr(value, "research15_Write26", None)
                setattr(value, "research15_Write26", self)

    @property
    def research15_Paragraph(self):
        return self.__research15_Paragraph

    @research15_Paragraph.setter
    def research15_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Paragraph__research15_Paragraph", None)
        self.__research15_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Paper"):
                opp_val = getattr(old_value, "research15_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Paper"):
                opp_val = getattr(value, "research15_Paper", None)
                if opp_val is None:
                    setattr(value, "research15_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research15_Position(Named):

    def __init__(self, description: str, research15_Position: "research15_Researcher" = None, research15_Position48: "research15_Position" = None, research15_Position46: "research15_Position" = None, research15_Position45: "research15_PublicationSystem" = None):
        self.description = description
        self.research15_Position = research15_Position
        self.research15_Position48 = research15_Position48
        self.research15_Position46 = research15_Position46
        self.research15_Position45 = research15_Position45
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research15_Position(self):
        return self.__research15_Position

    @research15_Position.setter
    def research15_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Position__research15_Position", None)
        self.__research15_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Researcher8"):
                opp_val = getattr(old_value, "research15_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "research15_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Researcher8"):
                opp_val = getattr(value, "research15_Researcher8", None)
                setattr(value, "research15_Researcher8", self)

    @property
    def research15_Position45(self):
        return self.__research15_Position45

    @research15_Position45.setter
    def research15_Position45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Position__research15_Position45", None)
        self.__research15_Position45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_PublicationSystem44"):
                opp_val = getattr(old_value, "research15_PublicationSystem44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_PublicationSystem44"):
                opp_val = getattr(value, "research15_PublicationSystem44", None)
                if opp_val is None:
                    setattr(value, "research15_PublicationSystem44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research15_Position48(self):
        return self.__research15_Position48

    @research15_Position48.setter
    def research15_Position48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Position__research15_Position48", None)
        self.__research15_Position48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Position46"):
                opp_val = getattr(old_value, "research15_Position46", None)
                if opp_val == self:
                    setattr(old_value, "research15_Position46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Position46"):
                opp_val = getattr(value, "research15_Position46", None)
                setattr(value, "research15_Position46", self)

    @property
    def research15_Position46(self):
        return self.__research15_Position46

    @research15_Position46.setter
    def research15_Position46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Position__research15_Position46", None)
        self.__research15_Position46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Position48"):
                opp_val = getattr(old_value, "research15_Position48", None)
                if opp_val == self:
                    setattr(old_value, "research15_Position48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Position48"):
                opp_val = getattr(value, "research15_Position48", None)
                setattr(value, "research15_Position48", self)

class research15_PublicationSystem(Named):

    pass
class research15_Paper(Named):

    pass
class research15_PublicationStructure(Named):

    pass
class research15_PublicationProcess(Named):

    def __init__(self, maxTime: int, minTime: int, research15_PublicationProcess: set["research15_Phase"] = None, research15_PublicationProcess22: "research15_Progress" = None, research15_PublicationProcess39: "research15_PublicationSystem" = None):
        self.maxTime = maxTime
        self.minTime = minTime
        self.research15_PublicationProcess = research15_PublicationProcess if research15_PublicationProcess is not None else set()
        self.research15_PublicationProcess22 = research15_PublicationProcess22
        self.research15_PublicationProcess39 = research15_PublicationProcess39
        
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
    def research15_PublicationProcess22(self):
        return self.__research15_PublicationProcess22

    @research15_PublicationProcess22.setter
    def research15_PublicationProcess22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_PublicationProcess__research15_PublicationProcess22", None)
        self.__research15_PublicationProcess22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_Progress"):
                opp_val = getattr(old_value, "research15_Progress", None)
                if opp_val == self:
                    setattr(old_value, "research15_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_Progress"):
                opp_val = getattr(value, "research15_Progress", None)
                setattr(value, "research15_Progress", self)

    @property
    def research15_PublicationProcess(self):
        return self.__research15_PublicationProcess

    @research15_PublicationProcess.setter
    def research15_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_PublicationProcess__research15_PublicationProcess", None)
        self.__research15_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research15_Phase"):
                    opp_val = getattr(item, "research15_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "research15_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research15_Phase"):
                    opp_val = getattr(item, "research15_Phase", None)
                    
                    setattr(item, "research15_Phase", self)
                    

    @property
    def research15_PublicationProcess39(self):
        return self.__research15_PublicationProcess39

    @research15_PublicationProcess39.setter
    def research15_PublicationProcess39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_PublicationProcess__research15_PublicationProcess39", None)
        self.__research15_PublicationProcess39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_PublicationSystem"):
                opp_val = getattr(old_value, "research15_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "research15_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_PublicationSystem"):
                opp_val = getattr(value, "research15_PublicationSystem", None)
                setattr(value, "research15_PublicationSystem", self)

class research15_Phase:

    def __init__(self, name: str, research15_Phase: "research15_PublicationProcess" = None):
        self.name = name
        self.research15_Phase = research15_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research15_Phase(self):
        return self.__research15_Phase

    @research15_Phase.setter
    def research15_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research15_Phase__research15_Phase", None)
        self.__research15_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research15_PublicationProcess"):
                opp_val = getattr(old_value, "research15_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research15_PublicationProcess"):
                opp_val = getattr(value, "research15_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "research15_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
