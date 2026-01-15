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
visType: Enumeration = Enumeration(
    name="visType",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private")
    }
)

# Classes
umlsimp_ModelElement = Class(name="umlsimp::ModelElement", is_abstract=True)
umlsimp_DataType = Class(name="umlsimp::DataType")
ModelElement = Class(name="ModelElement")
umlsimp_Class = Class(name="umlsimp::Class")
umlsimp_Property = Class(name="umlsimp::Property")
umlsimp_Operation = Class(name="umlsimp::Operation")
TypedElement = Class(name="TypedElement")
umlsimp_Parameter = Class(name="umlsimp::Parameter")
umlsimp_TypedElement = Class(name="umlsimp::TypedElement")
umlsimp_Model = Class(name="umlsimp::Model")

# umlsimp_ModelElement class attributes and methods
umlsimp_ModelElement_name: Property = Property(name="name", type=StringType)
umlsimp_ModelElement.attributes={umlsimp_ModelElement_name}

# umlsimp_DataType class attributes and methods

# ModelElement class attributes and methods

# umlsimp_Class class attributes and methods

# umlsimp_Property class attributes and methods
umlsimp_Property_visibility: Property = Property(name="visibility", type=StringType)
umlsimp_Property.attributes={umlsimp_Property_visibility}

# umlsimp_Operation class attributes and methods

# TypedElement class attributes and methods

# umlsimp_Parameter class attributes and methods

# umlsimp_TypedElement class attributes and methods

# umlsimp_Model class attributes and methods

# Relationships
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="Property", type=umlsimp_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=umlsimp_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations1: BinaryAssociation = BinaryAssociation(
    name="operations1",
    ends={
        Property(name="Operation", type=umlsimp_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class2", type=umlsimp_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class3: BinaryAssociation = BinaryAssociation(
    name="class3",
    ends={
        Property(name="Class", type=umlsimp_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operations", type=umlsimp_Class, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter4: BinaryAssociation = BinaryAssociation(
    name="ownedParameter4",
    ends={
        Property(name="umlsimp_Parameter", type=umlsimp_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlsimp_Operation", type=umlsimp_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class5: BinaryAssociation = BinaryAssociation(
    name="class5",
    ends={
        Property(name="Class6", type=umlsimp_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="properties", type=umlsimp_Class, multiplicity=Multiplicity(1, 1))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="umlsimp_DataType", type=umlsimp_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlsimp_TypedElement", type=umlsimp_DataType, multiplicity=Multiplicity(0, 1))
    }
)
modelElements8: BinaryAssociation = BinaryAssociation(
    name="modelElements8",
    ends={
        Property(name="umlsimp_ModelElement", type=umlsimp_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="umlsimp_Model", type=umlsimp_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_umlsimp_DataType_ModelElement = Generalization(general=ModelElement, specific=umlsimp_DataType)
gen_umlsimp_Class_ModelElement = Generalization(general=ModelElement, specific=umlsimp_Class)
gen_umlsimp_Operation_TypedElement = Generalization(general=TypedElement, specific=umlsimp_Operation)
gen_umlsimp_Property_TypedElement = Generalization(general=TypedElement, specific=umlsimp_Property)
gen_umlsimp_Parameter_TypedElement = Generalization(general=TypedElement, specific=umlsimp_Parameter)
gen_umlsimp_TypedElement_ModelElement = Generalization(general=ModelElement, specific=umlsimp_TypedElement)

# Domain Model
domain_model = DomainModel(
    name="umlsimp",
    types={umlsimp_ModelElement, umlsimp_DataType, ModelElement, umlsimp_Class, umlsimp_Property, umlsimp_Operation, TypedElement, umlsimp_Parameter, umlsimp_TypedElement, umlsimp_Model, visType},
    associations={properties0, operations1, class3, ownedParameter4, class5, type7, modelElements8},
    generalizations={gen_umlsimp_DataType_ModelElement, gen_umlsimp_Class_ModelElement, gen_umlsimp_Operation_TypedElement, gen_umlsimp_Property_TypedElement, gen_umlsimp_Parameter_TypedElement, gen_umlsimp_TypedElement_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)