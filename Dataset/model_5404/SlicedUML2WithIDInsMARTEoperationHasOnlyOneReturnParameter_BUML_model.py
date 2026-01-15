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
ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="return")
    }
)

# Classes
UML2WithID_Parameter = Class(name="UML2WithID::Parameter")
UML2WithID_Element = Class(name="UML2WithID::Element", is_abstract=True)
Element = Class(name="Element")
UML2WithID_Operation = Class(name="UML2WithID::Operation")

# UML2WithID_Parameter class attributes and methods
UML2WithID_Parameter_direction: Property = Property(name="direction", type=StringType)
UML2WithID_Parameter.attributes={UML2WithID_Parameter_direction}

# UML2WithID_Element class attributes and methods
UML2WithID_Element_ID: Property = Property(name="ID", type=StringType)
UML2WithID_Element.attributes={UML2WithID_Element_ID}

# Element class attributes and methods

# UML2WithID_Operation class attributes and methods

# Relationships
ownedParameter0: BinaryAssociation = BinaryAssociation(
    name="ownedParameter0",
    ends={
        Property(name="UML2WithID_Parameter", type=UML2WithID_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Operation", type=UML2WithID_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UML2WithID_Parameter_Element = Generalization(general=Element, specific=UML2WithID_Parameter)
gen_UML2WithID_Operation_Element = Generalization(general=Element, specific=UML2WithID_Operation)

# Domain Model
domain_model = DomainModel(
    name="UML2WithID",
    types={UML2WithID_Parameter, UML2WithID_Element, Element, UML2WithID_Operation, ParameterDirectionKind},
    associations={ownedParameter0},
    generalizations={gen_UML2WithID_Parameter_Element, gen_UML2WithID_Operation_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)