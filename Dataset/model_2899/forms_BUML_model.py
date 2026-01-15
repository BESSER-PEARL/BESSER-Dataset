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
forms_Feature = Class(name="forms::Feature")
forms_EntityModel = Class(name="forms::EntityModel")
forms_NamedElement = Class(name="forms::NamedElement", is_abstract=True)
forms_Type = Class(name="forms::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
forms_DataType = Class(name="forms::DataType")
Type = Class(name="Type")
forms_Entity = Class(name="forms::Entity")

# forms_Feature class attributes and methods
forms_Feature_kind: Property = Property(name="kind", type=StringType)
forms_Feature.attributes={forms_Feature_kind}

# forms_EntityModel class attributes and methods

# forms_NamedElement class attributes and methods
forms_NamedElement_name: Property = Property(name="name", type=StringType)
forms_NamedElement.attributes={forms_NamedElement_name}

# forms_Type class attributes and methods

# NamedElement class attributes and methods

# forms_DataType class attributes and methods

# Type class attributes and methods

# forms_Entity class attributes and methods
forms_Entity_abstract: Property = Property(name="abstract", type=BooleanType)
forms_Entity.attributes={forms_Entity_abstract}

# Relationships
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="forms_Feature", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity", type=forms_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="forms_Type", type=forms_EntityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EntityModel", type=forms_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="forms_Type4", type=forms_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Feature3", type=forms_Type, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_forms_Feature_NamedElement = Generalization(general=NamedElement, specific=forms_Feature)
gen_forms_Type_NamedElement = Generalization(general=NamedElement, specific=forms_Type)
gen_forms_DataType_Type = Generalization(general=Type, specific=forms_DataType)
gen_forms_Entity_Type = Generalization(general=Type, specific=forms_Entity)

# Domain Model
domain_model = DomainModel(
    name="forms",
    types={forms_Feature, forms_EntityModel, forms_NamedElement, forms_Type, NamedElement, forms_DataType, Type, forms_Entity, FeatureKind},
    associations={features0, types1, type2},
    generalizations={gen_forms_Feature_NamedElement, gen_forms_Type_NamedElement, gen_forms_DataType_Type, gen_forms_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)