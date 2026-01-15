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
Data_Field = Class(name="Data::Field")
Data_Model = Class(name="Data::Model")
Data_Class = Class(name="Data::Class")

# Data_Field class attributes and methods
Data_Field_name: Property = Property(name="name", type=StringType)
Data_Field_type: Property = Property(name="type", type=StringType)
Data_Field_modifier: Property = Property(name="modifier", type=StringType)
Data_Field.attributes={Data_Field_type, Data_Field_name, Data_Field_modifier}

# Data_Model class attributes and methods

# Data_Class class attributes and methods
Data_Class_name: Property = Property(name="name", type=StringType)
Data_Class.attributes={Data_Class_name}

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="Data_Model", type=Data_Class, multiplicity=Multiplicity(0, 9999)),
        Property(name="Data_Class", type=Data_Model, multiplicity=Multiplicity(1, 1))
    }
)
fields1: BinaryAssociation = BinaryAssociation(
    name="fields1",
    ends={
        Property(name="Data_Field", type=Data_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Class2", type=Data_Field, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Data",
    types={Data_Field, Data_Model, Data_Class},
    associations={classes0, fields1},
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