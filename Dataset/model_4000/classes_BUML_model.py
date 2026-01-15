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
Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="datetime"),
			EnumerationLiteral(name="bool")
    }
)

# Classes
classes_ClassDiagram = Class(name="classes::ClassDiagram")
classes_Class = Class(name="classes::Class")
classes_Attribute = Class(name="classes::Attribute")
classes_Reference = Class(name="classes::Reference")

# classes_ClassDiagram class attributes and methods
classes_ClassDiagram_name: Property = Property(name="name", type=StringType)
classes_ClassDiagram.attributes={classes_ClassDiagram_name}

# classes_Class class attributes and methods
classes_Class_name: Property = Property(name="name", type=StringType)
classes_Class.attributes={classes_Class_name}

# classes_Attribute class attributes and methods
classes_Attribute_name: Property = Property(name="name", type=StringType)
classes_Attribute_type: Property = Property(name="type", type=StringType)
classes_Attribute.attributes={classes_Attribute_type, classes_Attribute_name}

# classes_Reference class attributes and methods
classes_Reference_name: Property = Property(name="name", type=StringType)
classes_Reference.attributes={classes_Reference_name}

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="Class", type=classes_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram", type=classes_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="Attribute", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="cls", type=classes_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
_primary_key5: BinaryAssociation = BinaryAssociation(
    name="_primary_key5",
    ends={
        Property(name="classes_Attribute", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Class", type=classes_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
cls6: BinaryAssociation = BinaryAssociation(
    name="cls6",
    ends={
        Property(name="Class7", type=classes_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=classes_Class, multiplicity=Multiplicity(1, 1))
    }
)
cls8: BinaryAssociation = BinaryAssociation(
    name="cls8",
    ends={
        Property(name="Class9", type=classes_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="references", type=classes_Class, multiplicity=Multiplicity(1, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="classes_Class11", type=classes_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Reference", type=classes_Class, multiplicity=Multiplicity(1, 1))
    }
)
references2: BinaryAssociation = BinaryAssociation(
    name="references2",
    ends={
        Property(name="Reference", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="cls3", type=classes_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagram4: BinaryAssociation = BinaryAssociation(
    name="diagram4",
    ends={
        Property(name="ClassDiagram", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes", type=classes_ClassDiagram, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="classes",
    types={classes_ClassDiagram, classes_Class, classes_Attribute, classes_Reference, Type},
    associations={classes0, attributes1, _primary_key5, cls6, cls8, target10, references2, diagram4},
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