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
hbmxml_EntityModel = Class(name="hbmxml::EntityModel")
hbmxml_NamedElement = Class(name="hbmxml::NamedElement", is_abstract=True)
hbmxml_Type = Class(name="hbmxml::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
hbmxml_DataType = Class(name="hbmxml::DataType")
Type = Class(name="Type")
hbmxml_Entity = Class(name="hbmxml::Entity")
hbmxml_Feature = Class(name="hbmxml::Feature")

# hbmxml_EntityModel class attributes and methods

# hbmxml_NamedElement class attributes and methods
hbmxml_NamedElement_name: Property = Property(name="name", type=StringType)
hbmxml_NamedElement.attributes={hbmxml_NamedElement_name}

# hbmxml_Type class attributes and methods

# NamedElement class attributes and methods

# hbmxml_DataType class attributes and methods

# Type class attributes and methods

# hbmxml_Entity class attributes and methods
hbmxml_Entity_abstract: Property = Property(name="abstract", type=BooleanType)
hbmxml_Entity.attributes={hbmxml_Entity_abstract}

# hbmxml_Feature class attributes and methods
hbmxml_Feature_kind: Property = Property(name="kind", type=StringType)
hbmxml_Feature.attributes={hbmxml_Feature_kind}

# Relationships
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="hbmxml_Type", type=hbmxml_EntityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="hbmxml_EntityModel", type=hbmxml_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="hbmxml_Type4", type=hbmxml_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="hbmxml_Feature3", type=hbmxml_Type, multiplicity=Multiplicity(1, 1))
    }
)
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="hbmxml_Feature", type=hbmxml_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="hbmxml_Entity", type=hbmxml_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_hbmxml_Feature_NamedElement = Generalization(general=NamedElement, specific=hbmxml_Feature)
gen_hbmxml_Type_NamedElement = Generalization(general=NamedElement, specific=hbmxml_Type)
gen_hbmxml_DataType_Type = Generalization(general=Type, specific=hbmxml_DataType)
gen_hbmxml_Entity_Type = Generalization(general=Type, specific=hbmxml_Entity)

# Domain Model
domain_model = DomainModel(
    name="hbmxml",
    types={hbmxml_EntityModel, hbmxml_NamedElement, hbmxml_Type, NamedElement, hbmxml_DataType, Type, hbmxml_Entity, hbmxml_Feature, FeatureKind},
    associations={types1, type2, features0},
    generalizations={gen_hbmxml_Feature_NamedElement, gen_hbmxml_Type_NamedElement, gen_hbmxml_DataType_Type, gen_hbmxml_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)