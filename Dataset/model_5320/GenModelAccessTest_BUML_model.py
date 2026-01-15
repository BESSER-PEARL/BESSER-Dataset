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
RootEnum: Enumeration = Enumeration(
    name="RootEnum",
    literals={
            EnumerationLiteral(name="literal")
    }
)

NoLitEnum: Enumeration = Enumeration(
    name="NoLitEnum",
    literals={
            EnumerationLiteral(name="literal")
    }
)

# Classes
root_RootClass = Class(name="root::RootClass")
NestedClass1 = Class(name="NestedClass1")
root_nestedPackage1_NestedClass1 = Class(name="root::nestedPackage1::NestedClass1")
root_noLiterals_NoLitClass = Class(name="root::noLiterals::NoLitClass")

# root_RootClass class attributes and methods
root_RootClass_attribute1: Property = Property(name="attribute1", type=StringType)
root_RootClass.attributes={root_RootClass_attribute1}

# NestedClass1 class attributes and methods

# root_nestedPackage1_NestedClass1 class attributes and methods

# root_noLiterals_NoLitClass class attributes and methods
root_noLiterals_NoLitClass_attribute2: Property = Property(name="attribute2", type=StringType)
root_noLiterals_NoLitClass.attributes={root_noLiterals_NoLitClass_attribute2}

# Relationships
reference10: BinaryAssociation = BinaryAssociation(
    name="reference10",
    ends={
        Property(name="NestedClass1", type=root_RootClass, multiplicity=Multiplicity(1, 1)),
        Property(name="root_RootClass", type=NestedClass1, multiplicity=Multiplicity(0, 1))
    }
)
reference21: BinaryAssociation = BinaryAssociation(
    name="reference21",
    ends={
        Property(name="NestedClass12", type=root_noLiterals_NoLitClass, multiplicity=Multiplicity(1, 1)),
        Property(name="root_noLiterals_NoLitClass", type=NestedClass1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="root",
    types={root_RootClass, NestedClass1, root_nestedPackage1_NestedClass1, root_noLiterals_NoLitClass, RootEnum, NoLitEnum},
    associations={reference10, reference21},
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