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
classdiagram_ClassDiagram = Class(name="classdiagram::ClassDiagram")
classdiagram_Class = Class(name="classdiagram::Class")
classdiagram_Attribute = Class(name="classdiagram::Attribute")

# classdiagram_ClassDiagram class attributes and methods

# classdiagram_Class class attributes and methods
classdiagram_Class_name: Property = Property(name="name", type=StringType)
classdiagram_Class.attributes={classdiagram_Class_name}

# classdiagram_Attribute class attributes and methods
classdiagram_Attribute_name: Property = Property(name="name", type=StringType)
classdiagram_Attribute.attributes={classdiagram_Attribute_name}

# Relationships
attrs3: BinaryAssociation = BinaryAssociation(
    name="attrs3",
    ends={
        Property(name="classdiagram_Attribute5", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Class4", type=classdiagram_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="classdiagram_Class", type=classdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_ClassDiagram", type=classdiagram_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrs1: BinaryAssociation = BinaryAssociation(
    name="attrs1",
    ends={
        Property(name="classdiagram_Attribute", type=classdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_ClassDiagram2", type=classdiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="classdiagram",
    types={classdiagram_ClassDiagram, classdiagram_Class, classdiagram_Attribute},
    associations={attrs3, classes0, attrs1},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)