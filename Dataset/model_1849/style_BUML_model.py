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
style_StyleLibrary = Class(name="style::StyleLibrary")
style_StyleSet = Class(name="style::StyleSet")
style_StylePointer = Class(name="style::StylePointer")

# style_StyleLibrary class attributes and methods
style_StyleLibrary_uid: Property = Property(name="uid", type=StringType)
style_StyleLibrary_name: Property = Property(name="name", type=StringType)
style_StyleLibrary.attributes={style_StyleLibrary_name, style_StyleLibrary_uid}

# style_StyleSet class attributes and methods
style_StyleSet_uid: Property = Property(name="uid", type=StringType)
style_StyleSet_name: Property = Property(name="name", type=StringType)
style_StyleSet.attributes={style_StyleSet_name, style_StyleSet_uid}

# style_StylePointer class attributes and methods

# Relationships
styles0: BinaryAssociation = BinaryAssociation(
    name="styles0",
    ends={
        Property(name="style_StyleSet", type=style_StyleLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="style_StyleLibrary", type=style_StyleSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styleLibrary1: BinaryAssociation = BinaryAssociation(
    name="styleLibrary1",
    ends={
        Property(name="style_StyleLibrary2", type=style_StylePointer, multiplicity=Multiplicity(1, 1)),
        Property(name="style_StylePointer", type=style_StyleLibrary, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="style",
    types={style_StyleLibrary, style_StyleSet, style_StylePointer},
    associations={styles0, styleLibrary1},
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