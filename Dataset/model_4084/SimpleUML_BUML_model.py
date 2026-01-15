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
simpleUML_Model = Class(name="simpleUML::Model")
simpleUML_UMLClass = Class(name="simpleUML::UMLClass")
simpleUML_Generalization = Class(name="simpleUML::Generalization")

# simpleUML_Model class attributes and methods

# simpleUML_UMLClass class attributes and methods
simpleUML_UMLClass_umlName: Property = Property(name="umlName", type=StringType)
simpleUML_UMLClass.attributes={simpleUML_UMLClass_umlName}

# simpleUML_Generalization class attributes and methods

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="simpleUML_UMLClass", type=simpleUML_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_Model", type=simpleUML_UMLClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalizations1: BinaryAssociation = BinaryAssociation(
    name="generalizations1",
    ends={
        Property(name="simpleUML_Generalization", type=simpleUML_UMLClass, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_UMLClass2", type=simpleUML_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference3: BinaryAssociation = BinaryAssociation(
    name="reference3",
    ends={
        Property(name="simpleUML_UMLClass5", type=simpleUML_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_Generalization4", type=simpleUML_UMLClass, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="simpleUML",
    types={simpleUML_Model, simpleUML_UMLClass, simpleUML_Generalization},
    associations={classes0, generalizations1, reference3},
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