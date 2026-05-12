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
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
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
Issue = Class(name="Issue")
Card = Class(name="Card", is_abstract=True)
Sprint = Class(name="Sprint")
UserStory = Class(name="UserStory")
Steppable_Interface = Class(name="Steppable_Interface")
Descripible_Interface = Class(name="Descripible_Interface")
CardGroup = Class(name="CardGroup", is_abstract=True)
SimpleCard = Class(name="SimpleCard")

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
Documents_file: Property = Property(name="file", type=StringType)
Documents_data: Property = Property(name="data", type=Json)
Documents_file_name: Property = Property(name="file_name", type=StringType)
Documents_tab_counter: Property = Property(name="tab_counter", type=IntegerType)
Documents.attributes={Documents_file_name, Documents_file, Documents_data, Documents_tab_counter}

# Print class attributes and methods

# ArrPrint class attributes and methods

# Issue class attributes and methods

# Card class attributes and methods

# Sprint class attributes and methods

# UserStory class attributes and methods

# Steppable_Interface class attributes and methods

# Descripible_Interface class attributes and methods

# CardGroup class attributes and methods

# SimpleCard class attributes and methods

# Relationships
Sprint_Card: BinaryAssociation = BinaryAssociation(
    name="Sprint_Card",
    ends={
        Property(name="cards0", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="sprints1", type=Sprint, multiplicity=Multiplicity(0, 9999))
    }
)
Sprint_UserStory: BinaryAssociation = BinaryAssociation(
    name="Sprint_UserStory",
    ends={
        Property(name="groups2", type=CardGroup, multiplicity=Multiplicity(0, 9999)),
        Property(name="sprints3", type=Sprint, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7486a0e2_ed6b_41a2_93b0_427ecbbc50ec",
    types={Value, Null, String, Bool, Number, Array, Visitor, Json, Documents, Print, ArrPrint, Issue, Card, Sprint, UserStory, Steppable_Interface, Descripible_Interface, CardGroup, SimpleCard, Enumeration_},
    associations={Sprint_Card, Sprint_UserStory},
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