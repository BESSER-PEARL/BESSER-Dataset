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
Data_Model = Class(name="Data::Model")
Data_Class = Class(name="Data::Class")
Data_Attribute = Class(name="Data::Attribute")

# Data_Model class attributes and methods
Data_Model_name: Property = Property(name="name", type=StringType)
Data_Model.attributes={Data_Model_name}

# Data_Class class attributes and methods
Data_Class_name: Property = Property(name="name", type=StringType)
Data_Class.attributes={Data_Class_name}

# Data_Attribute class attributes and methods
Data_Attribute_name: Property = Property(name="name", type=StringType)
Data_Attribute_type: Property = Property(name="type", type=StringType)
Data_Attribute.attributes={Data_Attribute_type, Data_Attribute_name}

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="Data_Class", type=Data_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Model", type=Data_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="Data_Attribute", type=Data_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Class2", type=Data_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Data",
    types={Data_Model, Data_Class, Data_Attribute},
    associations={classes0, attributes1},
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