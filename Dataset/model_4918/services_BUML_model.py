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
services_services_EndPoint = Class(name="services::services::EndPoint")
RootElement = Class(name="RootElement")
services_services_Interface = Class(name="services::services::Interface")
Operation = Class(name="Operation")
services_services_EObject = Class(name="services::services::EObject")
services_services_Operation = Class(name="services::services::Operation")
BaseElement = Class(name="BaseElement")
Message = Class(name="Message")
Error = Class(name="Error")

# services_services_EndPoint class attributes and methods

# RootElement class attributes and methods

# services_services_Interface class attributes and methods
services_services_Interface_name: Property = Property(name="name", type=StringType)
services_services_Interface.attributes={services_services_Interface_name}

# Operation class attributes and methods

# services_services_EObject class attributes and methods

# services_services_Operation class attributes and methods
services_services_Operation_name: Property = Property(name="name", type=StringType)
services_services_Operation.attributes={services_services_Operation_name}

# BaseElement class attributes and methods

# Message class attributes and methods

# Error class attributes and methods

# Relationships
operations0: BinaryAssociation = BinaryAssociation(
    name="operations0",
    ends={
        Property(name="Operation", type=services_services_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="services_services_Interface", type=Operation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
implementationRef1: BinaryAssociation = BinaryAssociation(
    name="implementationRef1",
    ends={
        Property(name="services_services_EObject", type=services_services_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="services_services_Interface2", type=services_services_EObject, multiplicity=Multiplicity(0, 1))
    }
)
inMessageRef3: BinaryAssociation = BinaryAssociation(
    name="inMessageRef3",
    ends={
        Property(name="Message", type=services_services_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="services_services_Operation", type=Message, multiplicity=Multiplicity(1, 1))
    }
)
outMessageRef4: BinaryAssociation = BinaryAssociation(
    name="outMessageRef4",
    ends={
        Property(name="Message6", type=services_services_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="services_services_Operation5", type=Message, multiplicity=Multiplicity(0, 1))
    }
)
errorRefs7: BinaryAssociation = BinaryAssociation(
    name="errorRefs7",
    ends={
        Property(name="Error", type=services_services_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="services_services_Operation8", type=Error, multiplicity=Multiplicity(0, 9999))
    }
)
implementationRef9: BinaryAssociation = BinaryAssociation(
    name="implementationRef9",
    ends={
        Property(name="services_services_EObject11", type=services_services_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="services_services_Operation10", type=services_services_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_services_services_EndPoint_RootElement = Generalization(general=RootElement, specific=services_services_EndPoint)
gen_services_services_Interface_RootElement = Generalization(general=RootElement, specific=services_services_Interface)
gen_services_services_Operation_BaseElement = Generalization(general=BaseElement, specific=services_services_Operation)

# Domain Model
domain_model = DomainModel(
    name="services",
    types={services_services_EndPoint, RootElement, services_services_Interface, Operation, services_services_EObject, services_services_Operation, BaseElement, Message, Error},
    associations={operations0, implementationRef1, inMessageRef3, outMessageRef4, errorRefs7, implementationRef9},
    generalizations={gen_services_services_EndPoint_RootElement, gen_services_services_Interface_RootElement, gen_services_services_Operation_BaseElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)