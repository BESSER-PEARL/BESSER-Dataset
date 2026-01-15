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
Data_Method = Class(name="Data::Method")
Data_Parameter = Class(name="Data::Parameter")

# Data_Model class attributes and methods

# Data_Class class attributes and methods
Data_Class_name: Property = Property(name="name", type=StringType)
Data_Class.attributes={Data_Class_name}

# Data_Attribute class attributes and methods
Data_Attribute_name: Property = Property(name="name", type=StringType)
Data_Attribute_type: Property = Property(name="type", type=StringType)
Data_Attribute_encapsulation: Property = Property(name="encapsulation", type=StringType)
Data_Attribute.attributes={Data_Attribute_type, Data_Attribute_name, Data_Attribute_encapsulation}

# Data_Method class attributes and methods
Data_Method_return: Property = Property(name="return", type=StringType)
Data_Method_encapsulation: Property = Property(name="encapsulation", type=StringType)
Data_Method_name: Property = Property(name="name", type=StringType)
Data_Method.attributes={Data_Method_encapsulation, Data_Method_name, Data_Method_return}

# Data_Parameter class attributes and methods
Data_Parameter_name: Property = Property(name="name", type=StringType)
Data_Parameter_type: Property = Property(name="type", type=StringType)
Data_Parameter.attributes={Data_Parameter_type, Data_Parameter_name}

# Relationships
class0: BinaryAssociation = BinaryAssociation(
    name="class0",
    ends={
        Property(name="Data_Class", type=Data_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Model", type=Data_Class, multiplicity=Multiplicity(0, 9999))
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="Data_Attribute", type=Data_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Class2", type=Data_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
methods3: BinaryAssociation = BinaryAssociation(
    name="methods3",
    ends={
        Property(name="Data_Method", type=Data_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Class4", type=Data_Method, multiplicity=Multiplicity(0, 9999))
    }
)
Parameters5: BinaryAssociation = BinaryAssociation(
    name="Parameters5",
    ends={
        Property(name="Data_Parameter", type=Data_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Method6", type=Data_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Data",
    types={Data_Model, Data_Class, Data_Attribute, Data_Method, Data_Parameter},
    associations={class0, attributes1, methods3, Parameters5},
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