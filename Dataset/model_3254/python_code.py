from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Fetch(Enum):
    eager = "eager"
    lazy = "lazy"
class ConstantNameList(Enum):
    DAO = "DAO"
    interface = "interface"
    base = "base"
    class = "class"
    impl = "impl"
    Controller = "Controller"
    Domain = "Domain"
    Persistence = "Persistence"
    Application = "Application"
    View = "View"
class FrameworkKindList(Enum):
    StandardSpecification = "StandardSpecification"
    FrameworkSpecification = "FrameworkSpecification"
    FrameworkImplementation = "FrameworkImplementation"
    Custom = "Custom"
class InheritanceMapping(Enum):
    singletable = "singletable"
    union = "union"
    join = "join"
class FrameworkCategoryList(Enum):
    FrontController = "FrontController"
    DependencyInjection = "DependencyInjection"
    ObjetoRelacional = "ObjetoRelacional"
class Collection(Enum):
    set = "set"
    bag = "bag"
    list = "list"
    map = "map"
class Cascade(Enum):
    remove = "remove"
    merge = "merge"
    refresh = "refresh"
    persist = "persist"
    none = "none"
    all = "all"
class DateTimePrecision(Enum):
    timestamp = "timestamp"
    time = "time"
    date = "date"
class Generation(Enum):
    auto = "auto"
    identity = "identity"
    sequence = "sequence"
    none = "none"
    table = "table"
class Order(Enum):
    natural = "natural"
    columnNameAsc = "columnNameAsc"
    columnNameDesc = "columnNameDesc"


############################################
# Definition of Classes
############################################

class frameweb_NewInterface115(ABC):

    pass
class LiteralString:

    pass
class frameweb_VocabularyLiteral(LiteralString):

    pass
class VocabularyClassExpression:

    pass
class Individual:

    pass
class frameweb_AnonymousIndividual(Individual):

    pass
class DataType:

    pass
class VocabularyAssociation:

    pass
class VocabularyEntity:

    pass
class frameweb_VocabularyDataType(VocabularyEntity, DataType):

    pass
class frameweb_AnnotationProperty(VocabularyAssociation, VocabularyEntity):

    pass
class frameweb_DataProperty(VocabularyAssociation, VocabularyEntity):

    pass
class frameweb_NamedIndividual(Individual, VocabularyEntity):

    pass
class frameweb_VocabularyClass(VocabularyClassExpression, VocabularyEntity):

    pass
class frameweb_ObjectProperty(VocabularyEntity, VocabularyAssociation):

    pass
class frameweb_Type:

    pass
class Relationship:

    pass
class Classifier:

    pass
class frameweb_VocabularyEntity(Classifier):

    pass
