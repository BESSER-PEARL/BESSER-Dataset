####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
modelDsl_Entity = Class(name="modelDsl_Entity")
AllModelType = Class(name="AllModelType")
modelDsl_DefAttribute = Class(name="modelDsl_DefAttribute")
modelDsl_Method = Class(name="modelDsl_Method")
modelDsl_ModelType = Class(name="modelDsl_ModelType")
modelDsl_Link = Class(name="modelDsl_Link")
modelDsl_SimpleEntity = Class(name="modelDsl_SimpleEntity")
Entity = Class(name="Entity")
modelDsl_DefIdAttribute = Class(name="modelDsl_DefIdAttribute")
modelDsl_AssociativeEntity = Class(name="modelDsl_AssociativeEntity")
Link = Class(name="Link")
modelDsl_Relation = Class(name="modelDsl_Relation")
modelDsl_ValueType = Class(name="modelDsl_ValueType")
ModelType = Class(name="ModelType")
modelDsl_Enumerable = Class(name="modelDsl_Enumerable")
modelDsl_SimpleLink = Class(name="modelDsl_SimpleLink")
modelDsl_Model = Class(name="modelDsl_Model")
modelDsl_Element = Class(name="modelDsl_Element")
modelDsl_AllModelType = Class(name="modelDsl_AllModelType")
Element = Class(name="Element")
modelDsl_DefCollectionTypeVariable = Class(name="modelDsl_DefCollectionTypeVariable")
modelDsl_CollectionReturnType = Class(name="modelDsl_CollectionReturnType")
modelDsl_DefModelModelTypeCollectionVariable = Class(name="modelDsl_DefModelModelTypeCollectionVariable")
DefCollectionTypeAttribute = Class(name="DefCollectionTypeAttribute")
modelDsl_ModelTypeCollection = Class(name="modelDsl_ModelTypeCollection")
modelDsl_DefModelSimpleTypeCollectionVariable = Class(name="modelDsl_DefModelSimpleTypeCollectionVariable")
modelDsl_SimpleTypeCollection = Class(name="modelDsl_SimpleTypeCollection")
modelDsl_DefLinkVariable = Class(name="modelDsl_DefLinkVariable")
modelDsl_MethodSimpleReturn = Class(name="modelDsl_MethodSimpleReturn")
Method_ = Class(name="Method")
modelDsl_MethodCollectionReturn = Class(name="modelDsl_MethodCollectionReturn")
modelDsl_MethodAllModelReturn = Class(name="modelDsl_MethodAllModelReturn")
modelDsl_AllModelTypeCollection = Class(name="modelDsl_AllModelTypeCollection")
CollectionReturnType = Class(name="CollectionReturnType")
modelDsl_DefVariable = Class(name="modelDsl_DefVariable")
modelDsl_DefAllModelTypeVariable = Class(name="modelDsl_DefAllModelTypeVariable")
DefVariable = Class(name="DefVariable")
modelDsl_DefSimpleVariable = Class(name="modelDsl_DefSimpleVariable")
DefAttribute = Class(name="DefAttribute")
DefIdAttribute = Class(name="DefIdAttribute")
modelDsl_DefModelTypeVariable = Class(name="modelDsl_DefModelTypeVariable")
modelDsl_DefCollectionTypeAttribute = Class(name="modelDsl_DefCollectionTypeAttribute")

# modelDsl_Entity class attributes and methods

# AllModelType class attributes and methods

# modelDsl_DefAttribute class attributes and methods

# modelDsl_Method class attributes and methods
modelDsl_Method_name: Property = Property(name="name", type=StringType)
modelDsl_Method.attributes={modelDsl_Method_name}

# modelDsl_ModelType class attributes and methods

# modelDsl_Link class attributes and methods

# modelDsl_SimpleEntity class attributes and methods
modelDsl_SimpleEntity_implementation: Property = Property(name="implementation", type=StringType)
modelDsl_SimpleEntity.attributes={modelDsl_SimpleEntity_implementation}

