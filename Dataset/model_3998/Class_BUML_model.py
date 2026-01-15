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
Class_Class = Class(name="Class::Class")
Class_Attribute = Class(name="Class::Attribute")

# Class_Class class attributes and methods
Class_Class_id: Property = Property(name="id", type=StringType)
Class_Class_name: Property = Property(name="name", type=StringType)
Class_Class.attributes={Class_Class_name, Class_Class_id}

# Class_Attribute class attributes and methods
Class_Attribute_id: Property = Property(name="id", type=StringType)
Class_Attribute_multiValued: Property = Property(name="multiValued", type=BooleanType)
Class_Attribute_name: Property = Property(name="name", type=StringType)
Class_Attribute.attributes={Class_Attribute_multiValued, Class_Attribute_id, Class_Attribute_name}

# Relationships
attributes0: BinaryAssociation = BinaryAssociation(
    name="attributes0",
    ends={
        Property(name="Attribute", type=Class_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=Class_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="Class", type=Class_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=Class_Class, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Class",
    types={Class_Class, Class_Attribute},
    associations={attributes0, type1},
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