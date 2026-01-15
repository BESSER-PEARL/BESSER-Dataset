from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Role(Enum):
    Autheur = "Autheur"
    Correcteur = "Correcteur"
    Validateur = "Validateur"
    Revieweur = "Revieweur"


############################################
# Definition of Classes
############################################

class tp6_Keyword:

    def __init__(self, key: str, description: str, tp6_Keyword: set["tp6_Paper"] = None, tp6_Keyword33: "tp6_PaperKeywords" = None, tp6_Keyword36: "tp6_KnowledgeManager" = None):
        self.key = key
        self.description = description
        self.tp6_Keyword = tp6_Keyword if tp6_Keyword is not None else set()
        self.tp6_Keyword33 = tp6_Keyword33
        self.tp6_Keyword36 = tp6_Keyword36
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def tp6_Keyword36(self):
        return self.__tp6_Keyword36

    @tp6_Keyword36.setter
    def tp6_Keyword36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Keyword__tp6_Keyword36", None)
        self.__tp6_Keyword36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_KnowledgeManager35"):
                opp_val = getattr(old_value, "tp6_KnowledgeManager35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_KnowledgeManager35"):
                opp_val = getattr(value, "tp6_KnowledgeManager35", None)
                if opp_val is None:
                    setattr(value, "tp6_KnowledgeManager35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp6_Keyword33(self):
        return self.__tp6_Keyword33

    @tp6_Keyword33.setter
    def tp6_Keyword33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Keyword__tp6_Keyword33", None)
        self.__tp6_Keyword33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_PaperKeywords32"):
                opp_val = getattr(old_value, "tp6_PaperKeywords32", None)
                if opp_val == self:
                    setattr(old_value, "tp6_PaperKeywords32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_PaperKeywords32"):
                opp_val = getattr(value, "tp6_PaperKeywords32", None)
                setattr(value, "tp6_PaperKeywords32", self)

    @property
    def tp6_Keyword(self):
        return self.__tp6_Keyword

    @tp6_Keyword.setter
    def tp6_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Keyword__tp6_Keyword", None)
        self.__tp6_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp6_Paper30"):
                    opp_val = getattr(item, "tp6_Paper30", None)
                    
                    if opp_val == self:
                        setattr(item, "tp6_Paper30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp6_Paper30"):
                    opp_val = getattr(item, "tp6_Paper30", None)
                    
                    setattr(item, "tp6_Paper30", self)
                    

class tp6_PublicationStructure:

    pass
class tp6_PaperKeywords:

    def __init__(self, weight: int, tp6_PaperKeywords: "tp6_Paper" = None, tp6_PaperKeywords32: "tp6_Keyword" = None):
        self.weight = weight
        self.tp6_PaperKeywords = tp6_PaperKeywords
        self.tp6_PaperKeywords32 = tp6_PaperKeywords32
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def tp6_PaperKeywords(self):
        return self.__tp6_PaperKeywords

    @tp6_PaperKeywords.setter
    def tp6_PaperKeywords(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_PaperKeywords__tp6_PaperKeywords", None)
        self.__tp6_PaperKeywords = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Paper12"):
                opp_val = getattr(old_value, "tp6_Paper12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Paper12"):
                opp_val = getattr(value, "tp6_Paper12", None)
                if opp_val is None:
                    setattr(value, "tp6_Paper12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp6_PaperKeywords32(self):
        return self.__tp6_PaperKeywords32

    @tp6_PaperKeywords32.setter
    def tp6_PaperKeywords32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_PaperKeywords__tp6_PaperKeywords32", None)
        self.__tp6_PaperKeywords32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Keyword33"):
                opp_val = getattr(old_value, "tp6_Keyword33", None)
                if opp_val == self:
                    setattr(old_value, "tp6_Keyword33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Keyword33"):
                opp_val = getattr(value, "tp6_Keyword33", None)
                setattr(value, "tp6_Keyword33", self)

class tp6_KnowledgeManager:

    def __init__(self, name: str, tp6_KnowledgeManager: "tp6_PublicationStructure" = None, tp6_KnowledgeManager35: set["tp6_Keyword"] = None):
        self.name = name
        self.tp6_KnowledgeManager = tp6_KnowledgeManager
        self.tp6_KnowledgeManager35 = tp6_KnowledgeManager35 if tp6_KnowledgeManager35 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tp6_KnowledgeManager35(self):
        return self.__tp6_KnowledgeManager35

    @tp6_KnowledgeManager35.setter
    def tp6_KnowledgeManager35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_KnowledgeManager__tp6_KnowledgeManager35", None)
        self.__tp6_KnowledgeManager35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp6_Keyword36"):
                    opp_val = getattr(item, "tp6_Keyword36", None)
                    
                    if opp_val == self:
                        setattr(item, "tp6_Keyword36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp6_Keyword36"):
                    opp_val = getattr(item, "tp6_Keyword36", None)
                    
                    setattr(item, "tp6_Keyword36", self)
                    

    @property
    def tp6_KnowledgeManager(self):
        return self.__tp6_KnowledgeManager

    @tp6_KnowledgeManager.setter
    def tp6_KnowledgeManager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_KnowledgeManager__tp6_KnowledgeManager", None)
        self.__tp6_KnowledgeManager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_PublicationStructure22"):
                opp_val = getattr(old_value, "tp6_PublicationStructure22", None)
                if opp_val == self:
                    setattr(old_value, "tp6_PublicationStructure22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_PublicationStructure22"):
                opp_val = getattr(value, "tp6_PublicationStructure22", None)
                setattr(value, "tp6_PublicationStructure22", self)

class tp6_Collaboration:

    def __init__(self, ratio: int, role: str, tp6_Collaboration: "tp6_Researcher" = None, tp6_Collaboration27: "tp6_Paper" = None):
        self.ratio = ratio
        self.role = role
        self.tp6_Collaboration = tp6_Collaboration
        self.tp6_Collaboration27 = tp6_Collaboration27
        
    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def tp6_Collaboration27(self):
        return self.__tp6_Collaboration27

    @tp6_Collaboration27.setter
    def tp6_Collaboration27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Collaboration__tp6_Collaboration27", None)
        self.__tp6_Collaboration27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Paper28"):
                opp_val = getattr(old_value, "tp6_Paper28", None)
                if opp_val == self:
                    setattr(old_value, "tp6_Paper28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Paper28"):
                opp_val = getattr(value, "tp6_Paper28", None)
                setattr(value, "tp6_Paper28", self)

    @property
    def tp6_Collaboration(self):
        return self.__tp6_Collaboration

    @tp6_Collaboration.setter
    def tp6_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Collaboration__tp6_Collaboration", None)
        self.__tp6_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Researcher5"):
                opp_val = getattr(old_value, "tp6_Researcher5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Researcher5"):
                opp_val = getattr(value, "tp6_Researcher5", None)
                if opp_val is None:
                    setattr(value, "tp6_Researcher5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tp6_Position:

    def __init__(self, name: str, description: str, tp6_Position: "tp6_Researcher" = None, tp6_Position20: "tp6_PublicationStructure" = None, tp6_Position25: "tp6_Position" = None, tp6_Position23: "tp6_Position" = None):
        self.name = name
        self.description = description
        self.tp6_Position = tp6_Position
        self.tp6_Position20 = tp6_Position20
        self.tp6_Position25 = tp6_Position25
        self.tp6_Position23 = tp6_Position23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def tp6_Position20(self):
        return self.__tp6_Position20

    @tp6_Position20.setter
    def tp6_Position20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Position__tp6_Position20", None)
        self.__tp6_Position20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_PublicationStructure19"):
                opp_val = getattr(old_value, "tp6_PublicationStructure19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_PublicationStructure19"):
                opp_val = getattr(value, "tp6_PublicationStructure19", None)
                if opp_val is None:
                    setattr(value, "tp6_PublicationStructure19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp6_Position25(self):
        return self.__tp6_Position25

    @tp6_Position25.setter
    def tp6_Position25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Position__tp6_Position25", None)
        self.__tp6_Position25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Position23"):
                opp_val = getattr(old_value, "tp6_Position23", None)
                if opp_val == self:
                    setattr(old_value, "tp6_Position23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Position23"):
                opp_val = getattr(value, "tp6_Position23", None)
                setattr(value, "tp6_Position23", self)

    @property
    def tp6_Position(self):
        return self.__tp6_Position

    @tp6_Position.setter
    def tp6_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Position__tp6_Position", None)
        self.__tp6_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Researcher3"):
                opp_val = getattr(old_value, "tp6_Researcher3", None)
                if opp_val == self:
                    setattr(old_value, "tp6_Researcher3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Researcher3"):
                opp_val = getattr(value, "tp6_Researcher3", None)
                setattr(value, "tp6_Researcher3", self)

    @property
    def tp6_Position23(self):
        return self.__tp6_Position23

    @tp6_Position23.setter
    def tp6_Position23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Position__tp6_Position23", None)
        self.__tp6_Position23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Position25"):
                opp_val = getattr(old_value, "tp6_Position25", None)
                if opp_val == self:
                    setattr(old_value, "tp6_Position25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Position25"):
                opp_val = getattr(value, "tp6_Position25", None)
                setattr(value, "tp6_Position25", self)

class tp6_Skill:

    def __init__(self, description: str, tp6_Skill: "tp6_Researcher" = None):
        self.description = description
        self.tp6_Skill = tp6_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def tp6_Skill(self):
        return self.__tp6_Skill

    @tp6_Skill.setter
    def tp6_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Skill__tp6_Skill", None)
        self.__tp6_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Researcher"):
                opp_val = getattr(old_value, "tp6_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Researcher"):
                opp_val = getattr(value, "tp6_Researcher", None)
                if opp_val is None:
                    setattr(value, "tp6_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tp6_Paper:

    def __init__(self, name: str, tp6_Paper: set["tp6_Paragraph"] = None, res_papers: set["tp6_Researcher"] = None, tp6_Paper10: "tp6_Paper" = None, tp6_Paper8: "tp6_Paper" = None, Paper: "tp6_Researcher" = None, tp6_Paper17: "tp6_PublicationStructure" = None, tp6_Paper12: set["tp6_PaperKeywords"] = None, tp6_Paper30: "tp6_Keyword" = None, tp6_Paper28: "tp6_Collaboration" = None):
        self.name = name
        self.tp6_Paper = tp6_Paper if tp6_Paper is not None else set()
        self.res_papers = res_papers if res_papers is not None else set()
        self.tp6_Paper10 = tp6_Paper10
        self.tp6_Paper8 = tp6_Paper8
        self.Paper = Paper
        self.tp6_Paper17 = tp6_Paper17
        self.tp6_Paper12 = tp6_Paper12 if tp6_Paper12 is not None else set()
        self.tp6_Paper30 = tp6_Paper30
        self.tp6_Paper28 = tp6_Paper28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tp6_Paper28(self):
        return self.__tp6_Paper28

    @tp6_Paper28.setter
    def tp6_Paper28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Paper__tp6_Paper28", None)
        self.__tp6_Paper28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Collaboration27"):
                opp_val = getattr(old_value, "tp6_Collaboration27", None)
                if opp_val == self:
                    setattr(old_value, "tp6_Collaboration27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Collaboration27"):
                opp_val = getattr(value, "tp6_Collaboration27", None)
                setattr(value, "tp6_Collaboration27", self)

    @property
    def res_papers(self):
        return self.__res_papers

    @res_papers.setter
    def res_papers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Paper__res_papers", None)
        self.__res_papers = value if value is not None else set()
        
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
    def tp6_Paper30(self):
        return self.__tp6_Paper30

    @tp6_Paper30.setter
    def tp6_Paper30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Paper__tp6_Paper30", None)
        self.__tp6_Paper30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Keyword"):
                opp_val = getattr(old_value, "tp6_Keyword", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Keyword"):
                opp_val = getattr(value, "tp6_Keyword", None)
                if opp_val is None:
                    setattr(value, "tp6_Keyword", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp6_Paper17(self):
        return self.__tp6_Paper17

    @tp6_Paper17.setter
    def tp6_Paper17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Paper__tp6_Paper17", None)
        self.__tp6_Paper17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_PublicationStructure16"):
                opp_val = getattr(old_value, "tp6_PublicationStructure16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_PublicationStructure16"):
                opp_val = getattr(value, "tp6_PublicationStructure16", None)
                if opp_val is None:
                    setattr(value, "tp6_PublicationStructure16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp6_Paper12(self):
        return self.__tp6_Paper12

    @tp6_Paper12.setter
    def tp6_Paper12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Paper__tp6_Paper12", None)
        self.__tp6_Paper12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp6_PaperKeywords"):
                    opp_val = getattr(item, "tp6_PaperKeywords", None)
                    
                    if opp_val == self:
                        setattr(item, "tp6_PaperKeywords", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp6_PaperKeywords"):
                    opp_val = getattr(item, "tp6_PaperKeywords", None)
                    
                    setattr(item, "tp6_PaperKeywords", self)
                    

    @property
    def Paper(self):
        return self.__Paper

    @Paper.setter
    def Paper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Paper__Paper", None)
        self.__Paper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authors"):
                opp_val = getattr(old_value, "authors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authors"):
                opp_val = getattr(value, "authors", None)
                if opp_val is None:
                    setattr(value, "authors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp6_Paper8(self):
        return self.__tp6_Paper8

    @tp6_Paper8.setter
    def tp6_Paper8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Paper__tp6_Paper8", None)
        self.__tp6_Paper8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Paper10"):
                opp_val = getattr(old_value, "tp6_Paper10", None)
                if opp_val == self:
                    setattr(old_value, "tp6_Paper10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Paper10"):
                opp_val = getattr(value, "tp6_Paper10", None)
                setattr(value, "tp6_Paper10", self)

    @property
    def tp6_Paper(self):
        return self.__tp6_Paper

    @tp6_Paper.setter
    def tp6_Paper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Paper__tp6_Paper", None)
        self.__tp6_Paper = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp6_Paragraph"):
                    opp_val = getattr(item, "tp6_Paragraph", None)
                    
                    if opp_val == self:
                        setattr(item, "tp6_Paragraph", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp6_Paragraph"):
                    opp_val = getattr(item, "tp6_Paragraph", None)
                    
                    setattr(item, "tp6_Paragraph", self)
                    

    @property
    def tp6_Paper10(self):
        return self.__tp6_Paper10

    @tp6_Paper10.setter
    def tp6_Paper10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Paper__tp6_Paper10", None)
        self.__tp6_Paper10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Paper8"):
                opp_val = getattr(old_value, "tp6_Paper8", None)
                if opp_val == self:
                    setattr(old_value, "tp6_Paper8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Paper8"):
                opp_val = getattr(value, "tp6_Paper8", None)
                setattr(value, "tp6_Paper8", self)

class tp6_Paragraph:

    def __init__(self, name: str, id: int, content: str, tp6_Paragraph: "tp6_Paper" = None):
        self.name = name
        self.id = id
        self.content = content
        self.tp6_Paragraph = tp6_Paragraph
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tp6_Paragraph(self):
        return self.__tp6_Paragraph

    @tp6_Paragraph.setter
    def tp6_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Paragraph__tp6_Paragraph", None)
        self.__tp6_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Paper"):
                opp_val = getattr(old_value, "tp6_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Paper"):
                opp_val = getattr(value, "tp6_Paper", None)
                if opp_val is None:
                    setattr(value, "tp6_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tp6_Researcher:

    def __init__(self, name: str, forName: str, Researcher: "tp6_Paper" = None, authors: set["tp6_Paper"] = None, tp6_Researcher: set["tp6_Skill"] = None, tp6_Researcher3: "tp6_Position" = None, tp6_Researcher5: set["tp6_Collaboration"] = None, tp6_Researcher14: "tp6_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.Researcher = Researcher
        self.authors = authors if authors is not None else set()
        self.tp6_Researcher = tp6_Researcher if tp6_Researcher is not None else set()
        self.tp6_Researcher3 = tp6_Researcher3
        self.tp6_Researcher5 = tp6_Researcher5 if tp6_Researcher5 is not None else set()
        self.tp6_Researcher14 = tp6_Researcher14
        
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
    def tp6_Researcher3(self):
        return self.__tp6_Researcher3

    @tp6_Researcher3.setter
    def tp6_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Researcher__tp6_Researcher3", None)
        self.__tp6_Researcher3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_Position"):
                opp_val = getattr(old_value, "tp6_Position", None)
                if opp_val == self:
                    setattr(old_value, "tp6_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_Position"):
                opp_val = getattr(value, "tp6_Position", None)
                setattr(value, "tp6_Position", self)

    @property
    def tp6_Researcher14(self):
        return self.__tp6_Researcher14

    @tp6_Researcher14.setter
    def tp6_Researcher14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Researcher__tp6_Researcher14", None)
        self.__tp6_Researcher14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp6_PublicationStructure"):
                opp_val = getattr(old_value, "tp6_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp6_PublicationStructure"):
                opp_val = getattr(value, "tp6_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "tp6_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp6_Researcher5(self):
        return self.__tp6_Researcher5

    @tp6_Researcher5.setter
    def tp6_Researcher5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Researcher__tp6_Researcher5", None)
        self.__tp6_Researcher5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp6_Collaboration"):
                    opp_val = getattr(item, "tp6_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "tp6_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp6_Collaboration"):
                    opp_val = getattr(item, "tp6_Collaboration", None)
                    
                    setattr(item, "tp6_Collaboration", self)
                    

    @property
    def tp6_Researcher(self):
        return self.__tp6_Researcher

    @tp6_Researcher.setter
    def tp6_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Researcher__tp6_Researcher", None)
        self.__tp6_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp6_Skill"):
                    opp_val = getattr(item, "tp6_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "tp6_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp6_Skill"):
                    opp_val = getattr(item, "tp6_Skill", None)
                    
                    setattr(item, "tp6_Skill", self)
                    

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp6_Researcher__authors", None)
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
        old_value = getattr(self, f"_tp6_Researcher__Researcher", None)
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
