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
testport_Component = Class(name="testport::Component", is_abstract=True)
testport_Required = Class(name="testport::Required")
testport_Base = Class(name="testport::Base")
Component = Class(name="Component")

# testport_Component class attributes and methods
testport_Component_name: Property = Property(name="name", type=StringType)
testport_Component.attributes={testport_Component_name}

# testport_Required class attributes and methods

# testport_Base class attributes and methods

# Component class attributes and methods

# Relationships
requiredInterfaces0: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces0",
    ends={
        Property(name="testport_Required", type=testport_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="testport_Component", type=testport_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components2: BinaryAssociation = BinaryAssociation(
    name="components2",
    ends={
        Property(name="testport_Base", type=testport_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="testport_Base1", type=testport_Base, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_testport_Base_Component = Generalization(general=Component, specific=testport_Base)

# Domain Model
domain_model = DomainModel(
    name="testport",
    types={testport_Component, testport_Required, testport_Base, Component},
    associations={requiredInterfaces0, components2},
    generalizations={gen_testport_Base_Component},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)