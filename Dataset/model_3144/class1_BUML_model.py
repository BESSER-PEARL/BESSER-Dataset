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
Visibility: Enumeration = Enumeration(
    name="Visibility",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private")
    }
)

# Classes
classm1_Class = Class(name="classm1::Class")
CNamedElement = Class(name="CNamedElement")
classm1_Attribute = Class(name="classm1::Attribute")
classm1_CNamedElement = Class(name="classm1::CNamedElement", is_abstract=True)

# classm1_Class class attributes and methods

# CNamedElement class attributes and methods

# classm1_Attribute class attributes and methods
classm1_Attribute_isKey: Property = Property(name="isKey", type=BooleanType)
classm1_Attribute_visibility: Property = Property(name="visibility", type=StringType)
classm1_Attribute.attributes={classm1_Attribute_visibility, classm1_Attribute_isKey}

# classm1_CNamedElement class attributes and methods
classm1_CNamedElement_name: Property = Property(name="name", type=StringType)
classm1_CNamedElement.attributes={classm1_CNamedElement_name}

# Relationships
attrs0: BinaryAssociation = BinaryAssociation(
    name="attrs0",
    ends={
        Property(name="classm1_Attribute", type=classm1_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classm1_Class", type=classm1_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="classm1_Class3", type=classm1_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="classm1_Attribute2", type=classm1_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_classm1_Class_CNamedElement = Generalization(general=CNamedElement, specific=classm1_Class)
gen_classm1_Attribute_CNamedElement = Generalization(general=CNamedElement, specific=classm1_Attribute)

# Domain Model
domain_model = DomainModel(
    name="classm1",
    types={classm1_Class, CNamedElement, classm1_Attribute, classm1_CNamedElement, Visibility},
    associations={attrs0, type1},
    generalizations={gen_classm1_Class_CNamedElement, gen_classm1_Attribute_CNamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)