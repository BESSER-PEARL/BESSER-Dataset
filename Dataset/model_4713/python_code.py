from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FormElementKind(Enum):
    SubjectRole = "SubjectRole"
    ObjectRole = "ObjectRole"
    ParticleRole = "ParticleRole"
    ParticleElement = "ParticleElement"
    ItemElement = "ItemElement"
class QuantifierKind(Enum):
    Q_An = "Q_An"
    Q_The = "Q_The"
    Q_Any = "Q_Any"
    Q_All = "Q_All"
    AtLeast1 = "AtLeast1"
    Q_No = "Q_No"
    AtMost1 = "AtMost1"
    Exactly1 = "Exactly1"
    AtLeastN = "AtLeastN"
    AtMostN = "AtMostN"
    ExactlyN = "ExactlyN"
    LessThanN = "LessThanN"
    MoreThanN = "MoreThanN"
class VocItemKind(Enum):
    NounConcept = "NounConcept"
    VerbConcept = "VerbConcept"
    AdjectiveConcept = "AdjectiveConcept"
    PropertyConcept = "PropertyConcept"
    ProperName = "ProperName"
class Connective(Enum):
    And = "And"
    Or = "Or"
    Nor = "Nor"
    Xor = "Xor"
    If = "If"
    Unless = "Unless"
    OnlyIf = "OnlyIf"
    Eqv = "Eqv"
class SentenceType(Enum):
    Compound = "Compound"
    Implication = "Implication"
    Equivalence = "Equivalence"
    Domain = "Domain"
    Modal = "Modal"
    Other = "Other"
    Simple = "Simple"
class InstanceKind(Enum):
    Name = "Name"
    Number = "Number"
    String = "String"
    Quantity = "Quantity"
    Statement = "Statement"
    Question = "Question"
    Query = "Query"
    Concept = "Concept"
class GroupKind(Enum):
    Joint = "Joint"
    All = "All"
    Choice = "Choice"
    Neither = "Neither"
    Instead = "Instead"
class Modality(Enum):
    None_ = "None_"
    Negation = "Negation"
    Obligation = "Obligation"
    Prohibition = "Prohibition"
    Permission = "Permission"
    PermittedNot = "PermittedNot"
    Possibility = "Possibility"
    Impossibility = "Impossibility"
    Preference = "Preference"
    Antipreference = "Antipreference"
    Nonpreference = "Nonpreference"
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
    K_Something = "K_Something"
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
    K_Anything = "K_Anything"
    Pronoun = "Pronoun"
    K_Nothing = "K_Nothing"
    Genitive = "Genitive"
    K_Whether = "K_Whether"
    K_Self = "K_Self"
    K_What = "K_What"
    K_Everything = "K_Everything"
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
class ElementKind(Enum):
    Group = "Group"
    Query = "Query"
    Instance = "Instance"
    Property = "Property"
    Pronoun = "Pronoun"
    Role = "Role"
    None_ = "None_"
    Sentence = "Sentence"
    Qualifier = "Qualifier"
    Quantifier = "Quantifier"
    Condition = "Condition"
    Modifier = "Modifier"
    Noun = "Noun"
class PropositionKind(Enum):
    Relation = "Relation"
    Connection = "Connection"
    Implication = "Implication"
    Negation = "Negation"
    Quantification = "Quantification"
    Modal = "Modal"


############################################
# Definition of Classes
############################################

