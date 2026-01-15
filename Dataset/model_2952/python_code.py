from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class CollectionReturnType:

    pass
class modelDsl_AllModelTypeCollection(CollectionReturnType):

    pass
class DefCollectionTypeAttribute:

    pass
class modelDsl_DefModelModelTypeCollectionVariable(DefCollectionTypeAttribute):

    pass
class Method:

    pass
class modelDsl_MethodCollectionReturn(Method):

    pass
class modelDsl_MethodAllModelReturn(Method):

    pass
class modelDsl_MethodSimpleReturn(Method):

    def __init__(self, returnType: str):
        self.returnType = returnType
        
    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

class modelDsl_SimpleTypeCollection(CollectionReturnType):

    def __init__(self, type: str, modelDsl_SimpleTypeCollection: "modelDsl_DefModelSimpleTypeCollectionVariable" = None):
        self.type = type
        self.modelDsl_SimpleTypeCollection = modelDsl_SimpleTypeCollection
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def modelDsl_SimpleTypeCollection(self):
        return self.__modelDsl_SimpleTypeCollection

    @modelDsl_SimpleTypeCollection.setter
    def modelDsl_SimpleTypeCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_SimpleTypeCollection__modelDsl_SimpleTypeCollection", None)
        self.__modelDsl_SimpleTypeCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_DefModelSimpleTypeCollectionVariable"):
                opp_val = getattr(old_value, "modelDsl_DefModelSimpleTypeCollectionVariable", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_DefModelSimpleTypeCollectionVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_DefModelSimpleTypeCollectionVariable"):
                opp_val = getattr(value, "modelDsl_DefModelSimpleTypeCollectionVariable", None)
                setattr(value, "modelDsl_DefModelSimpleTypeCollectionVariable", self)

class modelDsl_DefModelSimpleTypeCollectionVariable(DefCollectionTypeAttribute):

    pass
class modelDsl_ModelTypeCollection:

    def __init__(self, collection: str, modelDsl_ModelTypeCollection: "modelDsl_DefModelModelTypeCollectionVariable" = None, modelDsl_ModelTypeCollection31: "modelDsl_ModelType" = None):
        self.collection = collection
        self.modelDsl_ModelTypeCollection = modelDsl_ModelTypeCollection
        self.modelDsl_ModelTypeCollection31 = modelDsl_ModelTypeCollection31
        
    @property
    def collection(self) -> str:
        return self.__collection

    @collection.setter
    def collection(self, collection: str):
        self.__collection = collection

    @property
    def modelDsl_ModelTypeCollection31(self):
        return self.__modelDsl_ModelTypeCollection31

    @modelDsl_ModelTypeCollection31.setter
    def modelDsl_ModelTypeCollection31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_ModelTypeCollection__modelDsl_ModelTypeCollection31", None)
        self.__modelDsl_ModelTypeCollection31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_ModelType32"):
                opp_val = getattr(old_value, "modelDsl_ModelType32", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_ModelType32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_ModelType32"):
                opp_val = getattr(value, "modelDsl_ModelType32", None)
                setattr(value, "modelDsl_ModelType32", self)

    @property
    def modelDsl_ModelTypeCollection(self):
        return self.__modelDsl_ModelTypeCollection

    @modelDsl_ModelTypeCollection.setter
    def modelDsl_ModelTypeCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_ModelTypeCollection__modelDsl_ModelTypeCollection", None)
        self.__modelDsl_ModelTypeCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_DefModelModelTypeCollectionVariable"):
                opp_val = getattr(old_value, "modelDsl_DefModelModelTypeCollectionVariable", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_DefModelModelTypeCollectionVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_DefModelModelTypeCollectionVariable"):
                opp_val = getattr(value, "modelDsl_DefModelModelTypeCollectionVariable", None)
                setattr(value, "modelDsl_DefModelModelTypeCollectionVariable", self)

class modelDsl_CollectionReturnType:

    def __init__(self, collection: str, modelDsl_CollectionReturnType: "modelDsl_DefCollectionTypeVariable" = None, modelDsl_CollectionReturnType25: "modelDsl_MethodCollectionReturn" = None):
        self.collection = collection
        self.modelDsl_CollectionReturnType = modelDsl_CollectionReturnType
        self.modelDsl_CollectionReturnType25 = modelDsl_CollectionReturnType25
        
    @property
    def collection(self) -> str:
        return self.__collection

    @collection.setter
    def collection(self, collection: str):
        self.__collection = collection

    @property
    def modelDsl_CollectionReturnType(self):
        return self.__modelDsl_CollectionReturnType

    @modelDsl_CollectionReturnType.setter
    def modelDsl_CollectionReturnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_CollectionReturnType__modelDsl_CollectionReturnType", None)
        self.__modelDsl_CollectionReturnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_DefCollectionTypeVariable"):
                opp_val = getattr(old_value, "modelDsl_DefCollectionTypeVariable", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_DefCollectionTypeVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_DefCollectionTypeVariable"):
                opp_val = getattr(value, "modelDsl_DefCollectionTypeVariable", None)
                setattr(value, "modelDsl_DefCollectionTypeVariable", self)

    @property
    def modelDsl_CollectionReturnType25(self):
        return self.__modelDsl_CollectionReturnType25

    @modelDsl_CollectionReturnType25.setter
    def modelDsl_CollectionReturnType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_CollectionReturnType__modelDsl_CollectionReturnType25", None)
        self.__modelDsl_CollectionReturnType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_MethodCollectionReturn"):
                opp_val = getattr(old_value, "modelDsl_MethodCollectionReturn", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_MethodCollectionReturn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_MethodCollectionReturn"):
                opp_val = getattr(value, "modelDsl_MethodCollectionReturn", None)
                setattr(value, "modelDsl_MethodCollectionReturn", self)

class DefIdAttribute:

    pass
class modelDsl_DefLinkVariable(DefIdAttribute):

    def __init__(self, name: str, modelDsl_DefLinkVariable: "modelDsl_Link" = None):
        self.name = name
        self.modelDsl_DefLinkVariable = modelDsl_DefLinkVariable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modelDsl_DefLinkVariable(self):
        return self.__modelDsl_DefLinkVariable

    @modelDsl_DefLinkVariable.setter
    def modelDsl_DefLinkVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_DefLinkVariable__modelDsl_DefLinkVariable", None)
        self.__modelDsl_DefLinkVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Link"):
                opp_val = getattr(old_value, "modelDsl_Link", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_Link", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Link"):
                opp_val = getattr(value, "modelDsl_Link", None)
                setattr(value, "modelDsl_Link", self)

class DefAttribute:

    pass
class modelDsl_DefModelTypeVariable(DefAttribute, DefIdAttribute):

    def __init__(self, nullable: str, name: str, modelDsl_DefModelTypeVariable: "modelDsl_ModelType" = None):
        self.nullable = nullable
        self.name = name
        self.modelDsl_DefModelTypeVariable = modelDsl_DefModelTypeVariable
        
    @property
    def nullable(self) -> str:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: str):
        self.__nullable = nullable

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modelDsl_DefModelTypeVariable(self):
        return self.__modelDsl_DefModelTypeVariable

    @modelDsl_DefModelTypeVariable.setter
    def modelDsl_DefModelTypeVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_DefModelTypeVariable__modelDsl_DefModelTypeVariable", None)
        self.__modelDsl_DefModelTypeVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_ModelType"):
                opp_val = getattr(old_value, "modelDsl_ModelType", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_ModelType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_ModelType"):
                opp_val = getattr(value, "modelDsl_ModelType", None)
                setattr(value, "modelDsl_ModelType", self)

class modelDsl_DefCollectionTypeAttribute(DefAttribute):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class DefVariable:

    pass
class modelDsl_DefSimpleVariable(DefVariable, DefIdAttribute, DefAttribute):

    def __init__(self, nullable: str, type: str):
        self.nullable = nullable
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def nullable(self) -> str:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: str):
        self.__nullable = nullable

class modelDsl_DefCollectionTypeVariable(DefVariable):

    pass
class modelDsl_DefAllModelTypeVariable(DefVariable):

    pass
class modelDsl_DefVariable:

    def __init__(self, name: str, modelDsl_DefVariable: "modelDsl_Method" = None):
        self.name = name
        self.modelDsl_DefVariable = modelDsl_DefVariable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modelDsl_DefVariable(self):
        return self.__modelDsl_DefVariable

    @modelDsl_DefVariable.setter
    def modelDsl_DefVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_DefVariable__modelDsl_DefVariable", None)
        self.__modelDsl_DefVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Method23"):
                opp_val = getattr(old_value, "modelDsl_Method23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Method23"):
                opp_val = getattr(value, "modelDsl_Method23", None)
                if opp_val is None:
                    setattr(value, "modelDsl_Method23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Entity:

    pass
class modelDsl_SimpleEntity(Entity):

    def __init__(self, implementation: str, modelDsl_SimpleEntity: "modelDsl_SimpleEntity" = None, modelDsl_SimpleEntity4: "modelDsl_SimpleEntity" = None, modelDsl_SimpleEntity7: set["modelDsl_DefIdAttribute"] = None):
        self.implementation = implementation
        self.modelDsl_SimpleEntity = modelDsl_SimpleEntity
        self.modelDsl_SimpleEntity4 = modelDsl_SimpleEntity4
        self.modelDsl_SimpleEntity7 = modelDsl_SimpleEntity7 if modelDsl_SimpleEntity7 is not None else set()
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def modelDsl_SimpleEntity7(self):
        return self.__modelDsl_SimpleEntity7

    @modelDsl_SimpleEntity7.setter
    def modelDsl_SimpleEntity7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_SimpleEntity__modelDsl_SimpleEntity7", None)
        self.__modelDsl_SimpleEntity7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modelDsl_DefIdAttribute"):
                    opp_val = getattr(item, "modelDsl_DefIdAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "modelDsl_DefIdAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modelDsl_DefIdAttribute"):
                    opp_val = getattr(item, "modelDsl_DefIdAttribute", None)
                    
                    setattr(item, "modelDsl_DefIdAttribute", self)
                    

    @property
    def modelDsl_SimpleEntity4(self):
        return self.__modelDsl_SimpleEntity4

    @modelDsl_SimpleEntity4.setter
    def modelDsl_SimpleEntity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_SimpleEntity__modelDsl_SimpleEntity4", None)
        self.__modelDsl_SimpleEntity4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_SimpleEntity"):
                opp_val = getattr(old_value, "modelDsl_SimpleEntity", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_SimpleEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_SimpleEntity"):
                opp_val = getattr(value, "modelDsl_SimpleEntity", None)
                setattr(value, "modelDsl_SimpleEntity", self)

    @property
    def modelDsl_SimpleEntity(self):
        return self.__modelDsl_SimpleEntity

    @modelDsl_SimpleEntity.setter
    def modelDsl_SimpleEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_SimpleEntity__modelDsl_SimpleEntity", None)
        self.__modelDsl_SimpleEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_SimpleEntity4"):
                opp_val = getattr(old_value, "modelDsl_SimpleEntity4", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_SimpleEntity4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_SimpleEntity4"):
                opp_val = getattr(value, "modelDsl_SimpleEntity4", None)
                setattr(value, "modelDsl_SimpleEntity4", self)

class ModelType:

    pass
class modelDsl_Enumerable(ModelType):

    def __init__(self, enums: str):
        self.enums = enums
        
    @property
    def enums(self) -> str:
        return self.__enums

    @enums.setter
    def enums(self, enums: str):
        self.__enums = enums

class modelDsl_ValueType(ModelType):

    pass
class modelDsl_Relation:

    def __init__(self, multiplicity: str, name: str, navigable: str, modelDsl_Relation: "modelDsl_AssociativeEntity" = None, modelDsl_Relation12: "modelDsl_SimpleLink" = None, modelDsl_Relation14: "modelDsl_Entity" = None):
        self.multiplicity = multiplicity
        self.name = name
        self.navigable = navigable
        self.modelDsl_Relation = modelDsl_Relation
        self.modelDsl_Relation12 = modelDsl_Relation12
        self.modelDsl_Relation14 = modelDsl_Relation14
        
    @property
    def multiplicity(self) -> str:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: str):
        self.__multiplicity = multiplicity

    @property
    def navigable(self) -> str:
        return self.__navigable

    @navigable.setter
    def navigable(self, navigable: str):
        self.__navigable = navigable

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modelDsl_Relation14(self):
        return self.__modelDsl_Relation14

    @modelDsl_Relation14.setter
    def modelDsl_Relation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Relation__modelDsl_Relation14", None)
        self.__modelDsl_Relation14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Entity15"):
                opp_val = getattr(old_value, "modelDsl_Entity15", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_Entity15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Entity15"):
                opp_val = getattr(value, "modelDsl_Entity15", None)
                setattr(value, "modelDsl_Entity15", self)

    @property
    def modelDsl_Relation(self):
        return self.__modelDsl_Relation

    @modelDsl_Relation.setter
    def modelDsl_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Relation__modelDsl_Relation", None)
        self.__modelDsl_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_AssociativeEntity"):
                opp_val = getattr(old_value, "modelDsl_AssociativeEntity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_AssociativeEntity"):
                opp_val = getattr(value, "modelDsl_AssociativeEntity", None)
                if opp_val is None:
                    setattr(value, "modelDsl_AssociativeEntity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modelDsl_Relation12(self):
        return self.__modelDsl_Relation12

    @modelDsl_Relation12.setter
    def modelDsl_Relation12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Relation__modelDsl_Relation12", None)
        self.__modelDsl_Relation12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_SimpleLink"):
                opp_val = getattr(old_value, "modelDsl_SimpleLink", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_SimpleLink"):
                opp_val = getattr(value, "modelDsl_SimpleLink", None)
                if opp_val is None:
                    setattr(value, "modelDsl_SimpleLink", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Link:

    pass
class modelDsl_AssociativeEntity(Entity, Link):

    pass
class modelDsl_DefIdAttribute:

    pass
class modelDsl_Link:

    pass
class modelDsl_Method:

    def __init__(self, name: str, modelDsl_Method: "modelDsl_Entity" = None, modelDsl_Method23: set["modelDsl_DefVariable"] = None):
        self.name = name
        self.modelDsl_Method = modelDsl_Method
        self.modelDsl_Method23 = modelDsl_Method23 if modelDsl_Method23 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modelDsl_Method(self):
        return self.__modelDsl_Method

    @modelDsl_Method.setter
    def modelDsl_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Method__modelDsl_Method", None)
        self.__modelDsl_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Entity3"):
                opp_val = getattr(old_value, "modelDsl_Entity3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Entity3"):
                opp_val = getattr(value, "modelDsl_Entity3", None)
                if opp_val is None:
                    setattr(value, "modelDsl_Entity3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modelDsl_Method23(self):
        return self.__modelDsl_Method23

    @modelDsl_Method23.setter
    def modelDsl_Method23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Method__modelDsl_Method23", None)
        self.__modelDsl_Method23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modelDsl_DefVariable"):
                    opp_val = getattr(item, "modelDsl_DefVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "modelDsl_DefVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modelDsl_DefVariable"):
                    opp_val = getattr(item, "modelDsl_DefVariable", None)
                    
                    setattr(item, "modelDsl_DefVariable", self)
                    

class modelDsl_DefAttribute:

    pass
class AllModelType:

    pass
class modelDsl_ModelType(AllModelType):

    pass
class modelDsl_Entity(AllModelType):

    pass
class Element:

    pass
class modelDsl_SimpleLink(Link, Element):

    pass
class modelDsl_AllModelType(Element):

    pass
class modelDsl_Element:

    def __init__(self, name: str, modelDsl_Element: "modelDsl_Model" = None):
        self.name = name
        self.modelDsl_Element = modelDsl_Element
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modelDsl_Element(self):
        return self.__modelDsl_Element

    @modelDsl_Element.setter
    def modelDsl_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Element__modelDsl_Element", None)
        self.__modelDsl_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Model"):
                opp_val = getattr(old_value, "modelDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Model"):
                opp_val = getattr(value, "modelDsl_Model", None)
                if opp_val is None:
                    setattr(value, "modelDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class modelDsl_Model:

    pass