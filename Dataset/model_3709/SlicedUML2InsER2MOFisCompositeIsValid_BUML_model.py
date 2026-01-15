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
AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="composite"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared")
    }
)

# Classes
UML2_ExtensionEnd = Class(name="UML2::ExtensionEnd")
Property_ = Class(name="Property")
UML2_Property = Class(name="UML2::Property")
UML2_Port = Class(name="UML2::Port")

# UML2_ExtensionEnd class attributes and methods

# Property class attributes and methods

# UML2_Property class attributes and methods
UML2_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
UML2_Property_aggregation: Property = Property(name="aggregation", type=StringType)
UML2_Property.attributes={UML2_Property_isComposite, UML2_Property_aggregation}

# UML2_Port class attributes and methods

# Generalizations
gen_UML2_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2_ExtensionEnd)
gen_UML2_Port_Property = Generalization(general=Property_, specific=UML2_Port)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_ExtensionEnd, Property_, UML2_Property, UML2_Port, AggregationKind},
    associations={},
    generalizations={gen_UML2_ExtensionEnd_Property, gen_UML2_Port_Property},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)