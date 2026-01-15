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
helloScoping_Model = Class(name="helloScoping::Model")
helloScoping_Greeting = Class(name="helloScoping::Greeting")
helloScoping_Field = Class(name="helloScoping::Field")
helloScoping_FieldReference = Class(name="helloScoping::FieldReference")

# helloScoping_Model class attributes and methods

# helloScoping_Greeting class attributes and methods
helloScoping_Greeting_name: Property = Property(name="name", type=StringType)
helloScoping_Greeting.attributes={helloScoping_Greeting_name}

# helloScoping_Field class attributes and methods
helloScoping_Field_name: Property = Property(name="name", type=StringType)
helloScoping_Field.attributes={helloScoping_Field_name}

# helloScoping_FieldReference class attributes and methods

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="helloScoping_Greeting", type=helloScoping_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="helloScoping_Model", type=helloScoping_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType2: BinaryAssociation = BinaryAssociation(
    name="superType2",
    ends={
        Property(name="helloScoping_Greeting3", type=helloScoping_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="helloScoping_Greeting1", type=helloScoping_Greeting, multiplicity=Multiplicity(0, 1))
    }
)
fields4: BinaryAssociation = BinaryAssociation(
    name="fields4",
    ends={
        Property(name="helloScoping_Field", type=helloScoping_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="helloScoping_Greeting5", type=helloScoping_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references6: BinaryAssociation = BinaryAssociation(
    name="references6",
    ends={
        Property(name="helloScoping_FieldReference", type=helloScoping_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="helloScoping_Greeting7", type=helloScoping_FieldReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference8: BinaryAssociation = BinaryAssociation(
    name="reference8",
    ends={
        Property(name="helloScoping_Field10", type=helloScoping_FieldReference, multiplicity=Multiplicity(1, 1)),
        Property(name="helloScoping_FieldReference9", type=helloScoping_Field, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="helloScoping",
    types={helloScoping_Model, helloScoping_Greeting, helloScoping_Field, helloScoping_FieldReference},
    associations={greetings0, superType2, fields4, references6, reference8},
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