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

# Enumerations
FeatureKind: Enumeration = Enumeration(
    name="FeatureKind",
    literals={
            EnumerationLiteral(name="attribute"),
			EnumerationLiteral(name="reference"),
			EnumerationLiteral(name="containment")
    }
)

# Classes
myDSL_DataType = Class(name="myDSL::DataType")
Type = Class(name="Type")
myDSL_Entity = Class(name="myDSL::Entity")
myDSL_Feature = Class(name="myDSL::Feature")
myDSL_NamedElement = Class(name="myDSL::NamedElement", is_abstract=True)
myDSL_Type = Class(name="myDSL::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
myDSL_EntityModel = Class(name="myDSL::EntityModel")

# myDSL_DataType class attributes and methods

# Type class attributes and methods

# myDSL_Entity class attributes and methods
myDSL_Entity_abstract: Property = Property(name="abstract", type=BooleanType)
myDSL_Entity.attributes={myDSL_Entity_abstract}

# myDSL_Feature class attributes and methods
myDSL_Feature_kind: Property = Property(name="kind", type=StringType)
myDSL_Feature.attributes={myDSL_Feature_kind}

# myDSL_NamedElement class attributes and methods
myDSL_NamedElement_name: Property = Property(name="name", type=StringType)
myDSL_NamedElement.attributes={myDSL_NamedElement_name}

# myDSL_Type class attributes and methods

# NamedElement class attributes and methods

# myDSL_EntityModel class attributes and methods

# Relationships
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="myDSL_Feature", type=myDSL_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDSL_Entity", type=myDSL_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="myDSL_Type", type=myDSL_EntityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="myDSL_EntityModel", type=myDSL_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="myDSL_Type4", type=myDSL_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="myDSL_Feature3", type=myDSL_Type, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_myDSL_DataType_Type = Generalization(general=Type, specific=myDSL_DataType)
gen_myDSL_Entity_Type = Generalization(general=Type, specific=myDSL_Entity)
gen_myDSL_Type_NamedElement = Generalization(general=NamedElement, specific=myDSL_Type)
gen_myDSL_Feature_NamedElement = Generalization(general=NamedElement, specific=myDSL_Feature)

# Domain Model
domain_model = DomainModel(
    name="myDSL",
    types={myDSL_DataType, Type, myDSL_Entity, myDSL_Feature, myDSL_NamedElement, myDSL_Type, NamedElement, myDSL_EntityModel, FeatureKind},
    associations={features0, types1, type2},
    generalizations={gen_myDSL_DataType_Type, gen_myDSL_Entity_Type, gen_myDSL_Type_NamedElement, gen_myDSL_Feature_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)