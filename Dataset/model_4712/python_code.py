from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Connective(Enum):
    And = "And"
    Or = "Or"
    Nor = "Nor"
    Xor = "Xor"
    If = "If"
    Unless = "Unless"
    OnlyIf = "OnlyIf"
    Eqv = "Eqv"
class FormElementKind(Enum):
    SubjectRole = "SubjectRole"
    ObjectRole = "ObjectRole"
    ParticleRole = "ParticleRole"
    ParticleElement = "ParticleElement"
    ItemElement = "ItemElement"
class ElementKind(Enum):
    None = "None"
    Sentence = "Sentence"
    Qualifier = "Qualifier"
    Quantifier = "Quantifier"
    Condition = "Condition"
    Modifier = "Modifier"
    Noun = "Noun"
    Group = "Group"
    Query = "Query"
    Instance = "Instance"
    Property = "Property"
    Pronoun = "Pronoun"
    Role = "Role"
class GroupKind(Enum):
    Joint = "Joint"
    All = "All"
    Choice = "Choice"
    Neither = "Neither"
    Instead = "Instead"
class SentenceType(Enum):
    Other = "Other"
    Simple = "Simple"
    Compound = "Compound"
    Implication = "Implication"
    Equivalence = "Equivalence"
    Domain = "Domain"
    Modal = "Modal"
class Modality(Enum):
    Permission = "Permission"
    PermittedNot = "PermittedNot"
    Possibility = "Possibility"
    Impossibility = "Impossibility"
    Preference = "Preference"
    Antipreference = "Antipreference"
    Nonpreference = "Nonpreference"
    None = "None"
    Negation = "Negation"
    Obligation = "Obligation"
    Prohibition = "Prohibition"
class PhraseType(Enum):
    Instance = "Instance"
    Group = "Group"
    Query = "Query"
    TypeNoun = "TypeNoun"
    Property = "Property"
    RoleNoun = "RoleNoun"
    Pronoun = "Pronoun"
    Anaphor = "Anaphor"
    Interrogative = "Interrogative"
    LocalName = "LocalName"
class InstanceKind(Enum):
    Name = "Name"
    Number = "Number"
    String = "String"
    Quantity = "Quantity"
    Statement = "Statement"
    Question = "Question"
    Query = "Query"
    Concept = "Concept"
class PropositionKind(Enum):
    Relation = "Relation"
    Connection = "Connection"
    Implication = "Implication"
    Negation = "Negation"
    Quantification = "Quantification"
    Modal = "Modal"
class VocItemKind(Enum):
    NounConcept = "NounConcept"
    VerbConcept = "VerbConcept"
    AdjectiveConcept = "AdjectiveConcept"
    PropertyConcept = "PropertyConcept"
    ProperName = "ProperName"
class QueryKind(Enum):
    Any = "Any"
    What = "What"
    Whether = "Whether"
    Why = "Why"
    How = "How"
    Where = "Where"
    When = "When"
    HowMany = "HowMany"
class KeywordKind(Enum):
    K_Than = "K_Than"
    K_Exactly = "K_Exactly"
    K_Many = "K_Many"
    K_Not = "K_Not"
    K_And = "K_And"
    K_Or = "K_Or"
    K_If = "K_If"
    K_Then = "K_Then"
    K_Else = "K_Else"
    K_Only = "K_Only"
    K_Unless = "K_Unless"
    K_Same = "K_Same"
    K_Different = "K_Different"
    K_Other = "K_Other"
    K_Another = "K_Another"
    K_Must = "K_Must"
    K_May = "K_May"
    K_Always = "K_Always"
    K_That = "K_That"
    K_Whose = "K_Whose"
    Anaphor = "Anaphor"
    Pronoun = "Pronoun"
    Genitive = "Genitive"
    K_Self = "K_Self"
    Adjunct = "Adjunct"
    K_An = "K_An"
    K_The = "K_The"
    K_All = "K_All"
    K_None = "K_None"
    K_No = "K_No"
    K_Any = "K_Any"
    K_One = "K_One"
    K_At = "K_At"
    K_Least = "K_Least"
    K_Less = "K_Less"
    K_Most = "K_Most"
    K_More = "K_More"
    K_Everything = "K_Everything"
    K_Something = "K_Something"
    K_Anything = "K_Anything"
    K_Nothing = "K_Nothing"
    K_Whether = "K_Whether"
    K_What = "K_What"
    K_Which = "K_Which"
    K_Where = "K_Where"
    K_When = "K_When"
    K_Why = "K_Why"
    K_How = "K_How"
    K_This = "K_This"
    K_Both = "K_Both"
    K_Either = "K_Either"
    K_Neither = "K_Neither"
    K_Nor = "K_Nor"
    K_Together = "K_Together"
    K_But = "K_But"
    K_Instead = "K_Instead"
    K_There = "K_There"
    K_For = "K_For"
    K_As = "K_As"
    K_Of = "K_Of"
    Function = "Function"
class QuantifierKind(Enum):
    Q_An = "Q_An"
    Q_The = "Q_The"
    Q_All = "Q_All"
    Q_No = "Q_No"
    Q_Any = "Q_Any"
    AtLeast1 = "AtLeast1"
    AtMost1 = "AtMost1"
    Exactly1 = "Exactly1"
    AtLeastN = "AtLeastN"
    AtMostN = "AtMostN"
    ExactlyN = "ExactlyN"
    LessThanN = "LessThanN"
    MoreThanN = "MoreThanN"


############################################
# Definition of Classes
############################################

class RoleVariable:

    pass
