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
classdiagram_NamedElement = Class(name="classdiagram::NamedElement")
classdiagram_Method = Class(name="classdiagram::Method")
classdiagram_Class = Class(name="classdiagram::Class")
NamedElement = Class(name="NamedElement")
classdiagram_Attribute = Class(name="classdiagram::Attribute")

# classdiagram_NamedElement class attributes and methods
classdiagram_NamedElement_name: Property = Property(name="name", type=StringType)
classdiagram_NamedElement.attributes={classdiagram_NamedElement_name}

# classdiagram_Method class attributes and methods

# classdiagram_Class class attributes and methods

# NamedElement class attributes and methods

# classdiagram_Attribute class attributes and methods

# Relationships
methods6: BinaryAssociation = BinaryAssociation(
    name="methods6",
    ends={
        Property(name="classdiagram_Method", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Class7", type=classdiagram_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super1: BinaryAssociation = BinaryAssociation(
    name="super1",
    ends={
        Property(name="Class", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=classdiagram_Class, multiplicity=Multiplicity(0, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="Class4", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="super", type=classdiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="classdiagram_Attribute", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Class", type=classdiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_classdiagram_Attribute_NamedElement = Generalization(general=NamedElement, specific=classdiagram_Attribute)
gen_classdiagram_Method_NamedElement = Generalization(general=NamedElement, specific=classdiagram_Method)
gen_classdiagram_Class_NamedElement = Generalization(general=NamedElement, specific=classdiagram_Class)

# Domain Model
domain_model = DomainModel(
    name="classdiagram",
    types={classdiagram_NamedElement, classdiagram_Method, classdiagram_Class, NamedElement, classdiagram_Attribute},
    associations={methods6, super1, children3, attributes5},
    generalizations={gen_classdiagram_Attribute_NamedElement, gen_classdiagram_Method_NamedElement, gen_classdiagram_Class_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)