from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class publication101_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class publication101_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class publication101_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class publication101_PaperKeyword:

    def __init__(self, weight: int, publication101_PaperKeyword: "publication101_Paper" = None, publication101_PaperKeyword55: "publication101_Keyword" = None):
        self.weight = weight
        self.publication101_PaperKeyword = publication101_PaperKeyword
        self.publication101_PaperKeyword55 = publication101_PaperKeyword55
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def publication101_PaperKeyword55(self):
        return self.__publication101_PaperKeyword55

    @publication101_PaperKeyword55.setter
    def publication101_PaperKeyword55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_PaperKeyword__publication101_PaperKeyword55", None)
        self.__publication101_PaperKeyword55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Keyword56"):
                opp_val = getattr(old_value, "publication101_Keyword56", None)
                if opp_val == self:
                    setattr(old_value, "publication101_Keyword56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Keyword56"):
                opp_val = getattr(value, "publication101_Keyword56", None)
                setattr(value, "publication101_Keyword56", self)

    @property
    def publication101_PaperKeyword(self):
        return self.__publication101_PaperKeyword

    @publication101_PaperKeyword.setter
    def publication101_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_PaperKeyword__publication101_PaperKeyword", None)
        self.__publication101_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Paper15"):
                opp_val = getattr(old_value, "publication101_Paper15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Paper15"):
                opp_val = getattr(value, "publication101_Paper15", None)
                if opp_val is None:
                    setattr(value, "publication101_Paper15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Labelled:

    pass
class Counted:

    pass
class publication101_Review(Labelled):

    def __init__(self, date: date, publication101_Review: "publication101_Researcher" = None, publication101_Review29: "publication101_ReviewNote" = None):
        self.date = date
        self.publication101_Review = publication101_Review
        self.publication101_Review29 = publication101_Review29
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def publication101_Review29(self):
        return self.__publication101_Review29

    @publication101_Review29.setter
    def publication101_Review29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Review__publication101_Review29", None)
        self.__publication101_Review29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_ReviewNote30"):
                opp_val = getattr(old_value, "publication101_ReviewNote30", None)
                if opp_val == self:
                    setattr(old_value, "publication101_ReviewNote30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_ReviewNote30"):
                opp_val = getattr(value, "publication101_ReviewNote30", None)
                setattr(value, "publication101_ReviewNote30", self)

    @property
    def publication101_Review(self):
        return self.__publication101_Review

    @publication101_Review.setter
    def publication101_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Review__publication101_Review", None)
        self.__publication101_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Researcher3"):
                opp_val = getattr(old_value, "publication101_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Researcher3"):
                opp_val = getattr(value, "publication101_Researcher3", None)
                if opp_val is None:
                    setattr(value, "publication101_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication101_Write(Labelled):

    def __init__(self, timeSpent: int, publication101_Write: "publication101_Researcher" = None, publication101_Write26: "publication101_Paragraph" = None):
        self.timeSpent = timeSpent
        self.publication101_Write = publication101_Write
        self.publication101_Write26 = publication101_Write26
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def publication101_Write26(self):
        return self.__publication101_Write26

    @publication101_Write26.setter
    def publication101_Write26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Write__publication101_Write26", None)
        self.__publication101_Write26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Paragraph27"):
                opp_val = getattr(old_value, "publication101_Paragraph27", None)
                if opp_val == self:
                    setattr(old_value, "publication101_Paragraph27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Paragraph27"):
                opp_val = getattr(value, "publication101_Paragraph27", None)
                setattr(value, "publication101_Paragraph27", self)

    @property
    def publication101_Write(self):
        return self.__publication101_Write

    @publication101_Write.setter
    def publication101_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Write__publication101_Write", None)
        self.__publication101_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Researcher"):
                opp_val = getattr(old_value, "publication101_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Researcher"):
                opp_val = getattr(value, "publication101_Researcher", None)
                if opp_val is None:
                    setattr(value, "publication101_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication101_Progress(Labelled):

    def __init__(self, percent: int, Progress: "publication101_Paper" = None, publication101_Progress: "publication101_PublicationProcess" = None, progress: "publication101_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.publication101_Progress = publication101_Progress
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
        old_value = getattr(self, f"_publication101_Progress__Progress", None)
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
        old_value = getattr(self, f"_publication101_Progress__progress", None)
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
    def publication101_Progress(self):
        return self.__publication101_Progress

    @publication101_Progress.setter
    def publication101_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Progress__publication101_Progress", None)
        self.__publication101_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_PublicationProcess22"):
                opp_val = getattr(old_value, "publication101_PublicationProcess22", None)
                if opp_val == self:
                    setattr(old_value, "publication101_PublicationProcess22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_PublicationProcess22"):
                opp_val = getattr(value, "publication101_PublicationProcess22", None)
                setattr(value, "publication101_PublicationProcess22", self)

class publication101_Collaboration:

    def __init__(self, ratio: int, publication101_Collaboration: "publication101_Researcher" = None, publication101_Collaboration58: "publication101_Paper" = None):
        self.ratio = ratio
        self.publication101_Collaboration = publication101_Collaboration
        self.publication101_Collaboration58 = publication101_Collaboration58
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def publication101_Collaboration(self):
        return self.__publication101_Collaboration

    @publication101_Collaboration.setter
    def publication101_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Collaboration__publication101_Collaboration", None)
        self.__publication101_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Researcher10"):
                opp_val = getattr(old_value, "publication101_Researcher10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Researcher10"):
                opp_val = getattr(value, "publication101_Researcher10", None)
                if opp_val is None:
                    setattr(value, "publication101_Researcher10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication101_Collaboration58(self):
        return self.__publication101_Collaboration58

    @publication101_Collaboration58.setter
    def publication101_Collaboration58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Collaboration__publication101_Collaboration58", None)
        self.__publication101_Collaboration58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Paper59"):
                opp_val = getattr(old_value, "publication101_Paper59", None)
                if opp_val == self:
                    setattr(old_value, "publication101_Paper59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Paper59"):
                opp_val = getattr(value, "publication101_Paper59", None)
                setattr(value, "publication101_Paper59", self)

class publication101_Skill:

    def __init__(self, description: str, publication101_Skill: "publication101_Researcher" = None):
        self.description = description
        self.publication101_Skill = publication101_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def publication101_Skill(self):
        return self.__publication101_Skill

    @publication101_Skill.setter
    def publication101_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Skill__publication101_Skill", None)
        self.__publication101_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Researcher6"):
                opp_val = getattr(old_value, "publication101_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Researcher6"):
                opp_val = getattr(value, "publication101_Researcher6", None)
                if opp_val is None:
                    setattr(value, "publication101_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication101_Researcher:

    def __init__(self, name: str, forName: str, publication101_Researcher3: set["publication101_Review"] = None, authors: set["publication101_Paper"] = None, publication101_Researcher6: set["publication101_Skill"] = None, publication101_Researcher8: "publication101_Position" = None, publication101_Researcher10: set["publication101_Collaboration"] = None, publication101_Researcher: set["publication101_Write"] = None, Researcher: "publication101_Paper" = None, publication101_Researcher32: "publication101_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.publication101_Researcher3 = publication101_Researcher3 if publication101_Researcher3 is not None else set()
        self.authors = authors if authors is not None else set()
        self.publication101_Researcher6 = publication101_Researcher6 if publication101_Researcher6 is not None else set()
        self.publication101_Researcher8 = publication101_Researcher8
        self.publication101_Researcher10 = publication101_Researcher10 if publication101_Researcher10 is not None else set()
        self.publication101_Researcher = publication101_Researcher if publication101_Researcher is not None else set()
        self.Researcher = Researcher
        self.publication101_Researcher32 = publication101_Researcher32
        
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
        old_value = getattr(self, f"_publication101_Researcher__Researcher", None)
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
    def publication101_Researcher32(self):
        return self.__publication101_Researcher32

    @publication101_Researcher32.setter
    def publication101_Researcher32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Researcher__publication101_Researcher32", None)
        self.__publication101_Researcher32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_PublicationStructure"):
                opp_val = getattr(old_value, "publication101_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_PublicationStructure"):
                opp_val = getattr(value, "publication101_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "publication101_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication101_Researcher8(self):
        return self.__publication101_Researcher8

    @publication101_Researcher8.setter
    def publication101_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Researcher__publication101_Researcher8", None)
        self.__publication101_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Position"):
                opp_val = getattr(old_value, "publication101_Position", None)
                if opp_val == self:
                    setattr(old_value, "publication101_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Position"):
                opp_val = getattr(value, "publication101_Position", None)
                setattr(value, "publication101_Position", self)

    @property
    def publication101_Researcher6(self):
        return self.__publication101_Researcher6

    @publication101_Researcher6.setter
    def publication101_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Researcher__publication101_Researcher6", None)
        self.__publication101_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication101_Skill"):
                    opp_val = getattr(item, "publication101_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "publication101_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication101_Skill"):
                    opp_val = getattr(item, "publication101_Skill", None)
                    
                    setattr(item, "publication101_Skill", self)
                    

    @property
    def publication101_Researcher10(self):
        return self.__publication101_Researcher10

    @publication101_Researcher10.setter
    def publication101_Researcher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Researcher__publication101_Researcher10", None)
        self.__publication101_Researcher10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication101_Collaboration"):
                    opp_val = getattr(item, "publication101_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "publication101_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication101_Collaboration"):
                    opp_val = getattr(item, "publication101_Collaboration", None)
                    
                    setattr(item, "publication101_Collaboration", self)
                    

    @property
    def publication101_Researcher(self):
        return self.__publication101_Researcher

    @publication101_Researcher.setter
    def publication101_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Researcher__publication101_Researcher", None)
        self.__publication101_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication101_Write"):
                    opp_val = getattr(item, "publication101_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "publication101_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication101_Write"):
                    opp_val = getattr(item, "publication101_Write", None)
                    
                    setattr(item, "publication101_Write", self)
                    

    @property
    def publication101_Researcher3(self):
        return self.__publication101_Researcher3

    @publication101_Researcher3.setter
    def publication101_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Researcher__publication101_Researcher3", None)
        self.__publication101_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication101_Review"):
                    opp_val = getattr(item, "publication101_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "publication101_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication101_Review"):
                    opp_val = getattr(item, "publication101_Review", None)
                    
                    setattr(item, "publication101_Review", self)
                    

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Researcher__authors", None)
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
                    

class publication101_Phase:

    def __init__(self, name: str, publication101_Phase: "publication101_PublicationProcess" = None):
        self.name = name
        self.publication101_Phase = publication101_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def publication101_Phase(self):
        return self.__publication101_Phase

    @publication101_Phase.setter
    def publication101_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Phase__publication101_Phase", None)
        self.__publication101_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_PublicationProcess"):
                opp_val = getattr(old_value, "publication101_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_PublicationProcess"):
                opp_val = getattr(value, "publication101_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "publication101_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class publication101_ReviewNote(Named):

    def __init__(self, content: str, publication101_ReviewNote: "publication101_Paragraph" = None, publication101_ReviewNote30: "publication101_Review" = None):
        self.content = content
        self.publication101_ReviewNote = publication101_ReviewNote
        self.publication101_ReviewNote30 = publication101_ReviewNote30
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication101_ReviewNote30(self):
        return self.__publication101_ReviewNote30

    @publication101_ReviewNote30.setter
    def publication101_ReviewNote30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_ReviewNote__publication101_ReviewNote30", None)
        self.__publication101_ReviewNote30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Review29"):
                opp_val = getattr(old_value, "publication101_Review29", None)
                if opp_val == self:
                    setattr(old_value, "publication101_Review29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Review29"):
                opp_val = getattr(value, "publication101_Review29", None)
                setattr(value, "publication101_Review29", self)

    @property
    def publication101_ReviewNote(self):
        return self.__publication101_ReviewNote

    @publication101_ReviewNote.setter
    def publication101_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_ReviewNote__publication101_ReviewNote", None)
        self.__publication101_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Paragraph20"):
                opp_val = getattr(old_value, "publication101_Paragraph20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Paragraph20"):
                opp_val = getattr(value, "publication101_Paragraph20", None)
                if opp_val is None:
                    setattr(value, "publication101_Paragraph20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication101_PublicationStructure(Named):

    pass
class publication101_Paragraph(Named, Counted):

    def __init__(self, content: str, publication101_Paragraph: "publication101_Paper" = None, publication101_Paragraph20: set["publication101_ReviewNote"] = None, publication101_Paragraph27: "publication101_Write" = None):
        self.content = content
        self.publication101_Paragraph = publication101_Paragraph
        self.publication101_Paragraph20 = publication101_Paragraph20 if publication101_Paragraph20 is not None else set()
        self.publication101_Paragraph27 = publication101_Paragraph27
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication101_Paragraph27(self):
        return self.__publication101_Paragraph27

    @publication101_Paragraph27.setter
    def publication101_Paragraph27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Paragraph__publication101_Paragraph27", None)
        self.__publication101_Paragraph27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Write26"):
                opp_val = getattr(old_value, "publication101_Write26", None)
                if opp_val == self:
                    setattr(old_value, "publication101_Write26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Write26"):
                opp_val = getattr(value, "publication101_Write26", None)
                setattr(value, "publication101_Write26", self)

    @property
    def publication101_Paragraph20(self):
        return self.__publication101_Paragraph20

    @publication101_Paragraph20.setter
    def publication101_Paragraph20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Paragraph__publication101_Paragraph20", None)
        self.__publication101_Paragraph20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication101_ReviewNote"):
                    opp_val = getattr(item, "publication101_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "publication101_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication101_ReviewNote"):
                    opp_val = getattr(item, "publication101_ReviewNote", None)
                    
                    setattr(item, "publication101_ReviewNote", self)
                    

    @property
    def publication101_Paragraph(self):
        return self.__publication101_Paragraph

    @publication101_Paragraph.setter
    def publication101_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Paragraph__publication101_Paragraph", None)
        self.__publication101_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Paper"):
                opp_val = getattr(old_value, "publication101_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Paper"):
                opp_val = getattr(value, "publication101_Paper", None)
                if opp_val is None:
                    setattr(value, "publication101_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication101_Paper(Named):

    pass
class publication101_PublicationSystem(Named):

    pass
class publication101_Keyword(Named):

    def __init__(self, description: str, publication101_Keyword: set["publication101_Paper"] = None, publication101_Keyword56: "publication101_PaperKeyword" = None, publication101_Keyword53: "publication101_KnowledgeManager" = None):
        self.description = description
        self.publication101_Keyword = publication101_Keyword if publication101_Keyword is not None else set()
        self.publication101_Keyword56 = publication101_Keyword56
        self.publication101_Keyword53 = publication101_Keyword53
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def publication101_Keyword56(self):
        return self.__publication101_Keyword56

    @publication101_Keyword56.setter
    def publication101_Keyword56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Keyword__publication101_Keyword56", None)
        self.__publication101_Keyword56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_PaperKeyword55"):
                opp_val = getattr(old_value, "publication101_PaperKeyword55", None)
                if opp_val == self:
                    setattr(old_value, "publication101_PaperKeyword55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_PaperKeyword55"):
                opp_val = getattr(value, "publication101_PaperKeyword55", None)
                setattr(value, "publication101_PaperKeyword55", self)

    @property
    def publication101_Keyword(self):
        return self.__publication101_Keyword

    @publication101_Keyword.setter
    def publication101_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Keyword__publication101_Keyword", None)
        self.__publication101_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication101_Paper50"):
                    opp_val = getattr(item, "publication101_Paper50", None)
                    
                    if opp_val == self:
                        setattr(item, "publication101_Paper50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication101_Paper50"):
                    opp_val = getattr(item, "publication101_Paper50", None)
                    
                    setattr(item, "publication101_Paper50", self)
                    

    @property
    def publication101_Keyword53(self):
        return self.__publication101_Keyword53

    @publication101_Keyword53.setter
    def publication101_Keyword53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Keyword__publication101_Keyword53", None)
        self.__publication101_Keyword53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_KnowledgeManager52"):
                opp_val = getattr(old_value, "publication101_KnowledgeManager52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_KnowledgeManager52"):
                opp_val = getattr(value, "publication101_KnowledgeManager52", None)
                if opp_val is None:
                    setattr(value, "publication101_KnowledgeManager52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication101_KnowledgeManager(Named):

    pass
class publication101_Position(Named):

    def __init__(self, description: str, publication101_Position: "publication101_Researcher" = None, publication101_Position45: "publication101_PublicationSystem" = None, publication101_Position48: "publication101_Position" = None, publication101_Position46: "publication101_Position" = None):
        self.description = description
        self.publication101_Position = publication101_Position
        self.publication101_Position45 = publication101_Position45
        self.publication101_Position48 = publication101_Position48
        self.publication101_Position46 = publication101_Position46
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def publication101_Position48(self):
        return self.__publication101_Position48

    @publication101_Position48.setter
    def publication101_Position48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Position__publication101_Position48", None)
        self.__publication101_Position48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Position46"):
                opp_val = getattr(old_value, "publication101_Position46", None)
                if opp_val == self:
                    setattr(old_value, "publication101_Position46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Position46"):
                opp_val = getattr(value, "publication101_Position46", None)
                setattr(value, "publication101_Position46", self)

    @property
    def publication101_Position(self):
        return self.__publication101_Position

    @publication101_Position.setter
    def publication101_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Position__publication101_Position", None)
        self.__publication101_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Researcher8"):
                opp_val = getattr(old_value, "publication101_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "publication101_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Researcher8"):
                opp_val = getattr(value, "publication101_Researcher8", None)
                setattr(value, "publication101_Researcher8", self)

    @property
    def publication101_Position46(self):
        return self.__publication101_Position46

    @publication101_Position46.setter
    def publication101_Position46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Position__publication101_Position46", None)
        self.__publication101_Position46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Position48"):
                opp_val = getattr(old_value, "publication101_Position48", None)
                if opp_val == self:
                    setattr(old_value, "publication101_Position48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Position48"):
                opp_val = getattr(value, "publication101_Position48", None)
                setattr(value, "publication101_Position48", self)

    @property
    def publication101_Position45(self):
        return self.__publication101_Position45

    @publication101_Position45.setter
    def publication101_Position45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_Position__publication101_Position45", None)
        self.__publication101_Position45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_PublicationSystem44"):
                opp_val = getattr(old_value, "publication101_PublicationSystem44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_PublicationSystem44"):
                opp_val = getattr(value, "publication101_PublicationSystem44", None)
                if opp_val is None:
                    setattr(value, "publication101_PublicationSystem44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication101_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, publication101_PublicationProcess: set["publication101_Phase"] = None, publication101_PublicationProcess22: "publication101_Progress" = None, publication101_PublicationProcess39: "publication101_PublicationSystem" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.publication101_PublicationProcess = publication101_PublicationProcess if publication101_PublicationProcess is not None else set()
        self.publication101_PublicationProcess22 = publication101_PublicationProcess22
        self.publication101_PublicationProcess39 = publication101_PublicationProcess39
        
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
    def publication101_PublicationProcess22(self):
        return self.__publication101_PublicationProcess22

    @publication101_PublicationProcess22.setter
    def publication101_PublicationProcess22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_PublicationProcess__publication101_PublicationProcess22", None)
        self.__publication101_PublicationProcess22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_Progress"):
                opp_val = getattr(old_value, "publication101_Progress", None)
                if opp_val == self:
                    setattr(old_value, "publication101_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_Progress"):
                opp_val = getattr(value, "publication101_Progress", None)
                setattr(value, "publication101_Progress", self)

    @property
    def publication101_PublicationProcess39(self):
        return self.__publication101_PublicationProcess39

    @publication101_PublicationProcess39.setter
    def publication101_PublicationProcess39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_PublicationProcess__publication101_PublicationProcess39", None)
        self.__publication101_PublicationProcess39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication101_PublicationSystem"):
                opp_val = getattr(old_value, "publication101_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "publication101_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication101_PublicationSystem"):
                opp_val = getattr(value, "publication101_PublicationSystem", None)
                setattr(value, "publication101_PublicationSystem", self)

    @property
    def publication101_PublicationProcess(self):
        return self.__publication101_PublicationProcess

    @publication101_PublicationProcess.setter
    def publication101_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication101_PublicationProcess__publication101_PublicationProcess", None)
        self.__publication101_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication101_Phase"):
                    opp_val = getattr(item, "publication101_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "publication101_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication101_Phase"):
                    opp_val = getattr(item, "publication101_Phase", None)
                    
                    setattr(item, "publication101_Phase", self)
                    