# Entity class attributes and methods

# modelDsl_DefIdAttribute class attributes and methods

# modelDsl_AssociativeEntity class attributes and methods

# Link class attributes and methods

# modelDsl_Relation class attributes and methods
modelDsl_Relation_multiplicity: Property = Property(name="multiplicity", type=StringType)
modelDsl_Relation_name: Property = Property(name="name", type=StringType)
modelDsl_Relation_navigable: Property = Property(name="navigable", type=StringType)
modelDsl_Relation.attributes={modelDsl_Relation_multiplicity, modelDsl_Relation_name, modelDsl_Relation_navigable}

# modelDsl_ValueType class attributes and methods

# ModelType class attributes and methods

# modelDsl_Enumerable class attributes and methods
modelDsl_Enumerable_enums: Property = Property(name="enums", type=StringType)
modelDsl_Enumerable.attributes={modelDsl_Enumerable_enums}

# modelDsl_SimpleLink class attributes and methods

# modelDsl_Model class attributes and methods

# modelDsl_Element class attributes and methods
modelDsl_Element_name: Property = Property(name="name", type=StringType)
modelDsl_Element.attributes={modelDsl_Element_name}

# modelDsl_AllModelType class attributes and methods

# Element class attributes and methods

# modelDsl_DefCollectionTypeVariable class attributes and methods

# modelDsl_CollectionReturnType class attributes and methods
modelDsl_CollectionReturnType_collection: Property = Property(name="collection", type=StringType)
modelDsl_CollectionReturnType.attributes={modelDsl_CollectionReturnType_collection}

# modelDsl_DefModelModelTypeCollectionVariable class attributes and methods

# DefCollectionTypeAttribute class attributes and methods

# modelDsl_ModelTypeCollection class attributes and methods
modelDsl_ModelTypeCollection_collection: Property = Property(name="collection", type=StringType)
modelDsl_ModelTypeCollection.attributes={modelDsl_ModelTypeCollection_collection}

# modelDsl_DefModelSimpleTypeCollectionVariable class attributes and methods

# modelDsl_SimpleTypeCollection class attributes and methods
modelDsl_SimpleTypeCollection_type: Property = Property(name="type", type=StringType)
modelDsl_SimpleTypeCollection.attributes={modelDsl_SimpleTypeCollection_type}

# modelDsl_DefLinkVariable class attributes and methods
modelDsl_DefLinkVariable_name: Property = Property(name="name", type=StringType)
modelDsl_DefLinkVariable.attributes={modelDsl_DefLinkVariable_name}

# modelDsl_MethodSimpleReturn class attributes and methods
modelDsl_MethodSimpleReturn_returnType: Property = Property(name="returnType", type=StringType)
modelDsl_MethodSimpleReturn.attributes={modelDsl_MethodSimpleReturn_returnType}

# Method class attributes and methods

# modelDsl_MethodCollectionReturn class attributes and methods

# modelDsl_MethodAllModelReturn class attributes and methods

# modelDsl_AllModelTypeCollection class attributes and methods

# CollectionReturnType class attributes and methods

# modelDsl_DefVariable class attributes and methods
modelDsl_DefVariable_name: Property = Property(name="name", type=StringType)
modelDsl_DefVariable.attributes={modelDsl_DefVariable_name}

# modelDsl_DefAllModelTypeVariable class attributes and methods

# DefVariable class attributes and methods

# modelDsl_DefSimpleVariable class attributes and methods
modelDsl_DefSimpleVariable_nullable: Property = Property(name="nullable", type=StringType)
modelDsl_DefSimpleVariable_type: Property = Property(name="type", type=StringType)
modelDsl_DefSimpleVariable.attributes={modelDsl_DefSimpleVariable_nullable, modelDsl_DefSimpleVariable_type}

# DefAttribute class attributes and methods

# DefIdAttribute class attributes and methods

