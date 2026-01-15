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
family_NamedElement = Class(name="family::NamedElement")
family_Family = Class(name="family::Family")
NamedElement = Class(name="NamedElement")

# family_NamedElement class attributes and methods
family_NamedElement_name: Property = Property(name="name", type=StringType)
family_NamedElement.attributes={family_NamedElement_name}

# family_Family class attributes and methods
family_Family_children: Property = Property(name="children", type=StringType)
family_Family_mother: Property = Property(name="mother", type=StringType)
family_Family_father: Property = Property(name="father", type=StringType)
family_Family.attributes={family_Family_children, family_Family_mother, family_Family_father}

# NamedElement class attributes and methods

# Generalizations
gen_family_Family_NamedElement = Generalization(general=NamedElement, specific=family_Family)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_NamedElement, family_Family, NamedElement},
    associations={},
    generalizations={gen_family_Family_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)