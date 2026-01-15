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
simpleUML_SimpleClass = Class(name="simpleUML::SimpleClass")
simpleUML_Generalization = Class(name="simpleUML::Generalization")
simpleUML_UMLAttribute = Class(name="simpleUML::UMLAttribute")

# simpleUML_Model class attributes and methods

# simpleUML_SimpleClass class attributes and methods
simpleUML_SimpleClass_simpleName: Property = Property(name="simpleName", type=StringType)
simpleUML_SimpleClass.attributes={simpleUML_SimpleClass_simpleName}

# simpleUML_Generalization class attributes and methods

# simpleUML_UMLAttribute class attributes and methods
simpleUML_UMLAttribute_umlName: Property = Property(name="umlName", type=StringType)
simpleUML_UMLAttribute.attributes={simpleUML_UMLAttribute_umlName}

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="simpleUML_SimpleClass", type=simpleUML_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_Model", type=simpleUML_SimpleClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclasses2: BinaryAssociation = BinaryAssociation(
    name="superclasses2",
    ends={
        Property(name="simpleUML_SimpleClass3", type=simpleUML_SimpleClass, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_SimpleClass1", type=simpleUML_SimpleClass, multiplicity=Multiplicity(0, 9999))
    }
)
generalizations4: BinaryAssociation = BinaryAssociation(
    name="generalizations4",
    ends={
        Property(name="simpleUML_Generalization", type=simpleUML_SimpleClass, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_SimpleClass5", type=simpleUML_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes6: BinaryAssociation = BinaryAssociation(
    name="attributes6",
    ends={
        Property(name="simpleUML_UMLAttribute", type=simpleUML_SimpleClass, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_SimpleClass7", type=simpleUML_UMLAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference8: BinaryAssociation = BinaryAssociation(
    name="reference8",
    ends={
        Property(name="simpleUML_SimpleClass10", type=simpleUML_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_Generalization9", type=simpleUML_SimpleClass, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="simpleUML",
    types={simpleUML_Model, simpleUML_SimpleClass, simpleUML_Generalization, simpleUML_UMLAttribute},
    associations={classes0, superclasses2, generalizations4, attributes6, reference8},
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