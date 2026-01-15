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
source_Attribute = Class(name="source::Attribute")
source_Association = Class(name="source::Association")
source_Class = Class(name="source::Class")
source_PrimitiveDataType = Class(name="source::PrimitiveDataType")
source_ClassDiagram = Class(name="source::ClassDiagram")

# source_Attribute class attributes and methods
source_Attribute_name: Property = Property(name="name", type=StringType)
source_Attribute_is_primary: Property = Property(name="is_primary", type=BooleanType)
source_Attribute.attributes={source_Attribute_is_primary, source_Attribute_name}

# source_Association class attributes and methods
source_Association_name: Property = Property(name="name", type=StringType)
source_Association.attributes={source_Association_name}

# source_Class class attributes and methods
source_Class_name: Property = Property(name="name", type=StringType)
source_Class.attributes={source_Class_name}

# source_PrimitiveDataType class attributes and methods
source_PrimitiveDataType_name: Property = Property(name="name", type=StringType)
source_PrimitiveDataType.attributes={source_PrimitiveDataType_name}

# source_ClassDiagram class attributes and methods

# Relationships
attrs2: BinaryAssociation = BinaryAssociation(
    name="attrs2",
    ends={
        Property(name="source_Attribute", type=source_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source_Class3", type=source_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
src4: BinaryAssociation = BinaryAssociation(
    name="src4",
    ends={
        Property(name="source_Class5", type=source_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="source_Association", type=source_Class, multiplicity=Multiplicity(1, 1))
    }
)
dest6: BinaryAssociation = BinaryAssociation(
    name="dest6",
    ends={
        Property(name="source_Class8", type=source_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="source_Association7", type=source_Class, multiplicity=Multiplicity(1, 1))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="source_Class11", type=source_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="source_Attribute10", type=source_Class, multiplicity=Multiplicity(0, 1))
    }
)
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="source_Class", type=source_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source_Class0", type=source_Class, multiplicity=Multiplicity(0, 1))
    }
)
class14: BinaryAssociation = BinaryAssociation(
    name="class14",
    ends={
        Property(name="source_Class15", type=source_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="source_ClassDiagram", type=source_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ass16: BinaryAssociation = BinaryAssociation(
    name="ass16",
    ends={
        Property(name="source_Association18", type=source_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="source_ClassDiagram17", type=source_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ptypes19: BinaryAssociation = BinaryAssociation(
    name="ptypes19",
    ends={
        Property(name="source_PrimitiveDataType21", type=source_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="source_ClassDiagram20", type=source_PrimitiveDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ptype12: BinaryAssociation = BinaryAssociation(
    name="ptype12",
    ends={
        Property(name="source_PrimitiveDataType", type=source_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="source_Attribute13", type=source_PrimitiveDataType, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="source",
    types={source_Attribute, source_Association, source_Class, source_PrimitiveDataType, source_ClassDiagram},
    associations={attrs2, src4, dest6, type9, parent1, class14, ass16, ptypes19, ptype12},
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