class NBVR_Logic_Predicate:

    def __init__(self, name: str, RoleVariable: set["RoleVariable"] = None, VocNoun289: "VocNoun" = None, VocVerb292: "VocVerb" = None):
        self.name = name
        self.RoleVariable = RoleVariable if RoleVariable is not None else set()
        self.VocNoun289 = VocNoun289
        self.VocVerb292 = VocVerb292
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def VocNoun289(self):
        return self.__VocNoun289

    @VocNoun289.setter
    def VocNoun289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Predicate__VocNoun289", None)
        self.__VocNoun289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary290"):
                opp_val = getattr(old_value, "Vocabulary290", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary290"):
                opp_val = getattr(value, "Vocabulary290", None)
                setattr(value, "Vocabulary290", self)

    @property
    def RoleVariable(self):
        return self.__RoleVariable

    @RoleVariable.setter
    def RoleVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Predicate__RoleVariable", None)
        self.__RoleVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Logic287"):
                    opp_val = getattr(item, "Logic287", None)
                    
                    if opp_val == self:
                        setattr(item, "Logic287", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Logic287"):
                    opp_val = getattr(item, "Logic287", None)
                    
                    setattr(item, "Logic287", self)
                    

    @property
    def VocVerb292(self):
        return self.__VocVerb292

    @VocVerb292.setter
    def VocVerb292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Predicate__VocVerb292", None)
        self.__VocVerb292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary293"):
                opp_val = getattr(old_value, "Vocabulary293", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary293"):
                opp_val = getattr(value, "Vocabulary293", None)
                setattr(value, "Vocabulary293", self)

class ExtentConstant:

    pass
class NBVR_Logic_Set:

    pass
class NBVR_Logic_Constant(ABC):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class Constant:

    pass
class NBVR_Logic_QuantityValue(Constant):

    def __init__(self, factor: str, unit: str, Constant: "NBVR_Logic_Argument"):
        self.factor = factor
        self.unit = unit
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def factor(self) -> str:
        return self.__factor

    @factor.setter
    def factor(self, factor: str):
        self.__factor = factor

class NBVR_Logic_NominalConstant(Constant):

    pass
class NBVR_Logic_ExtentConstant(Constant):

    pass
class NBVR_Logic_ValueConstant(Constant):

    def __init__(self, name: str, Constant: "NBVR_Logic_Argument"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NBVR_Logic_Argument:

    def __init__(self, NBVR_Logic_Argument: "Argument" = None, NBVR_Logic_Argument247: "Variable" = None, NBVR_Logic_Argument250: "RolePhrase" = None, NBVR_Logic_Argument253: "VerbRole" = None, NBVR_Logic_Argument256: "Constant" = None, Relation258: "Relation" = None):
        self.NBVR_Logic_Argument = NBVR_Logic_Argument
        self.NBVR_Logic_Argument247 = NBVR_Logic_Argument247
        self.NBVR_Logic_Argument250 = NBVR_Logic_Argument250
        self.NBVR_Logic_Argument253 = NBVR_Logic_Argument253
        self.NBVR_Logic_Argument256 = NBVR_Logic_Argument256
        self.Relation258 = Relation258
        
    @property
    def NBVR_Logic_Argument256(self):
        return self.__NBVR_Logic_Argument256

    @NBVR_Logic_Argument256.setter
    def NBVR_Logic_Argument256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Argument__NBVR_Logic_Argument256", None)
        self.__NBVR_Logic_Argument256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constant"):
                opp_val = getattr(old_value, "Constant", None)
                if opp_val == self:
                    setattr(old_value, "Constant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constant"):
                opp_val = getattr(value, "Constant", None)
                setattr(value, "Constant", self)

    @property
    def NBVR_Logic_Argument(self):
        return self.__NBVR_Logic_Argument

    @NBVR_Logic_Argument.setter
    def NBVR_Logic_Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Argument__NBVR_Logic_Argument", None)
        self.__NBVR_Logic_Argument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Argument245"):
                opp_val = getattr(old_value, "Argument245", None)
                if opp_val == self:
                    setattr(old_value, "Argument245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Argument245"):
                opp_val = getattr(value, "Argument245", None)
                setattr(value, "Argument245", self)

    @property
    def NBVR_Logic_Argument247(self):
        return self.__NBVR_Logic_Argument247

    @NBVR_Logic_Argument247.setter
    def NBVR_Logic_Argument247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Argument__NBVR_Logic_Argument247", None)
        self.__NBVR_Logic_Argument247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable248"):
                opp_val = getattr(old_value, "Variable248", None)
                if opp_val == self:
                    setattr(old_value, "Variable248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable248"):
                opp_val = getattr(value, "Variable248", None)
                setattr(value, "Variable248", self)

    @property
    def NBVR_Logic_Argument253(self):
        return self.__NBVR_Logic_Argument253

    @NBVR_Logic_Argument253.setter
    def NBVR_Logic_Argument253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Argument__NBVR_Logic_Argument253", None)
        self.__NBVR_Logic_Argument253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VerbRole254"):
                opp_val = getattr(old_value, "VerbRole254", None)
                if opp_val == self:
                    setattr(old_value, "VerbRole254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VerbRole254"):
                opp_val = getattr(value, "VerbRole254", None)
                setattr(value, "VerbRole254", self)

    @property
    def NBVR_Logic_Argument250(self):
        return self.__NBVR_Logic_Argument250

    @NBVR_Logic_Argument250.setter
    def NBVR_Logic_Argument250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Argument__NBVR_Logic_Argument250", None)
        self.__NBVR_Logic_Argument250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RolePhrase251"):
                opp_val = getattr(old_value, "RolePhrase251", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase251"):
                opp_val = getattr(value, "RolePhrase251", None)
                setattr(value, "RolePhrase251", self)

    @property
    def Relation258(self):
        return self.__Relation258

    @Relation258.setter
    def Relation258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Argument__Relation258", None)
        self.__Relation258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logic259"):
                opp_val = getattr(old_value, "Logic259", None)
                if opp_val == self:
                    setattr(old_value, "Logic259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logic259"):
                opp_val = getattr(value, "Logic259", None)
                setattr(value, "Logic259", self)

    def hasNext(self) -> bool:
        # TODO: Implement hasNext method
        pass

class Argument:

    pass
class NBVR_Grammar_ParseElement(ABC):

    def __init__(self, NBVR_Grammar_ParseElement: "ParseElement" = None):
        self.NBVR_Grammar_ParseElement = NBVR_Grammar_ParseElement
        
    @property
    def NBVR_Grammar_ParseElement(self):
        return self.__NBVR_Grammar_ParseElement

    @NBVR_Grammar_ParseElement.setter
    def NBVR_Grammar_ParseElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_ParseElement__NBVR_Grammar_ParseElement", None)
        self.__NBVR_Grammar_ParseElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ParseElement222"):
                opp_val = getattr(old_value, "ParseElement222", None)
                if opp_val == self:
                    setattr(old_value, "ParseElement222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ParseElement222"):
                opp_val = getattr(value, "ParseElement222", None)
                setattr(value, "ParseElement222", self)

    def isRolePhrase(self) -> bool:
        # TODO: Implement isRolePhrase method
        pass

    def isSentence(self) -> bool:
        # TODO: Implement isSentence method
        pass

    def getElementKind(self) -> str:
        # TODO: Implement getElementKind method
        pass

    def isInstance(self) -> bool:
        # TODO: Implement isInstance method
        pass

class LocalName:

    pass
class Set:

    pass
class Relation:

    pass
class Proposition:

    pass
class NBVR_Logic_Implication(Proposition):

    pass
class NBVR_Logic_Modal(Proposition):

    def __init__(self, kind: str, NBVR_Logic_Modal: "Proposition" = None, Proposition271: "NBVR_Logic_Implication", Proposition285: "NBVR_Logic_NominalConstant", Proposition276: "NBVR_Logic_Modal", Proposition278: "NBVR_Logic_Negation", Proposition234: "NBVR_Logic_Quantification", Proposition239: "NBVR_Logic_Proposition", Proposition269: "NBVR_Logic_Connection", Proposition274: "NBVR_Logic_Implication", Proposition: "NBVR_Logic_Variable"):
        self.kind = kind
        self.NBVR_Logic_Modal = NBVR_Logic_Modal
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def NBVR_Logic_Modal(self):
        return self.__NBVR_Logic_Modal

    @NBVR_Logic_Modal.setter
    def NBVR_Logic_Modal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Modal__NBVR_Logic_Modal", None)
        self.__NBVR_Logic_Modal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Proposition276"):
                opp_val = getattr(old_value, "Proposition276", None)
                if opp_val == self:
                    setattr(old_value, "Proposition276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Proposition276"):
                opp_val = getattr(value, "Proposition276", None)
                setattr(value, "Proposition276", self)

class NBVR_Logic_Negation(Proposition):

    pass
class NBVR_Logic_Relation(Proposition):

    def __init__(self, Argument: set["Argument"] = None, NBVR_Logic_Relation: "Predicate" = None, Proposition271: "NBVR_Logic_Implication", Proposition285: "NBVR_Logic_NominalConstant", Proposition276: "NBVR_Logic_Modal", Proposition278: "NBVR_Logic_Negation", Proposition234: "NBVR_Logic_Quantification", Proposition239: "NBVR_Logic_Proposition", Proposition269: "NBVR_Logic_Connection", Proposition274: "NBVR_Logic_Implication", Proposition: "NBVR_Logic_Variable"):
        self.Argument = Argument if Argument is not None else set()
        self.NBVR_Logic_Relation = NBVR_Logic_Relation
        
    @property
    def Argument(self):
        return self.__Argument

    @Argument.setter
    def Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Relation__Argument", None)
        self.__Argument = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Logic241"):
                    opp_val = getattr(item, "Logic241", None)
                    
                    if opp_val == self:
                        setattr(item, "Logic241", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Logic241"):
                    opp_val = getattr(item, "Logic241", None)
                    
                    setattr(item, "Logic241", self)
                    

    @property
    def NBVR_Logic_Relation(self):
        return self.__NBVR_Logic_Relation

    @NBVR_Logic_Relation.setter
    def NBVR_Logic_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Relation__NBVR_Logic_Relation", None)
        self.__NBVR_Logic_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Predicate243"):
                opp_val = getattr(old_value, "Predicate243", None)
                if opp_val == self:
                    setattr(old_value, "Predicate243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Predicate243"):
                opp_val = getattr(value, "Predicate243", None)
                setattr(value, "Predicate243", self)

    def getArgument(self) -> str:
        # TODO: Implement getArgument method
        pass

class NBVR_Logic_Connection(Proposition):

    def __init__(self, kind: str, NBVR_Logic_Connection: set["Proposition"] = None, Proposition271: "NBVR_Logic_Implication", Proposition285: "NBVR_Logic_NominalConstant", Proposition276: "NBVR_Logic_Modal", Proposition278: "NBVR_Logic_Negation", Proposition234: "NBVR_Logic_Quantification", Proposition239: "NBVR_Logic_Proposition", Proposition269: "NBVR_Logic_Connection", Proposition274: "NBVR_Logic_Implication", Proposition: "NBVR_Logic_Variable"):
        self.kind = kind
        self.NBVR_Logic_Connection = NBVR_Logic_Connection if NBVR_Logic_Connection is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def NBVR_Logic_Connection(self):
        return self.__NBVR_Logic_Connection

    @NBVR_Logic_Connection.setter
    def NBVR_Logic_Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Connection__NBVR_Logic_Connection", None)
        self.__NBVR_Logic_Connection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Proposition269"):
                    opp_val = getattr(item, "Proposition269", None)
                    
                    if opp_val == self:
                        setattr(item, "Proposition269", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Proposition269"):
                    opp_val = getattr(item, "Proposition269", None)
                    
                    setattr(item, "Proposition269", self)
                    

class NBVR_Logic_Quantification(Proposition):

    def __init__(self, kind: str, unique: bool, NBVR_Logic_Quantification: "Proposition" = None, Variable236: "Variable" = None, Proposition271: "NBVR_Logic_Implication", Proposition285: "NBVR_Logic_NominalConstant", Proposition276: "NBVR_Logic_Modal", Proposition278: "NBVR_Logic_Negation", Proposition234: "NBVR_Logic_Quantification", Proposition239: "NBVR_Logic_Proposition", Proposition269: "NBVR_Logic_Connection", Proposition274: "NBVR_Logic_Implication", Proposition: "NBVR_Logic_Variable"):
        self.kind = kind
        self.unique = unique
        self.NBVR_Logic_Quantification = NBVR_Logic_Quantification
        self.Variable236 = Variable236
        
    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def NBVR_Logic_Quantification(self):
        return self.__NBVR_Logic_Quantification

    @NBVR_Logic_Quantification.setter
    def NBVR_Logic_Quantification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Quantification__NBVR_Logic_Quantification", None)
        self.__NBVR_Logic_Quantification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Proposition234"):
                opp_val = getattr(old_value, "Proposition234", None)
                if opp_val == self:
                    setattr(old_value, "Proposition234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Proposition234"):
                opp_val = getattr(value, "Proposition234", None)
                setattr(value, "Proposition234", self)

    @property
    def Variable236(self):
        return self.__Variable236

    @Variable236.setter
    def Variable236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Quantification__Variable236", None)
        self.__Variable236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logic237"):
                opp_val = getattr(old_value, "Logic237", None)
                if opp_val == self:
                    setattr(old_value, "Logic237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logic237"):
                opp_val = getattr(value, "Logic237", None)
                setattr(value, "Logic237", self)

class Quantification:

    pass
class NBVR_Logic_Variable:

    def __init__(self, name: str, Quantification: "Quantification" = None, NBVR_Logic_Variable: "Proposition" = None, NBVR_Logic_Variable227: set["Relation"] = None, NBVR_Logic_Variable229: "VocNoun" = None, Set: "Set" = None):
        self.name = name
        self.Quantification = Quantification
        self.NBVR_Logic_Variable = NBVR_Logic_Variable
        self.NBVR_Logic_Variable227 = NBVR_Logic_Variable227 if NBVR_Logic_Variable227 is not None else set()
        self.NBVR_Logic_Variable229 = NBVR_Logic_Variable229
        self.Set = Set
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Quantification(self):
        return self.__Quantification

    @Quantification.setter
    def Quantification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Variable__Quantification", None)
        self.__Quantification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logic224"):
                opp_val = getattr(old_value, "Logic224", None)
                if opp_val == self:
                    setattr(old_value, "Logic224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logic224"):
                opp_val = getattr(value, "Logic224", None)
                setattr(value, "Logic224", self)

    @property
    def NBVR_Logic_Variable227(self):
        return self.__NBVR_Logic_Variable227

    @NBVR_Logic_Variable227.setter
    def NBVR_Logic_Variable227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Variable__NBVR_Logic_Variable227", None)
        self.__NBVR_Logic_Variable227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relation"):
                    opp_val = getattr(item, "Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relation"):
                    opp_val = getattr(item, "Relation", None)
                    
                    setattr(item, "Relation", self)
                    

    @property
    def Set(self):
        return self.__Set

    @Set.setter
    def Set(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Variable__Set", None)
        self.__Set = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logic232"):
                opp_val = getattr(old_value, "Logic232", None)
                if opp_val == self:
                    setattr(old_value, "Logic232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logic232"):
                opp_val = getattr(value, "Logic232", None)
                setattr(value, "Logic232", self)

    @property
    def NBVR_Logic_Variable(self):
        return self.__NBVR_Logic_Variable

    @NBVR_Logic_Variable.setter
    def NBVR_Logic_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Variable__NBVR_Logic_Variable", None)
        self.__NBVR_Logic_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Proposition"):
                opp_val = getattr(old_value, "Proposition", None)
                if opp_val == self:
                    setattr(old_value, "Proposition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Proposition"):
                opp_val = getattr(value, "Proposition", None)
                setattr(value, "Proposition", self)

    @property
    def NBVR_Logic_Variable229(self):
        return self.__NBVR_Logic_Variable229

    @NBVR_Logic_Variable229.setter
    def NBVR_Logic_Variable229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Variable__NBVR_Logic_Variable229", None)
        self.__NBVR_Logic_Variable229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocNoun230"):
                opp_val = getattr(old_value, "VocNoun230", None)
                if opp_val == self:
                    setattr(old_value, "VocNoun230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocNoun230"):
                opp_val = getattr(value, "VocNoun230", None)
                setattr(value, "VocNoun230", self)

class Question:

    pass
class NBVR_Grammar_Parse:

    pass
class Keyword:

    pass
class PartPhrase:

    pass
class QueryPhrase:

    pass
class Nominalization:

    pass
class NBVR_Grammar_Question(Nominalization):

    def __init__(self, query: str, QueryPhrase: "QueryPhrase" = None):
        self.query = query
        self.QueryPhrase = QueryPhrase
        
    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

    @property
    def QueryPhrase(self):
        return self.__QueryPhrase

    @QueryPhrase.setter
    def QueryPhrase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Question__QueryPhrase", None)
        self.__QueryPhrase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Grammar206"):
                opp_val = getattr(old_value, "Grammar206", None)
                if opp_val == self:
                    setattr(old_value, "Grammar206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Grammar206"):
                opp_val = getattr(value, "Grammar206", None)
                setattr(value, "Grammar206", self)

class NBVR_Grammar_Statement(Nominalization):

    pass
class TypeNoun:

    pass
class VerbPhrase:

    pass
class NBVR_Grammar_PartPhrase:

    pass
class NBVR_Grammar_VerbPhrase:

    def __init__(self, modality: str, negated: bool, NBVR_Grammar_VerbPhrase: "VocVerb" = None):
        self.modality = modality
        self.negated = negated
        self.NBVR_Grammar_VerbPhrase = NBVR_Grammar_VerbPhrase
        
    @property
    def negated(self) -> bool:
        return self.__negated

    @negated.setter
    def negated(self, negated: bool):
        self.__negated = negated

    @property
    def modality(self) -> str:
        return self.__modality

    @modality.setter
    def modality(self, modality: str):
        self.__modality = modality

    @property
    def NBVR_Grammar_VerbPhrase(self):
        return self.__NBVR_Grammar_VerbPhrase

    @NBVR_Grammar_VerbPhrase.setter
    def NBVR_Grammar_VerbPhrase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_VerbPhrase__NBVR_Grammar_VerbPhrase", None)
        self.__NBVR_Grammar_VerbPhrase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocVerb176"):
                opp_val = getattr(old_value, "VocVerb176", None)
                if opp_val == self:
                    setattr(old_value, "VocVerb176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocVerb176"):
                opp_val = getattr(value, "VocVerb176", None)
                setattr(value, "VocVerb176", self)

class Modifier:

    pass
class Quantifier:

    pass
class ModifiedTerm:

    pass
class NBVR_Grammar_Pronoun(ModifiedTerm):

    pass
class NBVR_Grammar_PropertyNoun(ModifiedTerm):

    pass
class NBVR_Grammar_TypeNoun(ModifiedTerm):

    pass
class VocAdjective:

    pass
class VocUnit:

    pass
class NBVR_Grammar_Dimension:

    def __init__(self, exponent: int, NBVR_Grammar_Dimension: "VocUnit" = None):
        self.exponent = exponent
        self.NBVR_Grammar_Dimension = NBVR_Grammar_Dimension
        
    @property
    def exponent(self) -> int:
        return self.__exponent

    @exponent.setter
    def exponent(self, exponent: int):
        self.__exponent = exponent

    @property
    def NBVR_Grammar_Dimension(self):
        return self.__NBVR_Grammar_Dimension

    @NBVR_Grammar_Dimension.setter
    def NBVR_Grammar_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Dimension__NBVR_Grammar_Dimension", None)
        self.__NBVR_Grammar_Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocUnit"):
                opp_val = getattr(old_value, "VocUnit", None)
                if opp_val == self:
                    setattr(old_value, "VocUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocUnit"):
                opp_val = getattr(value, "VocUnit", None)
                setattr(value, "VocUnit", self)

class Dimension:

    pass
class NumberWord:

    pass
class Instance:

    pass
class NBVR_Grammar_Nominalization(Instance):

    pass
class NBVR_Grammar_LexicalInstance(Instance):

    pass
class NBVR_Grammar_ProperName(Instance):

    pass
class NBVR_Grammar_Intension(Instance):

    pass
class NBVR_Grammar_Quantity(Instance):

    pass
class Quantity:

    pass
class Condition:

    pass
class QualifierChain:

    pass
class Qualifier:

    pass
class NBVR_Grammar_SimpleQualifier(Qualifier):

    pass
class Sentence:

    pass
class NBVR_Grammar_ImplicationForm(Sentence):

    def __init__(self, kind: str, NBVR_Grammar_ImplicationForm: "Sentence" = None, NBVR_Grammar_ImplicationForm194: "Sentence" = None, NBVR_Grammar_ImplicationForm197: "Sentence" = None, Sentence198: "NBVR_Grammar_ImplicationForm", Sentence: "NBVR_Grammar_Condition", Sentence216: "NBVR_Grammar_DomainForm", Sentence139: "NBVR_Grammar_SimpleQualifier", Sentence204: "NBVR_Grammar_Nominalization", Sentence195: "NBVR_Grammar_ImplicationForm", Sentence200: "NBVR_Grammar_CompoundForm", Sentence192: "NBVR_Grammar_ImplicationForm", Sentence149: "NBVR_Grammar_Sentence"):
        self.kind = kind
        self.NBVR_Grammar_ImplicationForm = NBVR_Grammar_ImplicationForm
        self.NBVR_Grammar_ImplicationForm194 = NBVR_Grammar_ImplicationForm194
        self.NBVR_Grammar_ImplicationForm197 = NBVR_Grammar_ImplicationForm197
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def NBVR_Grammar_ImplicationForm197(self):
        return self.__NBVR_Grammar_ImplicationForm197

    @NBVR_Grammar_ImplicationForm197.setter
    def NBVR_Grammar_ImplicationForm197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_ImplicationForm__NBVR_Grammar_ImplicationForm197", None)
        self.__NBVR_Grammar_ImplicationForm197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sentence198"):
                opp_val = getattr(old_value, "Sentence198", None)
                if opp_val == self:
                    setattr(old_value, "Sentence198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sentence198"):
                opp_val = getattr(value, "Sentence198", None)
                setattr(value, "Sentence198", self)

    @property
    def NBVR_Grammar_ImplicationForm194(self):
        return self.__NBVR_Grammar_ImplicationForm194

    @NBVR_Grammar_ImplicationForm194.setter
    def NBVR_Grammar_ImplicationForm194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_ImplicationForm__NBVR_Grammar_ImplicationForm194", None)
        self.__NBVR_Grammar_ImplicationForm194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sentence195"):
                opp_val = getattr(old_value, "Sentence195", None)
                if opp_val == self:
                    setattr(old_value, "Sentence195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sentence195"):
                opp_val = getattr(value, "Sentence195", None)
                setattr(value, "Sentence195", self)

    @property
    def NBVR_Grammar_ImplicationForm(self):
        return self.__NBVR_Grammar_ImplicationForm

    @NBVR_Grammar_ImplicationForm.setter
    def NBVR_Grammar_ImplicationForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_ImplicationForm__NBVR_Grammar_ImplicationForm", None)
        self.__NBVR_Grammar_ImplicationForm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sentence192"):
                opp_val = getattr(old_value, "Sentence192", None)
                if opp_val == self:
                    setattr(old_value, "Sentence192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sentence192"):
                opp_val = getattr(value, "Sentence192", None)
                setattr(value, "Sentence192", self)

class NBVR_Grammar_DomainForm(Sentence):

    def __init__(self, modality: str, NBVR_Grammar_DomainForm: "Sentence" = None, Sentence198: "NBVR_Grammar_ImplicationForm", Sentence: "NBVR_Grammar_Condition", Sentence216: "NBVR_Grammar_DomainForm", Sentence139: "NBVR_Grammar_SimpleQualifier", Sentence204: "NBVR_Grammar_Nominalization", Sentence195: "NBVR_Grammar_ImplicationForm", Sentence200: "NBVR_Grammar_CompoundForm", Sentence192: "NBVR_Grammar_ImplicationForm", Sentence149: "NBVR_Grammar_Sentence"):
        self.modality = modality
        self.NBVR_Grammar_DomainForm = NBVR_Grammar_DomainForm
        
    @property
    def modality(self) -> str:
        return self.__modality

    @modality.setter
    def modality(self, modality: str):
        self.__modality = modality

    @property
    def NBVR_Grammar_DomainForm(self):
        return self.__NBVR_Grammar_DomainForm

    @NBVR_Grammar_DomainForm.setter
    def NBVR_Grammar_DomainForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_DomainForm__NBVR_Grammar_DomainForm", None)
        self.__NBVR_Grammar_DomainForm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sentence216"):
                opp_val = getattr(old_value, "Sentence216", None)
                if opp_val == self:
                    setattr(old_value, "Sentence216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sentence216"):
                opp_val = getattr(value, "Sentence216", None)
                setattr(value, "Sentence216", self)

class NBVR_Grammar_CompoundForm(Sentence):

    def __init__(self, kind: str, NBVR_Grammar_CompoundForm: set["Sentence"] = None, Sentence198: "NBVR_Grammar_ImplicationForm", Sentence: "NBVR_Grammar_Condition", Sentence216: "NBVR_Grammar_DomainForm", Sentence139: "NBVR_Grammar_SimpleQualifier", Sentence204: "NBVR_Grammar_Nominalization", Sentence195: "NBVR_Grammar_ImplicationForm", Sentence200: "NBVR_Grammar_CompoundForm", Sentence192: "NBVR_Grammar_ImplicationForm", Sentence149: "NBVR_Grammar_Sentence"):
        self.kind = kind
        self.NBVR_Grammar_CompoundForm = NBVR_Grammar_CompoundForm if NBVR_Grammar_CompoundForm is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def NBVR_Grammar_CompoundForm(self):
        return self.__NBVR_Grammar_CompoundForm

    @NBVR_Grammar_CompoundForm.setter
    def NBVR_Grammar_CompoundForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_CompoundForm__NBVR_Grammar_CompoundForm", None)
        self.__NBVR_Grammar_CompoundForm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Sentence200"):
                    opp_val = getattr(item, "Sentence200", None)
                    
                    if opp_val == self:
                        setattr(item, "Sentence200", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Sentence200"):
                    opp_val = getattr(item, "Sentence200", None)
                    
                    setattr(item, "Sentence200", self)
                    

class NBVR_Grammar_SimpleForm(Sentence):

    def __init__(self, NBVR_Grammar_SimpleForm: "VerbPhrase" = None, NBVR_Grammar_SimpleForm184: set["PartPhrase"] = None, NBVR_Grammar_SimpleForm186: "RolePhrase" = None, NBVR_Grammar_SimpleForm189: "RolePhrase" = None, Sentence198: "NBVR_Grammar_ImplicationForm", Sentence: "NBVR_Grammar_Condition", Sentence216: "NBVR_Grammar_DomainForm", Sentence139: "NBVR_Grammar_SimpleQualifier", Sentence204: "NBVR_Grammar_Nominalization", Sentence195: "NBVR_Grammar_ImplicationForm", Sentence200: "NBVR_Grammar_CompoundForm", Sentence192: "NBVR_Grammar_ImplicationForm", Sentence149: "NBVR_Grammar_Sentence"):
        self.NBVR_Grammar_SimpleForm = NBVR_Grammar_SimpleForm
        self.NBVR_Grammar_SimpleForm184 = NBVR_Grammar_SimpleForm184 if NBVR_Grammar_SimpleForm184 is not None else set()
        self.NBVR_Grammar_SimpleForm186 = NBVR_Grammar_SimpleForm186
        self.NBVR_Grammar_SimpleForm189 = NBVR_Grammar_SimpleForm189
        
    @property
    def NBVR_Grammar_SimpleForm186(self):
        return self.__NBVR_Grammar_SimpleForm186

    @NBVR_Grammar_SimpleForm186.setter
    def NBVR_Grammar_SimpleForm186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_SimpleForm__NBVR_Grammar_SimpleForm186", None)
        self.__NBVR_Grammar_SimpleForm186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RolePhrase187"):
                opp_val = getattr(old_value, "RolePhrase187", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase187"):
                opp_val = getattr(value, "RolePhrase187", None)
                setattr(value, "RolePhrase187", self)

    @property
    def NBVR_Grammar_SimpleForm(self):
        return self.__NBVR_Grammar_SimpleForm

    @NBVR_Grammar_SimpleForm.setter
    def NBVR_Grammar_SimpleForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_SimpleForm__NBVR_Grammar_SimpleForm", None)
        self.__NBVR_Grammar_SimpleForm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VerbPhrase"):
                opp_val = getattr(old_value, "VerbPhrase", None)
                if opp_val == self:
                    setattr(old_value, "VerbPhrase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VerbPhrase"):
                opp_val = getattr(value, "VerbPhrase", None)
                setattr(value, "VerbPhrase", self)

    @property
    def NBVR_Grammar_SimpleForm189(self):
        return self.__NBVR_Grammar_SimpleForm189

    @NBVR_Grammar_SimpleForm189.setter
    def NBVR_Grammar_SimpleForm189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_SimpleForm__NBVR_Grammar_SimpleForm189", None)
        self.__NBVR_Grammar_SimpleForm189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RolePhrase190"):
                opp_val = getattr(old_value, "RolePhrase190", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase190"):
                opp_val = getattr(value, "RolePhrase190", None)
                setattr(value, "RolePhrase190", self)

    @property
    def NBVR_Grammar_SimpleForm184(self):
        return self.__NBVR_Grammar_SimpleForm184

    @NBVR_Grammar_SimpleForm184.setter
    def NBVR_Grammar_SimpleForm184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_SimpleForm__NBVR_Grammar_SimpleForm184", None)
        self.__NBVR_Grammar_SimpleForm184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PartPhrase"):
                    opp_val = getattr(item, "PartPhrase", None)
                    
                    if opp_val == self:
                        setattr(item, "PartPhrase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PartPhrase"):
                    opp_val = getattr(item, "PartPhrase", None)
                    
                    setattr(item, "PartPhrase", self)
                    

    def getModality(self) -> str:
        # TODO: Implement getModality method
        pass

    def isNegated(self) -> bool:
        # TODO: Implement isNegated method
        pass

class SimpleQualifier:

    pass
class NBVR_Grammar_QualifierChain(Qualifier):

    pass
class Grammar_ParseElement:

    pass
class Vocabulary_FormulationForm:

    pass
class NBVR_Grammar_Sentence(Vocabulary_FormulationForm, Grammar_ParseElement):

    def __init__(self, NBVR_Grammar_Sentence: "RolePhrase" = None, NBVR_Grammar_Sentence148: "Sentence" = None):
        self.NBVR_Grammar_Sentence = NBVR_Grammar_Sentence
        self.NBVR_Grammar_Sentence148 = NBVR_Grammar_Sentence148
        
    @property
    def NBVR_Grammar_Sentence(self):
        return self.__NBVR_Grammar_Sentence

    @NBVR_Grammar_Sentence.setter
    def NBVR_Grammar_Sentence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Sentence__NBVR_Grammar_Sentence", None)
        self.__NBVR_Grammar_Sentence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RolePhrase146"):
                opp_val = getattr(old_value, "RolePhrase146", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase146"):
                opp_val = getattr(value, "RolePhrase146", None)
                setattr(value, "RolePhrase146", self)

    @property
    def NBVR_Grammar_Sentence148(self):
        return self.__NBVR_Grammar_Sentence148

    @NBVR_Grammar_Sentence148.setter
    def NBVR_Grammar_Sentence148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Sentence__NBVR_Grammar_Sentence148", None)
        self.__NBVR_Grammar_Sentence148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sentence149"):
                opp_val = getattr(old_value, "Sentence149", None)
                if opp_val == self:
                    setattr(old_value, "Sentence149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sentence149"):
                opp_val = getattr(value, "Sentence149", None)
                setattr(value, "Sentence149", self)

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

class NBVR_Grammar_RolePhrase(Vocabulary_FormulationForm, Grammar_ParseElement):

    def __init__(self, NBVR_Grammar_RolePhrase: "VerbRole" = None, NBVR_Grammar_RolePhrase131: "Variable" = None, NBVR_Grammar_RolePhrase133: "RolePhrase" = None):
        self.NBVR_Grammar_RolePhrase = NBVR_Grammar_RolePhrase
        self.NBVR_Grammar_RolePhrase131 = NBVR_Grammar_RolePhrase131
        self.NBVR_Grammar_RolePhrase133 = NBVR_Grammar_RolePhrase133
        
    @property
    def NBVR_Grammar_RolePhrase131(self):
        return self.__NBVR_Grammar_RolePhrase131

    @NBVR_Grammar_RolePhrase131.setter
    def NBVR_Grammar_RolePhrase131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_RolePhrase__NBVR_Grammar_RolePhrase131", None)
        self.__NBVR_Grammar_RolePhrase131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable"):
                opp_val = getattr(old_value, "Variable", None)
                if opp_val == self:
                    setattr(old_value, "Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable"):
                opp_val = getattr(value, "Variable", None)
                setattr(value, "Variable", self)

    @property
    def NBVR_Grammar_RolePhrase133(self):
        return self.__NBVR_Grammar_RolePhrase133

    @NBVR_Grammar_RolePhrase133.setter
    def NBVR_Grammar_RolePhrase133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_RolePhrase__NBVR_Grammar_RolePhrase133", None)
        self.__NBVR_Grammar_RolePhrase133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RolePhrase"):
                opp_val = getattr(old_value, "RolePhrase", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase"):
                opp_val = getattr(value, "RolePhrase", None)
                setattr(value, "RolePhrase", self)

    @property
    def NBVR_Grammar_RolePhrase(self):
        return self.__NBVR_Grammar_RolePhrase

    @NBVR_Grammar_RolePhrase.setter
    def NBVR_Grammar_RolePhrase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_RolePhrase__NBVR_Grammar_RolePhrase", None)
        self.__NBVR_Grammar_RolePhrase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VerbRole129"):
                opp_val = getattr(old_value, "VerbRole129", None)
                if opp_val == self:
                    setattr(old_value, "VerbRole129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VerbRole129"):
                opp_val = getattr(value, "VerbRole129", None)
                setattr(value, "VerbRole129", self)

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

class SimpleNounPhrase:

    pass
class NBVR_Grammar_Instance(SimpleNounPhrase):

    def __init__(self, SimpleNounPhrase: "NBVR_Grammar_GroupPhrase", SimpleNounPhrase170: "NBVR_Grammar_PropertyNoun"):
        
    def getKind(self) -> str:
        # TODO: Implement getKind method
        pass

class NBVR_Grammar_RoleNoun(SimpleNounPhrase):

    pass
class NBVR_Grammar_LocalName(SimpleNounPhrase):

    pass
class NBVR_Grammar_ModifiedTerm(SimpleNounPhrase):

    pass
class RolePhrase:

    pass
class NBVR_Grammar_SimpleNounPhrase(RolePhrase):

    pass
class NBVR_Grammar_QueryPhrase(RolePhrase):

    def __init__(self, query: str, NBVR_Grammar_QueryPhrase: "RolePhrase" = None, Question: "Question" = None, RolePhrase187: "NBVR_Grammar_SimpleForm", RolePhrase146: "NBVR_Grammar_Sentence", RolePhrase208: "NBVR_Grammar_QueryPhrase", RolePhrase: "NBVR_Grammar_RolePhrase", RolePhrase190: "NBVR_Grammar_SimpleForm", RolePhrase214: "NBVR_Grammar_Intension", RolePhrase165: "NBVR_Grammar_Modifier", RolePhrase178: "NBVR_Grammar_PartPhrase", RolePhrase251: "NBVR_Logic_Argument"):
        self.query = query
        self.NBVR_Grammar_QueryPhrase = NBVR_Grammar_QueryPhrase
        self.Question = Question
        
    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

    @property
    def Question(self):
        return self.__Question

    @Question.setter
    def Question(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_QueryPhrase__Question", None)
        self.__Question = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Grammar210"):
                opp_val = getattr(old_value, "Grammar210", None)
                if opp_val == self:
                    setattr(old_value, "Grammar210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Grammar210"):
                opp_val = getattr(value, "Grammar210", None)
                setattr(value, "Grammar210", self)

    @property
    def NBVR_Grammar_QueryPhrase(self):
        return self.__NBVR_Grammar_QueryPhrase

    @NBVR_Grammar_QueryPhrase.setter
    def NBVR_Grammar_QueryPhrase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_QueryPhrase__NBVR_Grammar_QueryPhrase", None)
        self.__NBVR_Grammar_QueryPhrase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RolePhrase208"):
                opp_val = getattr(old_value, "RolePhrase208", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase208"):
                opp_val = getattr(value, "RolePhrase208", None)
                setattr(value, "RolePhrase208", self)

class NBVR_Grammar_GroupPhrase(RolePhrase):

    def __init__(self, kind: str, NBVR_Grammar_GroupPhrase: set["SimpleNounPhrase"] = None, RolePhrase187: "NBVR_Grammar_SimpleForm", RolePhrase146: "NBVR_Grammar_Sentence", RolePhrase208: "NBVR_Grammar_QueryPhrase", RolePhrase: "NBVR_Grammar_RolePhrase", RolePhrase190: "NBVR_Grammar_SimpleForm", RolePhrase214: "NBVR_Grammar_Intension", RolePhrase165: "NBVR_Grammar_Modifier", RolePhrase178: "NBVR_Grammar_PartPhrase", RolePhrase251: "NBVR_Logic_Argument"):
        self.kind = kind
        self.NBVR_Grammar_GroupPhrase = NBVR_Grammar_GroupPhrase if NBVR_Grammar_GroupPhrase is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def NBVR_Grammar_GroupPhrase(self):
        return self.__NBVR_Grammar_GroupPhrase

    @NBVR_Grammar_GroupPhrase.setter
    def NBVR_Grammar_GroupPhrase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_GroupPhrase__NBVR_Grammar_GroupPhrase", None)
        self.__NBVR_Grammar_GroupPhrase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SimpleNounPhrase"):
                    opp_val = getattr(item, "SimpleNounPhrase", None)
                    
                    if opp_val == self:
                        setattr(item, "SimpleNounPhrase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimpleNounPhrase"):
                    opp_val = getattr(item, "SimpleNounPhrase", None)
                    
                    setattr(item, "SimpleNounPhrase", self)
                    

class Verb:

    pass
class NBVR_Vocabulary_IsVerb(Verb):

    pass
class NBVR_Vocabulary_Terminology:

    pass
class Variable:

    pass
class NBVR_Logic_RoleVariable(Variable):

    pass
class NBVR_Vocabulary_Dictionary:

    pass
class RoleElement:

    pass
class NBVR_Vocabulary_FormElement(ABC):

    def __init__(self, kind: str, SyntaxForm69: "SyntaxForm" = None):
        self.kind = kind
        self.SyntaxForm69 = SyntaxForm69
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def SyntaxForm69(self):
        return self.__SyntaxForm69

    @SyntaxForm69.setter
    def SyntaxForm69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_FormElement__SyntaxForm69", None)
        self.__SyntaxForm69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary70"):
                opp_val = getattr(old_value, "Vocabulary70", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary70"):
                opp_val = getattr(value, "Vocabulary70", None)
                setattr(value, "Vocabulary70", self)

class VocProperty:

    pass
class FormElement:

    pass
class NBVR_Vocabulary_ItemElement(FormElement):

    pass
class NBVR_Vocabulary_RoleElement(FormElement):

    def __init__(self, slot: int, NBVR_Vocabulary_RoleElement: "VerbRole" = None, Vocabulary62: "NBVR_Vocabulary_SyntaxForm"):
        self.slot = slot
        self.NBVR_Vocabulary_RoleElement = NBVR_Vocabulary_RoleElement
        
    @property
    def slot(self) -> int:
        return self.__slot

    @slot.setter
    def slot(self, slot: int):
        self.__slot = slot

    @property
    def NBVR_Vocabulary_RoleElement(self):
        return self.__NBVR_Vocabulary_RoleElement

    @NBVR_Vocabulary_RoleElement.setter
    def NBVR_Vocabulary_RoleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_RoleElement__NBVR_Vocabulary_RoleElement", None)
        self.__NBVR_Vocabulary_RoleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VerbRole94"):
                opp_val = getattr(old_value, "VerbRole94", None)
                if opp_val == self:
                    setattr(old_value, "VerbRole94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VerbRole94"):
                opp_val = getattr(value, "VerbRole94", None)
                setattr(value, "VerbRole94", self)

class NBVR_Vocabulary_Particle(FormElement):

    pass
class NBVR_Vocabulary_SyntaxForm:

    def __init__(self, isAuxForm: bool, text: str, FormElement: set["FormElement"] = None, VocProperty: "VocProperty" = None, VocVerb66: "VocVerb" = None):
        self.isAuxForm = isAuxForm
        self.text = text
        self.FormElement = FormElement if FormElement is not None else set()
        self.VocProperty = VocProperty
        self.VocVerb66 = VocVerb66
        
    @property
    def isAuxForm(self) -> bool:
        return self.__isAuxForm

    @isAuxForm.setter
    def isAuxForm(self, isAuxForm: bool):
        self.__isAuxForm = isAuxForm

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def VocVerb66(self):
        return self.__VocVerb66

    @VocVerb66.setter
    def VocVerb66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_SyntaxForm__VocVerb66", None)
        self.__VocVerb66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary67"):
                opp_val = getattr(old_value, "Vocabulary67", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary67"):
                opp_val = getattr(value, "Vocabulary67", None)
                setattr(value, "Vocabulary67", self)

    @property
    def FormElement(self):
        return self.__FormElement

    @FormElement.setter
    def FormElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_SyntaxForm__FormElement", None)
        self.__FormElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vocabulary62"):
                    opp_val = getattr(item, "Vocabulary62", None)
                    
                    if opp_val == self:
                        setattr(item, "Vocabulary62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vocabulary62"):
                    opp_val = getattr(item, "Vocabulary62", None)
                    
                    setattr(item, "Vocabulary62", self)
                    

    @property
    def VocProperty(self):
        return self.__VocProperty

    @VocProperty.setter
    def VocProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_SyntaxForm__VocProperty", None)
        self.__VocProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary64"):
                opp_val = getattr(old_value, "Vocabulary64", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary64"):
                opp_val = getattr(value, "Vocabulary64", None)
                setattr(value, "Vocabulary64", self)

class VocName:

    pass
class NBVR_Vocabulary_VocUnit(VocName):

    pass
class VocVerb:

    pass
class VocNoun:

    pass
class NBVR_Vocabulary_VerbRole:

    def __init__(self, isRange: bool, NBVR_Vocabulary_VerbRole: "VocNoun" = None, VocVerb: "VocVerb" = None, Term48: "Term" = None):
        self.isRange = isRange
        self.NBVR_Vocabulary_VerbRole = NBVR_Vocabulary_VerbRole
        self.VocVerb = VocVerb
        self.Term48 = Term48
        
    @property
    def isRange(self) -> bool:
        return self.__isRange

    @isRange.setter
    def isRange(self, isRange: bool):
        self.__isRange = isRange

    @property
    def Term48(self):
        return self.__Term48

    @Term48.setter
    def Term48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VerbRole__Term48", None)
        self.__Term48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary49"):
                opp_val = getattr(old_value, "Vocabulary49", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary49"):
                opp_val = getattr(value, "Vocabulary49", None)
                setattr(value, "Vocabulary49", self)

    @property
    def NBVR_Vocabulary_VerbRole(self):
        return self.__NBVR_Vocabulary_VerbRole

    @NBVR_Vocabulary_VerbRole.setter
    def NBVR_Vocabulary_VerbRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VerbRole__NBVR_Vocabulary_VerbRole", None)
        self.__NBVR_Vocabulary_VerbRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocNoun"):
                opp_val = getattr(old_value, "VocNoun", None)
                if opp_val == self:
                    setattr(old_value, "VocNoun", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocNoun"):
                opp_val = getattr(value, "VocNoun", None)
                setattr(value, "VocNoun", self)

    @property
    def VocVerb(self):
        return self.__VocVerb

    @VocVerb.setter
    def VocVerb(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VerbRole__VocVerb", None)
        self.__VocVerb = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary46"):
                opp_val = getattr(old_value, "Vocabulary46", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary46"):
                opp_val = getattr(value, "Vocabulary46", None)
                setattr(value, "Vocabulary46", self)

class NBVR_Vocabulary_FormulationForm(ABC):

    def __init__(self, Formulation42: "Formulation" = None):
        self.Formulation42 = Formulation42
        
    @property
    def Formulation42(self):
        return self.__Formulation42

    @Formulation42.setter
    def Formulation42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_FormulationForm__Formulation42", None)
        self.__Formulation42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary43"):
                opp_val = getattr(old_value, "Vocabulary43", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary43"):
                opp_val = getattr(value, "Vocabulary43", None)
                setattr(value, "Vocabulary43", self)

    def isStructured(self) -> bool:
        # TODO: Implement isStructured method
        pass

class ParseElement:

    pass
class NBVR_Grammar_Modifier(ParseElement):

    def __init__(self, kind: str, NBVR_Grammar_Modifier: "VocAdjective" = None, NBVR_Grammar_Modifier164: "RolePhrase" = None, ParseElement222: "NBVR_Grammar_ParseElement", ParseElement: "NBVR_Vocabulary_Formulation"):
        self.kind = kind
        self.NBVR_Grammar_Modifier = NBVR_Grammar_Modifier
        self.NBVR_Grammar_Modifier164 = NBVR_Grammar_Modifier164
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def NBVR_Grammar_Modifier164(self):
        return self.__NBVR_Grammar_Modifier164

    @NBVR_Grammar_Modifier164.setter
    def NBVR_Grammar_Modifier164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Modifier__NBVR_Grammar_Modifier164", None)
        self.__NBVR_Grammar_Modifier164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RolePhrase165"):
                opp_val = getattr(old_value, "RolePhrase165", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase165"):
                opp_val = getattr(value, "RolePhrase165", None)
                setattr(value, "RolePhrase165", self)

    @property
    def NBVR_Grammar_Modifier(self):
        return self.__NBVR_Grammar_Modifier

    @NBVR_Grammar_Modifier.setter
    def NBVR_Grammar_Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Modifier__NBVR_Grammar_Modifier", None)
        self.__NBVR_Grammar_Modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocAdjective"):
                opp_val = getattr(old_value, "VocAdjective", None)
                if opp_val == self:
                    setattr(old_value, "VocAdjective", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocAdjective"):
                opp_val = getattr(value, "VocAdjective", None)
                setattr(value, "VocAdjective", self)

class NBVR_Grammar_Quantifier(ParseElement):

    def __init__(self, count: int, kind: str, NBVR_Grammar_Quantifier: "Quantity" = None, ParseElement222: "NBVR_Grammar_ParseElement", ParseElement: "NBVR_Vocabulary_Formulation"):
        self.count = count
        self.kind = kind
        self.NBVR_Grammar_Quantifier = NBVR_Grammar_Quantifier
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def NBVR_Grammar_Quantifier(self):
        return self.__NBVR_Grammar_Quantifier

    @NBVR_Grammar_Quantifier.setter
    def NBVR_Grammar_Quantifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Quantifier__NBVR_Grammar_Quantifier", None)
        self.__NBVR_Grammar_Quantifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Quantity"):
                opp_val = getattr(old_value, "Quantity", None)
                if opp_val == self:
                    setattr(old_value, "Quantity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Quantity"):
                opp_val = getattr(value, "Quantity", None)
                setattr(value, "Quantity", self)

class NBVR_Grammar_Condition(ParseElement):

    def __init__(self, otherwise: bool, SimpleQualifier: "SimpleQualifier" = None, NBVR_Grammar_Condition: "Sentence" = None, ParseElement222: "NBVR_Grammar_ParseElement", ParseElement: "NBVR_Vocabulary_Formulation"):
        self.otherwise = otherwise
        self.SimpleQualifier = SimpleQualifier
        self.NBVR_Grammar_Condition = NBVR_Grammar_Condition
        
    @property
    def otherwise(self) -> bool:
        return self.__otherwise

    @otherwise.setter
    def otherwise(self, otherwise: bool):
        self.__otherwise = otherwise

    @property
    def SimpleQualifier(self):
        return self.__SimpleQualifier

    @SimpleQualifier.setter
    def SimpleQualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Condition__SimpleQualifier", None)
        self.__SimpleQualifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Grammar"):
                opp_val = getattr(old_value, "Grammar", None)
                if opp_val == self:
                    setattr(old_value, "Grammar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Grammar"):
                opp_val = getattr(value, "Grammar", None)
                setattr(value, "Grammar", self)

    @property
    def NBVR_Grammar_Condition(self):
        return self.__NBVR_Grammar_Condition

    @NBVR_Grammar_Condition.setter
    def NBVR_Grammar_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Condition__NBVR_Grammar_Condition", None)
        self.__NBVR_Grammar_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sentence"):
                opp_val = getattr(old_value, "Sentence", None)
                if opp_val == self:
                    setattr(old_value, "Sentence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sentence"):
                opp_val = getattr(value, "Sentence", None)
                setattr(value, "Sentence", self)

class NBVR_Grammar_Qualifier(ParseElement):

    def __init__(self, ParseElement222: "NBVR_Grammar_ParseElement", ParseElement: "NBVR_Vocabulary_Formulation"):
        
    def isSimple(self) -> bool:
        # TODO: Implement isSimple method
        pass

class FormulationForm:

    pass
class NBVR_Logic_Proposition(FormulationForm):

    def __init__(self, text: str, NBVR_Logic_Proposition: "Proposition" = None, Vocabulary36: "NBVR_Vocabulary_Formulation"):
        self.text = text
        self.NBVR_Logic_Proposition = NBVR_Logic_Proposition
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def NBVR_Logic_Proposition(self):
        return self.__NBVR_Logic_Proposition

    @NBVR_Logic_Proposition.setter
    def NBVR_Logic_Proposition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Proposition__NBVR_Logic_Proposition", None)
        self.__NBVR_Logic_Proposition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Proposition239"):
                opp_val = getattr(old_value, "Proposition239", None)
                if opp_val == self:
                    setattr(old_value, "Proposition239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Proposition239"):
                opp_val = getattr(value, "Proposition239", None)
                setattr(value, "Proposition239", self)

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

class SyntaxForm:

    pass
class Predicate:

    pass
class Formulation:

    pass
class NBVR_Vocabulary_Definition(Formulation):

    pass
class NBVR_Vocabulary_Formulation:

    def __init__(self, text: str, language: str, FormulationForm: "FormulationForm" = None, NBVR_Vocabulary_Formulation: set["ParseElement"] = None, VocabularyItem39: "VocabularyItem" = None):
        self.text = text
        self.language = language
        self.FormulationForm = FormulationForm
        self.NBVR_Vocabulary_Formulation = NBVR_Vocabulary_Formulation if NBVR_Vocabulary_Formulation is not None else set()
        self.VocabularyItem39 = VocabularyItem39
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def VocabularyItem39(self):
        return self.__VocabularyItem39

    @VocabularyItem39.setter
    def VocabularyItem39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Formulation__VocabularyItem39", None)
        self.__VocabularyItem39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary40"):
                opp_val = getattr(old_value, "Vocabulary40", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary40"):
                opp_val = getattr(value, "Vocabulary40", None)
                setattr(value, "Vocabulary40", self)

    @property
    def NBVR_Vocabulary_Formulation(self):
        return self.__NBVR_Vocabulary_Formulation

    @NBVR_Vocabulary_Formulation.setter
    def NBVR_Vocabulary_Formulation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Formulation__NBVR_Vocabulary_Formulation", None)
        self.__NBVR_Vocabulary_Formulation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParseElement"):
                    opp_val = getattr(item, "ParseElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ParseElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParseElement"):
                    opp_val = getattr(item, "ParseElement", None)
                    
                    setattr(item, "ParseElement", self)
                    

    @property
    def FormulationForm(self):
        return self.__FormulationForm

    @FormulationForm.setter
    def FormulationForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Formulation__FormulationForm", None)
        self.__FormulationForm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary36"):
                opp_val = getattr(old_value, "Vocabulary36", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary36"):
                opp_val = getattr(value, "Vocabulary36", None)
                setattr(value, "Vocabulary36", self)

    def isStructured(self) -> bool:
        # TODO: Implement isStructured method
        pass

    def addElement(self, elt: str):
        # TODO: Implement addElement method
        pass

class NBVR_Vocabulary_WordForm:

    def __init__(self, text: str, NBVR_Vocabulary_WordForm11: "Word" = None, NBVR_Vocabulary_WordForm: "WordForm" = None, NBVR_Vocabulary_WordForm8: "Word" = None):
        self.text = text
        self.NBVR_Vocabulary_WordForm11 = NBVR_Vocabulary_WordForm11
        self.NBVR_Vocabulary_WordForm = NBVR_Vocabulary_WordForm
        self.NBVR_Vocabulary_WordForm8 = NBVR_Vocabulary_WordForm8
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def NBVR_Vocabulary_WordForm8(self):
        return self.__NBVR_Vocabulary_WordForm8

    @NBVR_Vocabulary_WordForm8.setter
    def NBVR_Vocabulary_WordForm8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_WordForm__NBVR_Vocabulary_WordForm8", None)
        self.__NBVR_Vocabulary_WordForm8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Word9"):
                opp_val = getattr(old_value, "Word9", None)
                if opp_val == self:
                    setattr(old_value, "Word9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Word9"):
                opp_val = getattr(value, "Word9", None)
                setattr(value, "Word9", self)

    @property
    def NBVR_Vocabulary_WordForm(self):
        return self.__NBVR_Vocabulary_WordForm

    @NBVR_Vocabulary_WordForm.setter
    def NBVR_Vocabulary_WordForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_WordForm__NBVR_Vocabulary_WordForm", None)
        self.__NBVR_Vocabulary_WordForm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm6"):
                opp_val = getattr(old_value, "WordForm6", None)
                if opp_val == self:
                    setattr(old_value, "WordForm6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm6"):
                opp_val = getattr(value, "WordForm6", None)
                setattr(value, "WordForm6", self)

    @property
    def NBVR_Vocabulary_WordForm11(self):
        return self.__NBVR_Vocabulary_WordForm11

    @NBVR_Vocabulary_WordForm11.setter
    def NBVR_Vocabulary_WordForm11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_WordForm__NBVR_Vocabulary_WordForm11", None)
        self.__NBVR_Vocabulary_WordForm11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Word12"):
                opp_val = getattr(old_value, "Word12", None)
                if opp_val == self:
                    setattr(old_value, "Word12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Word12"):
                opp_val = getattr(value, "Word12", None)
                setattr(value, "Word12", self)

class Term:

    pass
class WordForm:

    pass
class NBVR_Vocabulary_VocabularyItem(ABC):

    def __init__(self, NBVR_Vocabulary_VocabularyItem30: "VocabularyItem" = None, Term33: set["Term"] = None, Formulation: set["Formulation"] = None, NBVR_Vocabulary_VocabularyItem: set["VocabularyItem"] = None):
        self.NBVR_Vocabulary_VocabularyItem30 = NBVR_Vocabulary_VocabularyItem30
        self.Term33 = Term33 if Term33 is not None else set()
        self.Formulation = Formulation if Formulation is not None else set()
        self.NBVR_Vocabulary_VocabularyItem = NBVR_Vocabulary_VocabularyItem if NBVR_Vocabulary_VocabularyItem is not None else set()
        
    @property
    def NBVR_Vocabulary_VocabularyItem(self):
        return self.__NBVR_Vocabulary_VocabularyItem

    @NBVR_Vocabulary_VocabularyItem.setter
    def NBVR_Vocabulary_VocabularyItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocabularyItem__NBVR_Vocabulary_VocabularyItem", None)
        self.__NBVR_Vocabulary_VocabularyItem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VocabularyItem28"):
                    opp_val = getattr(item, "VocabularyItem28", None)
                    
                    if opp_val == self:
                        setattr(item, "VocabularyItem28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VocabularyItem28"):
                    opp_val = getattr(item, "VocabularyItem28", None)
                    
                    setattr(item, "VocabularyItem28", self)
                    

    @property
    def Formulation(self):
        return self.__Formulation

    @Formulation.setter
    def Formulation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocabularyItem__Formulation", None)
        self.__Formulation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vocabulary26"):
                    opp_val = getattr(item, "Vocabulary26", None)
                    
                    if opp_val == self:
                        setattr(item, "Vocabulary26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vocabulary26"):
                    opp_val = getattr(item, "Vocabulary26", None)
                    
                    setattr(item, "Vocabulary26", self)
                    

    @property
    def Term33(self):
        return self.__Term33

    @Term33.setter
    def Term33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocabularyItem__Term33", None)
        self.__Term33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vocabulary34"):
                    opp_val = getattr(item, "Vocabulary34", None)
                    
                    if opp_val == self:
                        setattr(item, "Vocabulary34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vocabulary34"):
                    opp_val = getattr(item, "Vocabulary34", None)
                    
                    setattr(item, "Vocabulary34", self)
                    

    @property
    def NBVR_Vocabulary_VocabularyItem30(self):
        return self.__NBVR_Vocabulary_VocabularyItem30

    @NBVR_Vocabulary_VocabularyItem30.setter
    def NBVR_Vocabulary_VocabularyItem30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocabularyItem__NBVR_Vocabulary_VocabularyItem30", None)
        self.__NBVR_Vocabulary_VocabularyItem30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocabularyItem31"):
                opp_val = getattr(old_value, "VocabularyItem31", None)
                if opp_val == self:
                    setattr(old_value, "VocabularyItem31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocabularyItem31"):
                opp_val = getattr(value, "VocabularyItem31", None)
                setattr(value, "VocabularyItem31", self)

    def getKind(self) -> str:
        # TODO: Implement getKind method
        pass

    def isPrimitive(self) -> bool:
        # TODO: Implement isPrimitive method
        pass

class ItemElement:

    pass
class Particle:

    pass
class VerbRole:

    pass
class VocabularyItem:

    pass
class NBVR_Vocabulary_VocName(VocabularyItem):

    def __init__(self, VocabularyItem123: "NBVR_Vocabulary_Terminology", VocabularyItem22: "NBVR_Vocabulary_Term", VocabularyItem126: "NBVR_Vocabulary_Terminology", VocabularyItem31: "NBVR_Vocabulary_VocabularyItem", Vocabulary40: "NBVR_Vocabulary_Formulation", VocabularyItem28: "NBVR_Vocabulary_VocabularyItem", Vocabulary: "NBVR_Vocabulary_Term"):
        
    def isUnit(self) -> bool:
        # TODO: Implement isUnit method
        pass

class NBVR_Vocabulary_VocAdjective(VocabularyItem):

    pass
class NBVR_Vocabulary_VocProperty(VocabularyItem):

    pass
class NBVR_Vocabulary_VocVerb(VocabularyItem):

    def __init__(self, arity: int, VerbRole54: set["VerbRole"] = None, SyntaxForm: set["SyntaxForm"] = None, Predicate59: "Predicate" = None, VocabularyItem123: "NBVR_Vocabulary_Terminology", VocabularyItem22: "NBVR_Vocabulary_Term", VocabularyItem126: "NBVR_Vocabulary_Terminology", VocabularyItem31: "NBVR_Vocabulary_VocabularyItem", Vocabulary40: "NBVR_Vocabulary_Formulation", VocabularyItem28: "NBVR_Vocabulary_VocabularyItem", Vocabulary: "NBVR_Vocabulary_Term"):
        self.arity = arity
        self.VerbRole54 = VerbRole54 if VerbRole54 is not None else set()
        self.SyntaxForm = SyntaxForm if SyntaxForm is not None else set()
        self.Predicate59 = Predicate59
        
    @property
    def arity(self) -> int:
        return self.__arity

    @arity.setter
    def arity(self, arity: int):
        self.__arity = arity

    @property
    def SyntaxForm(self):
        return self.__SyntaxForm

    @SyntaxForm.setter
    def SyntaxForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocVerb__SyntaxForm", None)
        self.__SyntaxForm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vocabulary57"):
                    opp_val = getattr(item, "Vocabulary57", None)
                    
                    if opp_val == self:
                        setattr(item, "Vocabulary57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vocabulary57"):
                    opp_val = getattr(item, "Vocabulary57", None)
                    
                    setattr(item, "Vocabulary57", self)
                    

    @property
    def Predicate59(self):
        return self.__Predicate59

    @Predicate59.setter
    def Predicate59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocVerb__Predicate59", None)
        self.__Predicate59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logic60"):
                opp_val = getattr(old_value, "Logic60", None)
                if opp_val == self:
                    setattr(old_value, "Logic60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logic60"):
                opp_val = getattr(value, "Logic60", None)
                setattr(value, "Logic60", self)

    @property
    def VerbRole54(self):
        return self.__VerbRole54

    @VerbRole54.setter
    def VerbRole54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocVerb__VerbRole54", None)
        self.__VerbRole54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vocabulary55"):
                    opp_val = getattr(item, "Vocabulary55", None)
                    
                    if opp_val == self:
                        setattr(item, "Vocabulary55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vocabulary55"):
                    opp_val = getattr(item, "Vocabulary55", None)
                    
                    setattr(item, "Vocabulary55", self)
                    

class NBVR_Vocabulary_VocNoun(VocabularyItem):

    def __init__(self, massNoun: bool, NBVR_Vocabulary_VocNoun: "VocVerb" = None, Predicate: "Predicate" = None, VocabularyItem123: "NBVR_Vocabulary_Terminology", VocabularyItem22: "NBVR_Vocabulary_Term", VocabularyItem126: "NBVR_Vocabulary_Terminology", VocabularyItem31: "NBVR_Vocabulary_VocabularyItem", Vocabulary40: "NBVR_Vocabulary_Formulation", VocabularyItem28: "NBVR_Vocabulary_VocabularyItem", Vocabulary: "NBVR_Vocabulary_Term"):
        self.massNoun = massNoun
        self.NBVR_Vocabulary_VocNoun = NBVR_Vocabulary_VocNoun
        self.Predicate = Predicate
        
    @property
    def massNoun(self) -> bool:
        return self.__massNoun

    @massNoun.setter
    def massNoun(self, massNoun: bool):
        self.__massNoun = massNoun

    @property
    def NBVR_Vocabulary_VocNoun(self):
        return self.__NBVR_Vocabulary_VocNoun

    @NBVR_Vocabulary_VocNoun.setter
    def NBVR_Vocabulary_VocNoun(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocNoun__NBVR_Vocabulary_VocNoun", None)
        self.__NBVR_Vocabulary_VocNoun = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocVerb51"):
                opp_val = getattr(old_value, "VocVerb51", None)
                if opp_val == self:
                    setattr(old_value, "VocVerb51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocVerb51"):
                opp_val = getattr(value, "VocVerb51", None)
                setattr(value, "VocVerb51", self)

    @property
    def Predicate(self):
        return self.__Predicate

    @Predicate.setter
    def Predicate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocNoun__Predicate", None)
        self.__Predicate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logic"):
                opp_val = getattr(old_value, "Logic", None)
                if opp_val == self:
                    setattr(old_value, "Logic", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logic"):
                opp_val = getattr(value, "Logic", None)
                setattr(value, "Logic", self)

class NBVR_Vocabulary_Term:

    def __init__(self, text: str, VocabularyItem: "VocabularyItem" = None, VerbRole: "VerbRole" = None, Particle: "Particle" = None, NBVR_Vocabulary_Term: set["Word"] = None, NBVR_Vocabulary_Term21: "VocabularyItem" = None, ItemElement: set["ItemElement"] = None):
        self.text = text
        self.VocabularyItem = VocabularyItem
        self.VerbRole = VerbRole
        self.Particle = Particle
        self.NBVR_Vocabulary_Term = NBVR_Vocabulary_Term if NBVR_Vocabulary_Term is not None else set()
        self.NBVR_Vocabulary_Term21 = NBVR_Vocabulary_Term21
        self.ItemElement = ItemElement if ItemElement is not None else set()
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def NBVR_Vocabulary_Term(self):
        return self.__NBVR_Vocabulary_Term

    @NBVR_Vocabulary_Term.setter
    def NBVR_Vocabulary_Term(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Term__NBVR_Vocabulary_Term", None)
        self.__NBVR_Vocabulary_Term = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Word19"):
                    opp_val = getattr(item, "Word19", None)
                    
                    if opp_val == self:
                        setattr(item, "Word19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Word19"):
                    opp_val = getattr(item, "Word19", None)
                    
                    setattr(item, "Word19", self)
                    

    @property
    def ItemElement(self):
        return self.__ItemElement

    @ItemElement.setter
    def ItemElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Term__ItemElement", None)
        self.__ItemElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vocabulary24"):
                    opp_val = getattr(item, "Vocabulary24", None)
                    
                    if opp_val == self:
                        setattr(item, "Vocabulary24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vocabulary24"):
                    opp_val = getattr(item, "Vocabulary24", None)
                    
                    setattr(item, "Vocabulary24", self)
                    

    @property
    def NBVR_Vocabulary_Term21(self):
        return self.__NBVR_Vocabulary_Term21

    @NBVR_Vocabulary_Term21.setter
    def NBVR_Vocabulary_Term21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Term__NBVR_Vocabulary_Term21", None)
        self.__NBVR_Vocabulary_Term21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocabularyItem22"):
                opp_val = getattr(old_value, "VocabularyItem22", None)
                if opp_val == self:
                    setattr(old_value, "VocabularyItem22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocabularyItem22"):
                opp_val = getattr(value, "VocabularyItem22", None)
                setattr(value, "VocabularyItem22", self)

    @property
    def VerbRole(self):
        return self.__VerbRole

    @VerbRole.setter
    def VerbRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Term__VerbRole", None)
        self.__VerbRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary15"):
                opp_val = getattr(old_value, "Vocabulary15", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary15"):
                opp_val = getattr(value, "Vocabulary15", None)
                setattr(value, "Vocabulary15", self)

    @property
    def Particle(self):
        return self.__Particle

    @Particle.setter
    def Particle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Term__Particle", None)
        self.__Particle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary17"):
                opp_val = getattr(old_value, "Vocabulary17", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary17"):
                opp_val = getattr(value, "Vocabulary17", None)
                setattr(value, "Vocabulary17", self)

    @property
    def VocabularyItem(self):
        return self.__VocabularyItem

    @VocabularyItem.setter
    def VocabularyItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Term__VocabularyItem", None)
        self.__VocabularyItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vocabulary"):
                opp_val = getattr(old_value, "Vocabulary", None)
                if opp_val == self:
                    setattr(old_value, "Vocabulary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vocabulary"):
                opp_val = getattr(value, "Vocabulary", None)
                setattr(value, "Vocabulary", self)

class NBVR_Vocabulary_Word(ABC):

    def __init__(self, NBVR_Vocabulary_Word: "WordForm" = None, NBVR_Vocabulary_Word2: set["Term"] = None, NBVR_Vocabulary_Word4: "Word" = None):
        self.NBVR_Vocabulary_Word = NBVR_Vocabulary_Word
        self.NBVR_Vocabulary_Word2 = NBVR_Vocabulary_Word2 if NBVR_Vocabulary_Word2 is not None else set()
        self.NBVR_Vocabulary_Word4 = NBVR_Vocabulary_Word4
        
    @property
    def NBVR_Vocabulary_Word(self):
        return self.__NBVR_Vocabulary_Word

    @NBVR_Vocabulary_Word.setter
    def NBVR_Vocabulary_Word(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Word__NBVR_Vocabulary_Word", None)
        self.__NBVR_Vocabulary_Word = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm"):
                opp_val = getattr(old_value, "WordForm", None)
                if opp_val == self:
                    setattr(old_value, "WordForm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm"):
                opp_val = getattr(value, "WordForm", None)
                setattr(value, "WordForm", self)

    @property
    def NBVR_Vocabulary_Word2(self):
        return self.__NBVR_Vocabulary_Word2

    @NBVR_Vocabulary_Word2.setter
    def NBVR_Vocabulary_Word2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Word__NBVR_Vocabulary_Word2", None)
        self.__NBVR_Vocabulary_Word2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Term"):
                    opp_val = getattr(item, "Term", None)
                    
                    if opp_val == self:
                        setattr(item, "Term", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Term"):
                    opp_val = getattr(item, "Term", None)
                    
                    setattr(item, "Term", self)
                    

    @property
    def NBVR_Vocabulary_Word4(self):
        return self.__NBVR_Vocabulary_Word4

    @NBVR_Vocabulary_Word4.setter
    def NBVR_Vocabulary_Word4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Word__NBVR_Vocabulary_Word4", None)
        self.__NBVR_Vocabulary_Word4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Word"):
                opp_val = getattr(old_value, "Word", None)
                if opp_val == self:
                    setattr(old_value, "Word", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Word"):
                opp_val = getattr(value, "Word", None)
                setattr(value, "Word", self)

    def isKeyword(self, kind: str) -> bool:
        # TODO: Implement isKeyword method
        pass

    def isIs(self) -> bool:
        # TODO: Implement isIs method
        pass

    def isText(self) -> bool:
        # TODO: Implement isText method
        pass

    def isNumber(self) -> bool:
        # TODO: Implement isNumber method
        pass

    def isKeyword(self) -> bool:
        # TODO: Implement isKeyword method
        pass

    def isArticle(self) -> bool:
        # TODO: Implement isArticle method
        pass

class Word:

    pass
class NBVR_Vocabulary_Noun(Word):

    pass
class NBVR_Vocabulary_NumberWord(Word):

    def __init__(self, value: int, decimal: bool, Word121: "NBVR_Vocabulary_Dictionary", Word202: "NBVR_Grammar_LexicalInstance", Word12: "NBVR_Vocabulary_WordForm", Word19: "NBVR_Vocabulary_Term", Word9: "NBVR_Vocabulary_WordForm", Word: "NBVR_Vocabulary_Word", Word218: "NBVR_Grammar_LocalName"):
        self.value = value
        self.decimal = decimal
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def decimal(self) -> bool:
        return self.__decimal

    @decimal.setter
    def decimal(self, decimal: bool):
        self.__decimal = decimal

class NBVR_Vocabulary_Keyword(Word):

    def __init__(self, kind: str, Word121: "NBVR_Vocabulary_Dictionary", Word202: "NBVR_Grammar_LexicalInstance", Word12: "NBVR_Vocabulary_WordForm", Word19: "NBVR_Vocabulary_Term", Word9: "NBVR_Vocabulary_WordForm", Word: "NBVR_Vocabulary_Word", Word218: "NBVR_Grammar_LocalName"):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class NBVR_Vocabulary_Adjunct(Word):

    pass
class NBVR_Vocabulary_StringWord(Word):

    pass
class NBVR_Vocabulary_Verb(Word):

    def __init__(self, NBVR_Vocabulary_Verb: "WordForm" = None, NBVR_Vocabulary_Verb106: "WordForm" = None, NBVR_Vocabulary_Verb109: "WordForm" = None, NBVR_Vocabulary_Verb112: "WordForm" = None, NBVR_Vocabulary_Verb115: "WordForm" = None, NBVR_Vocabulary_Verb118: "WordForm" = None, Word121: "NBVR_Vocabulary_Dictionary", Word202: "NBVR_Grammar_LexicalInstance", Word12: "NBVR_Vocabulary_WordForm", Word19: "NBVR_Vocabulary_Term", Word9: "NBVR_Vocabulary_WordForm", Word: "NBVR_Vocabulary_Word", Word218: "NBVR_Grammar_LocalName"):
        self.NBVR_Vocabulary_Verb = NBVR_Vocabulary_Verb
        self.NBVR_Vocabulary_Verb106 = NBVR_Vocabulary_Verb106
        self.NBVR_Vocabulary_Verb109 = NBVR_Vocabulary_Verb109
        self.NBVR_Vocabulary_Verb112 = NBVR_Vocabulary_Verb112
        self.NBVR_Vocabulary_Verb115 = NBVR_Vocabulary_Verb115
        self.NBVR_Vocabulary_Verb118 = NBVR_Vocabulary_Verb118
        
    @property
    def NBVR_Vocabulary_Verb(self):
        return self.__NBVR_Vocabulary_Verb

    @NBVR_Vocabulary_Verb.setter
    def NBVR_Vocabulary_Verb(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Verb__NBVR_Vocabulary_Verb", None)
        self.__NBVR_Vocabulary_Verb = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm104"):
                opp_val = getattr(old_value, "WordForm104", None)
                if opp_val == self:
                    setattr(old_value, "WordForm104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm104"):
                opp_val = getattr(value, "WordForm104", None)
                setattr(value, "WordForm104", self)

    @property
    def NBVR_Vocabulary_Verb118(self):
        return self.__NBVR_Vocabulary_Verb118

    @NBVR_Vocabulary_Verb118.setter
    def NBVR_Vocabulary_Verb118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Verb__NBVR_Vocabulary_Verb118", None)
        self.__NBVR_Vocabulary_Verb118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm119"):
                opp_val = getattr(old_value, "WordForm119", None)
                if opp_val == self:
                    setattr(old_value, "WordForm119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm119"):
                opp_val = getattr(value, "WordForm119", None)
                setattr(value, "WordForm119", self)

    @property
    def NBVR_Vocabulary_Verb109(self):
        return self.__NBVR_Vocabulary_Verb109

    @NBVR_Vocabulary_Verb109.setter
    def NBVR_Vocabulary_Verb109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Verb__NBVR_Vocabulary_Verb109", None)
        self.__NBVR_Vocabulary_Verb109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm110"):
                opp_val = getattr(old_value, "WordForm110", None)
                if opp_val == self:
                    setattr(old_value, "WordForm110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm110"):
                opp_val = getattr(value, "WordForm110", None)
                setattr(value, "WordForm110", self)

    @property
    def NBVR_Vocabulary_Verb115(self):
        return self.__NBVR_Vocabulary_Verb115

    @NBVR_Vocabulary_Verb115.setter
    def NBVR_Vocabulary_Verb115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Verb__NBVR_Vocabulary_Verb115", None)
        self.__NBVR_Vocabulary_Verb115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm116"):
                opp_val = getattr(old_value, "WordForm116", None)
                if opp_val == self:
                    setattr(old_value, "WordForm116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm116"):
                opp_val = getattr(value, "WordForm116", None)
                setattr(value, "WordForm116", self)

    @property
    def NBVR_Vocabulary_Verb106(self):
        return self.__NBVR_Vocabulary_Verb106

    @NBVR_Vocabulary_Verb106.setter
    def NBVR_Vocabulary_Verb106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Verb__NBVR_Vocabulary_Verb106", None)
        self.__NBVR_Vocabulary_Verb106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm107"):
                opp_val = getattr(old_value, "WordForm107", None)
                if opp_val == self:
                    setattr(old_value, "WordForm107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm107"):
                opp_val = getattr(value, "WordForm107", None)
                setattr(value, "WordForm107", self)

    @property
    def NBVR_Vocabulary_Verb112(self):
        return self.__NBVR_Vocabulary_Verb112

    @NBVR_Vocabulary_Verb112.setter
    def NBVR_Vocabulary_Verb112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Verb__NBVR_Vocabulary_Verb112", None)
        self.__NBVR_Vocabulary_Verb112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm113"):
                opp_val = getattr(old_value, "WordForm113", None)
                if opp_val == self:
                    setattr(old_value, "WordForm113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm113"):
                opp_val = getattr(value, "WordForm113", None)
                setattr(value, "WordForm113", self)

    def isProgressive(self, wf: str) -> bool:
        # TODO: Implement isProgressive method
        pass

    def isPast(self, wf: str) -> bool:
        # TODO: Implement isPast method
        pass

    def isPerfective(self, wf: str) -> bool:
        # TODO: Implement isPerfective method
        pass

class NBVR_Vocabulary_DateTime(Word):

    pass
class NBVR_Vocabulary_Name(Word):

    pass
class NBVR_Vocabulary_Adjective(Word):

    pass