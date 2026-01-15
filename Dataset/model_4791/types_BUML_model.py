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
NamedElement = Class(name="NamedElement")
types_Feature = Class(name="types::Feature", is_abstract=True)
TypedElement = Class(name="TypedElement")
types_Operation = Class(name="types::Operation")
Feature = Class(name="Feature")
types_Parameter = Class(name="types::Parameter")
types_Property = Class(name="types::Property")
types_TypedElement = Class(name="types::TypedElement", is_abstract=True)
types_Event = Class(name="types::Event")
types_Library = Class(name="types::Library")
types_Type = Class(name="types::Type")

# NamedElement class attributes and methods

# types_Feature class attributes and methods

# TypedElement class attributes and methods

# types_Operation class attributes and methods

# Feature class attributes and methods

# types_Parameter class attributes and methods

# types_Property class attributes and methods

# types_TypedElement class attributes and methods

# types_Event class attributes and methods

# types_Library class attributes and methods
types_Library_id: Property = Property(name="id", type=StringType)
types_Library.attributes={types_Library_id}

# types_Type class attributes and methods

# Relationships
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="Feature", type=types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="owningType", type=types_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superTypes3: BinaryAssociation = BinaryAssociation(
    name="superTypes3",
    ends={
        Property(name="types_Type", type=types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Type2", type=types_Type, multiplicity=Multiplicity(0, 9999))
    }
)
owningLibrary4: BinaryAssociation = BinaryAssociation(
    name="owningLibrary4",
    ends={
        Property(name="Library", type=types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="types", type=types_Library, multiplicity=Multiplicity(0, 1))
    }
)
owningType5: BinaryAssociation = BinaryAssociation(
    name="owningType5",
    ends={
        Property(name="Type6", type=types_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
parameters7: BinaryAssociation = BinaryAssociation(
    name="parameters7",
    ends={
        Property(name="Parameter", type=types_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=types_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningOperation8: BinaryAssociation = BinaryAssociation(
    name="owningOperation8",
    ends={
        Property(name="Operation", type=types_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=types_Operation, multiplicity=Multiplicity(0, 1))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="types_Type10", type=types_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypedElement", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="Type", type=types_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="owningLibrary", type=types_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_types_Type_NamedElement = Generalization(general=NamedElement, specific=types_Type)
gen_types_Feature_TypedElement = Generalization(general=TypedElement, specific=types_Feature)
gen_types_Feature_NamedElement = Generalization(general=NamedElement, specific=types_Feature)
gen_types_Operation_Feature = Generalization(general=Feature, specific=types_Operation)
gen_types_Property_Feature = Generalization(general=Feature, specific=types_Property)
gen_types_Parameter_TypedElement = Generalization(general=TypedElement, specific=types_Parameter)
gen_types_Parameter_NamedElement = Generalization(general=NamedElement, specific=types_Parameter)
gen_types_Event_Feature = Generalization(general=Feature, specific=types_Event)

# Domain Model
domain_model = DomainModel(
    name="types",
    types={NamedElement, types_Feature, TypedElement, types_Operation, Feature, types_Parameter, types_Property, types_TypedElement, types_Event, types_Library, types_Type},
    associations={features1, superTypes3, owningLibrary4, owningType5, parameters7, owningOperation8, type9, types0},
    generalizations={gen_types_Type_NamedElement, gen_types_Feature_TypedElement, gen_types_Feature_NamedElement, gen_types_Operation_Feature, gen_types_Property_Feature, gen_types_Parameter_TypedElement, gen_types_Parameter_NamedElement, gen_types_Event_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)