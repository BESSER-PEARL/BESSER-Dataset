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
class_ClassDiagram = Class(name="class::ClassDiagram")
class_Clazz = Class(name="class::Clazz")
class_Association = Class(name="class::Association")
class_Attribute = Class(name="class::Attribute")

# class_ClassDiagram class attributes and methods
class_ClassDiagram_id: Property = Property(name="id", type=StringType)
class_ClassDiagram.attributes={class_ClassDiagram_id}

# class_Clazz class attributes and methods
class_Clazz_id: Property = Property(name="id", type=StringType)
class_Clazz.attributes={class_Clazz_id}

# class_Association class attributes and methods
class_Association_id: Property = Property(name="id", type=StringType)
class_Association.attributes={class_Association_id}

# class_Attribute class attributes and methods
class_Attribute_id: Property = Property(name="id", type=StringType)
class_Attribute.attributes={class_Attribute_id}

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="class_Clazz", type=class_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="class_ClassDiagram", type=class_Clazz, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations1: BinaryAssociation = BinaryAssociation(
    name="associations1",
    ends={
        Property(name="class_Association", type=class_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="class_ClassDiagram2", type=class_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute3: BinaryAssociation = BinaryAssociation(
    name="attribute3",
    ends={
        Property(name="class_Attribute", type=class_Clazz, multiplicity=Multiplicity(1, 1)),
        Property(name="class_Clazz4", type=class_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super6: BinaryAssociation = BinaryAssociation(
    name="super6",
    ends={
        Property(name="class_Clazz7", type=class_Clazz, multiplicity=Multiplicity(1, 1)),
        Property(name="class_Clazz5", type=class_Clazz, multiplicity=Multiplicity(0, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="class_Clazz13", type=class_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="class_Association12", type=class_Clazz, multiplicity=Multiplicity(0, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="class_Clazz10", type=class_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="class_Association9", type=class_Clazz, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="class",
    types={class_ClassDiagram, class_Clazz, class_Association, class_Attribute},
    associations={classes0, associations1, attribute3, super6, target11, source8},
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