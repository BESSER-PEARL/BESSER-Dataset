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
ecore_EClass = Class(name="ecore::EClass")
ecore_EPackage = Class(name="ecore::EPackage")

# ecore_EClass class attributes and methods

# ecore_EPackage class attributes and methods

# Relationships
conflictingOpposite0: BinaryAssociation = BinaryAssociation(
    name="conflictingOpposite0",
    ends={
        Property(name="EPackage", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myClasses", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
myClasses1: BinaryAssociation = BinaryAssociation(
    name="myClasses1",
    ends={
        Property(name="EClass", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="conflictingOpposite", type=ecore_EClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={ecore_EClass, ecore_EPackage},
    associations={conflictingOpposite0, myClasses1},
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