# modelDsl_DefModelTypeVariable class attributes and methods
modelDsl_DefModelTypeVariable_nullable: Property = Property(name="nullable", type=StringType)
modelDsl_DefModelTypeVariable_name: Property = Property(name="name", type=StringType)
modelDsl_DefModelTypeVariable.attributes={modelDsl_DefModelTypeVariable_name, modelDsl_DefModelTypeVariable_nullable}

# modelDsl_DefCollectionTypeAttribute class attributes and methods
modelDsl_DefCollectionTypeAttribute_name: Property = Property(name="name", type=StringType)
modelDsl_DefCollectionTypeAttribute.attributes={modelDsl_DefCollectionTypeAttribute_name}

# Relationships
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="modelDsl_DefAttribute", type=modelDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Entity", type=modelDsl_DefAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods2: BinaryAssociation = BinaryAssociation(
    name="methods2",
    ends={
        Property(name="modelDsl_Method", type=modelDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Entity3", type=modelDsl_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass5: BinaryAssociation = BinaryAssociation(
    name="superClass5",
    ends={
        Property(name="modelDsl_SimpleEntity", type=modelDsl_SimpleEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_SimpleEntity4", type=modelDsl_SimpleEntity, multiplicity=Multiplicity(0, 1))
    }
)
attributesId6: BinaryAssociation = BinaryAssociation(
    name="attributesId6",
    ends={
        Property(name="modelDsl_DefIdAttribute", type=modelDsl_SimpleEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_SimpleEntity7", type=modelDsl_DefIdAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations8: BinaryAssociation = BinaryAssociation(
    name="relations8",
    ends={
        Property(name="modelDsl_Relation", type=modelDsl_AssociativeEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_AssociativeEntity", type=modelDsl_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes9: BinaryAssociation = BinaryAssociation(
    name="attributes9",
    ends={
        Property(name="modelDsl_DefAttribute10", type=modelDsl_ValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_ValueType", type=modelDsl_DefAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations11: BinaryAssociation = BinaryAssociation(
    name="relations11",
    ends={
        Property(name="modelDsl_Relation12", type=modelDsl_SimpleLink, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_SimpleLink", type=modelDsl_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="modelDsl_Entity15", type=modelDsl_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Relation14", type=modelDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="modelDsl_Element", type=modelDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Model", type=modelDsl_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="modelDsl_CollectionReturnType", type=modelDsl_DefCollectionTypeVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_DefCollectionTypeVariable", type=modelDsl_CollectionReturnType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="modelDsl_ModelTypeCollection", type=modelDsl_DefModelModelTypeCollectionVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_DefModelModelTypeCollectionVariable", type=modelDsl_ModelTypeCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type20: BinaryAssociation = BinaryAssociation(
    name="type20",
    ends={
        Property(name="modelDsl_SimpleTypeCollection", type=modelDsl_DefModelSimpleTypeCollectionVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_DefModelSimpleTypeCollectionVariable", type=modelDsl_SimpleTypeCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type21: BinaryAssociation = BinaryAssociation(
    name="type21",
    ends={
        Property(name="modelDsl_Link", type=modelDsl_DefLinkVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_DefLinkVariable", type=modelDsl_Link, multiplicity=Multiplicity(0, 1))
    }
)
parameters22: BinaryAssociation = BinaryAssociation(
    name="parameters22",
    ends={
        Property(name="modelDsl_DefVariable", type=modelDsl_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Method23", type=modelDsl_DefVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType24: BinaryAssociation = BinaryAssociation(
    name="returnType24",
    ends={
        Property(name="modelDsl_CollectionReturnType25", type=modelDsl_MethodCollectionReturn, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_MethodCollectionReturn", type=modelDsl_CollectionReturnType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType26: BinaryAssociation = BinaryAssociation(
    name="returnType26",
    ends={
        Property(name="modelDsl_AllModelType27", type=modelDsl_MethodAllModelReturn, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_MethodAllModelReturn", type=modelDsl_AllModelType, multiplicity=Multiplicity(0, 1))
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="modelDsl_AllModelType29", type=modelDsl_AllModelTypeCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_AllModelTypeCollection", type=modelDsl_AllModelType, multiplicity=Multiplicity(0, 1))
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="modelDsl_AllModelType", type=modelDsl_DefAllModelTypeVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_DefAllModelTypeVariable", type=modelDsl_AllModelType, multiplicity=Multiplicity(0, 1))
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="modelDsl_ModelType", type=modelDsl_DefModelTypeVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_DefModelTypeVariable", type=modelDsl_ModelType, multiplicity=Multiplicity(0, 1))
    }
)
type30: BinaryAssociation = BinaryAssociation(
    name="type30",
    ends={
        Property(name="modelDsl_ModelType32", type=modelDsl_ModelTypeCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_ModelTypeCollection31", type=modelDsl_ModelType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_modelDsl_Entity_AllModelType = Generalization(general=AllModelType, specific=modelDsl_Entity)
gen_modelDsl_ModelType_AllModelType = Generalization(general=AllModelType, specific=modelDsl_ModelType)
gen_modelDsl_SimpleEntity_Entity = Generalization(general=Entity, specific=modelDsl_SimpleEntity)
gen_modelDsl_AssociativeEntity_Entity = Generalization(general=Entity, specific=modelDsl_AssociativeEntity)
gen_modelDsl_AssociativeEntity_Link = Generalization(general=Link, specific=modelDsl_AssociativeEntity)
gen_modelDsl_ValueType_ModelType = Generalization(general=ModelType, specific=modelDsl_ValueType)
gen_modelDsl_Enumerable_ModelType = Generalization(general=ModelType, specific=modelDsl_Enumerable)
gen_modelDsl_SimpleLink_Element = Generalization(general=Element, specific=modelDsl_SimpleLink)
gen_modelDsl_SimpleLink_Link = Generalization(general=Link, specific=modelDsl_SimpleLink)
gen_modelDsl_AllModelType_Element = Generalization(general=Element, specific=modelDsl_AllModelType)
gen_modelDsl_DefCollectionTypeVariable_DefVariable = Generalization(general=DefVariable, specific=modelDsl_DefCollectionTypeVariable)
gen_modelDsl_DefModelModelTypeCollectionVariable_DefCollectionTypeAttribute = Generalization(general=DefCollectionTypeAttribute, specific=modelDsl_DefModelModelTypeCollectionVariable)
gen_modelDsl_DefModelSimpleTypeCollectionVariable_DefCollectionTypeAttribute = Generalization(general=DefCollectionTypeAttribute, specific=modelDsl_DefModelSimpleTypeCollectionVariable)
gen_modelDsl_DefLinkVariable_DefIdAttribute = Generalization(general=DefIdAttribute, specific=modelDsl_DefLinkVariable)
gen_modelDsl_MethodSimpleReturn_Method = Generalization(general=Method_, specific=modelDsl_MethodSimpleReturn)
gen_modelDsl_MethodCollectionReturn_Method = Generalization(general=Method_, specific=modelDsl_MethodCollectionReturn)
gen_modelDsl_MethodAllModelReturn_Method = Generalization(general=Method_, specific=modelDsl_MethodAllModelReturn)
gen_modelDsl_AllModelTypeCollection_CollectionReturnType = Generalization(general=CollectionReturnType, specific=modelDsl_AllModelTypeCollection)
gen_modelDsl_DefAllModelTypeVariable_DefVariable = Generalization(general=DefVariable, specific=modelDsl_DefAllModelTypeVariable)
gen_modelDsl_DefSimpleVariable_DefAttribute = Generalization(general=DefAttribute, specific=modelDsl_DefSimpleVariable)
gen_modelDsl_DefSimpleVariable_DefVariable = Generalization(general=DefVariable, specific=modelDsl_DefSimpleVariable)
gen_modelDsl_DefSimpleVariable_DefIdAttribute = Generalization(general=DefIdAttribute, specific=modelDsl_DefSimpleVariable)
gen_modelDsl_DefModelTypeVariable_DefAttribute = Generalization(general=DefAttribute, specific=modelDsl_DefModelTypeVariable)
gen_modelDsl_DefModelTypeVariable_DefIdAttribute = Generalization(general=DefIdAttribute, specific=modelDsl_DefModelTypeVariable)
gen_modelDsl_DefCollectionTypeAttribute_DefAttribute = Generalization(general=DefAttribute, specific=modelDsl_DefCollectionTypeAttribute)
gen_modelDsl_SimpleTypeCollection_CollectionReturnType = Generalization(general=CollectionReturnType, specific=modelDsl_SimpleTypeCollection)

# Domain Model
domain_model = DomainModel(
    name="modelDsl",
    types={modelDsl_Entity, AllModelType, modelDsl_DefAttribute, modelDsl_Method, modelDsl_ModelType, modelDsl_Link, modelDsl_SimpleEntity, Entity, modelDsl_DefIdAttribute, modelDsl_AssociativeEntity, Link, modelDsl_Relation, modelDsl_ValueType, ModelType, modelDsl_Enumerable, modelDsl_SimpleLink, modelDsl_Model, modelDsl_Element, modelDsl_AllModelType, Element, modelDsl_DefCollectionTypeVariable, modelDsl_CollectionReturnType, modelDsl_DefModelModelTypeCollectionVariable, DefCollectionTypeAttribute, modelDsl_ModelTypeCollection, modelDsl_DefModelSimpleTypeCollectionVariable, modelDsl_SimpleTypeCollection, modelDsl_DefLinkVariable, modelDsl_MethodSimpleReturn, Method_, modelDsl_MethodCollectionReturn, modelDsl_MethodAllModelReturn, modelDsl_AllModelTypeCollection, CollectionReturnType, modelDsl_DefVariable, modelDsl_DefAllModelTypeVariable, DefVariable, modelDsl_DefSimpleVariable, DefAttribute, DefIdAttribute, modelDsl_DefModelTypeVariable, modelDsl_DefCollectionTypeAttribute},
    associations={attributes1, methods2, superClass5, attributesId6, relations8, attributes9, relations11, type13, elements0, type18, type19, type20, type21, parameters22, returnType24, returnType26, type28, type16, type17, type30},
    generalizations={gen_modelDsl_Entity_AllModelType, gen_modelDsl_ModelType_AllModelType, gen_modelDsl_SimpleEntity_Entity, gen_modelDsl_AssociativeEntity_Entity, gen_modelDsl_AssociativeEntity_Link, gen_modelDsl_ValueType_ModelType, gen_modelDsl_Enumerable_ModelType, gen_modelDsl_SimpleLink_Element, gen_modelDsl_SimpleLink_Link, gen_modelDsl_AllModelType_Element, gen_modelDsl_DefCollectionTypeVariable_DefVariable, gen_modelDsl_DefModelModelTypeCollectionVariable_DefCollectionTypeAttribute, gen_modelDsl_DefModelSimpleTypeCollectionVariable_DefCollectionTypeAttribute, gen_modelDsl_DefLinkVariable_DefIdAttribute, gen_modelDsl_MethodSimpleReturn_Method, gen_modelDsl_MethodCollectionReturn_Method, gen_modelDsl_MethodAllModelReturn_Method, gen_modelDsl_AllModelTypeCollection_CollectionReturnType, gen_modelDsl_DefAllModelTypeVariable_DefVariable, gen_modelDsl_DefSimpleVariable_DefAttribute, gen_modelDsl_DefSimpleVariable_DefVariable, gen_modelDsl_DefSimpleVariable_DefIdAttribute, gen_modelDsl_DefModelTypeVariable_DefAttribute, gen_modelDsl_DefModelTypeVariable_DefIdAttribute, gen_modelDsl_DefCollectionTypeAttribute_DefAttribute, gen_modelDsl_SimpleTypeCollection_CollectionReturnType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)