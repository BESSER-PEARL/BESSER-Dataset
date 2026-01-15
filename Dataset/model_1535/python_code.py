from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class research13_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class research13_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class research13_Named(ABC):

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
class research13_PaperKeyword:

    def __init__(self, weight: int, research13_PaperKeyword: "research13_Paper" = None, research13_PaperKeyword55: "research13_Keyword" = None):
        self.weight = weight
        self.research13_PaperKeyword = research13_PaperKeyword
        self.research13_PaperKeyword55 = research13_PaperKeyword55
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def research13_PaperKeyword(self):
        return self.__research13_PaperKeyword

    @research13_PaperKeyword.setter
    def research13_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_PaperKeyword__research13_PaperKeyword", None)
        self.__research13_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Paper15"):
                opp_val = getattr(old_value, "research13_Paper15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Paper15"):
                opp_val = getattr(value, "research13_Paper15", None)
                if opp_val is None:
                    setattr(value, "research13_Paper15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research13_PaperKeyword55(self):
        return self.__research13_PaperKeyword55

    @research13_PaperKeyword55.setter
    def research13_PaperKeyword55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_PaperKeyword__research13_PaperKeyword55", None)
        self.__research13_PaperKeyword55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Keyword56"):
                opp_val = getattr(old_value, "research13_Keyword56", None)
                if opp_val == self:
                    setattr(old_value, "research13_Keyword56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Keyword56"):
                opp_val = getattr(value, "research13_Keyword56", None)
                setattr(value, "research13_Keyword56", self)

class Labelled:

    pass
class research13_Collaboration:

    def __init__(self, ratio: int, research13_Collaboration: "research13_Researcher" = None, research13_Collaboration58: "research13_Paper" = None):
        self.ratio = ratio
        self.research13_Collaboration = research13_Collaboration
        self.research13_Collaboration58 = research13_Collaboration58
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def research13_Collaboration58(self):
        return self.__research13_Collaboration58

    @research13_Collaboration58.setter
    def research13_Collaboration58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Collaboration__research13_Collaboration58", None)
        self.__research13_Collaboration58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Paper59"):
                opp_val = getattr(old_value, "research13_Paper59", None)
                if opp_val == self:
                    setattr(old_value, "research13_Paper59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Paper59"):
                opp_val = getattr(value, "research13_Paper59", None)
                setattr(value, "research13_Paper59", self)

    @property
    def research13_Collaboration(self):
        return self.__research13_Collaboration

    @research13_Collaboration.setter
    def research13_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Collaboration__research13_Collaboration", None)
        self.__research13_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Researcher10"):
                opp_val = getattr(old_value, "research13_Researcher10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Researcher10"):
                opp_val = getattr(value, "research13_Researcher10", None)
                if opp_val is None:
                    setattr(value, "research13_Researcher10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research13_Skill:

    def __init__(self, description: str, research13_Skill: "research13_Researcher" = None):
        self.description = description
        self.research13_Skill = research13_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research13_Skill(self):
        return self.__research13_Skill

    @research13_Skill.setter
    def research13_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Skill__research13_Skill", None)
        self.__research13_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Researcher6"):
                opp_val = getattr(old_value, "research13_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Researcher6"):
                opp_val = getattr(value, "research13_Researcher6", None)
                if opp_val is None:
                    setattr(value, "research13_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research13_Review(Labelled):

    def __init__(self, date: date, research13_Review: "research13_Researcher" = None, research13_Review29: "research13_ReviewNote" = None):
        self.date = date
        self.research13_Review = research13_Review
        self.research13_Review29 = research13_Review29
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def research13_Review29(self):
        return self.__research13_Review29

    @research13_Review29.setter
    def research13_Review29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Review__research13_Review29", None)
        self.__research13_Review29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_ReviewNote30"):
                opp_val = getattr(old_value, "research13_ReviewNote30", None)
                if opp_val == self:
                    setattr(old_value, "research13_ReviewNote30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_ReviewNote30"):
                opp_val = getattr(value, "research13_ReviewNote30", None)
                setattr(value, "research13_ReviewNote30", self)

    @property
    def research13_Review(self):
        return self.__research13_Review

    @research13_Review.setter
    def research13_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Review__research13_Review", None)
        self.__research13_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Researcher3"):
                opp_val = getattr(old_value, "research13_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Researcher3"):
                opp_val = getattr(value, "research13_Researcher3", None)
                if opp_val is None:
                    setattr(value, "research13_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research13_Researcher:

    def __init__(self, name: str, forName: str, research13_Researcher: set["research13_Write"] = None, research13_Researcher3: set["research13_Review"] = None, authors: set["research13_Paper"] = None, research13_Researcher6: set["research13_Skill"] = None, research13_Researcher8: "research13_Position" = None, research13_Researcher10: set["research13_Collaboration"] = None, Researcher: "research13_Paper" = None, research13_Researcher32: "research13_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.research13_Researcher = research13_Researcher if research13_Researcher is not None else set()
        self.research13_Researcher3 = research13_Researcher3 if research13_Researcher3 is not None else set()
        self.authors = authors if authors is not None else set()
        self.research13_Researcher6 = research13_Researcher6 if research13_Researcher6 is not None else set()
        self.research13_Researcher8 = research13_Researcher8
        self.research13_Researcher10 = research13_Researcher10 if research13_Researcher10 is not None else set()
        self.Researcher = Researcher
        self.research13_Researcher32 = research13_Researcher32
        
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
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Researcher__authors", None)
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
    def research13_Researcher(self):
        return self.__research13_Researcher

    @research13_Researcher.setter
    def research13_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Researcher__research13_Researcher", None)
        self.__research13_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research13_Write"):
                    opp_val = getattr(item, "research13_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "research13_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research13_Write"):
                    opp_val = getattr(item, "research13_Write", None)
                    
                    setattr(item, "research13_Write", self)
                    

    @property
    def research13_Researcher8(self):
        return self.__research13_Researcher8

    @research13_Researcher8.setter
    def research13_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Researcher__research13_Researcher8", None)
        self.__research13_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Position"):
                opp_val = getattr(old_value, "research13_Position", None)
                if opp_val == self:
                    setattr(old_value, "research13_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Position"):
                opp_val = getattr(value, "research13_Position", None)
                setattr(value, "research13_Position", self)

    @property
    def research13_Researcher10(self):
        return self.__research13_Researcher10

    @research13_Researcher10.setter
    def research13_Researcher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Researcher__research13_Researcher10", None)
        self.__research13_Researcher10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research13_Collaboration"):
                    opp_val = getattr(item, "research13_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "research13_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research13_Collaboration"):
                    opp_val = getattr(item, "research13_Collaboration", None)
                    
                    setattr(item, "research13_Collaboration", self)
                    

    @property
    def research13_Researcher32(self):
        return self.__research13_Researcher32

    @research13_Researcher32.setter
    def research13_Researcher32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Researcher__research13_Researcher32", None)
        self.__research13_Researcher32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_PublicationStructure"):
                opp_val = getattr(old_value, "research13_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_PublicationStructure"):
                opp_val = getattr(value, "research13_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "research13_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Researcher__Researcher", None)
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
    def research13_Researcher3(self):
        return self.__research13_Researcher3

    @research13_Researcher3.setter
    def research13_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Researcher__research13_Researcher3", None)
        self.__research13_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research13_Review"):
                    opp_val = getattr(item, "research13_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "research13_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research13_Review"):
                    opp_val = getattr(item, "research13_Review", None)
                    
                    setattr(item, "research13_Review", self)
                    

    @property
    def research13_Researcher6(self):
        return self.__research13_Researcher6

    @research13_Researcher6.setter
    def research13_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Researcher__research13_Researcher6", None)
        self.__research13_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research13_Skill"):
                    opp_val = getattr(item, "research13_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "research13_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research13_Skill"):
                    opp_val = getattr(item, "research13_Skill", None)
                    
                    setattr(item, "research13_Skill", self)
                    

class research13_Write(Labelled):

    def __init__(self, timeSpent: int, research13_Write: "research13_Researcher" = None, research13_Write26: "research13_Paragraph" = None):
        self.timeSpent = timeSpent
        self.research13_Write = research13_Write
        self.research13_Write26 = research13_Write26
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def research13_Write26(self):
        return self.__research13_Write26

    @research13_Write26.setter
    def research13_Write26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Write__research13_Write26", None)
        self.__research13_Write26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Paragraph27"):
                opp_val = getattr(old_value, "research13_Paragraph27", None)
                if opp_val == self:
                    setattr(old_value, "research13_Paragraph27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Paragraph27"):
                opp_val = getattr(value, "research13_Paragraph27", None)
                setattr(value, "research13_Paragraph27", self)

    @property
    def research13_Write(self):
        return self.__research13_Write

    @research13_Write.setter
    def research13_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Write__research13_Write", None)
        self.__research13_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Researcher"):
                opp_val = getattr(old_value, "research13_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Researcher"):
                opp_val = getattr(value, "research13_Researcher", None)
                if opp_val is None:
                    setattr(value, "research13_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research13_Progress(Labelled):

    def __init__(self, percent: int, Progress: "research13_Paper" = None, research13_Progress: "research13_PublicationProcess" = None, progress: "research13_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.research13_Progress = research13_Progress
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
        old_value = getattr(self, f"_research13_Progress__progress", None)
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
    def research13_Progress(self):
        return self.__research13_Progress

    @research13_Progress.setter
    def research13_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Progress__research13_Progress", None)
        self.__research13_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_PublicationProcess22"):
                opp_val = getattr(old_value, "research13_PublicationProcess22", None)
                if opp_val == self:
                    setattr(old_value, "research13_PublicationProcess22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_PublicationProcess22"):
                opp_val = getattr(value, "research13_PublicationProcess22", None)
                setattr(value, "research13_PublicationProcess22", self)

    @property
    def Progress(self):
        return self.__Progress

    @Progress.setter
    def Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Progress__Progress", None)
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

class research13_Phase:

    def __init__(self, name: str, research13_Phase: "research13_PublicationProcess" = None):
        self.name = name
        self.research13_Phase = research13_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research13_Phase(self):
        return self.__research13_Phase

    @research13_Phase.setter
    def research13_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Phase__research13_Phase", None)
        self.__research13_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_PublicationProcess"):
                opp_val = getattr(old_value, "research13_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_PublicationProcess"):
                opp_val = getattr(value, "research13_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "research13_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class research13_PublicationStructure(Named):

    pass
class research13_Paragraph(Named, Counted):

    def __init__(self, content: str, research13_Paragraph: "research13_Paper" = None, research13_Paragraph20: set["research13_ReviewNote"] = None, research13_Paragraph27: "research13_Write" = None):
        self.content = content
        self.research13_Paragraph = research13_Paragraph
        self.research13_Paragraph20 = research13_Paragraph20 if research13_Paragraph20 is not None else set()
        self.research13_Paragraph27 = research13_Paragraph27
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research13_Paragraph(self):
        return self.__research13_Paragraph

    @research13_Paragraph.setter
    def research13_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Paragraph__research13_Paragraph", None)
        self.__research13_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Paper"):
                opp_val = getattr(old_value, "research13_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Paper"):
                opp_val = getattr(value, "research13_Paper", None)
                if opp_val is None:
                    setattr(value, "research13_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research13_Paragraph20(self):
        return self.__research13_Paragraph20

    @research13_Paragraph20.setter
    def research13_Paragraph20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Paragraph__research13_Paragraph20", None)
        self.__research13_Paragraph20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research13_ReviewNote"):
                    opp_val = getattr(item, "research13_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "research13_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research13_ReviewNote"):
                    opp_val = getattr(item, "research13_ReviewNote", None)
                    
                    setattr(item, "research13_ReviewNote", self)
                    

    @property
    def research13_Paragraph27(self):
        return self.__research13_Paragraph27

    @research13_Paragraph27.setter
    def research13_Paragraph27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Paragraph__research13_Paragraph27", None)
        self.__research13_Paragraph27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Write26"):
                opp_val = getattr(old_value, "research13_Write26", None)
                if opp_val == self:
                    setattr(old_value, "research13_Write26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Write26"):
                opp_val = getattr(value, "research13_Write26", None)
                setattr(value, "research13_Write26", self)

class research13_PublicationSystem(Named):

    pass
class research13_ReviewNote(Named):

    def __init__(self, content: str, research13_ReviewNote: "research13_Paragraph" = None, research13_ReviewNote30: "research13_Review" = None):
        self.content = content
        self.research13_ReviewNote = research13_ReviewNote
        self.research13_ReviewNote30 = research13_ReviewNote30
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research13_ReviewNote(self):
        return self.__research13_ReviewNote

    @research13_ReviewNote.setter
    def research13_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_ReviewNote__research13_ReviewNote", None)
        self.__research13_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Paragraph20"):
                opp_val = getattr(old_value, "research13_Paragraph20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Paragraph20"):
                opp_val = getattr(value, "research13_Paragraph20", None)
                if opp_val is None:
                    setattr(value, "research13_Paragraph20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research13_ReviewNote30(self):
        return self.__research13_ReviewNote30

    @research13_ReviewNote30.setter
    def research13_ReviewNote30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_ReviewNote__research13_ReviewNote30", None)
        self.__research13_ReviewNote30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Review29"):
                opp_val = getattr(old_value, "research13_Review29", None)
                if opp_val == self:
                    setattr(old_value, "research13_Review29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Review29"):
                opp_val = getattr(value, "research13_Review29", None)
                setattr(value, "research13_Review29", self)

class research13_KnowledgeManager(Named):

    pass
class research13_Position(Named):

    def __init__(self, description: str, research13_Position: "research13_Researcher" = None, research13_Position45: "research13_PublicationSystem" = None, research13_Position48: "research13_Position" = None, research13_Position46: "research13_Position" = None):
        self.description = description
        self.research13_Position = research13_Position
        self.research13_Position45 = research13_Position45
        self.research13_Position48 = research13_Position48
        self.research13_Position46 = research13_Position46
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research13_Position(self):
        return self.__research13_Position

    @research13_Position.setter
    def research13_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Position__research13_Position", None)
        self.__research13_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Researcher8"):
                opp_val = getattr(old_value, "research13_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "research13_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Researcher8"):
                opp_val = getattr(value, "research13_Researcher8", None)
                setattr(value, "research13_Researcher8", self)

    @property
    def research13_Position45(self):
        return self.__research13_Position45

    @research13_Position45.setter
    def research13_Position45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Position__research13_Position45", None)
        self.__research13_Position45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_PublicationSystem44"):
                opp_val = getattr(old_value, "research13_PublicationSystem44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_PublicationSystem44"):
                opp_val = getattr(value, "research13_PublicationSystem44", None)
                if opp_val is None:
                    setattr(value, "research13_PublicationSystem44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research13_Position48(self):
        return self.__research13_Position48

    @research13_Position48.setter
    def research13_Position48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Position__research13_Position48", None)
        self.__research13_Position48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Position46"):
                opp_val = getattr(old_value, "research13_Position46", None)
                if opp_val == self:
                    setattr(old_value, "research13_Position46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Position46"):
                opp_val = getattr(value, "research13_Position46", None)
                setattr(value, "research13_Position46", self)

    @property
    def research13_Position46(self):
        return self.__research13_Position46

    @research13_Position46.setter
    def research13_Position46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Position__research13_Position46", None)
        self.__research13_Position46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Position48"):
                opp_val = getattr(old_value, "research13_Position48", None)
                if opp_val == self:
                    setattr(old_value, "research13_Position48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Position48"):
                opp_val = getattr(value, "research13_Position48", None)
                setattr(value, "research13_Position48", self)

class research13_Paper(Named):

    pass
class research13_Keyword(Named):

    def __init__(self, description: str, research13_Keyword: set["research13_Paper"] = None, research13_Keyword53: "research13_KnowledgeManager" = None, research13_Keyword56: "research13_PaperKeyword" = None):
        self.description = description
        self.research13_Keyword = research13_Keyword if research13_Keyword is not None else set()
        self.research13_Keyword53 = research13_Keyword53
        self.research13_Keyword56 = research13_Keyword56
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research13_Keyword53(self):
        return self.__research13_Keyword53

    @research13_Keyword53.setter
    def research13_Keyword53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Keyword__research13_Keyword53", None)
        self.__research13_Keyword53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_KnowledgeManager52"):
                opp_val = getattr(old_value, "research13_KnowledgeManager52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_KnowledgeManager52"):
                opp_val = getattr(value, "research13_KnowledgeManager52", None)
                if opp_val is None:
                    setattr(value, "research13_KnowledgeManager52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research13_Keyword(self):
        return self.__research13_Keyword

    @research13_Keyword.setter
    def research13_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Keyword__research13_Keyword", None)
        self.__research13_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research13_Paper50"):
                    opp_val = getattr(item, "research13_Paper50", None)
                    
                    if opp_val == self:
                        setattr(item, "research13_Paper50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research13_Paper50"):
                    opp_val = getattr(item, "research13_Paper50", None)
                    
                    setattr(item, "research13_Paper50", self)
                    

    @property
    def research13_Keyword56(self):
        return self.__research13_Keyword56

    @research13_Keyword56.setter
    def research13_Keyword56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_Keyword__research13_Keyword56", None)
        self.__research13_Keyword56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_PaperKeyword55"):
                opp_val = getattr(old_value, "research13_PaperKeyword55", None)
                if opp_val == self:
                    setattr(old_value, "research13_PaperKeyword55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_PaperKeyword55"):
                opp_val = getattr(value, "research13_PaperKeyword55", None)
                setattr(value, "research13_PaperKeyword55", self)

class research13_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, research13_PublicationProcess: set["research13_Phase"] = None, research13_PublicationProcess22: "research13_Progress" = None, research13_PublicationProcess39: "research13_PublicationSystem" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.research13_PublicationProcess = research13_PublicationProcess if research13_PublicationProcess is not None else set()
        self.research13_PublicationProcess22 = research13_PublicationProcess22
        self.research13_PublicationProcess39 = research13_PublicationProcess39
        
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
    def research13_PublicationProcess(self):
        return self.__research13_PublicationProcess

    @research13_PublicationProcess.setter
    def research13_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_PublicationProcess__research13_PublicationProcess", None)
        self.__research13_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research13_Phase"):
                    opp_val = getattr(item, "research13_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "research13_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research13_Phase"):
                    opp_val = getattr(item, "research13_Phase", None)
                    
                    setattr(item, "research13_Phase", self)
                    

    @property
    def research13_PublicationProcess39(self):
        return self.__research13_PublicationProcess39

    @research13_PublicationProcess39.setter
    def research13_PublicationProcess39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_PublicationProcess__research13_PublicationProcess39", None)
        self.__research13_PublicationProcess39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_PublicationSystem"):
                opp_val = getattr(old_value, "research13_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "research13_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_PublicationSystem"):
                opp_val = getattr(value, "research13_PublicationSystem", None)
                setattr(value, "research13_PublicationSystem", self)

    @property
    def research13_PublicationProcess22(self):
        return self.__research13_PublicationProcess22

    @research13_PublicationProcess22.setter
    def research13_PublicationProcess22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research13_PublicationProcess__research13_PublicationProcess22", None)
        self.__research13_PublicationProcess22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research13_Progress"):
                opp_val = getattr(old_value, "research13_Progress", None)
                if opp_val == self:
                    setattr(old_value, "research13_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research13_Progress"):
                opp_val = getattr(value, "research13_Progress", None)
                setattr(value, "research13_Progress", self)
