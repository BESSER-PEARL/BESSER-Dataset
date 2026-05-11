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
extmetadata_NamedElement = Class(name="extmetadata_NamedElement")
extmetadata_Class = Class(name="extmetadata_Class")
NamedElement = Class(name="NamedElement")
extmetadata_Attribute = Class(name="extmetadata_Attribute")

# extmetadata_NamedElement class attributes and methods
extmetadata_NamedElement_name: Property = Property(name="name", type=StringType)
extmetadata_NamedElement.attributes={extmetadata_NamedElement_name}

# extmetadata_Class class attributes and methods

# NamedElement class attributes and methods

# extmetadata_Attribute class attributes and methods

# Relationships
attribute0: BinaryAssociation = BinaryAssociation(
    name="attribute0",
    ends={
        Property(name="extmetadata_Attribute", type=extmetadata_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="extmetadata_Class", type=extmetadata_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="extmetadata_Class3", type=extmetadata_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="extmetadata_Attribute2", type=extmetadata_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_extmetadata_Class_NamedElement = Generalization(general=NamedElement, specific=extmetadata_Class)
gen_extmetadata_Attribute_NamedElement = Generalization(general=NamedElement, specific=extmetadata_Attribute)

# Domain Model
domain_model = DomainModel(
    name="extmetadata",
    types={extmetadata_NamedElement, extmetadata_Class, NamedElement, extmetadata_Attribute},
    associations={attribute0, type1},
    generalizations={gen_extmetadata_Class_NamedElement, gen_extmetadata_Attribute_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)