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
ube_DataType = Class(name="ube::DataType")
Type = Class(name="Type")
ube_Entity = Class(name="ube::Entity")
ube_Feature = Class(name="ube::Feature")
ube_EntityModel = Class(name="ube::EntityModel")
ube_NamedElement = Class(name="ube::NamedElement", is_abstract=True)
ube_Type = Class(name="ube::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")

# ube_DataType class attributes and methods

# Type class attributes and methods

# ube_Entity class attributes and methods
ube_Entity_abstract: Property = Property(name="abstract", type=BooleanType)
ube_Entity.attributes={ube_Entity_abstract}

# ube_Feature class attributes and methods
ube_Feature_kind: Property = Property(name="kind", type=StringType)
ube_Feature.attributes={ube_Feature_kind}

# ube_EntityModel class attributes and methods

# ube_NamedElement class attributes and methods
ube_NamedElement_name: Property = Property(name="name", type=StringType)
ube_NamedElement.attributes={ube_NamedElement_name}

# ube_Type class attributes and methods

# NamedElement class attributes and methods

# Relationships
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="ube_Feature", type=ube_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="ube_Entity", type=ube_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="ube_Type", type=ube_EntityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ube_EntityModel", type=ube_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="ube_Type4", type=ube_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="ube_Feature3", type=ube_Type, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ube_DataType_Type = Generalization(general=Type, specific=ube_DataType)
gen_ube_Entity_Type = Generalization(general=Type, specific=ube_Entity)
gen_ube_Feature_NamedElement = Generalization(general=NamedElement, specific=ube_Feature)
gen_ube_Type_NamedElement = Generalization(general=NamedElement, specific=ube_Type)

# Domain Model
domain_model = DomainModel(
    name="ube",
    types={ube_DataType, Type, ube_Entity, ube_Feature, ube_EntityModel, ube_NamedElement, ube_Type, NamedElement, FeatureKind},
    associations={features0, types1, type2},
    generalizations={gen_ube_DataType_Type, gen_ube_Entity_Type, gen_ube_Feature_NamedElement, gen_ube_Type_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)