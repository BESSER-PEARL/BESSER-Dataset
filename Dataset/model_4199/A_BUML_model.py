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
a_Model = Class(name="a::Model")
a_PackageDeclaration = Class(name="a::PackageDeclaration")
a_Greeting = Class(name="a::Greeting")

# a_Model class attributes and methods

# a_PackageDeclaration class attributes and methods
a_PackageDeclaration_name: Property = Property(name="name", type=StringType)
a_PackageDeclaration.attributes={a_PackageDeclaration_name}

# a_Greeting class attributes and methods
a_Greeting_name: Property = Property(name="name", type=StringType)
a_Greeting.attributes={a_Greeting_name}

# Relationships
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="a_PackageDeclaration", type=a_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="a_Model", type=a_PackageDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
greetings1: BinaryAssociation = BinaryAssociation(
    name="greetings1",
    ends={
        Property(name="a_Greeting", type=a_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="a_PackageDeclaration2", type=a_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="a",
    types={a_Model, a_PackageDeclaration, a_Greeting},
    associations={package0, greetings1},
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