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
necsis14_classdiagram_ClassDiagram = Class(name="necsis14::classdiagram::ClassDiagram")
necsis14_classdiagram_Class = Class(name="necsis14::classdiagram::Class")
necsis14_classdiagram_Association = Class(name="necsis14::classdiagram::Association")
necsis14_classdiagram_NamedElement = Class(name="necsis14::classdiagram::NamedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
necsis14_classdiagram_Attribute = Class(name="necsis14::classdiagram::Attribute")

# necsis14_classdiagram_ClassDiagram class attributes and methods

# necsis14_classdiagram_Class class attributes and methods

# necsis14_classdiagram_Association class attributes and methods
necsis14_classdiagram_Association_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
necsis14_classdiagram_Association_upperBound: Property = Property(name="upperBound", type=IntegerType)
necsis14_classdiagram_Association.attributes={necsis14_classdiagram_Association_upperBound, necsis14_classdiagram_Association_lowerBound}

# necsis14_classdiagram_NamedElement class attributes and methods
necsis14_classdiagram_NamedElement_name: Property = Property(name="name", type=StringType)
necsis14_classdiagram_NamedElement.attributes={necsis14_classdiagram_NamedElement_name}

# NamedElement class attributes and methods

# necsis14_classdiagram_Attribute class attributes and methods

# Relationships
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="necsis14_classdiagram_Class10", type=necsis14_classdiagram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="necsis14_classdiagram_Association9", type=necsis14_classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="necsis14_classdiagram_Class13", type=necsis14_classdiagram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="necsis14_classdiagram_Association12", type=necsis14_classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="necsis14_classdiagram_Class", type=necsis14_classdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="necsis14_classdiagram_ClassDiagram", type=necsis14_classdiagram_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations1: BinaryAssociation = BinaryAssociation(
    name="associations1",
    ends={
        Property(name="necsis14_classdiagram_Association", type=necsis14_classdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="necsis14_classdiagram_ClassDiagram2", type=necsis14_classdiagram_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent4: BinaryAssociation = BinaryAssociation(
    name="parent4",
    ends={
        Property(name="necsis14_classdiagram_Class5", type=necsis14_classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="necsis14_classdiagram_Class3", type=necsis14_classdiagram_Class, multiplicity=Multiplicity(0, 1))
    }
)
attributes6: BinaryAssociation = BinaryAssociation(
    name="attributes6",
    ends={
        Property(name="necsis14_classdiagram_Attribute", type=necsis14_classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="necsis14_classdiagram_Class7", type=necsis14_classdiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_necsis14_classdiagram_Attribute_NamedElement = Generalization(general=NamedElement, specific=necsis14_classdiagram_Attribute)
gen_necsis14_classdiagram_Class_NamedElement = Generalization(general=NamedElement, specific=necsis14_classdiagram_Class)
gen_necsis14_classdiagram_Association_NamedElement = Generalization(general=NamedElement, specific=necsis14_classdiagram_Association)

# Domain Model
domain_model = DomainModel(
    name="necsis14_classdiagram",
    types={necsis14_classdiagram_ClassDiagram, necsis14_classdiagram_Class, necsis14_classdiagram_Association, necsis14_classdiagram_NamedElement, NamedElement, necsis14_classdiagram_Attribute},
    associations={source8, target11, classes0, associations1, parent4, attributes6},
    generalizations={gen_necsis14_classdiagram_Attribute_NamedElement, gen_necsis14_classdiagram_Class_NamedElement, gen_necsis14_classdiagram_Association_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)