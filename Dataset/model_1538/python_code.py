from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class research2_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class research2_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class research2_Named(ABC):

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
class research2_Skill:

    def __init__(self, description: str, research2_Skill: "research2_Researcher" = None):
        self.description = description
        self.research2_Skill = research2_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research2_Skill(self):
        return self.__research2_Skill

    @research2_Skill.setter
    def research2_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Skill__research2_Skill", None)
        self.__research2_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Researcher6"):
                opp_val = getattr(old_value, "research2_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Researcher6"):
                opp_val = getattr(value, "research2_Researcher6", None)
                if opp_val is None:
                    setattr(value, "research2_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research2_Progress(Labelled):

    def __init__(self, percent: int, Progress: "research2_Paper" = None, research2_Progress: "research2_PublicationProcess" = None, progress: "research2_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.research2_Progress = research2_Progress
        self.progress = progress
        
    @property
    def percent(self) -> int:
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent

    @property
    def research2_Progress(self):
        return self.__research2_Progress

    @research2_Progress.setter
    def research2_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Progress__research2_Progress", None)
        self.__research2_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_PublicationProcess19"):
                opp_val = getattr(old_value, "research2_PublicationProcess19", None)
                if opp_val == self:
                    setattr(old_value, "research2_PublicationProcess19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_PublicationProcess19"):
                opp_val = getattr(value, "research2_PublicationProcess19", None)
                setattr(value, "research2_PublicationProcess19", self)

    @property
    def Progress(self):
        return self.__Progress

    @Progress.setter
    def Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Progress__Progress", None)
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
        old_value = getattr(self, f"_research2_Progress__progress", None)
        self.__progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Paper21"):
                opp_val = getattr(old_value, "Paper21", None)
                if opp_val == self:
                    setattr(old_value, "Paper21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Paper21"):
                opp_val = getattr(value, "Paper21", None)
                setattr(value, "Paper21", self)

class research2_Researcher:

    def __init__(self, name: str, forName: str, research2_Researcher: set["research2_Write"] = None, research2_Researcher3: set["research2_Review"] = None, Researcher: "research2_Paper" = None, authors: set["research2_Paper"] = None, research2_Researcher6: set["research2_Skill"] = None, research2_Researcher8: "research2_Position" = None, research2_Researcher29: "research2_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.research2_Researcher = research2_Researcher if research2_Researcher is not None else set()
        self.research2_Researcher3 = research2_Researcher3 if research2_Researcher3 is not None else set()
        self.Researcher = Researcher
        self.authors = authors if authors is not None else set()
        self.research2_Researcher6 = research2_Researcher6 if research2_Researcher6 is not None else set()
        self.research2_Researcher8 = research2_Researcher8
        self.research2_Researcher29 = research2_Researcher29
        
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
    def research2_Researcher6(self):
        return self.__research2_Researcher6

    @research2_Researcher6.setter
    def research2_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Researcher__research2_Researcher6", None)
        self.__research2_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research2_Skill"):
                    opp_val = getattr(item, "research2_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "research2_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research2_Skill"):
                    opp_val = getattr(item, "research2_Skill", None)
                    
                    setattr(item, "research2_Skill", self)
                    

    @property
    def research2_Researcher3(self):
        return self.__research2_Researcher3

    @research2_Researcher3.setter
    def research2_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Researcher__research2_Researcher3", None)
        self.__research2_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research2_Review"):
                    opp_val = getattr(item, "research2_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "research2_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research2_Review"):
                    opp_val = getattr(item, "research2_Review", None)
                    
                    setattr(item, "research2_Review", self)
                    

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Researcher__Researcher", None)
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
    def research2_Researcher8(self):
        return self.__research2_Researcher8

    @research2_Researcher8.setter
    def research2_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Researcher__research2_Researcher8", None)
        self.__research2_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Position"):
                opp_val = getattr(old_value, "research2_Position", None)
                if opp_val == self:
                    setattr(old_value, "research2_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Position"):
                opp_val = getattr(value, "research2_Position", None)
                setattr(value, "research2_Position", self)

    @property
    def research2_Researcher(self):
        return self.__research2_Researcher

    @research2_Researcher.setter
    def research2_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Researcher__research2_Researcher", None)
        self.__research2_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research2_Write"):
                    opp_val = getattr(item, "research2_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "research2_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research2_Write"):
                    opp_val = getattr(item, "research2_Write", None)
                    
                    setattr(item, "research2_Write", self)
                    

    @property
    def research2_Researcher29(self):
        return self.__research2_Researcher29

    @research2_Researcher29.setter
    def research2_Researcher29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Researcher__research2_Researcher29", None)
        self.__research2_Researcher29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_PublicationStructure"):
                opp_val = getattr(old_value, "research2_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_PublicationStructure"):
                opp_val = getattr(value, "research2_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "research2_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Researcher__authors", None)
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
                    

class research2_Phase:

    def __init__(self, name: str, research2_Phase: "research2_PublicationProcess" = None):
        self.name = name
        self.research2_Phase = research2_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research2_Phase(self):
        return self.__research2_Phase

    @research2_Phase.setter
    def research2_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Phase__research2_Phase", None)
        self.__research2_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_PublicationProcess"):
                opp_val = getattr(old_value, "research2_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_PublicationProcess"):
                opp_val = getattr(value, "research2_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "research2_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class research2_Paper(Named):

    pass
class research2_Position(Named):

    def __init__(self, description: str, research2_Position: "research2_Researcher" = None, research2_Position42: "research2_PublicationSystem" = None, research2_Position45: "research2_Position" = None, research2_Position43: "research2_Position" = None):
        self.description = description
        self.research2_Position = research2_Position
        self.research2_Position42 = research2_Position42
        self.research2_Position45 = research2_Position45
        self.research2_Position43 = research2_Position43
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research2_Position43(self):
        return self.__research2_Position43

    @research2_Position43.setter
    def research2_Position43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Position__research2_Position43", None)
        self.__research2_Position43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Position45"):
                opp_val = getattr(old_value, "research2_Position45", None)
                if opp_val == self:
                    setattr(old_value, "research2_Position45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Position45"):
                opp_val = getattr(value, "research2_Position45", None)
                setattr(value, "research2_Position45", self)

    @property
    def research2_Position42(self):
        return self.__research2_Position42

    @research2_Position42.setter
    def research2_Position42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Position__research2_Position42", None)
        self.__research2_Position42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_PublicationSystem41"):
                opp_val = getattr(old_value, "research2_PublicationSystem41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_PublicationSystem41"):
                opp_val = getattr(value, "research2_PublicationSystem41", None)
                if opp_val is None:
                    setattr(value, "research2_PublicationSystem41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research2_Position45(self):
        return self.__research2_Position45

    @research2_Position45.setter
    def research2_Position45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Position__research2_Position45", None)
        self.__research2_Position45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Position43"):
                opp_val = getattr(old_value, "research2_Position43", None)
                if opp_val == self:
                    setattr(old_value, "research2_Position43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Position43"):
                opp_val = getattr(value, "research2_Position43", None)
                setattr(value, "research2_Position43", self)

    @property
    def research2_Position(self):
        return self.__research2_Position

    @research2_Position.setter
    def research2_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Position__research2_Position", None)
        self.__research2_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Researcher8"):
                opp_val = getattr(old_value, "research2_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "research2_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Researcher8"):
                opp_val = getattr(value, "research2_Researcher8", None)
                setattr(value, "research2_Researcher8", self)

class research2_Paragraph(Counted, Named):

    def __init__(self, content: str, research2_Paragraph: "research2_Paper" = None, research2_Paragraph17: set["research2_ReviewNote"] = None, research2_Paragraph24: "research2_Write" = None):
        self.content = content
        self.research2_Paragraph = research2_Paragraph
        self.research2_Paragraph17 = research2_Paragraph17 if research2_Paragraph17 is not None else set()
        self.research2_Paragraph24 = research2_Paragraph24
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research2_Paragraph17(self):
        return self.__research2_Paragraph17

    @research2_Paragraph17.setter
    def research2_Paragraph17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Paragraph__research2_Paragraph17", None)
        self.__research2_Paragraph17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research2_ReviewNote"):
                    opp_val = getattr(item, "research2_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "research2_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research2_ReviewNote"):
                    opp_val = getattr(item, "research2_ReviewNote", None)
                    
                    setattr(item, "research2_ReviewNote", self)
                    

    @property
    def research2_Paragraph(self):
        return self.__research2_Paragraph

    @research2_Paragraph.setter
    def research2_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Paragraph__research2_Paragraph", None)
        self.__research2_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Paper"):
                opp_val = getattr(old_value, "research2_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Paper"):
                opp_val = getattr(value, "research2_Paper", None)
                if opp_val is None:
                    setattr(value, "research2_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research2_Paragraph24(self):
        return self.__research2_Paragraph24

    @research2_Paragraph24.setter
    def research2_Paragraph24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Paragraph__research2_Paragraph24", None)
        self.__research2_Paragraph24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Write23"):
                opp_val = getattr(old_value, "research2_Write23", None)
                if opp_val == self:
                    setattr(old_value, "research2_Write23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Write23"):
                opp_val = getattr(value, "research2_Write23", None)
                setattr(value, "research2_Write23", self)

class research2_PublicationSystem(Named):

    pass
class research2_Keyword(Named):

    def __init__(self, description: str, Keyword: "research2_Paper" = None, keywords: set["research2_Paper"] = None, research2_Keyword: "research2_KnowledgeManager" = None):
        self.description = description
        self.Keyword = Keyword
        self.keywords = keywords if keywords is not None else set()
        self.research2_Keyword = research2_Keyword
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Keyword__keywords", None)
        self.__keywords = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Paper47"):
                    opp_val = getattr(item, "Paper47", None)
                    
                    if opp_val == self:
                        setattr(item, "Paper47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Paper47"):
                    opp_val = getattr(item, "Paper47", None)
                    
                    setattr(item, "Paper47", self)
                    

    @property
    def research2_Keyword(self):
        return self.__research2_Keyword

    @research2_Keyword.setter
    def research2_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Keyword__research2_Keyword", None)
        self.__research2_Keyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_KnowledgeManager49"):
                opp_val = getattr(old_value, "research2_KnowledgeManager49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_KnowledgeManager49"):
                opp_val = getattr(value, "research2_KnowledgeManager49", None)
                if opp_val is None:
                    setattr(value, "research2_KnowledgeManager49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Keyword(self):
        return self.__Keyword

    @Keyword.setter
    def Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Keyword__Keyword", None)
        self.__Keyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kpapers"):
                opp_val = getattr(old_value, "kpapers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kpapers"):
                opp_val = getattr(value, "kpapers", None)
                if opp_val is None:
                    setattr(value, "kpapers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research2_PublicationStructure(Named):

    pass
class research2_ReviewNote(Named):

    def __init__(self, content: str, research2_ReviewNote: "research2_Paragraph" = None, research2_ReviewNote27: "research2_Review" = None):
        self.content = content
        self.research2_ReviewNote = research2_ReviewNote
        self.research2_ReviewNote27 = research2_ReviewNote27
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research2_ReviewNote(self):
        return self.__research2_ReviewNote

    @research2_ReviewNote.setter
    def research2_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_ReviewNote__research2_ReviewNote", None)
        self.__research2_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Paragraph17"):
                opp_val = getattr(old_value, "research2_Paragraph17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Paragraph17"):
                opp_val = getattr(value, "research2_Paragraph17", None)
                if opp_val is None:
                    setattr(value, "research2_Paragraph17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research2_ReviewNote27(self):
        return self.__research2_ReviewNote27

    @research2_ReviewNote27.setter
    def research2_ReviewNote27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_ReviewNote__research2_ReviewNote27", None)
        self.__research2_ReviewNote27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Review26"):
                opp_val = getattr(old_value, "research2_Review26", None)
                if opp_val == self:
                    setattr(old_value, "research2_Review26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Review26"):
                opp_val = getattr(value, "research2_Review26", None)
                setattr(value, "research2_Review26", self)

class research2_KnowledgeManager(Named):

    pass
class research2_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, research2_PublicationProcess: set["research2_Phase"] = None, research2_PublicationProcess19: "research2_Progress" = None, research2_PublicationProcess36: "research2_PublicationSystem" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.research2_PublicationProcess = research2_PublicationProcess if research2_PublicationProcess is not None else set()
        self.research2_PublicationProcess19 = research2_PublicationProcess19
        self.research2_PublicationProcess36 = research2_PublicationProcess36
        
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
    def research2_PublicationProcess(self):
        return self.__research2_PublicationProcess

    @research2_PublicationProcess.setter
    def research2_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_PublicationProcess__research2_PublicationProcess", None)
        self.__research2_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research2_Phase"):
                    opp_val = getattr(item, "research2_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "research2_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research2_Phase"):
                    opp_val = getattr(item, "research2_Phase", None)
                    
                    setattr(item, "research2_Phase", self)
                    

    @property
    def research2_PublicationProcess36(self):
        return self.__research2_PublicationProcess36

    @research2_PublicationProcess36.setter
    def research2_PublicationProcess36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_PublicationProcess__research2_PublicationProcess36", None)
        self.__research2_PublicationProcess36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_PublicationSystem"):
                opp_val = getattr(old_value, "research2_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "research2_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_PublicationSystem"):
                opp_val = getattr(value, "research2_PublicationSystem", None)
                setattr(value, "research2_PublicationSystem", self)

    @property
    def research2_PublicationProcess19(self):
        return self.__research2_PublicationProcess19

    @research2_PublicationProcess19.setter
    def research2_PublicationProcess19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_PublicationProcess__research2_PublicationProcess19", None)
        self.__research2_PublicationProcess19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Progress"):
                opp_val = getattr(old_value, "research2_Progress", None)
                if opp_val == self:
                    setattr(old_value, "research2_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Progress"):
                opp_val = getattr(value, "research2_Progress", None)
                setattr(value, "research2_Progress", self)

class research2_Review(Labelled):

    def __init__(self, date: date, research2_Review: "research2_Researcher" = None, research2_Review26: "research2_ReviewNote" = None):
        self.date = date
        self.research2_Review = research2_Review
        self.research2_Review26 = research2_Review26
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def research2_Review(self):
        return self.__research2_Review

    @research2_Review.setter
    def research2_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Review__research2_Review", None)
        self.__research2_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Researcher3"):
                opp_val = getattr(old_value, "research2_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Researcher3"):
                opp_val = getattr(value, "research2_Researcher3", None)
                if opp_val is None:
                    setattr(value, "research2_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research2_Review26(self):
        return self.__research2_Review26

    @research2_Review26.setter
    def research2_Review26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Review__research2_Review26", None)
        self.__research2_Review26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_ReviewNote27"):
                opp_val = getattr(old_value, "research2_ReviewNote27", None)
                if opp_val == self:
                    setattr(old_value, "research2_ReviewNote27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_ReviewNote27"):
                opp_val = getattr(value, "research2_ReviewNote27", None)
                setattr(value, "research2_ReviewNote27", self)

class research2_Write(Labelled):

    def __init__(self, timeSpent: int, research2_Write: "research2_Researcher" = None, research2_Write23: "research2_Paragraph" = None):
        self.timeSpent = timeSpent
        self.research2_Write = research2_Write
        self.research2_Write23 = research2_Write23
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def research2_Write(self):
        return self.__research2_Write

    @research2_Write.setter
    def research2_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Write__research2_Write", None)
        self.__research2_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Researcher"):
                opp_val = getattr(old_value, "research2_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Researcher"):
                opp_val = getattr(value, "research2_Researcher", None)
                if opp_val is None:
                    setattr(value, "research2_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research2_Write23(self):
        return self.__research2_Write23

    @research2_Write23.setter
    def research2_Write23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research2_Write__research2_Write23", None)
        self.__research2_Write23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research2_Paragraph24"):
                opp_val = getattr(old_value, "research2_Paragraph24", None)
                if opp_val == self:
                    setattr(old_value, "research2_Paragraph24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research2_Paragraph24"):
                opp_val = getattr(value, "research2_Paragraph24", None)
                setattr(value, "research2_Paragraph24", self)
