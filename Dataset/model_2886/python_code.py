from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Feature:

    pass
class Relation:

    pass
class metamodel_ManyToMany(Relation):

    pass
class metamodel_OneToMany(Relation):

    pass
class metamodel_OneToOne(Relation):

    pass
class metamodel_Feature:

    def __init__(self, name: str, nullable: bool, xmltransient: bool, metamodel_Feature15: "metamodel_Type" = None, metamodel_Feature: "metamodel_Entity" = None, metamodel_Feature23: "metamodel_AssociationEntity" = None):
        self.name = name
        self.nullable = nullable
        self.xmltransient = xmltransient
        self.metamodel_Feature15 = metamodel_Feature15
        self.metamodel_Feature = metamodel_Feature
        self.metamodel_Feature23 = metamodel_Feature23
        
    @property
    def xmltransient(self) -> bool:
        return self.__xmltransient

    @xmltransient.setter
    def xmltransient(self, xmltransient: bool):
        self.__xmltransient = xmltransient

    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Feature23(self):
        return self.__metamodel_Feature23

    @metamodel_Feature23.setter
    def metamodel_Feature23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Feature__metamodel_Feature23", None)
        self.__metamodel_Feature23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_AssociationEntity"):
                opp_val = getattr(old_value, "metamodel_AssociationEntity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_AssociationEntity"):
                opp_val = getattr(value, "metamodel_AssociationEntity", None)
                if opp_val is None:
                    setattr(value, "metamodel_AssociationEntity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_Feature(self):
        return self.__metamodel_Feature

    @metamodel_Feature.setter
    def metamodel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Feature__metamodel_Feature", None)
        self.__metamodel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Entity"):
                opp_val = getattr(old_value, "metamodel_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Entity"):
                opp_val = getattr(value, "metamodel_Entity", None)
                if opp_val is None:
                    setattr(value, "metamodel_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_Feature15(self):
        return self.__metamodel_Feature15

    @metamodel_Feature15.setter
    def metamodel_Feature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Feature__metamodel_Feature15", None)
        self.__metamodel_Feature15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Type16"):
                opp_val = getattr(old_value, "metamodel_Type16", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Type16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Type16"):
                opp_val = getattr(value, "metamodel_Type16", None)
                setattr(value, "metamodel_Type16", self)

class Type:

    pass
class metamodel_AssociationEntity(Type):

    pass
class metamodel_Relation(Type):

    def __init__(self, optional: bool, unidirectional: bool, Relation6: "metamodel_Entity" = None, Relation: "metamodel_Entity" = None, relation: "metamodel_AssociationEntity" = None, owns: "metamodel_Entity" = None, ownedBy: "metamodel_Entity" = None, Relation25: "metamodel_AssociationEntity" = None):
        self.optional = optional
        self.unidirectional = unidirectional
        self.Relation6 = Relation6
        self.Relation = Relation
        self.relation = relation
        self.owns = owns
        self.ownedBy = ownedBy
        self.Relation25 = Relation25
        
    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def unidirectional(self) -> bool:
        return self.__unidirectional

    @unidirectional.setter
    def unidirectional(self, unidirectional: bool):
        self.__unidirectional = unidirectional

    @property
    def ownedBy(self):
        return self.__ownedBy

    @ownedBy.setter
    def ownedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Relation__ownedBy", None)
        self.__ownedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity20"):
                opp_val = getattr(old_value, "Entity20", None)
                if opp_val == self:
                    setattr(old_value, "Entity20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity20"):
                opp_val = getattr(value, "Entity20", None)
                setattr(value, "Entity20", self)

    @property
    def owns(self):
        return self.__owns

    @owns.setter
    def owns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Relation__owns", None)
        self.__owns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity18"):
                opp_val = getattr(old_value, "Entity18", None)
                if opp_val == self:
                    setattr(old_value, "Entity18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity18"):
                opp_val = getattr(value, "Entity18", None)
                setattr(value, "Entity18", self)

    @property
    def Relation25(self):
        return self.__Relation25

    @Relation25.setter
    def Relation25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Relation__Relation25", None)
        self.__Relation25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associates"):
                opp_val = getattr(old_value, "associates", None)
                if opp_val == self:
                    setattr(old_value, "associates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associates"):
                opp_val = getattr(value, "associates", None)
                setattr(value, "associates", self)

    @property
    def Relation(self):
        return self.__Relation

    @Relation.setter
    def Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Relation__Relation", None)
        self.__Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Relation6(self):
        return self.__Relation6

    @Relation6.setter
    def Relation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Relation__Relation6", None)
        self.__Relation6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slave"):
                opp_val = getattr(old_value, "slave", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slave"):
                opp_val = getattr(value, "slave", None)
                if opp_val is None:
                    setattr(value, "slave", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relation(self):
        return self.__relation

    @relation.setter
    def relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Relation__relation", None)
        self.__relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssociationEntity"):
                opp_val = getattr(old_value, "AssociationEntity", None)
                if opp_val == self:
                    setattr(old_value, "AssociationEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssociationEntity"):
                opp_val = getattr(value, "AssociationEntity", None)
                setattr(value, "AssociationEntity", self)

class metamodel_Entity(Type):

    pass
class metamodel_Datatype(Type):

    pass
class metamodel_idFeature(Feature):

    def __init__(self, generationType: str, metamodel_idFeature: "metamodel_Entity" = None):
        self.generationType = generationType
        self.metamodel_idFeature = metamodel_idFeature
        
    @property
    def generationType(self) -> str:
        return self.__generationType

    @generationType.setter
    def generationType(self, generationType: str):
        self.__generationType = generationType

    @property
    def metamodel_idFeature(self):
        return self.__metamodel_idFeature

    @metamodel_idFeature.setter
    def metamodel_idFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_idFeature__metamodel_idFeature", None)
        self.__metamodel_idFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Entity8"):
                opp_val = getattr(old_value, "metamodel_Entity8", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Entity8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Entity8"):
                opp_val = getattr(value, "metamodel_Entity8", None)
                setattr(value, "metamodel_Entity8", self)

class metamodel_DatabaseConnection:

    def __init__(self, jdbcDriver: str, jdbcUrl: str, jdbcUser: str, jdbcPassword: str, persistenceUnit: str, jdbcPrefix: str, metamodel_DatabaseConnection: "metamodel_Model" = None):
        self.jdbcDriver = jdbcDriver
        self.jdbcUrl = jdbcUrl
        self.jdbcUser = jdbcUser
        self.jdbcPassword = jdbcPassword
        self.persistenceUnit = persistenceUnit
        self.jdbcPrefix = jdbcPrefix
        self.metamodel_DatabaseConnection = metamodel_DatabaseConnection
        
    @property
    def persistenceUnit(self) -> str:
        return self.__persistenceUnit

    @persistenceUnit.setter
    def persistenceUnit(self, persistenceUnit: str):
        self.__persistenceUnit = persistenceUnit

    @property
    def jdbcUrl(self) -> str:
        return self.__jdbcUrl

    @jdbcUrl.setter
    def jdbcUrl(self, jdbcUrl: str):
        self.__jdbcUrl = jdbcUrl

    @property
    def jdbcUser(self) -> str:
        return self.__jdbcUser

    @jdbcUser.setter
    def jdbcUser(self, jdbcUser: str):
        self.__jdbcUser = jdbcUser

    @property
    def jdbcDriver(self) -> str:
        return self.__jdbcDriver

    @jdbcDriver.setter
    def jdbcDriver(self, jdbcDriver: str):
        self.__jdbcDriver = jdbcDriver

    @property
    def jdbcPrefix(self) -> str:
        return self.__jdbcPrefix

    @jdbcPrefix.setter
    def jdbcPrefix(self, jdbcPrefix: str):
        self.__jdbcPrefix = jdbcPrefix

    @property
    def jdbcPassword(self) -> str:
        return self.__jdbcPassword

    @jdbcPassword.setter
    def jdbcPassword(self, jdbcPassword: str):
        self.__jdbcPassword = jdbcPassword

    @property
    def metamodel_DatabaseConnection(self):
        return self.__metamodel_DatabaseConnection

    @metamodel_DatabaseConnection.setter
    def metamodel_DatabaseConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_DatabaseConnection__metamodel_DatabaseConnection", None)
        self.__metamodel_DatabaseConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Model2"):
                opp_val = getattr(old_value, "metamodel_Model2", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Model2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Model2"):
                opp_val = getattr(value, "metamodel_Model2", None)
                setattr(value, "metamodel_Model2", self)

class metamodel_Type(ABC):

    def __init__(self, name: str, metamodel_Type: "metamodel_Model" = None, metamodel_Type16: "metamodel_Feature" = None):
        self.name = name
        self.metamodel_Type = metamodel_Type
        self.metamodel_Type16 = metamodel_Type16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Type16(self):
        return self.__metamodel_Type16

    @metamodel_Type16.setter
    def metamodel_Type16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Type__metamodel_Type16", None)
        self.__metamodel_Type16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Feature15"):
                opp_val = getattr(old_value, "metamodel_Feature15", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Feature15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Feature15"):
                opp_val = getattr(value, "metamodel_Feature15", None)
                setattr(value, "metamodel_Feature15", self)

    @property
    def metamodel_Type(self):
        return self.__metamodel_Type

    @metamodel_Type.setter
    def metamodel_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Type__metamodel_Type", None)
        self.__metamodel_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Model"):
                opp_val = getattr(old_value, "metamodel_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Model"):
                opp_val = getattr(value, "metamodel_Model", None)
                if opp_val is None:
                    setattr(value, "metamodel_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_Model:

    def __init__(self, name: str, metamodel_Model: set["metamodel_Type"] = None, metamodel_Model2: "metamodel_DatabaseConnection" = None):
        self.name = name
        self.metamodel_Model = metamodel_Model if metamodel_Model is not None else set()
        self.metamodel_Model2 = metamodel_Model2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Model(self):
        return self.__metamodel_Model

    @metamodel_Model.setter
    def metamodel_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Model__metamodel_Model", None)
        self.__metamodel_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Type"):
                    opp_val = getattr(item, "metamodel_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Type"):
                    opp_val = getattr(item, "metamodel_Type", None)
                    
                    setattr(item, "metamodel_Type", self)
                    

    @property
    def metamodel_Model2(self):
        return self.__metamodel_Model2

    @metamodel_Model2.setter
    def metamodel_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Model__metamodel_Model2", None)
        self.__metamodel_Model2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_DatabaseConnection"):
                opp_val = getattr(old_value, "metamodel_DatabaseConnection", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_DatabaseConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_DatabaseConnection"):
                opp_val = getattr(value, "metamodel_DatabaseConnection", None)
                setattr(value, "metamodel_DatabaseConnection", self)
