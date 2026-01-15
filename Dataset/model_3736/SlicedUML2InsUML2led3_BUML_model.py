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
UML2_LinkEndCreationData = Class(name="UML2::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
UML2_Port = Class(name="UML2::Port")
UML2_ExtensionEnd = Class(name="UML2::ExtensionEnd")
Property_ = Class(name="Property")
UML2_LinkEndData = Class(name="UML2::LinkEndData")
UML2_Property = Class(name="UML2::Property")
UML2_QualifierValue = Class(name="UML2::QualifierValue")

# UML2_LinkEndCreationData class attributes and methods

# LinkEndData class attributes and methods

# UML2_Port class attributes and methods

# UML2_ExtensionEnd class attributes and methods

# Property class attributes and methods

# UML2_LinkEndData class attributes and methods

# UML2_Property class attributes and methods

# UML2_QualifierValue class attributes and methods

# Relationships
qualifier4: BinaryAssociation = BinaryAssociation(
    name="qualifier4",
    ends={
        Property(name="UML2_Property5", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Property3", type=UML2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier6: BinaryAssociation = BinaryAssociation(
    name="qualifier6",
    ends={
        Property(name="UML2_Property8", type=UML2_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_QualifierValue7", type=UML2_Property, multiplicity=Multiplicity(1, 1))
    }
)
end0: BinaryAssociation = BinaryAssociation(
    name="end0",
    ends={
        Property(name="UML2_Property", type=UML2_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LinkEndData", type=UML2_Property, multiplicity=Multiplicity(1, 1))
    }
)
qualifier1: BinaryAssociation = BinaryAssociation(
    name="qualifier1",
    ends={
        Property(name="UML2_QualifierValue", type=UML2_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LinkEndData2", type=UML2_QualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UML2_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=UML2_LinkEndCreationData)
gen_UML2_Port_Property = Generalization(general=Property_, specific=UML2_Port)
gen_UML2_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2_ExtensionEnd)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_LinkEndCreationData, LinkEndData, UML2_Port, UML2_ExtensionEnd, Property_, UML2_LinkEndData, UML2_Property, UML2_QualifierValue},
    associations={qualifier4, qualifier6, end0, qualifier1},
    generalizations={gen_UML2_LinkEndCreationData_LinkEndData, gen_UML2_Port_Property, gen_UML2_ExtensionEnd_Property},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)