class NBVR_Logic_Predicate:

    def __init__(self, name: str, predicate: set["RoleVariable"] = None, predicate263: "VocNoun" = None, predicate266: "VocVerb" = None):
        self.name = name
        self.predicate = predicate if predicate is not None else set()
        self.predicate263 = predicate263
        self.predicate266 = predicate266
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def predicate(self):
        return self.__predicate

    @predicate.setter
    def predicate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Predicate__predicate", None)
        self.__predicate = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RoleVariable"):
                    opp_val = getattr(item, "RoleVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "RoleVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RoleVariable"):
                    opp_val = getattr(item, "RoleVariable", None)
                    
                    setattr(item, "RoleVariable", self)
                    

    @property
    def predicate263(self):
        return self.__predicate263

    @predicate263.setter
    def predicate263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Predicate__predicate263", None)
        self.__predicate263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocNoun264"):
                opp_val = getattr(old_value, "VocNoun264", None)
                if opp_val == self:
                    setattr(old_value, "VocNoun264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocNoun264"):
                opp_val = getattr(value, "VocNoun264", None)
                setattr(value, "VocNoun264", self)

    @property
    def predicate266(self):
        return self.__predicate266

    @predicate266.setter
    def predicate266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Predicate__predicate266", None)
        self.__predicate266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocVerb267"):
                opp_val = getattr(old_value, "VocVerb267", None)
                if opp_val == self:
                    setattr(old_value, "VocVerb267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocVerb267"):
                opp_val = getattr(value, "VocVerb267", None)
                setattr(value, "VocVerb267", self)

class RoleVariable:

    pass
class ExtentConstant:

    pass
class NBVR_Logic_Set:

    pass
class NBVR_Logic_Constant(ABC):

    def __init__(self, kind: str):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class Constant:

    pass
class NBVR_Logic_ValueConstant(Constant):

    def __init__(self, name: str, Constant: "NBVR_Logic_Argument" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class NBVR_Logic_ExtentConstant(Constant):

    pass
class NBVR_Logic_QuantityValue(Constant):

    def __init__(self, factor: str, unit: str, Constant: "NBVR_Logic_Argument" = None):
        self.factor = factor
        self.unit = unit
        
        pass
    @property
    def factor(self):
        return self.__factor

    @factor.setter
    def factor(self, factor: str):
        self.__factor = factor


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


class NBVR_Logic_NominalConstant(Constant):

    pass
class NBVR_Logic_Argument:

    def __init__(self, NBVR_Logic_Argument: "Argument" = None, NBVR_Logic_Argument226: "Variable" = None, NBVR_Logic_Argument229: "RolePhrase" = None, NBVR_Logic_Argument232: "VerbRole" = None, NBVR_Logic_Argument235: "Constant" = None, arguments: "Relation" = None):
        self.NBVR_Logic_Argument = NBVR_Logic_Argument
        self.NBVR_Logic_Argument226 = NBVR_Logic_Argument226
        self.NBVR_Logic_Argument229 = NBVR_Logic_Argument229
        self.NBVR_Logic_Argument232 = NBVR_Logic_Argument232
        self.NBVR_Logic_Argument235 = NBVR_Logic_Argument235
        self.arguments = arguments
        
        pass
    @property
    def NBVR_Logic_Argument232(self):
        return self.__NBVR_Logic_Argument232

    @NBVR_Logic_Argument232.setter
    def NBVR_Logic_Argument232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Argument__NBVR_Logic_Argument232", None)
        self.__NBVR_Logic_Argument232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VerbRole233"):
                opp_val = getattr(old_value, "VerbRole233", None)
                if opp_val == self:
                    setattr(old_value, "VerbRole233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VerbRole233"):
                opp_val = getattr(value, "VerbRole233", None)
                setattr(value, "VerbRole233", self)

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
            if hasattr(old_value, "Argument224"):
                opp_val = getattr(old_value, "Argument224", None)
                if opp_val == self:
                    setattr(old_value, "Argument224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Argument224"):
                opp_val = getattr(value, "Argument224", None)
                setattr(value, "Argument224", self)

    @property
    def NBVR_Logic_Argument226(self):
        return self.__NBVR_Logic_Argument226

    @NBVR_Logic_Argument226.setter
    def NBVR_Logic_Argument226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Argument__NBVR_Logic_Argument226", None)
        self.__NBVR_Logic_Argument226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable227"):
                opp_val = getattr(old_value, "Variable227", None)
                if opp_val == self:
                    setattr(old_value, "Variable227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable227"):
                opp_val = getattr(value, "Variable227", None)
                setattr(value, "Variable227", self)

    @property
    def NBVR_Logic_Argument235(self):
        return self.__NBVR_Logic_Argument235

    @NBVR_Logic_Argument235.setter
    def NBVR_Logic_Argument235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Argument__NBVR_Logic_Argument235", None)
        self.__NBVR_Logic_Argument235 = value
        
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
    def NBVR_Logic_Argument229(self):
        return self.__NBVR_Logic_Argument229

    @NBVR_Logic_Argument229.setter
    def NBVR_Logic_Argument229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Argument__NBVR_Logic_Argument229", None)
        self.__NBVR_Logic_Argument229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RolePhrase230"):
                opp_val = getattr(old_value, "RolePhrase230", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase230"):
                opp_val = getattr(value, "RolePhrase230", None)
                setattr(value, "RolePhrase230", self)

    @property
    def arguments(self):
        return self.__arguments

    @arguments.setter
    def arguments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Argument__arguments", None)
        self.__arguments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relation237"):
                opp_val = getattr(old_value, "Relation237", None)
                if opp_val == self:
                    setattr(old_value, "Relation237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relation237"):
                opp_val = getattr(value, "Relation237", None)
                setattr(value, "Relation237", self)

    def hasNext(self) :
        # TODO: Implement hasNext method
        pass

class Argument:

    pass
class SimpleNounPhrase:

    pass
class RolePhrase:

    pass
class NBVR_Grammar_GroupPhrase(RolePhrase):

    def __init__(self, kind: str, NBVR_Grammar_GroupPhrase: set["SimpleNounPhrase"] = None, RolePhrase230: "NBVR_Logic_Argument" = None, RolePhrase174: "NBVR_Grammar_SimpleForm" = None, RolePhrase196: "NBVR_Grammar_Intension" = None, RolePhrase: "NBVR_Grammar_RolePhrase" = None, RolePhrase149: "NBVR_Grammar_Modifier" = None, RolePhrase191: "NBVR_Grammar_QueryPhrase" = None, RolePhrase171: "NBVR_Grammar_SimpleForm" = None, RolePhrase162: "NBVR_Grammar_PartPhrase" = None, RolePhrase130: "NBVR_Grammar_Sentence" = None):
        self.kind = kind
        self.NBVR_Grammar_GroupPhrase = NBVR_Grammar_GroupPhrase if NBVR_Grammar_GroupPhrase is not None else set()
        
        pass
    @property
    def kind(self):
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
class NBVR_Vocabulary_Dictionary:

    pass
class RoleElement:

    pass
class VocName:

    pass
class NBVR_Vocabulary_VocUnit(VocName):

    pass
class NBVR_Vocabulary_FormElement(ABC):

    def __init__(self, kind: str, elements: "SyntaxForm" = None):
        self.kind = kind
        self.elements = elements
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_FormElement__elements", None)
        self.__elements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SyntaxForm60"):
                opp_val = getattr(old_value, "SyntaxForm60", None)
                if opp_val == self:
                    setattr(old_value, "SyntaxForm60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SyntaxForm60"):
                opp_val = getattr(value, "SyntaxForm60", None)
                setattr(value, "SyntaxForm60", self)

class FormElement:

    pass
class NBVR_Vocabulary_Particle(FormElement):

    pass
class NBVR_Vocabulary_RoleElement(FormElement):

    def __init__(self, slot: int, NBVR_Vocabulary_RoleElement: "VerbRole" = None, FormElement: "NBVR_Vocabulary_SyntaxForm" = None):
        self.slot = slot
        self.NBVR_Vocabulary_RoleElement = NBVR_Vocabulary_RoleElement
        
        pass
    @property
    def slot(self):
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
            if hasattr(old_value, "VerbRole82"):
                opp_val = getattr(old_value, "VerbRole82", None)
                if opp_val == self:
                    setattr(old_value, "VerbRole82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VerbRole82"):
                opp_val = getattr(value, "VerbRole82", None)
                setattr(value, "VerbRole82", self)

class NBVR_Vocabulary_ItemElement(FormElement):

    pass
class NBVR_Vocabulary_SyntaxForm:

    def __init__(self, text: str, isAuxForm: bool, propertyForm: "VocProperty" = None, form54: set["FormElement"] = None, form57: "VocVerb" = None):
        self.text = text
        self.isAuxForm = isAuxForm
        self.propertyForm = propertyForm
        self.form54 = form54 if form54 is not None else set()
        self.form57 = form57
        
        pass
    @property
    def isAuxForm(self):
        return self.__isAuxForm

    @isAuxForm.setter
    def isAuxForm(self, isAuxForm: bool):
        self.__isAuxForm = isAuxForm


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def form54(self):
        return self.__form54

    @form54.setter
    def form54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_SyntaxForm__form54", None)
        self.__form54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FormElement"):
                    opp_val = getattr(item, "FormElement", None)
                    
                    if opp_val == self:
                        setattr(item, "FormElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FormElement"):
                    opp_val = getattr(item, "FormElement", None)
                    
                    setattr(item, "FormElement", self)
                    

    @property
    def form57(self):
        return self.__form57

    @form57.setter
    def form57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_SyntaxForm__form57", None)
        self.__form57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocVerb58"):
                opp_val = getattr(old_value, "VocVerb58", None)
                if opp_val == self:
                    setattr(old_value, "VocVerb58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocVerb58"):
                opp_val = getattr(value, "VocVerb58", None)
                setattr(value, "VocVerb58", self)

    @property
    def propertyForm(self):
        return self.__propertyForm

    @propertyForm.setter
    def propertyForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_SyntaxForm__propertyForm", None)
        self.__propertyForm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocProperty"):
                opp_val = getattr(old_value, "VocProperty", None)
                if opp_val == self:
                    setattr(old_value, "VocProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocProperty"):
                opp_val = getattr(value, "VocProperty", None)
                setattr(value, "VocProperty", self)

class SyntaxForm:

    pass
class Predicate:

    pass
class VocVerb:

    pass
class VocNoun:

    pass
class NBVR_Vocabulary_VerbRole:

    def __init__(self, isRange: bool, NBVR_Vocabulary_VerbRole: "VocNoun" = None, roles: "VocVerb" = None, role: "Term" = None):
        self.isRange = isRange
        self.NBVR_Vocabulary_VerbRole = NBVR_Vocabulary_VerbRole
        self.roles = roles
        self.role = role
        
        pass
    @property
    def isRange(self):
        return self.__isRange

    @isRange.setter
    def isRange(self, isRange: bool):
        self.__isRange = isRange


    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VerbRole__role", None)
        self.__role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Term42"):
                opp_val = getattr(old_value, "Term42", None)
                if opp_val == self:
                    setattr(old_value, "Term42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Term42"):
                opp_val = getattr(value, "Term42", None)
                setattr(value, "Term42", self)

    @property
    def roles(self):
        return self.__roles

    @roles.setter
    def roles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VerbRole__roles", None)
        self.__roles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocVerb"):
                opp_val = getattr(old_value, "VocVerb", None)
                if opp_val == self:
                    setattr(old_value, "VocVerb", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocVerb"):
                opp_val = getattr(value, "VocVerb", None)
                setattr(value, "VocVerb", self)

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

class NBVR_Vocabulary_FormulationForm(ABC):

    def __init__(self, form: "Formulation" = None):
        self.form = form
        
        pass
    @property
    def form(self):
        return self.__form

    @form.setter
    def form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_FormulationForm__form", None)
        self.__form = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Formulation38"):
                opp_val = getattr(old_value, "Formulation38", None)
                if opp_val == self:
                    setattr(old_value, "Formulation38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Formulation38"):
                opp_val = getattr(value, "Formulation38", None)
                setattr(value, "Formulation38", self)

    def isStructured(self) :
        # TODO: Implement isStructured method
        pass

class VocProperty:

    pass
class FormulationForm:

    pass
class NBVR_Logic_Proposition(FormulationForm):

    def __init__(self, text: str, NBVR_Logic_Proposition: "Proposition" = None, FormulationForm: "NBVR_Vocabulary_Formulation" = None):
        self.text = text
        self.NBVR_Logic_Proposition = NBVR_Logic_Proposition
        
        pass
    @property
    def text(self):
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
            if hasattr(old_value, "Proposition219"):
                opp_val = getattr(old_value, "Proposition219", None)
                if opp_val == self:
                    setattr(old_value, "Proposition219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Proposition219"):
                opp_val = getattr(value, "Proposition219", None)
                setattr(value, "Proposition219", self)

    def getType(self) :
        # TODO: Implement getType method
        pass

class NBVR_Vocabulary_Formulation:

    def __init__(self, text: str, language: str, formulation: "FormulationForm" = None, NBVR_Vocabulary_Formulation: set["ParseElement"] = None, formulations: "VocabularyItem" = None):
        self.text = text
        self.language = language
        self.formulation = formulation
        self.NBVR_Vocabulary_Formulation = NBVR_Vocabulary_Formulation if NBVR_Vocabulary_Formulation is not None else set()
        self.formulations = formulations
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def formulation(self):
        return self.__formulation

    @formulation.setter
    def formulation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Formulation__formulation", None)
        self.__formulation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FormulationForm"):
                opp_val = getattr(old_value, "FormulationForm", None)
                if opp_val == self:
                    setattr(old_value, "FormulationForm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FormulationForm"):
                opp_val = getattr(value, "FormulationForm", None)
                setattr(value, "FormulationForm", self)

    @property
    def formulations(self):
        return self.__formulations

    @formulations.setter
    def formulations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Formulation__formulations", None)
        self.__formulations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocabularyItem36"):
                opp_val = getattr(old_value, "VocabularyItem36", None)
                if opp_val == self:
                    setattr(old_value, "VocabularyItem36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocabularyItem36"):
                opp_val = getattr(value, "VocabularyItem36", None)
                setattr(value, "VocabularyItem36", self)

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
                    

    def isStructured(self) :
        # TODO: Implement isStructured method
        pass

    def addElement(self, NBVR_elt):
        # TODO: Implement addElement method
        pass

class Formulation:

    pass
class NBVR_Vocabulary_Definition(Formulation):

    pass
class NBVR_Vocabulary_VocabularyItem(ABC):

    def __init__(self, concept31: set["Term"] = None, concept: set["Formulation"] = None, NBVR_Vocabulary_VocabularyItem: set["VocabularyItem"] = None, NBVR_Vocabulary_VocabularyItem28: "VocabularyItem" = None):
        self.concept31 = concept31 if concept31 is not None else set()
        self.concept = concept if concept is not None else set()
        self.NBVR_Vocabulary_VocabularyItem = NBVR_Vocabulary_VocabularyItem if NBVR_Vocabulary_VocabularyItem is not None else set()
        self.NBVR_Vocabulary_VocabularyItem28 = NBVR_Vocabulary_VocabularyItem28
        
        pass
    @property
    def NBVR_Vocabulary_VocabularyItem28(self):
        return self.__NBVR_Vocabulary_VocabularyItem28

    @NBVR_Vocabulary_VocabularyItem28.setter
    def NBVR_Vocabulary_VocabularyItem28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocabularyItem__NBVR_Vocabulary_VocabularyItem28", None)
        self.__NBVR_Vocabulary_VocabularyItem28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocabularyItem29"):
                opp_val = getattr(old_value, "VocabularyItem29", None)
                if opp_val == self:
                    setattr(old_value, "VocabularyItem29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocabularyItem29"):
                opp_val = getattr(value, "VocabularyItem29", None)
                setattr(value, "VocabularyItem29", self)

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
                if hasattr(item, "VocabularyItem26"):
                    opp_val = getattr(item, "VocabularyItem26", None)
                    
                    if opp_val == self:
                        setattr(item, "VocabularyItem26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VocabularyItem26"):
                    opp_val = getattr(item, "VocabularyItem26", None)
                    
                    setattr(item, "VocabularyItem26", self)
                    

    @property
    def concept(self):
        return self.__concept

    @concept.setter
    def concept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocabularyItem__concept", None)
        self.__concept = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Formulation"):
                    opp_val = getattr(item, "Formulation", None)
                    
                    if opp_val == self:
                        setattr(item, "Formulation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Formulation"):
                    opp_val = getattr(item, "Formulation", None)
                    
                    setattr(item, "Formulation", self)
                    

    @property
    def concept31(self):
        return self.__concept31

    @concept31.setter
    def concept31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocabularyItem__concept31", None)
        self.__concept31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Term32"):
                    opp_val = getattr(item, "Term32", None)
                    
                    if opp_val == self:
                        setattr(item, "Term32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Term32"):
                    opp_val = getattr(item, "Term32", None)
                    
                    setattr(item, "Term32", self)
                    

    def getKind(self) :
        # TODO: Implement getKind method
        pass

    def isPrimitive(self) :
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
class NBVR_Vocabulary_VocVerb(VocabularyItem):

    def __init__(self, arity: int, verb: set["VerbRole"] = None, verb49: set["SyntaxForm"] = None, verb51: "Predicate" = None, VocabularyItem113: "NBVR_Vocabulary_Terminology" = None, VocabularyItem29: "NBVR_Vocabulary_VocabularyItem" = None, VocabularyItem110: "NBVR_Vocabulary_Terminology" = None, VocabularyItem: "NBVR_Vocabulary_Term" = None, VocabularyItem36: "NBVR_Vocabulary_Formulation" = None, VocabularyItem26: "NBVR_Vocabulary_VocabularyItem" = None, VocabularyItem21: "NBVR_Vocabulary_Term" = None):
        self.arity = arity
        self.verb = verb if verb is not None else set()
        self.verb49 = verb49 if verb49 is not None else set()
        self.verb51 = verb51
        
        pass
    @property
    def arity(self):
        return self.__arity

    @arity.setter
    def arity(self, arity: int):
        self.__arity = arity


    @property
    def verb51(self):
        return self.__verb51

    @verb51.setter
    def verb51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocVerb__verb51", None)
        self.__verb51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Predicate52"):
                opp_val = getattr(old_value, "Predicate52", None)
                if opp_val == self:
                    setattr(old_value, "Predicate52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Predicate52"):
                opp_val = getattr(value, "Predicate52", None)
                setattr(value, "Predicate52", self)

    @property
    def verb(self):
        return self.__verb

    @verb.setter
    def verb(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocVerb__verb", None)
        self.__verb = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VerbRole47"):
                    opp_val = getattr(item, "VerbRole47", None)
                    
                    if opp_val == self:
                        setattr(item, "VerbRole47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VerbRole47"):
                    opp_val = getattr(item, "VerbRole47", None)
                    
                    setattr(item, "VerbRole47", self)
                    

    @property
    def verb49(self):
        return self.__verb49

    @verb49.setter
    def verb49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocVerb__verb49", None)
        self.__verb49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SyntaxForm"):
                    opp_val = getattr(item, "SyntaxForm", None)
                    
                    if opp_val == self:
                        setattr(item, "SyntaxForm", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SyntaxForm"):
                    opp_val = getattr(item, "SyntaxForm", None)
                    
                    setattr(item, "SyntaxForm", self)
                    

class NBVR_Vocabulary_VocAdjective(VocabularyItem):

    pass
class NBVR_Vocabulary_VocName(VocabularyItem):

    def __init__(self, VocabularyItem113: "NBVR_Vocabulary_Terminology" = None, VocabularyItem29: "NBVR_Vocabulary_VocabularyItem" = None, VocabularyItem110: "NBVR_Vocabulary_Terminology" = None, VocabularyItem: "NBVR_Vocabulary_Term" = None, VocabularyItem36: "NBVR_Vocabulary_Formulation" = None, VocabularyItem26: "NBVR_Vocabulary_VocabularyItem" = None, VocabularyItem21: "NBVR_Vocabulary_Term" = None):
        
        pass
    def isUnit(self) :
        # TODO: Implement isUnit method
        pass

class NBVR_Vocabulary_VocNoun(VocabularyItem):

    def __init__(self, massNoun: bool, NBVR_Vocabulary_VocNoun: "VocVerb" = None, noun: "Predicate" = None, VocabularyItem113: "NBVR_Vocabulary_Terminology" = None, VocabularyItem29: "NBVR_Vocabulary_VocabularyItem" = None, VocabularyItem110: "NBVR_Vocabulary_Terminology" = None, VocabularyItem: "NBVR_Vocabulary_Term" = None, VocabularyItem36: "NBVR_Vocabulary_Formulation" = None, VocabularyItem26: "NBVR_Vocabulary_VocabularyItem" = None, VocabularyItem21: "NBVR_Vocabulary_Term" = None):
        self.massNoun = massNoun
        self.NBVR_Vocabulary_VocNoun = NBVR_Vocabulary_VocNoun
        self.noun = noun
        
        pass
    @property
    def massNoun(self):
        return self.__massNoun

    @massNoun.setter
    def massNoun(self, massNoun: bool):
        self.__massNoun = massNoun


    @property
    def noun(self):
        return self.__noun

    @noun.setter
    def noun(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_VocNoun__noun", None)
        self.__noun = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Predicate"):
                opp_val = getattr(old_value, "Predicate", None)
                if opp_val == self:
                    setattr(old_value, "Predicate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Predicate"):
                opp_val = getattr(value, "Predicate", None)
                setattr(value, "Predicate", self)

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
            if hasattr(old_value, "VocVerb44"):
                opp_val = getattr(old_value, "VocVerb44", None)
                if opp_val == self:
                    setattr(old_value, "VocVerb44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocVerb44"):
                opp_val = getattr(value, "VocVerb44", None)
                setattr(value, "VocVerb44", self)

class NBVR_Vocabulary_VocProperty(VocabularyItem):

    pass
class NBVR_Vocabulary_Term:

    def __init__(self, text: str, terms: "VocabularyItem" = None, term: "VerbRole" = None, term16: "Particle" = None, NBVR_Vocabulary_Term: set["Word"] = None, NBVR_Vocabulary_Term20: "VocabularyItem" = None, term23: set["ItemElement"] = None):
        self.text = text
        self.terms = terms
        self.term = term
        self.term16 = term16
        self.NBVR_Vocabulary_Term = NBVR_Vocabulary_Term if NBVR_Vocabulary_Term is not None else set()
        self.NBVR_Vocabulary_Term20 = NBVR_Vocabulary_Term20
        self.term23 = term23 if term23 is not None else set()
        
        pass
    @property
    def text(self):
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
                if hasattr(item, "Word18"):
                    opp_val = getattr(item, "Word18", None)
                    
                    if opp_val == self:
                        setattr(item, "Word18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Word18"):
                    opp_val = getattr(item, "Word18", None)
                    
                    setattr(item, "Word18", self)
                    

    @property
    def terms(self):
        return self.__terms

    @terms.setter
    def terms(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Term__terms", None)
        self.__terms = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocabularyItem"):
                opp_val = getattr(old_value, "VocabularyItem", None)
                if opp_val == self:
                    setattr(old_value, "VocabularyItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocabularyItem"):
                opp_val = getattr(value, "VocabularyItem", None)
                setattr(value, "VocabularyItem", self)

    @property
    def term16(self):
        return self.__term16

    @term16.setter
    def term16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Term__term16", None)
        self.__term16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Particle"):
                opp_val = getattr(old_value, "Particle", None)
                if opp_val == self:
                    setattr(old_value, "Particle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Particle"):
                opp_val = getattr(value, "Particle", None)
                setattr(value, "Particle", self)

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Term__term", None)
        self.__term = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VerbRole"):
                opp_val = getattr(old_value, "VerbRole", None)
                if opp_val == self:
                    setattr(old_value, "VerbRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VerbRole"):
                opp_val = getattr(value, "VerbRole", None)
                setattr(value, "VerbRole", self)

    @property
    def term23(self):
        return self.__term23

    @term23.setter
    def term23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Term__term23", None)
        self.__term23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ItemElement"):
                    opp_val = getattr(item, "ItemElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ItemElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ItemElement"):
                    opp_val = getattr(item, "ItemElement", None)
                    
                    setattr(item, "ItemElement", self)
                    

    @property
    def NBVR_Vocabulary_Term20(self):
        return self.__NBVR_Vocabulary_Term20

    @NBVR_Vocabulary_Term20.setter
    def NBVR_Vocabulary_Term20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Term__NBVR_Vocabulary_Term20", None)
        self.__NBVR_Vocabulary_Term20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocabularyItem21"):
                opp_val = getattr(old_value, "VocabularyItem21", None)
                if opp_val == self:
                    setattr(old_value, "VocabularyItem21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocabularyItem21"):
                opp_val = getattr(value, "VocabularyItem21", None)
                setattr(value, "VocabularyItem21", self)

class ParseElement:

    pass
class NBVR_Vocabulary_WordForm:

    def __init__(self, text: str, NBVR_Vocabulary_WordForm8: "Word" = None, NBVR_Vocabulary_WordForm11: "Word" = None, NBVR_Vocabulary_WordForm: "WordForm" = None):
        self.text = text
        self.NBVR_Vocabulary_WordForm8 = NBVR_Vocabulary_WordForm8
        self.NBVR_Vocabulary_WordForm11 = NBVR_Vocabulary_WordForm11
        self.NBVR_Vocabulary_WordForm = NBVR_Vocabulary_WordForm
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


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

class Term:

    pass
class WordForm:

    pass
class NBVR_Vocabulary_Word(ABC):

    def __init__(self, NBVR_Vocabulary_Word: "WordForm" = None, NBVR_Vocabulary_Word2: set["Term"] = None, NBVR_Vocabulary_Word4: "Word" = None):
        self.NBVR_Vocabulary_Word = NBVR_Vocabulary_Word
        self.NBVR_Vocabulary_Word2 = NBVR_Vocabulary_Word2 if NBVR_Vocabulary_Word2 is not None else set()
        self.NBVR_Vocabulary_Word4 = NBVR_Vocabulary_Word4
        
        pass
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

    def isArticle(self) :
        # TODO: Implement isArticle method
        pass

    def isText(self) :
        # TODO: Implement isText method
        pass

    def isKeyword(self) :
        # TODO: Implement isKeyword method
        pass

    def isNumber(self) :
        # TODO: Implement isNumber method
        pass

    def isIs(self) :
        # TODO: Implement isIs method
        pass

class Word:

    pass
class NBVR_Vocabulary_StringWord(Word):

    pass
class NBVR_Vocabulary_Noun(Word):

    pass
class NBVR_Vocabulary_NumberWord(Word):

    def __init__(self, value: int, decimal: bool, Word108: "NBVR_Vocabulary_Dictionary" = None, Word9: "NBVR_Vocabulary_WordForm" = None, Word: "NBVR_Vocabulary_Word" = None, Word200: "NBVR_Grammar_LocalName" = None, Word12: "NBVR_Vocabulary_WordForm" = None, Word186: "NBVR_Grammar_LexicalInstance" = None, Word18: "NBVR_Vocabulary_Term" = None):
        self.value = value
        self.decimal = decimal
        
        pass
    @property
    def decimal(self):
        return self.__decimal

    @decimal.setter
    def decimal(self, decimal: bool):
        self.__decimal = decimal


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class NBVR_Vocabulary_Adjunct(Word):

    pass
class NBVR_Vocabulary_DateTime(Word):

    pass
class NBVR_Vocabulary_Name(Word):

    pass
class NBVR_Vocabulary_Verb(Word):

    def __init__(self, NBVR_Vocabulary_Verb: "WordForm" = None, NBVR_Vocabulary_Verb93: "WordForm" = None, NBVR_Vocabulary_Verb96: "WordForm" = None, NBVR_Vocabulary_Verb99: "WordForm" = None, NBVR_Vocabulary_Verb102: "WordForm" = None, NBVR_Vocabulary_Verb105: "WordForm" = None, Word108: "NBVR_Vocabulary_Dictionary" = None, Word9: "NBVR_Vocabulary_WordForm" = None, Word: "NBVR_Vocabulary_Word" = None, Word200: "NBVR_Grammar_LocalName" = None, Word12: "NBVR_Vocabulary_WordForm" = None, Word186: "NBVR_Grammar_LexicalInstance" = None, Word18: "NBVR_Vocabulary_Term" = None):
        self.NBVR_Vocabulary_Verb = NBVR_Vocabulary_Verb
        self.NBVR_Vocabulary_Verb93 = NBVR_Vocabulary_Verb93
        self.NBVR_Vocabulary_Verb96 = NBVR_Vocabulary_Verb96
        self.NBVR_Vocabulary_Verb99 = NBVR_Vocabulary_Verb99
        self.NBVR_Vocabulary_Verb102 = NBVR_Vocabulary_Verb102
        self.NBVR_Vocabulary_Verb105 = NBVR_Vocabulary_Verb105
        
        pass
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
            if hasattr(old_value, "WordForm91"):
                opp_val = getattr(old_value, "WordForm91", None)
                if opp_val == self:
                    setattr(old_value, "WordForm91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm91"):
                opp_val = getattr(value, "WordForm91", None)
                setattr(value, "WordForm91", self)

    @property
    def NBVR_Vocabulary_Verb93(self):
        return self.__NBVR_Vocabulary_Verb93

    @NBVR_Vocabulary_Verb93.setter
    def NBVR_Vocabulary_Verb93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Verb__NBVR_Vocabulary_Verb93", None)
        self.__NBVR_Vocabulary_Verb93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm94"):
                opp_val = getattr(old_value, "WordForm94", None)
                if opp_val == self:
                    setattr(old_value, "WordForm94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm94"):
                opp_val = getattr(value, "WordForm94", None)
                setattr(value, "WordForm94", self)

    @property
    def NBVR_Vocabulary_Verb99(self):
        return self.__NBVR_Vocabulary_Verb99

    @NBVR_Vocabulary_Verb99.setter
    def NBVR_Vocabulary_Verb99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Verb__NBVR_Vocabulary_Verb99", None)
        self.__NBVR_Vocabulary_Verb99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm100"):
                opp_val = getattr(old_value, "WordForm100", None)
                if opp_val == self:
                    setattr(old_value, "WordForm100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm100"):
                opp_val = getattr(value, "WordForm100", None)
                setattr(value, "WordForm100", self)

    @property
    def NBVR_Vocabulary_Verb96(self):
        return self.__NBVR_Vocabulary_Verb96

    @NBVR_Vocabulary_Verb96.setter
    def NBVR_Vocabulary_Verb96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Verb__NBVR_Vocabulary_Verb96", None)
        self.__NBVR_Vocabulary_Verb96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm97"):
                opp_val = getattr(old_value, "WordForm97", None)
                if opp_val == self:
                    setattr(old_value, "WordForm97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm97"):
                opp_val = getattr(value, "WordForm97", None)
                setattr(value, "WordForm97", self)

    @property
    def NBVR_Vocabulary_Verb102(self):
        return self.__NBVR_Vocabulary_Verb102

    @NBVR_Vocabulary_Verb102.setter
    def NBVR_Vocabulary_Verb102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Verb__NBVR_Vocabulary_Verb102", None)
        self.__NBVR_Vocabulary_Verb102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm103"):
                opp_val = getattr(old_value, "WordForm103", None)
                if opp_val == self:
                    setattr(old_value, "WordForm103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm103"):
                opp_val = getattr(value, "WordForm103", None)
                setattr(value, "WordForm103", self)

    @property
    def NBVR_Vocabulary_Verb105(self):
        return self.__NBVR_Vocabulary_Verb105

    @NBVR_Vocabulary_Verb105.setter
    def NBVR_Vocabulary_Verb105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Vocabulary_Verb__NBVR_Vocabulary_Verb105", None)
        self.__NBVR_Vocabulary_Verb105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordForm106"):
                opp_val = getattr(old_value, "WordForm106", None)
                if opp_val == self:
                    setattr(old_value, "WordForm106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordForm106"):
                opp_val = getattr(value, "WordForm106", None)
                setattr(value, "WordForm106", self)

    def isPerfective(self, NBVR_wf) :
        # TODO: Implement isPerfective method
        pass

    def isPast(self, NBVR_wf) :
        # TODO: Implement isPast method
        pass

    def isProgressive(self, NBVR_wf) :
        # TODO: Implement isProgressive method
        pass

class NBVR_Vocabulary_Keyword(Word):

    def __init__(self, kind: str, Word108: "NBVR_Vocabulary_Dictionary" = None, Word9: "NBVR_Vocabulary_WordForm" = None, Word: "NBVR_Vocabulary_Word" = None, Word200: "NBVR_Grammar_LocalName" = None, Word12: "NBVR_Vocabulary_WordForm" = None, Word186: "NBVR_Grammar_LexicalInstance" = None, Word18: "NBVR_Vocabulary_Term" = None):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class NBVR_Vocabulary_Adjective(Word):

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

    def __init__(self, kind: str, NBVR_Logic_Modal: "Proposition" = None, Proposition219: "NBVR_Logic_Proposition" = None, Proposition215: "NBVR_Logic_Quantification" = None, Proposition254: "NBVR_Logic_Negation" = None, Proposition: "NBVR_Logic_Variable" = None, Proposition260: "NBVR_Logic_NominalConstant" = None, Proposition245: "NBVR_Logic_Connection" = None, Proposition252: "NBVR_Logic_Modal" = None, Proposition247: "NBVR_Logic_Implication" = None, Proposition250: "NBVR_Logic_Implication" = None):
        self.kind = kind
        self.NBVR_Logic_Modal = NBVR_Logic_Modal
        
        pass
    @property
    def kind(self):
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
            if hasattr(old_value, "Proposition252"):
                opp_val = getattr(old_value, "Proposition252", None)
                if opp_val == self:
                    setattr(old_value, "Proposition252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Proposition252"):
                opp_val = getattr(value, "Proposition252", None)
                setattr(value, "Proposition252", self)

class NBVR_Logic_Connection(Proposition):

    def __init__(self, kind: str, NBVR_Logic_Connection: set["Proposition"] = None, Proposition219: "NBVR_Logic_Proposition" = None, Proposition215: "NBVR_Logic_Quantification" = None, Proposition254: "NBVR_Logic_Negation" = None, Proposition: "NBVR_Logic_Variable" = None, Proposition260: "NBVR_Logic_NominalConstant" = None, Proposition245: "NBVR_Logic_Connection" = None, Proposition252: "NBVR_Logic_Modal" = None, Proposition247: "NBVR_Logic_Implication" = None, Proposition250: "NBVR_Logic_Implication" = None):
        self.kind = kind
        self.NBVR_Logic_Connection = NBVR_Logic_Connection if NBVR_Logic_Connection is not None else set()
        
        pass
    @property
    def kind(self):
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
                if hasattr(item, "Proposition245"):
                    opp_val = getattr(item, "Proposition245", None)
                    
                    if opp_val == self:
                        setattr(item, "Proposition245", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Proposition245"):
                    opp_val = getattr(item, "Proposition245", None)
                    
                    setattr(item, "Proposition245", self)
                    

class NBVR_Logic_Quantification(Proposition):

    def __init__(self, kind: str, unique: bool, NBVR_Logic_Quantification: "Proposition" = None, source: "Variable" = None, Proposition219: "NBVR_Logic_Proposition" = None, Proposition215: "NBVR_Logic_Quantification" = None, Proposition254: "NBVR_Logic_Negation" = None, Proposition: "NBVR_Logic_Variable" = None, Proposition260: "NBVR_Logic_NominalConstant" = None, Proposition245: "NBVR_Logic_Connection" = None, Proposition252: "NBVR_Logic_Modal" = None, Proposition247: "NBVR_Logic_Implication" = None, Proposition250: "NBVR_Logic_Implication" = None):
        self.kind = kind
        self.unique = unique
        self.NBVR_Logic_Quantification = NBVR_Logic_Quantification
        self.source = source
        
        pass
    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Quantification__source", None)
        self.__source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable217"):
                opp_val = getattr(old_value, "Variable217", None)
                if opp_val == self:
                    setattr(old_value, "Variable217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable217"):
                opp_val = getattr(value, "Variable217", None)
                setattr(value, "Variable217", self)

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
            if hasattr(old_value, "Proposition215"):
                opp_val = getattr(old_value, "Proposition215", None)
                if opp_val == self:
                    setattr(old_value, "Proposition215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Proposition215"):
                opp_val = getattr(value, "Proposition215", None)
                setattr(value, "Proposition215", self)

class NBVR_Logic_Relation(Proposition):

    def __init__(self, relation: set["Argument"] = None, NBVR_Logic_Relation: "Predicate" = None, Proposition219: "NBVR_Logic_Proposition" = None, Proposition215: "NBVR_Logic_Quantification" = None, Proposition254: "NBVR_Logic_Negation" = None, Proposition: "NBVR_Logic_Variable" = None, Proposition260: "NBVR_Logic_NominalConstant" = None, Proposition245: "NBVR_Logic_Connection" = None, Proposition252: "NBVR_Logic_Modal" = None, Proposition247: "NBVR_Logic_Implication" = None, Proposition250: "NBVR_Logic_Implication" = None):
        self.relation = relation if relation is not None else set()
        self.NBVR_Logic_Relation = NBVR_Logic_Relation
        
        pass
    @property
    def relation(self):
        return self.__relation

    @relation.setter
    def relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Relation__relation", None)
        self.__relation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Argument"):
                    opp_val = getattr(item, "Argument", None)
                    
                    if opp_val == self:
                        setattr(item, "Argument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Argument"):
                    opp_val = getattr(item, "Argument", None)
                    
                    setattr(item, "Argument", self)
                    

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
            if hasattr(old_value, "Predicate222"):
                opp_val = getattr(old_value, "Predicate222", None)
                if opp_val == self:
                    setattr(old_value, "Predicate222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Predicate222"):
                opp_val = getattr(value, "Predicate222", None)
                setattr(value, "Predicate222", self)

    def getArgument(self) :
        # TODO: Implement getArgument method
        pass

class NBVR_Logic_Negation(Proposition):

    pass
class Quantification:

    pass
class NBVR_Logic_Variable:

    def __init__(self, name: str, variable: "Quantification" = None, NBVR_Logic_Variable: "Proposition" = None, NBVR_Logic_Variable208: set["Relation"] = None, NBVR_Logic_Variable210: "VocNoun" = None, variable213: "Set" = None):
        self.name = name
        self.variable = variable
        self.NBVR_Logic_Variable = NBVR_Logic_Variable
        self.NBVR_Logic_Variable208 = NBVR_Logic_Variable208 if NBVR_Logic_Variable208 is not None else set()
        self.NBVR_Logic_Variable210 = NBVR_Logic_Variable210
        self.variable213 = variable213
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def NBVR_Logic_Variable208(self):
        return self.__NBVR_Logic_Variable208

    @NBVR_Logic_Variable208.setter
    def NBVR_Logic_Variable208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Variable__NBVR_Logic_Variable208", None)
        self.__NBVR_Logic_Variable208 = value if value is not None else set()
        
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
    def variable213(self):
        return self.__variable213

    @variable213.setter
    def variable213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Variable__variable213", None)
        self.__variable213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Set"):
                opp_val = getattr(old_value, "Set", None)
                if opp_val == self:
                    setattr(old_value, "Set", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Set"):
                opp_val = getattr(value, "Set", None)
                setattr(value, "Set", self)

    @property
    def NBVR_Logic_Variable210(self):
        return self.__NBVR_Logic_Variable210

    @NBVR_Logic_Variable210.setter
    def NBVR_Logic_Variable210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Variable__NBVR_Logic_Variable210", None)
        self.__NBVR_Logic_Variable210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VocNoun211"):
                opp_val = getattr(old_value, "VocNoun211", None)
                if opp_val == self:
                    setattr(old_value, "VocNoun211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocNoun211"):
                opp_val = getattr(value, "VocNoun211", None)
                setattr(value, "VocNoun211", self)

    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Logic_Variable__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Quantification"):
                opp_val = getattr(old_value, "Quantification", None)
                if opp_val == self:
                    setattr(old_value, "Quantification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Quantification"):
                opp_val = getattr(value, "Quantification", None)
                setattr(value, "Quantification", self)

class LocalName:

    pass
class NBVR_Grammar_LocalName(SimpleNounPhrase):

    pass
class NBVR_Grammar_Parse:

    pass
class Keyword:

    pass
class Question:

    pass
class NBVR_Grammar_ParseElement(ABC):

    def __init__(self, NBVR_Grammar_ParseElement: "ParseElement" = None):
        self.NBVR_Grammar_ParseElement = NBVR_Grammar_ParseElement
        
        pass
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
            if hasattr(old_value, "ParseElement204"):
                opp_val = getattr(old_value, "ParseElement204", None)
                if opp_val == self:
                    setattr(old_value, "ParseElement204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ParseElement204"):
                opp_val = getattr(value, "ParseElement204", None)
                setattr(value, "ParseElement204", self)

    def isSentence(self) :
        # TODO: Implement isSentence method
        pass

    def isInstance(self) :
        # TODO: Implement isInstance method
        pass

    def getElementKind(self) :
        # TODO: Implement getElementKind method
        pass

    def isRolePhrase(self) :
        # TODO: Implement isRolePhrase method
        pass

class NBVR_Grammar_QueryPhrase(RolePhrase):

    def __init__(self, query: str, NBVR_Grammar_QueryPhrase: "RolePhrase" = None, queryPhrase: "Question" = None, RolePhrase230: "NBVR_Logic_Argument" = None, RolePhrase174: "NBVR_Grammar_SimpleForm" = None, RolePhrase196: "NBVR_Grammar_Intension" = None, RolePhrase: "NBVR_Grammar_RolePhrase" = None, RolePhrase149: "NBVR_Grammar_Modifier" = None, RolePhrase191: "NBVR_Grammar_QueryPhrase" = None, RolePhrase171: "NBVR_Grammar_SimpleForm" = None, RolePhrase162: "NBVR_Grammar_PartPhrase" = None, RolePhrase130: "NBVR_Grammar_Sentence" = None):
        self.query = query
        self.NBVR_Grammar_QueryPhrase = NBVR_Grammar_QueryPhrase
        self.queryPhrase = queryPhrase
        
        pass
    @property
    def query(self):
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query


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
            if hasattr(old_value, "RolePhrase191"):
                opp_val = getattr(old_value, "RolePhrase191", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase191"):
                opp_val = getattr(value, "RolePhrase191", None)
                setattr(value, "RolePhrase191", self)

    @property
    def queryPhrase(self):
        return self.__queryPhrase

    @queryPhrase.setter
    def queryPhrase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_QueryPhrase__queryPhrase", None)
        self.__queryPhrase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Question"):
                opp_val = getattr(old_value, "Question", None)
                if opp_val == self:
                    setattr(old_value, "Question", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Question"):
                opp_val = getattr(value, "Question", None)
                setattr(value, "Question", self)

class QueryPhrase:

    pass
class Nominalization:

    pass
class NBVR_Grammar_Question(Nominalization):

    def __init__(self, query: str, question: "QueryPhrase" = None):
        self.query = query
        self.question = question
        
        pass
    @property
    def query(self):
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query


    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Question__question", None)
        self.__question = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryPhrase"):
                opp_val = getattr(old_value, "QueryPhrase", None)
                if opp_val == self:
                    setattr(old_value, "QueryPhrase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryPhrase"):
                opp_val = getattr(value, "QueryPhrase", None)
                setattr(value, "QueryPhrase", self)

class NBVR_Grammar_Statement(Nominalization):

    pass
class PartPhrase:

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
        
        pass
    @property
    def modality(self):
        return self.__modality

    @modality.setter
    def modality(self, modality: str):
        self.__modality = modality


    @property
    def negated(self):
        return self.__negated

    @negated.setter
    def negated(self, negated: bool):
        self.__negated = negated


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
            if hasattr(old_value, "VocVerb160"):
                opp_val = getattr(old_value, "VocVerb160", None)
                if opp_val == self:
                    setattr(old_value, "VocVerb160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VocVerb160"):
                opp_val = getattr(value, "VocVerb160", None)
                setattr(value, "VocVerb160", self)

class NBVR_Grammar_RoleNoun(SimpleNounPhrase):

    pass
class TypeNoun:

    pass
class VocAdjective:

    pass
class NBVR_Grammar_Modifier(ParseElement):

    def __init__(self, kind: str, NBVR_Grammar_Modifier148: "RolePhrase" = None, NBVR_Grammar_Modifier: "VocAdjective" = None, ParseElement: "NBVR_Vocabulary_Formulation" = None, ParseElement204: "NBVR_Grammar_ParseElement" = None):
        self.kind = kind
        self.NBVR_Grammar_Modifier148 = NBVR_Grammar_Modifier148
        self.NBVR_Grammar_Modifier = NBVR_Grammar_Modifier
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def NBVR_Grammar_Modifier148(self):
        return self.__NBVR_Grammar_Modifier148

    @NBVR_Grammar_Modifier148.setter
    def NBVR_Grammar_Modifier148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Modifier__NBVR_Grammar_Modifier148", None)
        self.__NBVR_Grammar_Modifier148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RolePhrase149"):
                opp_val = getattr(old_value, "RolePhrase149", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase149"):
                opp_val = getattr(value, "RolePhrase149", None)
                setattr(value, "RolePhrase149", self)

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

class VocUnit:

    pass
class NBVR_Grammar_Dimension:

    def __init__(self, exponent: int, NBVR_Grammar_Dimension: "VocUnit" = None):
        self.exponent = exponent
        self.NBVR_Grammar_Dimension = NBVR_Grammar_Dimension
        
        pass
    @property
    def exponent(self):
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

class NBVR_Grammar_Instance(SimpleNounPhrase):

    def __init__(self, SimpleNounPhrase: "NBVR_Grammar_GroupPhrase" = None, SimpleNounPhrase154: "NBVR_Grammar_PropertyNoun" = None):
        
        pass
    def getKind(self) :
        # TODO: Implement getKind method
        pass

class Dimension:

    pass
class NumberWord:

    pass
class Instance:

    pass
class NBVR_Grammar_Nominalization(Instance):

    pass
class NBVR_Grammar_ProperName(Instance):

    pass
class NBVR_Grammar_Intension(Instance):

    pass
class NBVR_Grammar_LexicalInstance(Instance):

    pass
class NBVR_Grammar_Quantity(Instance):

    pass
class Quantity:

    pass
class NBVR_Grammar_Quantifier(ParseElement):

    def __init__(self, kind: str, count: int, NBVR_Grammar_Quantifier: "Quantity" = None, ParseElement: "NBVR_Vocabulary_Formulation" = None, ParseElement204: "NBVR_Grammar_ParseElement" = None):
        self.kind = kind
        self.count = count
        self.NBVR_Grammar_Quantifier = NBVR_Grammar_Quantifier
        
        pass
    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count


    @property
    def kind(self):
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

class Modifier:

    pass
class Quantifier:

    pass
class NBVR_Grammar_ModifiedTerm(SimpleNounPhrase):

    pass
class NBVR_Grammar_Qualifier(ParseElement):

    def __init__(self, ParseElement: "NBVR_Vocabulary_Formulation" = None, ParseElement204: "NBVR_Grammar_ParseElement" = None):
        
        pass
    def isSimple(self) :
        # TODO: Implement isSimple method
        pass

class Condition:

    pass
class QualifierChain:

    pass
class Qualifier:

    pass
class NBVR_Grammar_QualifierChain(Qualifier):

    pass
class NBVR_Grammar_SimpleQualifier(Qualifier):

    pass
class Sentence:

    pass
class NBVR_Grammar_ImplicationForm(Sentence):

    def __init__(self, kind: str, NBVR_Grammar_ImplicationForm181: "Sentence" = None, NBVR_Grammar_ImplicationForm: "Sentence" = None, NBVR_Grammar_ImplicationForm178: "Sentence" = None, Sentence133: "NBVR_Grammar_Sentence" = None, Sentence: "NBVR_Grammar_Condition" = None, Sentence198: "NBVR_Grammar_DomainForm" = None, Sentence179: "NBVR_Grammar_ImplicationForm" = None, Sentence125: "NBVR_Grammar_SimpleQualifier" = None, Sentence176: "NBVR_Grammar_ImplicationForm" = None, Sentence182: "NBVR_Grammar_ImplicationForm" = None, Sentence188: "NBVR_Grammar_Nominalization" = None, Sentence184: "NBVR_Grammar_CompoundForm" = None):
        self.kind = kind
        self.NBVR_Grammar_ImplicationForm181 = NBVR_Grammar_ImplicationForm181
        self.NBVR_Grammar_ImplicationForm = NBVR_Grammar_ImplicationForm
        self.NBVR_Grammar_ImplicationForm178 = NBVR_Grammar_ImplicationForm178
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def NBVR_Grammar_ImplicationForm181(self):
        return self.__NBVR_Grammar_ImplicationForm181

    @NBVR_Grammar_ImplicationForm181.setter
    def NBVR_Grammar_ImplicationForm181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_ImplicationForm__NBVR_Grammar_ImplicationForm181", None)
        self.__NBVR_Grammar_ImplicationForm181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sentence182"):
                opp_val = getattr(old_value, "Sentence182", None)
                if opp_val == self:
                    setattr(old_value, "Sentence182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sentence182"):
                opp_val = getattr(value, "Sentence182", None)
                setattr(value, "Sentence182", self)

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
            if hasattr(old_value, "Sentence176"):
                opp_val = getattr(old_value, "Sentence176", None)
                if opp_val == self:
                    setattr(old_value, "Sentence176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sentence176"):
                opp_val = getattr(value, "Sentence176", None)
                setattr(value, "Sentence176", self)

    @property
    def NBVR_Grammar_ImplicationForm178(self):
        return self.__NBVR_Grammar_ImplicationForm178

    @NBVR_Grammar_ImplicationForm178.setter
    def NBVR_Grammar_ImplicationForm178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_ImplicationForm__NBVR_Grammar_ImplicationForm178", None)
        self.__NBVR_Grammar_ImplicationForm178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sentence179"):
                opp_val = getattr(old_value, "Sentence179", None)
                if opp_val == self:
                    setattr(old_value, "Sentence179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sentence179"):
                opp_val = getattr(value, "Sentence179", None)
                setattr(value, "Sentence179", self)

class NBVR_Grammar_DomainForm(Sentence):

    def __init__(self, modality: str, NBVR_Grammar_DomainForm: "Sentence" = None, Sentence133: "NBVR_Grammar_Sentence" = None, Sentence: "NBVR_Grammar_Condition" = None, Sentence198: "NBVR_Grammar_DomainForm" = None, Sentence179: "NBVR_Grammar_ImplicationForm" = None, Sentence125: "NBVR_Grammar_SimpleQualifier" = None, Sentence176: "NBVR_Grammar_ImplicationForm" = None, Sentence182: "NBVR_Grammar_ImplicationForm" = None, Sentence188: "NBVR_Grammar_Nominalization" = None, Sentence184: "NBVR_Grammar_CompoundForm" = None):
        self.modality = modality
        self.NBVR_Grammar_DomainForm = NBVR_Grammar_DomainForm
        
        pass
    @property
    def modality(self):
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
            if hasattr(old_value, "Sentence198"):
                opp_val = getattr(old_value, "Sentence198", None)
                if opp_val == self:
                    setattr(old_value, "Sentence198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sentence198"):
                opp_val = getattr(value, "Sentence198", None)
                setattr(value, "Sentence198", self)

class NBVR_Grammar_SimpleForm(Sentence):

    def __init__(self, NBVR_Grammar_SimpleForm168: set["PartPhrase"] = None, NBVR_Grammar_SimpleForm170: "RolePhrase" = None, NBVR_Grammar_SimpleForm173: "RolePhrase" = None, NBVR_Grammar_SimpleForm: "VerbPhrase" = None, Sentence133: "NBVR_Grammar_Sentence" = None, Sentence: "NBVR_Grammar_Condition" = None, Sentence198: "NBVR_Grammar_DomainForm" = None, Sentence179: "NBVR_Grammar_ImplicationForm" = None, Sentence125: "NBVR_Grammar_SimpleQualifier" = None, Sentence176: "NBVR_Grammar_ImplicationForm" = None, Sentence182: "NBVR_Grammar_ImplicationForm" = None, Sentence188: "NBVR_Grammar_Nominalization" = None, Sentence184: "NBVR_Grammar_CompoundForm" = None):
        self.NBVR_Grammar_SimpleForm168 = NBVR_Grammar_SimpleForm168 if NBVR_Grammar_SimpleForm168 is not None else set()
        self.NBVR_Grammar_SimpleForm170 = NBVR_Grammar_SimpleForm170
        self.NBVR_Grammar_SimpleForm173 = NBVR_Grammar_SimpleForm173
        self.NBVR_Grammar_SimpleForm = NBVR_Grammar_SimpleForm
        
        pass
    @property
    def NBVR_Grammar_SimpleForm173(self):
        return self.__NBVR_Grammar_SimpleForm173

    @NBVR_Grammar_SimpleForm173.setter
    def NBVR_Grammar_SimpleForm173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_SimpleForm__NBVR_Grammar_SimpleForm173", None)
        self.__NBVR_Grammar_SimpleForm173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RolePhrase174"):
                opp_val = getattr(old_value, "RolePhrase174", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase174"):
                opp_val = getattr(value, "RolePhrase174", None)
                setattr(value, "RolePhrase174", self)

    @property
    def NBVR_Grammar_SimpleForm168(self):
        return self.__NBVR_Grammar_SimpleForm168

    @NBVR_Grammar_SimpleForm168.setter
    def NBVR_Grammar_SimpleForm168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_SimpleForm__NBVR_Grammar_SimpleForm168", None)
        self.__NBVR_Grammar_SimpleForm168 = value if value is not None else set()
        
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
                    

    @property
    def NBVR_Grammar_SimpleForm170(self):
        return self.__NBVR_Grammar_SimpleForm170

    @NBVR_Grammar_SimpleForm170.setter
    def NBVR_Grammar_SimpleForm170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_SimpleForm__NBVR_Grammar_SimpleForm170", None)
        self.__NBVR_Grammar_SimpleForm170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RolePhrase171"):
                opp_val = getattr(old_value, "RolePhrase171", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase171"):
                opp_val = getattr(value, "RolePhrase171", None)
                setattr(value, "RolePhrase171", self)

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

    def getModality(self) :
        # TODO: Implement getModality method
        pass

    def isNegated(self) :
        # TODO: Implement isNegated method
        pass

class NBVR_Grammar_CompoundForm(Sentence):

    def __init__(self, kind: str, NBVR_Grammar_CompoundForm: set["Sentence"] = None, Sentence133: "NBVR_Grammar_Sentence" = None, Sentence: "NBVR_Grammar_Condition" = None, Sentence198: "NBVR_Grammar_DomainForm" = None, Sentence179: "NBVR_Grammar_ImplicationForm" = None, Sentence125: "NBVR_Grammar_SimpleQualifier" = None, Sentence176: "NBVR_Grammar_ImplicationForm" = None, Sentence182: "NBVR_Grammar_ImplicationForm" = None, Sentence188: "NBVR_Grammar_Nominalization" = None, Sentence184: "NBVR_Grammar_CompoundForm" = None):
        self.kind = kind
        self.NBVR_Grammar_CompoundForm = NBVR_Grammar_CompoundForm if NBVR_Grammar_CompoundForm is not None else set()
        
        pass
    @property
    def kind(self):
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
                if hasattr(item, "Sentence184"):
                    opp_val = getattr(item, "Sentence184", None)
                    
                    if opp_val == self:
                        setattr(item, "Sentence184", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Sentence184"):
                    opp_val = getattr(item, "Sentence184", None)
                    
                    setattr(item, "Sentence184", self)
                    

class SimpleQualifier:

    pass
class NBVR_Grammar_Condition(ParseElement):

    def __init__(self, otherwise: bool, condition: "SimpleQualifier" = None, NBVR_Grammar_Condition: "Sentence" = None, ParseElement: "NBVR_Vocabulary_Formulation" = None, ParseElement204: "NBVR_Grammar_ParseElement" = None):
        self.otherwise = otherwise
        self.condition = condition
        self.NBVR_Grammar_Condition = NBVR_Grammar_Condition
        
        pass
    @property
    def otherwise(self):
        return self.__otherwise

    @otherwise.setter
    def otherwise(self, otherwise: bool):
        self.__otherwise = otherwise


    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Condition__condition", None)
        self.__condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleQualifier"):
                opp_val = getattr(old_value, "SimpleQualifier", None)
                if opp_val == self:
                    setattr(old_value, "SimpleQualifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleQualifier"):
                opp_val = getattr(value, "SimpleQualifier", None)
                setattr(value, "SimpleQualifier", self)

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

class ModifiedTerm:

    pass
class NBVR_Grammar_Pronoun(ModifiedTerm):

    pass
class NBVR_Grammar_PropertyNoun(ModifiedTerm):

    pass
class NBVR_Grammar_TypeNoun(ModifiedTerm):

    pass
class NBVR_Grammar_SimpleNounPhrase(RolePhrase):

    pass
class Variable:

    pass
class NBVR_Logic_RoleVariable(Variable):

    pass
class Grammar_ParseElement:

    pass
class Vocabulary_FormulationForm:

    pass
class NBVR_Grammar_Sentence(Vocabulary_FormulationForm, Grammar_ParseElement):

    def __init__(self, NBVR_Grammar_Sentence: "RolePhrase" = None, NBVR_Grammar_Sentence132: "Sentence" = None):
        self.NBVR_Grammar_Sentence = NBVR_Grammar_Sentence
        self.NBVR_Grammar_Sentence132 = NBVR_Grammar_Sentence132
        
        pass
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
            if hasattr(old_value, "RolePhrase130"):
                opp_val = getattr(old_value, "RolePhrase130", None)
                if opp_val == self:
                    setattr(old_value, "RolePhrase130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePhrase130"):
                opp_val = getattr(value, "RolePhrase130", None)
                setattr(value, "RolePhrase130", self)

    @property
    def NBVR_Grammar_Sentence132(self):
        return self.__NBVR_Grammar_Sentence132

    @NBVR_Grammar_Sentence132.setter
    def NBVR_Grammar_Sentence132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_Sentence__NBVR_Grammar_Sentence132", None)
        self.__NBVR_Grammar_Sentence132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sentence133"):
                opp_val = getattr(old_value, "Sentence133", None)
                if opp_val == self:
                    setattr(old_value, "Sentence133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sentence133"):
                opp_val = getattr(value, "Sentence133", None)
                setattr(value, "Sentence133", self)

    def getType(self) :
        # TODO: Implement getType method
        pass

class NBVR_Grammar_RolePhrase(Vocabulary_FormulationForm, Grammar_ParseElement):

    def __init__(self, NBVR_Grammar_RolePhrase: "VerbRole" = None, NBVR_Grammar_RolePhrase118: "Variable" = None, NBVR_Grammar_RolePhrase120: "RolePhrase" = None):
        self.NBVR_Grammar_RolePhrase = NBVR_Grammar_RolePhrase
        self.NBVR_Grammar_RolePhrase118 = NBVR_Grammar_RolePhrase118
        self.NBVR_Grammar_RolePhrase120 = NBVR_Grammar_RolePhrase120
        
        pass
    @property
    def NBVR_Grammar_RolePhrase118(self):
        return self.__NBVR_Grammar_RolePhrase118

    @NBVR_Grammar_RolePhrase118.setter
    def NBVR_Grammar_RolePhrase118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_RolePhrase__NBVR_Grammar_RolePhrase118", None)
        self.__NBVR_Grammar_RolePhrase118 = value
        
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
    def NBVR_Grammar_RolePhrase120(self):
        return self.__NBVR_Grammar_RolePhrase120

    @NBVR_Grammar_RolePhrase120.setter
    def NBVR_Grammar_RolePhrase120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NBVR_Grammar_RolePhrase__NBVR_Grammar_RolePhrase120", None)
        self.__NBVR_Grammar_RolePhrase120 = value
        
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
            if hasattr(old_value, "VerbRole116"):
                opp_val = getattr(old_value, "VerbRole116", None)
                if opp_val == self:
                    setattr(old_value, "VerbRole116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VerbRole116"):
                opp_val = getattr(value, "VerbRole116", None)
                setattr(value, "VerbRole116", self)

    def getType(self) :
        # TODO: Implement getType method
        pass
