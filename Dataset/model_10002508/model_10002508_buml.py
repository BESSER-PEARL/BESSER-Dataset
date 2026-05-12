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
Value = Class(name="Value", is_abstract=True)
Null = Class(name="Null")
String = Class(name="String")
Bool = Class(name="Bool")
Number = Class(name="Number")
Array = Class(name="Array")
Visitor = Class(name="Visitor")
Json = Class(name="Json")
Documents = Class(name="Documents")
Print = Class(name="Print")
ArrPrint = Class(name="ArrPrint")
NamedCapabilityMetadata = Class(name="NamedCapabilityMetadata")
NamedCapabilityMetadata1 = Class(name="NamedCapabilityMetadata1")

# Value class attributes and methods
Value_attribute: Property = Property(name="attribute", type=StringType)
Value.attributes={Value_attribute}

# Null class attributes and methods

# String class attributes and methods
String_data: Property = Property(name="data", type=String)
String.attributes={String_data}

# Bool class attributes and methods
Bool_data: Property = Property(name="data", type=BooleanType)
Bool.attributes={Bool_data}

# Number class attributes and methods
Number_data: Property = Property(name="data", type=IntegerType)
Number.attributes={Number_data}

# Array class attributes and methods
Array_data: Property = Property(name="data", type=Value)
Array.attributes={Array_data}

# Visitor class attributes and methods

# Json class attributes and methods
Json_values: Property = Property(name="values", type=Value)
Json.attributes={Json_values}

# Documents class attributes and methods
Documents_tab_counter: Property = Property(name="tab_counter", type=IntegerType)
Documents_file: Property = Property(name="file", type=StringType)
Documents_data: Property = Property(name="data", type=Json)
Documents_file_name: Property = Property(name="file_name", type=StringType)
Documents.attributes={Documents_tab_counter, Documents_file, Documents_file_name, Documents_data}

# Print class attributes and methods

# ArrPrint class attributes and methods

# NamedCapabilityMetadata class attributes and methods

# NamedCapabilityMetadata1 class attributes and methods
NamedCapabilityMetadata1_name: Property = Property(name="name", type=StringType)
NamedCapabilityMetadata1.attributes={NamedCapabilityMetadata1_name}

# Domain Model
domain_model = DomainModel(
    name="bb138be6_ee71_4dcb_9ee1_8b8f5db206c7",
    types={Value, Null, String, Bool, Number, Array, Visitor, Json, Documents, Print, ArrPrint, NamedCapabilityMetadata, NamedCapabilityMetadata1},
    associations={},
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