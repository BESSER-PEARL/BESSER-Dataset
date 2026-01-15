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
coral_Entity = Class(name="coral::Entity")
coral_Feature = Class(name="coral::Feature")
coral_EntityModel = Class(name="coral::EntityModel")
coral_NamedElement = Class(name="coral::NamedElement", is_abstract=True)
coral_Type = Class(name="coral::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
coral_DataType = Class(name="coral::DataType")
Type = Class(name="Type")

# coral_Entity class attributes and methods
coral_Entity_abstract: Property = Property(name="abstract", type=BooleanType)
coral_Entity.attributes={coral_Entity_abstract}

# coral_Feature class attributes and methods
coral_Feature_kind: Property = Property(name="kind", type=StringType)
coral_Feature.attributes={coral_Feature_kind}

# coral_EntityModel class attributes and methods

# coral_NamedElement class attributes and methods
coral_NamedElement_name: Property = Property(name="name", type=StringType)
coral_NamedElement.attributes={coral_NamedElement_name}

# coral_Type class attributes and methods

# NamedElement class attributes and methods

# coral_DataType class attributes and methods

# Type class attributes and methods

# Relationships
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="coral_Feature", type=coral_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="coral_Entity", type=coral_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="coral_Type", type=coral_EntityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="coral_EntityModel", type=coral_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="coral_Type4", type=coral_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="coral_Feature3", type=coral_Type, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_coral_Entity_Type = Generalization(general=Type, specific=coral_Entity)
gen_coral_Type_NamedElement = Generalization(general=NamedElement, specific=coral_Type)
gen_coral_DataType_Type = Generalization(general=Type, specific=coral_DataType)
gen_coral_Feature_NamedElement = Generalization(general=NamedElement, specific=coral_Feature)

# Domain Model
domain_model = DomainModel(
    name="coral",
    types={coral_Entity, coral_Feature, coral_EntityModel, coral_NamedElement, coral_Type, NamedElement, coral_DataType, Type, FeatureKind},
    associations={features0, types1, type2},
    generalizations={gen_coral_Entity_Type, gen_coral_Type_NamedElement, gen_coral_DataType_Type, gen_coral_Feature_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)