class frameweb_Association(Classifier, Relationship):

    def __init__(self, isDerived: str, Association: "frameweb_Property" = None, Association56: "frameweb_Property" = None, frameweb_Association: set["frameweb_Type"] = None, association: set["frameweb_Property"] = None, owningAssociation: set["frameweb_Property"] = None, frameweb_Association63: set["frameweb_Property"] = None):
        self.isDerived = isDerived
        self.Association = Association
        self.Association56 = Association56
        self.frameweb_Association = frameweb_Association if frameweb_Association is not None else set()
        self.association = association if association is not None else set()
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        self.frameweb_Association63 = frameweb_Association63 if frameweb_Association63 is not None else set()
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def frameweb_Association63(self):
        return self.__frameweb_Association63

    @frameweb_Association63.setter
    def frameweb_Association63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Association__frameweb_Association63", None)
        self.__frameweb_Association63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "frameweb_Property64"):
                    opp_val = getattr(item, "frameweb_Property64", None)
                    
                    if opp_val == self:
                        setattr(item, "frameweb_Property64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "frameweb_Property64"):
                    opp_val = getattr(item, "frameweb_Property64", None)
                    
                    setattr(item, "frameweb_Property64", self)
                    

    @property
    def frameweb_Association(self):
        return self.__frameweb_Association

    @frameweb_Association.setter
    def frameweb_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Association__frameweb_Association", None)
        self.__frameweb_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "frameweb_Type"):
                    opp_val = getattr(item, "frameweb_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "frameweb_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "frameweb_Type"):
                    opp_val = getattr(item, "frameweb_Type", None)
                    
                    setattr(item, "frameweb_Type", self)
                    

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Association__association", None)
        self.__association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property59"):
                    opp_val = getattr(item, "Property59", None)
                    
                    if opp_val == self:
                        setattr(item, "Property59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property59"):
                    opp_val = getattr(item, "Property59", None)
                    
                    setattr(item, "Property59", self)
                    

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Association__Association", None)
        self.__Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedEnd"):
                opp_val = getattr(old_value, "ownedEnd", None)
                if opp_val == self:
                    setattr(old_value, "ownedEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedEnd"):
                opp_val = getattr(value, "ownedEnd", None)
                setattr(value, "ownedEnd", self)

    @property
    def Association56(self):
        return self.__Association56

    @Association56.setter
    def Association56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Association__Association56", None)
        self.__Association56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "memberEnd"):
                opp_val = getattr(old_value, "memberEnd", None)
                if opp_val == self:
                    setattr(old_value, "memberEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "memberEnd"):
                opp_val = getattr(value, "memberEnd", None)
                setattr(value, "memberEnd", self)

    @property
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Association__owningAssociation", None)
        self.__owningAssociation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property61"):
                    opp_val = getattr(item, "Property61", None)
                    
                    if opp_val == self:
                        setattr(item, "Property61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property61"):
                    opp_val = getattr(item, "Property61", None)
                    
                    setattr(item, "Property61", self)
                    

    def binary_associations(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement binary_associations method
        pass

    def getEndTypes(self) -> str:
        # TODO: Implement getEndTypes method
        pass

    def association_ends(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement association_ends method
        pass

    def isBinary(self) -> str:
        # TODO: Implement isBinary method
        pass

    def ends_must_be_typed(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ends_must_be_typed method
        pass

    def specialized_end_number(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement specialized_end_number method
        pass

    def specialized_end_types(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement specialized_end_types method
        pass

class frameweb_Interface:

    pass
class frameweb_ValueSpecification:

    pass
class frameweb_Class:

    pass
class frameweb_DataType:

    pass
class DeploymentTarget:

    pass
class ConnectableElement:

    pass
class StructuralFeature:

    pass
class frameweb_Property(DeploymentTarget, StructuralFeature, ConnectableElement):

    def __init__(self, isComposite: str, isDerived: str, isDerivedUnion: str, isID: str, default: str, aggregation: str, frameweb_Property: "frameweb_DataType" = None, frameweb_Property42: "frameweb_Class" = None, frameweb_Property44: "frameweb_ValueSpecification" = None, frameweb_Property35: "frameweb_Interface" = None, Property: "frameweb_Property" = None, qualifier: "frameweb_Property" = None, Property40: "frameweb_Property" = None, associationEnd: set["frameweb_Property"] = None, frameweb_Property47: "frameweb_Property" = None, frameweb_Property45: "frameweb_Property" = None, ownedEnd: "frameweb_Association" = None, frameweb_Property51: "frameweb_Property" = None, frameweb_Property49: set["frameweb_Property"] = None, frameweb_Property54: "frameweb_Property" = None, frameweb_Property52: set["frameweb_Property"] = None, memberEnd: "frameweb_Association" = None, Property59: "frameweb_Association" = None, Property61: "frameweb_Association" = None, frameweb_Property64: "frameweb_Association" = None):
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.isID = isID
        self.default = default
        self.aggregation = aggregation
        self.frameweb_Property = frameweb_Property
        self.frameweb_Property42 = frameweb_Property42
        self.frameweb_Property44 = frameweb_Property44
        self.frameweb_Property35 = frameweb_Property35
        self.Property = Property
        self.qualifier = qualifier
        self.Property40 = Property40
        self.associationEnd = associationEnd if associationEnd is not None else set()
        self.frameweb_Property47 = frameweb_Property47
        self.frameweb_Property45 = frameweb_Property45
        self.ownedEnd = ownedEnd
        self.frameweb_Property51 = frameweb_Property51
        self.frameweb_Property49 = frameweb_Property49 if frameweb_Property49 is not None else set()
        self.frameweb_Property54 = frameweb_Property54
        self.frameweb_Property52 = frameweb_Property52 if frameweb_Property52 is not None else set()
        self.memberEnd = memberEnd
        self.Property59 = Property59
        self.Property61 = Property61
        self.frameweb_Property64 = frameweb_Property64
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def isID(self) -> str:
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isDerivedUnion(self) -> str:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: str):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__ownedEnd", None)
        self.__ownedEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

    @property
    def qualifier(self):
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__qualifier", None)
        self.__qualifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property"):
                opp_val = getattr(old_value, "Property", None)
                if opp_val == self:
                    setattr(old_value, "Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property"):
                opp_val = getattr(value, "Property", None)
                setattr(value, "Property", self)

    @property
    def frameweb_Property52(self):
        return self.__frameweb_Property52

    @frameweb_Property52.setter
    def frameweb_Property52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__frameweb_Property52", None)
        self.__frameweb_Property52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "frameweb_Property54"):
                    opp_val = getattr(item, "frameweb_Property54", None)
                    
                    if opp_val == self:
                        setattr(item, "frameweb_Property54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "frameweb_Property54"):
                    opp_val = getattr(item, "frameweb_Property54", None)
                    
                    setattr(item, "frameweb_Property54", self)
                    

    @property
    def frameweb_Property54(self):
        return self.__frameweb_Property54

    @frameweb_Property54.setter
    def frameweb_Property54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__frameweb_Property54", None)
        self.__frameweb_Property54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_Property52"):
                opp_val = getattr(old_value, "frameweb_Property52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_Property52"):
                opp_val = getattr(value, "frameweb_Property52", None)
                if opp_val is None:
                    setattr(value, "frameweb_Property52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def frameweb_Property44(self):
        return self.__frameweb_Property44

    @frameweb_Property44.setter
    def frameweb_Property44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__frameweb_Property44", None)
        self.__frameweb_Property44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_ValueSpecification"):
                opp_val = getattr(old_value, "frameweb_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_ValueSpecification"):
                opp_val = getattr(value, "frameweb_ValueSpecification", None)
                setattr(value, "frameweb_ValueSpecification", self)

    @property
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__memberEnd", None)
        self.__memberEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association56"):
                opp_val = getattr(old_value, "Association56", None)
                if opp_val == self:
                    setattr(old_value, "Association56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association56"):
                opp_val = getattr(value, "Association56", None)
                setattr(value, "Association56", self)

    @property
    def associationEnd(self):
        return self.__associationEnd

    @associationEnd.setter
    def associationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__associationEnd", None)
        self.__associationEnd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property40"):
                    opp_val = getattr(item, "Property40", None)
                    
                    if opp_val == self:
                        setattr(item, "Property40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property40"):
                    opp_val = getattr(item, "Property40", None)
                    
                    setattr(item, "Property40", self)
                    

    @property
    def frameweb_Property47(self):
        return self.__frameweb_Property47

    @frameweb_Property47.setter
    def frameweb_Property47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__frameweb_Property47", None)
        self.__frameweb_Property47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_Property45"):
                opp_val = getattr(old_value, "frameweb_Property45", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_Property45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_Property45"):
                opp_val = getattr(value, "frameweb_Property45", None)
                setattr(value, "frameweb_Property45", self)

    @property
    def Property40(self):
        return self.__Property40

    @Property40.setter
    def Property40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__Property40", None)
        self.__Property40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associationEnd"):
                opp_val = getattr(old_value, "associationEnd", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associationEnd"):
                opp_val = getattr(value, "associationEnd", None)
                if opp_val is None:
                    setattr(value, "associationEnd", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def frameweb_Property45(self):
        return self.__frameweb_Property45

    @frameweb_Property45.setter
    def frameweb_Property45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__frameweb_Property45", None)
        self.__frameweb_Property45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_Property47"):
                opp_val = getattr(old_value, "frameweb_Property47", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_Property47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_Property47"):
                opp_val = getattr(value, "frameweb_Property47", None)
                setattr(value, "frameweb_Property47", self)

    @property
    def frameweb_Property42(self):
        return self.__frameweb_Property42

    @frameweb_Property42.setter
    def frameweb_Property42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__frameweb_Property42", None)
        self.__frameweb_Property42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_Class"):
                opp_val = getattr(old_value, "frameweb_Class", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_Class"):
                opp_val = getattr(value, "frameweb_Class", None)
                setattr(value, "frameweb_Class", self)

    @property
    def frameweb_Property35(self):
        return self.__frameweb_Property35

    @frameweb_Property35.setter
    def frameweb_Property35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__frameweb_Property35", None)
        self.__frameweb_Property35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_Interface"):
                opp_val = getattr(old_value, "frameweb_Interface", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_Interface"):
                opp_val = getattr(value, "frameweb_Interface", None)
                setattr(value, "frameweb_Interface", self)

    @property
    def frameweb_Property51(self):
        return self.__frameweb_Property51

    @frameweb_Property51.setter
    def frameweb_Property51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__frameweb_Property51", None)
        self.__frameweb_Property51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_Property49"):
                opp_val = getattr(old_value, "frameweb_Property49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_Property49"):
                opp_val = getattr(value, "frameweb_Property49", None)
                if opp_val is None:
                    setattr(value, "frameweb_Property49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property59(self):
        return self.__Property59

    @Property59.setter
    def Property59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__Property59", None)
        self.__Property59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "association"):
                opp_val = getattr(old_value, "association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "association"):
                opp_val = getattr(value, "association", None)
                if opp_val is None:
                    setattr(value, "association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def frameweb_Property49(self):
        return self.__frameweb_Property49

    @frameweb_Property49.setter
    def frameweb_Property49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__frameweb_Property49", None)
        self.__frameweb_Property49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "frameweb_Property51"):
                    opp_val = getattr(item, "frameweb_Property51", None)
                    
                    if opp_val == self:
                        setattr(item, "frameweb_Property51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "frameweb_Property51"):
                    opp_val = getattr(item, "frameweb_Property51", None)
                    
                    setattr(item, "frameweb_Property51", self)
                    

    @property
    def frameweb_Property(self):
        return self.__frameweb_Property

    @frameweb_Property.setter
    def frameweb_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__frameweb_Property", None)
        self.__frameweb_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_DataType"):
                opp_val = getattr(old_value, "frameweb_DataType", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_DataType"):
                opp_val = getattr(value, "frameweb_DataType", None)
                setattr(value, "frameweb_DataType", self)

    @property
    def frameweb_Property64(self):
        return self.__frameweb_Property64

    @frameweb_Property64.setter
    def frameweb_Property64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__frameweb_Property64", None)
        self.__frameweb_Property64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_Association63"):
                opp_val = getattr(old_value, "frameweb_Association63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_Association63"):
                opp_val = getattr(value, "frameweb_Association63", None)
                if opp_val is None:
                    setattr(value, "frameweb_Association63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualifier"):
                opp_val = getattr(old_value, "qualifier", None)
                if opp_val == self:
                    setattr(old_value, "qualifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualifier"):
                opp_val = getattr(value, "qualifier", None)
                setattr(value, "qualifier", self)

    @property
    def Property61(self):
        return self.__Property61

    @Property61.setter
    def Property61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Property__Property61", None)
        self.__Property61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningAssociation"):
                opp_val = getattr(old_value, "owningAssociation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningAssociation"):
                opp_val = getattr(value, "owningAssociation", None)
                if opp_val is None:
                    setattr(value, "owningAssociation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def derived_union_is_derived(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement derived_union_is_derived method
        pass

    def subsetting_context_conforms(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement subsetting_context_conforms method
        pass

    def getOpposite(self) -> Property:
        # TODO: Implement getOpposite method
        pass

    def isAttribute(self) -> str:
        # TODO: Implement isAttribute method
        pass

    def subsettingContext(self) -> str:
        # TODO: Implement subsettingContext method
        pass

    def isSetDefault(self) -> str:
        # TODO: Implement isSetDefault method
        pass

    def setNullDefaultValue(self):
        # TODO: Implement setNullDefaultValue method
        pass

    def isComposite(self) -> str:
        # TODO: Implement isComposite method
        pass

    def subsetting_rules(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement subsetting_rules method
        pass

    def setIsComposite(self, newIsComposite: str):
        # TODO: Implement setIsComposite method
        pass

    def setOpposite(self, newOpposite: Property):
        # TODO: Implement setOpposite method
        pass

    def deployment_target(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement deployment_target method
        pass

    def qualified_is_association_end(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement qualified_is_association_end method
        pass

    def derived_union_is_read_only(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement derived_union_is_read_only method
        pass

    def getDefault(self) -> str:
        # TODO: Implement getDefault method
        pass

    def setUnlimitedNaturalDefaultValue(self, value: str):
        # TODO: Implement setUnlimitedNaturalDefaultValue method
        pass

    def setBooleanDefaultValue(self, value: str):
        # TODO: Implement setBooleanDefaultValue method
        pass

    def setStringDefaultValue(self, value: str):
        # TODO: Implement setStringDefaultValue method
        pass

    def isNavigable(self) -> str:
        # TODO: Implement isNavigable method
        pass

    def setIsNavigable(self, isNavigable: str):
        # TODO: Implement setIsNavigable method
        pass

    def setRealDefaultValue(self, value: str):
        # TODO: Implement setRealDefaultValue method
        pass

    def type_of_opposite_end(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement type_of_opposite_end method
        pass

    def setIntegerDefaultValue(self, value: str):
        # TODO: Implement setIntegerDefaultValue method
        pass

    def binding_to_attribute(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement binding_to_attribute method
        pass

    def setDefault(self, newDefault: str):
        # TODO: Implement setDefault method
        pass

    def subsetted_property_names(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement subsetted_property_names method
        pass

    def getOtherEnd(self) -> Property:
        # TODO: Implement getOtherEnd method
        pass

    def redefined_property_inherited(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement redefined_property_inherited method
        pass

    def unsetDefault(self):
        # TODO: Implement unsetDefault method
        pass

    def multiplicity_of_composite(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement multiplicity_of_composite method
        pass

class FrameworkExtension:

    pass
class frameweb_DomainExtension(FrameworkExtension):

    pass
class frameweb_NavigationExtension(FrameworkExtension):

    pass
class ExtensionEnd:

    pass
class frameweb_ResultExtensionEnd(ExtensionEnd):

    pass
class frameweb_AttributeMappingExtensionEnd(ExtensionEnd):

    pass
class frameweb_ClassMappingExtensionEnd(ExtensionEnd):

    pass
class frameweb_TagExtensionEnd(ExtensionEnd):

    pass
class frameweb_ControllerExtensionEnd(ExtensionEnd):

    pass
class DomainExtension:

    pass
class frameweb_AttributeMappingExtension(DomainExtension):

    pass
class frameweb_ClassMappingExtension(DomainExtension):

    pass
class NavigationConstraint:

    pass
class Constraint:

    pass
class frameweb_VocabularyConstraints(Constraint):

    pass
class frameweb_NavigationConstraint(Constraint):

    pass
class NavigationProperty:

    pass
class frameweb_NavigationCompositionWhole(NavigationProperty):

    pass
class frameweb_NavigationCompositionPart(NavigationProperty):

    pass
class Stereotype:

    pass
class frameweb_Tag(Stereotype):

    pass
class frameweb_ResultType(Stereotype):

    pass
class frameweb_Controller(Stereotype):

    pass
class ProfileApplication:

    pass
class frameweb_FrameworkApplication(ProfileApplication):

    pass
class NavigationExtension:

    pass
class frameweb_ResultExtension(NavigationExtension):

    pass
class frameweb_ControllerExtension(NavigationExtension):

    pass
class frameweb_TagExtension(NavigationExtension):

    pass
class Extension:

    pass
class frameweb_FrameworkExtension(Extension):

    pass
class GeneralizationSet:

    pass
class frameweb_NavigationGeneralizationSet(GeneralizationSet):

    pass
class frameweb_ServiceGeneralizationSet(GeneralizationSet):

    pass
class frameweb_DAOGeneralizationSet(GeneralizationSet):

    pass
class frameweb_DomainGeneralizationSet(GeneralizationSet):

    def __init__(self, mapping: str):
        self.mapping = mapping
        
    @property
    def mapping(self) -> str:
        return self.__mapping

    @mapping.setter
    def mapping(self, mapping: str):
        self.__mapping = mapping

class frameweb_AttributeMapping(Stereotype):

    pass
class frameweb_ClassMapping(Stereotype):

    pass
class frameweb_DomainConstraints(Constraint):

    pass
class frameweb_ChainingConstraint(NavigationConstraint):

    pass
class frameweb_PageConstraint(NavigationConstraint):

    pass
class frameweb_MethodCosntraint(NavigationConstraint):

    pass
class NavigationPackage:

    pass
class frameweb_ControllerPackage(NavigationPackage):

    pass
class frameweb_ViewPackage(NavigationPackage):

    pass
class Package:

    pass
class frameweb_SemanticPackage(Package):

    pass
class frameweb_MappingLib(Package):

    pass
class frameweb_ControllerSet(Package):

    pass
class frameweb_ApplicationPackage(Package):

    pass
class frameweb_Vocabulary(Package):

    def __init__(self, vocabularyDocument: str, frameweb_Vocabulary: set["frameweb_IRI"] = None, frameweb_Vocabulary27: "frameweb_IRI" = None, frameweb_Vocabulary30: set["frameweb_Axiom"] = None, frameweb_Vocabulary32: set["frameweb_Annotation"] = None):
        self.vocabularyDocument = vocabularyDocument
        self.frameweb_Vocabulary = frameweb_Vocabulary if frameweb_Vocabulary is not None else set()
        self.frameweb_Vocabulary27 = frameweb_Vocabulary27
        self.frameweb_Vocabulary30 = frameweb_Vocabulary30 if frameweb_Vocabulary30 is not None else set()
        self.frameweb_Vocabulary32 = frameweb_Vocabulary32 if frameweb_Vocabulary32 is not None else set()
        
    @property
    def vocabularyDocument(self) -> str:
        return self.__vocabularyDocument

    @vocabularyDocument.setter
    def vocabularyDocument(self, vocabularyDocument: str):
        self.__vocabularyDocument = vocabularyDocument

    @property
    def frameweb_Vocabulary(self):
        return self.__frameweb_Vocabulary

    @frameweb_Vocabulary.setter
    def frameweb_Vocabulary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Vocabulary__frameweb_Vocabulary", None)
        self.__frameweb_Vocabulary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "frameweb_IRI"):
                    opp_val = getattr(item, "frameweb_IRI", None)
                    
                    if opp_val == self:
                        setattr(item, "frameweb_IRI", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "frameweb_IRI"):
                    opp_val = getattr(item, "frameweb_IRI", None)
                    
                    setattr(item, "frameweb_IRI", self)
                    

    @property
    def frameweb_Vocabulary32(self):
        return self.__frameweb_Vocabulary32

    @frameweb_Vocabulary32.setter
    def frameweb_Vocabulary32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Vocabulary__frameweb_Vocabulary32", None)
        self.__frameweb_Vocabulary32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "frameweb_Annotation"):
                    opp_val = getattr(item, "frameweb_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "frameweb_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "frameweb_Annotation"):
                    opp_val = getattr(item, "frameweb_Annotation", None)
                    
                    setattr(item, "frameweb_Annotation", self)
                    

    @property
    def frameweb_Vocabulary30(self):
        return self.__frameweb_Vocabulary30

    @frameweb_Vocabulary30.setter
    def frameweb_Vocabulary30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Vocabulary__frameweb_Vocabulary30", None)
        self.__frameweb_Vocabulary30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "frameweb_Axiom"):
                    opp_val = getattr(item, "frameweb_Axiom", None)
                    
                    if opp_val == self:
                        setattr(item, "frameweb_Axiom", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "frameweb_Axiom"):
                    opp_val = getattr(item, "frameweb_Axiom", None)
                    
                    setattr(item, "frameweb_Axiom", self)
                    

    @property
    def frameweb_Vocabulary27(self):
        return self.__frameweb_Vocabulary27

    @frameweb_Vocabulary27.setter
    def frameweb_Vocabulary27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_Vocabulary__frameweb_Vocabulary27", None)
        self.__frameweb_Vocabulary27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_IRI28"):
                opp_val = getattr(old_value, "frameweb_IRI28", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_IRI28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_IRI28"):
                opp_val = getattr(value, "frameweb_IRI28", None)
                setattr(value, "frameweb_IRI28", self)

class frameweb_ResultSet(Package):

    pass
class frameweb_NavigationPackage(Package):

    pass
class frameweb_PersistencePackage(Package):

    pass
class frameweb_DomainPackage(Package):

    pass
class Dependency:

    pass
class frameweb_NavigationDependency(Dependency):

    pass
class frameweb_ResultConstraint(NavigationConstraint):

    pass
class NavigationDependency:

    pass
class frameweb_ChainingDependency(NavigationDependency):

    pass
class frameweb_FrontControllerDependency(NavigationDependency):

    pass
class frameweb_PageDependency(NavigationDependency):

    pass
class frameweb_ResultDependency(NavigationDependency):

    def __init__(self, render: str, execute: str, ajax: bool, frameweb_ResultDependency: set["frameweb_Result"] = None, frameweb_ResultDependency9: "frameweb_FrontControllerMethod" = None, frameweb_ResultDependency11: "frameweb_ResultConstraint" = None):
        self.render = render
        self.execute = execute
        self.ajax = ajax
        self.frameweb_ResultDependency = frameweb_ResultDependency if frameweb_ResultDependency is not None else set()
        self.frameweb_ResultDependency9 = frameweb_ResultDependency9
        self.frameweb_ResultDependency11 = frameweb_ResultDependency11
        
    @property
    def ajax(self) -> bool:
        return self.__ajax

    @ajax.setter
    def ajax(self, ajax: bool):
        self.__ajax = ajax

    @property
    def execute(self) -> str:
        return self.__execute

    @execute.setter
    def execute(self, execute: str):
        self.__execute = execute

    @property
    def render(self) -> str:
        return self.__render

    @render.setter
    def render(self, render: str):
        self.__render = render

    @property
    def frameweb_ResultDependency(self):
        return self.__frameweb_ResultDependency

    @frameweb_ResultDependency.setter
    def frameweb_ResultDependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_ResultDependency__frameweb_ResultDependency", None)
        self.__frameweb_ResultDependency = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "frameweb_Result"):
                    opp_val = getattr(item, "frameweb_Result", None)
                    
                    if opp_val == self:
                        setattr(item, "frameweb_Result", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "frameweb_Result"):
                    opp_val = getattr(item, "frameweb_Result", None)
                    
                    setattr(item, "frameweb_Result", self)
                    

    @property
    def frameweb_ResultDependency9(self):
        return self.__frameweb_ResultDependency9

    @frameweb_ResultDependency9.setter
    def frameweb_ResultDependency9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_ResultDependency__frameweb_ResultDependency9", None)
        self.__frameweb_ResultDependency9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_FrontControllerMethod"):
                opp_val = getattr(old_value, "frameweb_FrontControllerMethod", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_FrontControllerMethod", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_FrontControllerMethod"):
                opp_val = getattr(value, "frameweb_FrontControllerMethod", None)
                setattr(value, "frameweb_FrontControllerMethod", self)

    @property
    def frameweb_ResultDependency11(self):
        return self.__frameweb_ResultDependency11

    @frameweb_ResultDependency11.setter
    def frameweb_ResultDependency11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_ResultDependency__frameweb_ResultDependency11", None)
        self.__frameweb_ResultDependency11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_ResultConstraint"):
                opp_val = getattr(old_value, "frameweb_ResultConstraint", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_ResultConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_ResultConstraint"):
                opp_val = getattr(value, "frameweb_ResultConstraint", None)
                setattr(value, "frameweb_ResultConstraint", self)

class NavigationAttribute:

    pass
class frameweb_UIComponentField(NavigationAttribute):

    pass
class frameweb_IOParameter(NavigationAttribute):

    pass
class InterfaceRealization:

    pass
class frameweb_SeviceRealization(InterfaceRealization):

    pass
class frameweb_DAORealization(InterfaceRealization):

    pass
class ServiceAssociation:

    pass
class frameweb_DAOServiceAssociation(ServiceAssociation):

    pass
class frameweb_ServiceControllerAssociation(ServiceAssociation):

    pass
class Generalization:

    pass
class frameweb_NavigationGeneralization(Generalization):

    pass
class frameweb_DomainGeneralization(Generalization):

    pass
class frameweb_DAOGeneralization(Generalization):

    pass
class frameweb_ServiceGeneralization(Generalization):

    pass
class Operation:

    pass
class frameweb_ServiceMethod(Operation):

    pass
class frameweb_DomainMethod(Operation):

    pass
class frameweb_DAOMethod(Operation):

    pass
class frameweb_FrontControllerMethod(Operation):

    def __init__(self, isDefault: bool, frameweb_FrontControllerMethod: "frameweb_ResultDependency" = None, frameweb_FrontControllerMethod13: "frameweb_FrontControllerDependency" = None, frameweb_FrontControllerMethod18: "frameweb_ChainingDependency" = None, frameweb_FrontControllerMethod21: "frameweb_ChainingDependency" = None):
        self.isDefault = isDefault
        self.frameweb_FrontControllerMethod = frameweb_FrontControllerMethod
        self.frameweb_FrontControllerMethod13 = frameweb_FrontControllerMethod13
        self.frameweb_FrontControllerMethod18 = frameweb_FrontControllerMethod18
        self.frameweb_FrontControllerMethod21 = frameweb_FrontControllerMethod21
        
    @property
    def isDefault(self) -> bool:
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: bool):
        self.__isDefault = isDefault

    @property
    def frameweb_FrontControllerMethod21(self):
        return self.__frameweb_FrontControllerMethod21

    @frameweb_FrontControllerMethod21.setter
    def frameweb_FrontControllerMethod21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_FrontControllerMethod__frameweb_FrontControllerMethod21", None)
        self.__frameweb_FrontControllerMethod21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_ChainingDependency20"):
                opp_val = getattr(old_value, "frameweb_ChainingDependency20", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_ChainingDependency20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_ChainingDependency20"):
                opp_val = getattr(value, "frameweb_ChainingDependency20", None)
                setattr(value, "frameweb_ChainingDependency20", self)

    @property
    def frameweb_FrontControllerMethod18(self):
        return self.__frameweb_FrontControllerMethod18

    @frameweb_FrontControllerMethod18.setter
    def frameweb_FrontControllerMethod18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_FrontControllerMethod__frameweb_FrontControllerMethod18", None)
        self.__frameweb_FrontControllerMethod18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_ChainingDependency"):
                opp_val = getattr(old_value, "frameweb_ChainingDependency", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_ChainingDependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_ChainingDependency"):
                opp_val = getattr(value, "frameweb_ChainingDependency", None)
                setattr(value, "frameweb_ChainingDependency", self)

    @property
    def frameweb_FrontControllerMethod(self):
        return self.__frameweb_FrontControllerMethod

    @frameweb_FrontControllerMethod.setter
    def frameweb_FrontControllerMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_FrontControllerMethod__frameweb_FrontControllerMethod", None)
        self.__frameweb_FrontControllerMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_ResultDependency9"):
                opp_val = getattr(old_value, "frameweb_ResultDependency9", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_ResultDependency9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_ResultDependency9"):
                opp_val = getattr(value, "frameweb_ResultDependency9", None)
                setattr(value, "frameweb_ResultDependency9", self)

    @property
    def frameweb_FrontControllerMethod13(self):
        return self.__frameweb_FrontControllerMethod13

    @frameweb_FrontControllerMethod13.setter
    def frameweb_FrontControllerMethod13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_FrontControllerMethod__frameweb_FrontControllerMethod13", None)
        self.__frameweb_FrontControllerMethod13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_FrontControllerDependency"):
                opp_val = getattr(old_value, "frameweb_FrontControllerDependency", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_FrontControllerDependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_FrontControllerDependency"):
                opp_val = getattr(value, "frameweb_FrontControllerDependency", None)
                setattr(value, "frameweb_FrontControllerDependency", self)

class Class:

    pass
class frameweb_NavigationClass(Class):

    pass
class frameweb_Result(Class):

    pass
class frameweb_FrontControllerClass(Class):

    pass
class frameweb_ServiceClass(Class):

    pass
class frameweb_DomainClass(Class):

    def __init__(self, table: str):
        self.table = table
        
    @property
    def table(self) -> str:
        return self.__table

    @table.setter
    def table(self, table: str):
        self.__table = table

class frameweb_VocabularyClassExpression(Class):

    pass
class frameweb_Annotation(Class):

    pass
class frameweb_Axiom(Class):

    pass
class frameweb_DAOClass(Class):

    def __init__(self, sufix: str, infix: str, prefix: str):
        self.sufix = sufix
        self.infix = infix
        self.prefix = prefix
        
    @property
    def sufix(self) -> str:
        return self.__sufix

    @sufix.setter
    def sufix(self, sufix: str):
        self.__sufix = sufix

    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def infix(self) -> str:
        return self.__infix

    @infix.setter
    def infix(self, infix: str):
        self.__infix = infix

class Interface:

    pass
class frameweb_ServiceInterface(Interface):

    pass
class frameweb_DAOInterface(Interface):

    def __init__(self, infix: str, sufix: str):
        self.infix = infix
        self.sufix = sufix
        
    @property
    def sufix(self) -> str:
        return self.__sufix

    @sufix.setter
    def sufix(self, sufix: str):
        self.__sufix = sufix

    @property
    def infix(self) -> str:
        return self.__infix

    @infix.setter
    def infix(self, infix: str):
        self.__infix = infix

class frameweb_TagLib(Package):

    def __init__(self, prefix: str, frameweb_TagLib: "frameweb_Page" = None, frameweb_TagLib5: "frameweb_Template" = None):
        self.prefix = prefix
        self.frameweb_TagLib = frameweb_TagLib
        self.frameweb_TagLib5 = frameweb_TagLib5
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def frameweb_TagLib5(self):
        return self.__frameweb_TagLib5

    @frameweb_TagLib5.setter
    def frameweb_TagLib5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_TagLib__frameweb_TagLib5", None)
        self.__frameweb_TagLib5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_Template"):
                opp_val = getattr(old_value, "frameweb_Template", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_Template"):
                opp_val = getattr(value, "frameweb_Template", None)
                if opp_val is None:
                    setattr(value, "frameweb_Template", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def frameweb_TagLib(self):
        return self.__frameweb_TagLib

    @frameweb_TagLib.setter
    def frameweb_TagLib(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_TagLib__frameweb_TagLib", None)
        self.__frameweb_TagLib = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_Page"):
                opp_val = getattr(old_value, "frameweb_Page", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_Page"):
                opp_val = getattr(value, "frameweb_Page", None)
                if opp_val is None:
                    setattr(value, "frameweb_Page", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NavigationClass:

    pass
class frameweb_UIComponent(NavigationClass):

    pass
class frameweb_Template(NavigationClass):

    pass
class frameweb_Page(NavigationClass):

    pass
class FramewebModel:

    pass
class frameweb_VocabularyModel(FramewebModel):

    pass
class frameweb_EntityModel(FramewebModel):

    pass
class Profile:

    pass
class Model:

    pass
class frameweb_FrameworkProfile(Profile):

    def __init__(self, category: str, kind: str, frameweb_FrameworkProfile: "frameweb_FramewebProject" = None):
        self.category = category
        self.kind = kind
        self.frameweb_FrameworkProfile = frameweb_FrameworkProfile
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def frameweb_FrameworkProfile(self):
        return self.__frameweb_FrameworkProfile

    @frameweb_FrameworkProfile.setter
    def frameweb_FrameworkProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_FrameworkProfile__frameweb_FrameworkProfile", None)
        self.__frameweb_FrameworkProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_FramewebProject2"):
                opp_val = getattr(old_value, "frameweb_FramewebProject2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_FramewebProject2"):
                opp_val = getattr(value, "frameweb_FramewebProject2", None)
                if opp_val is None:
                    setattr(value, "frameweb_FramewebProject2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class frameweb_FramewebModel(Model):

    pass
class frameweb_FramewebProject:

    pass
class DomainAttribute:

    pass
class frameweb_LOBAttribute(DomainAttribute):

    pass
class frameweb_DecimalAttribute(DomainAttribute):

    def __init__(self, decimalPrecision: str, decimalScale: str):
        self.decimalPrecision = decimalPrecision
        self.decimalScale = decimalScale
        
    @property
    def decimalScale(self) -> str:
        return self.__decimalScale

    @decimalScale.setter
    def decimalScale(self, decimalScale: str):
        self.__decimalScale = decimalScale

    @property
    def decimalPrecision(self) -> str:
        return self.__decimalPrecision

    @decimalPrecision.setter
    def decimalPrecision(self, decimalPrecision: str):
        self.__decimalPrecision = decimalPrecision

class frameweb_EmbeddedAttribute(DomainAttribute):

    pass
class frameweb_DateTimeAttribute(DomainAttribute):

    def __init__(self, dateTimePrecision: str):
        self.dateTimePrecision = dateTimePrecision
        
    @property
    def dateTimePrecision(self) -> str:
        return self.__dateTimePrecision

    @dateTimePrecision.setter
    def dateTimePrecision(self, dateTimePrecision: str):
        self.__dateTimePrecision = dateTimePrecision

class frameweb_IdAttribute(DomainAttribute):

    def __init__(self, generation: str):
        self.generation = generation
        
    @property
    def generation(self) -> str:
        return self.__generation

    @generation.setter
    def generation(self, generation: str):
        self.__generation = generation

class frameweb_VersionAttribute(DomainAttribute):

    pass
class Property:

    pass
class frameweb_NavigationAttribute(Property):

    pass
class frameweb_ServiceAttribute(Property):

    pass
class frameweb_IRI(Property):

    def __init__(self, iri: str, iriVersion: str, frameweb_IRI: "frameweb_Vocabulary" = None, frameweb_IRI28: "frameweb_Vocabulary" = None, frameweb_IRI66: "frameweb_VocabularyEntity" = None):
        self.iri = iri
        self.iriVersion = iriVersion
        self.frameweb_IRI = frameweb_IRI
        self.frameweb_IRI28 = frameweb_IRI28
        self.frameweb_IRI66 = frameweb_IRI66
        
    @property
    def iriVersion(self) -> str:
        return self.__iriVersion

    @iriVersion.setter
    def iriVersion(self, iriVersion: str):
        self.__iriVersion = iriVersion

    @property
    def iri(self) -> str:
        return self.__iri

    @iri.setter
    def iri(self, iri: str):
        self.__iri = iri

    @property
    def frameweb_IRI66(self):
        return self.__frameweb_IRI66

    @frameweb_IRI66.setter
    def frameweb_IRI66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_IRI__frameweb_IRI66", None)
        self.__frameweb_IRI66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_VocabularyEntity"):
                opp_val = getattr(old_value, "frameweb_VocabularyEntity", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_VocabularyEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_VocabularyEntity"):
                opp_val = getattr(value, "frameweb_VocabularyEntity", None)
                setattr(value, "frameweb_VocabularyEntity", self)

    @property
    def frameweb_IRI28(self):
        return self.__frameweb_IRI28

    @frameweb_IRI28.setter
    def frameweb_IRI28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_IRI__frameweb_IRI28", None)
        self.__frameweb_IRI28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_Vocabulary27"):
                opp_val = getattr(old_value, "frameweb_Vocabulary27", None)
                if opp_val == self:
                    setattr(old_value, "frameweb_Vocabulary27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_Vocabulary27"):
                opp_val = getattr(value, "frameweb_Vocabulary27", None)
                setattr(value, "frameweb_Vocabulary27", self)

    @property
    def frameweb_IRI(self):
        return self.__frameweb_IRI

    @frameweb_IRI.setter
    def frameweb_IRI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_frameweb_IRI__frameweb_IRI", None)
        self.__frameweb_IRI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "frameweb_Vocabulary"):
                opp_val = getattr(old_value, "frameweb_Vocabulary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "frameweb_Vocabulary"):
                opp_val = getattr(value, "frameweb_Vocabulary", None)
                if opp_val is None:
                    setattr(value, "frameweb_Vocabulary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class frameweb_ClassMappingPropery(Property):

    pass
class frameweb_Individual(Property):

    pass
class frameweb_NavigationProperty(Property):

    pass
class frameweb_ResultProperty(Property):

    pass
class frameweb_ControllerProperty(Property):

    pass
class frameweb_DAOAttribute(Property):

    pass
class frameweb_TagProperty(Property):

    pass
class frameweb_AttributeMappingProperty(Property):

    pass
class frameweb_VocabularyProperty(Property):

    pass
class frameweb_DomainProperty(Property):

    pass
class frameweb_DomainAttribute(Property):

    def __init__(self, size: str, isNull: bool, isPersistent: bool):
        self.size = size
        self.isNull = isNull
        self.isPersistent = isPersistent
        
    @property
    def isPersistent(self) -> bool:
        return self.__isPersistent

    @isPersistent.setter
    def isPersistent(self, isPersistent: bool):
        self.__isPersistent = isPersistent

    @property
    def isNull(self) -> bool:
        return self.__isNull

    @isNull.setter
    def isNull(self, isNull: bool):
        self.__isNull = isNull

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

class Association:

    pass
class frameweb_VocabularyAssociation(Association):

    pass
class frameweb_ServiceAssociation(Association):

    pass
class frameweb_NavigationAssociation(Association):

    pass
class frameweb_DomainAssociation(Association):

    def __init__(self, collection: str, cascade: str, fetch: str, order: str):
        self.collection = collection
        self.cascade = cascade
        self.fetch = fetch
        self.order = order
        
    @property
    def fetch(self) -> str:
        return self.__fetch

    @fetch.setter
    def fetch(self, fetch: str):
        self.__fetch = fetch

    @property
    def cascade(self) -> str:
        return self.__cascade

    @cascade.setter
    def cascade(self, cascade: str):
        self.__cascade = cascade

    @property
    def order(self) -> str:
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order

    @property
    def collection(self) -> str:
        return self.__collection

    @collection.setter
    def collection(self, collection: str):
        self.__collection = collection

class frameweb_PersistenceModel(FramewebModel):

    pass
class frameweb_ApplicationModel(FramewebModel):

    pass
class frameweb_NavigationModel(FramewebModel):

    pass