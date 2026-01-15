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
bombXML_NamedElement = Class(name="bombXML::NamedElement", is_abstract=True)
bombXML_Type = Class(name="bombXML::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
bombXML_DataType = Class(name="bombXML::DataType")
Type = Class(name="Type")
bombXML_Entity = Class(name="bombXML::Entity")
bombXML_Feature = Class(name="bombXML::Feature")
bombXML_EntityModel = Class(name="bombXML::EntityModel")

# bombXML_NamedElement class attributes and methods
bombXML_NamedElement_name: Property = Property(name="name", type=StringType)
bombXML_NamedElement.attributes={bombXML_NamedElement_name}

# bombXML_Type class attributes and methods

# NamedElement class attributes and methods

# bombXML_DataType class attributes and methods

# Type class attributes and methods

# bombXML_Entity class attributes and methods
bombXML_Entity_abstract: Property = Property(name="abstract", type=BooleanType)
bombXML_Entity.attributes={bombXML_Entity_abstract}

# bombXML_Feature class attributes and methods
bombXML_Feature_kind: Property = Property(name="kind", type=StringType)
bombXML_Feature.attributes={bombXML_Feature_kind}

# bombXML_EntityModel class attributes and methods

# Relationships
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="bombXML_Feature", type=bombXML_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="bombXML_Entity", type=bombXML_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="bombXML_Type", type=bombXML_EntityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="bombXML_EntityModel", type=bombXML_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="bombXML_Type4", type=bombXML_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="bombXML_Feature3", type=bombXML_Type, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_bombXML_Type_NamedElement = Generalization(general=NamedElement, specific=bombXML_Type)
gen_bombXML_DataType_Type = Generalization(general=Type, specific=bombXML_DataType)
gen_bombXML_Entity_Type = Generalization(general=Type, specific=bombXML_Entity)
gen_bombXML_Feature_NamedElement = Generalization(general=NamedElement, specific=bombXML_Feature)

# Domain Model
domain_model = DomainModel(
    name="bombXML",
    types={bombXML_NamedElement, bombXML_Type, NamedElement, bombXML_DataType, Type, bombXML_Entity, bombXML_Feature, bombXML_EntityModel, FeatureKind},
    associations={features0, types1, type2},
    generalizations={gen_bombXML_Type_NamedElement, gen_bombXML_DataType_Type, gen_bombXML_Entity_Type, gen_bombXML_Feature_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)