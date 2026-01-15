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
clazz_B = Class(name="clazz::B")
clazz_Annotation = Class(name="clazz::Annotation")
clazz_BRef = Class(name="clazz::BRef")

# clazz_B class attributes and methods
clazz_B_name: Property = Property(name="name", type=StringType)
clazz_B.attributes={clazz_B_name}

# clazz_Annotation class attributes and methods
clazz_Annotation_tag: Property = Property(name="tag", type=StringType)
clazz_Annotation.attributes={clazz_Annotation_tag}

# clazz_BRef class attributes and methods
clazz_BRef_name: Property = Property(name="name", type=StringType)
clazz_BRef.attributes={clazz_BRef_name}

# Relationships
annotation0: BinaryAssociation = BinaryAssociation(
    name="annotation0",
    ends={
        Property(name="clazz_Annotation", type=clazz_B, multiplicity=Multiplicity(1, 1)),
        Property(name="clazz_B", type=clazz_Annotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref1: BinaryAssociation = BinaryAssociation(
    name="ref1",
    ends={
        Property(name="clazz_B2", type=clazz_BRef, multiplicity=Multiplicity(1, 1)),
        Property(name="clazz_BRef", type=clazz_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="clazz",
    types={clazz_B, clazz_Annotation, clazz_BRef},
    associations={annotation0, ref1},
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