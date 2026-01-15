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
ramRoot_MT__Element = Class(name="ramRoot::MT::::Element", is_abstract=True)
ramRoot_MTpos__Element = Class(name="ramRoot::MTpos::::Element", is_abstract=True)
MT__Element = Class(name="MT::::Element")
ramRoot_MTpre__Element = Class(name="ramRoot::MTpre::::Element", is_abstract=True)
ramRoot_MTpos__Person = Class(name="ramRoot::MTpos::::Person")
MTpos__Element = Class(name="MTpos::::Element")
ramRoot_MTpos__Classroom = Class(name="ramRoot::MTpos::::Classroom")
ramRoot_MTpos__Man = Class(name="ramRoot::MTpos::::Man")
MTpos__Person = Class(name="MTpos::::Person")
ramRoot_MTpos__Woman = Class(name="ramRoot::MTpos::::Woman")
ramRoot_MTpre__Person = Class(name="ramRoot::MTpre::::Person")
MTpre__Element = Class(name="MTpre::::Element")
ramRoot_MTpre__Classroom = Class(name="ramRoot::MTpre::::Classroom")
ramRoot_MTpre__Man = Class(name="ramRoot::MTpre::::Man")
MTpre__Person = Class(name="MTpre::::Person")
ramRoot_MTpre__Woman = Class(name="ramRoot::MTpre::::Woman")
ramRoot_GenericNode = Class(name="ramRoot::GenericNode")

# ramRoot_MT__Element class attributes and methods
ramRoot_MT__Element_MT__isProcessed: Property = Property(name="MT__isProcessed", type=BooleanType)
ramRoot_MT__Element_MT__label: Property = Property(name="MT__label", type=StringType)
ramRoot_MT__Element.attributes={ramRoot_MT__Element_MT__isProcessed, ramRoot_MT__Element_MT__label}

# ramRoot_MTpos__Element class attributes and methods

# MT__Element class attributes and methods

# ramRoot_MTpre__Element class attributes and methods
ramRoot_MTpre__Element_MT__matchSubtype: Property = Property(name="MT__matchSubtype", type=BooleanType)
ramRoot_MTpre__Element.attributes={ramRoot_MTpre__Element_MT__matchSubtype}

# ramRoot_MTpos__Person class attributes and methods
ramRoot_MTpos__Person_name: Property = Property(name="name", type=StringType)
ramRoot_MTpos__Person.attributes={ramRoot_MTpos__Person_name}

# MTpos__Element class attributes and methods

# ramRoot_MTpos__Classroom class attributes and methods
ramRoot_MTpos__Classroom_id: Property = Property(name="id", type=StringType)
ramRoot_MTpos__Classroom.attributes={ramRoot_MTpos__Classroom_id}

# ramRoot_MTpos__Man class attributes and methods

# MTpos__Person class attributes and methods

# ramRoot_MTpos__Woman class attributes and methods

# ramRoot_MTpre__Person class attributes and methods
ramRoot_MTpre__Person_name: Property = Property(name="name", type=StringType)
ramRoot_MTpre__Person.attributes={ramRoot_MTpre__Person_name}

# MTpre__Element class attributes and methods

# ramRoot_MTpre__Classroom class attributes and methods
ramRoot_MTpre__Classroom_id: Property = Property(name="id", type=StringType)
ramRoot_MTpre__Classroom.attributes={ramRoot_MTpre__Classroom_id}

# ramRoot_MTpre__Man class attributes and methods

# MTpre__Person class attributes and methods

# ramRoot_MTpre__Woman class attributes and methods

# ramRoot_GenericNode class attributes and methods

# Relationships
teacher_of1: BinaryAssociation = BinaryAssociation(
    name="teacher_of1",
    ends={
        Property(name="ramRoot_MTpos__Classroom", type=ramRoot_MTpos__Person, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpos__Person", type=ramRoot_MTpos__Classroom, multiplicity=Multiplicity(0, 1))
    }
)
friend_with3: BinaryAssociation = BinaryAssociation(
    name="friend_with3",
    ends={
        Property(name="ramRoot_MTpos__Person4", type=ramRoot_MTpos__Person, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpos__Person2", type=ramRoot_MTpos__Person, multiplicity=Multiplicity(0, 9999))
    }
)
person5: BinaryAssociation = BinaryAssociation(
    name="person5",
    ends={
        Property(name="ramRoot_MTpos__Person7", type=ramRoot_MTpos__Classroom, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpos__Classroom6", type=ramRoot_MTpos__Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teacher_of8: BinaryAssociation = BinaryAssociation(
    name="teacher_of8",
    ends={
        Property(name="ramRoot_MTpre__Classroom", type=ramRoot_MTpre__Person, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpre__Person", type=ramRoot_MTpre__Classroom, multiplicity=Multiplicity(0, 1))
    }
)
friend_with10: BinaryAssociation = BinaryAssociation(
    name="friend_with10",
    ends={
        Property(name="ramRoot_MTpre__Person11", type=ramRoot_MTpre__Person, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpre__Person9", type=ramRoot_MTpre__Person, multiplicity=Multiplicity(0, 9999))
    }
)
GenericLink0: BinaryAssociation = BinaryAssociation(
    name="GenericLink0",
    ends={
        Property(name="ramRoot_MT__Element", type=ramRoot_GenericNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_GenericNode", type=ramRoot_MT__Element, multiplicity=Multiplicity(0, 9999))
    }
)
person12: BinaryAssociation = BinaryAssociation(
    name="person12",
    ends={
        Property(name="ramRoot_MTpre__Person14", type=ramRoot_MTpre__Classroom, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpre__Classroom13", type=ramRoot_MTpre__Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ramRoot_MTpos__Element_MT__Element = Generalization(general=MT__Element, specific=ramRoot_MTpos__Element)
gen_ramRoot_MTpre__Element_MT__Element = Generalization(general=MT__Element, specific=ramRoot_MTpre__Element)
gen_ramRoot_MTpos__Person_MTpos__Element = Generalization(general=MTpos__Element, specific=ramRoot_MTpos__Person)
gen_ramRoot_MTpos__Man_MTpos__Person = Generalization(general=MTpos__Person, specific=ramRoot_MTpos__Man)
gen_ramRoot_MTpos__Woman_MTpos__Person = Generalization(general=MTpos__Person, specific=ramRoot_MTpos__Woman)
gen_ramRoot_MTpos__Classroom_MTpos__Element = Generalization(general=MTpos__Element, specific=ramRoot_MTpos__Classroom)
gen_ramRoot_MTpre__Person_MTpre__Element = Generalization(general=MTpre__Element, specific=ramRoot_MTpre__Person)
gen_ramRoot_MTpre__Man_MTpre__Person = Generalization(general=MTpre__Person, specific=ramRoot_MTpre__Man)
gen_ramRoot_MTpre__Woman_MTpre__Person = Generalization(general=MTpre__Person, specific=ramRoot_MTpre__Woman)
gen_ramRoot_GenericNode_MT__Element = Generalization(general=MT__Element, specific=ramRoot_GenericNode)
gen_ramRoot_MTpre__Classroom_MTpre__Element = Generalization(general=MTpre__Element, specific=ramRoot_MTpre__Classroom)

# Domain Model
domain_model = DomainModel(
    name="ramRoot",
    types={ramRoot_MT__Element, ramRoot_MTpos__Element, MT__Element, ramRoot_MTpre__Element, ramRoot_MTpos__Person, MTpos__Element, ramRoot_MTpos__Classroom, ramRoot_MTpos__Man, MTpos__Person, ramRoot_MTpos__Woman, ramRoot_MTpre__Person, MTpre__Element, ramRoot_MTpre__Classroom, ramRoot_MTpre__Man, MTpre__Person, ramRoot_MTpre__Woman, ramRoot_GenericNode},
    associations={teacher_of1, friend_with3, person5, teacher_of8, friend_with10, GenericLink0, person12},
    generalizations={gen_ramRoot_MTpos__Element_MT__Element, gen_ramRoot_MTpre__Element_MT__Element, gen_ramRoot_MTpos__Person_MTpos__Element, gen_ramRoot_MTpos__Man_MTpos__Person, gen_ramRoot_MTpos__Woman_MTpos__Person, gen_ramRoot_MTpos__Classroom_MTpos__Element, gen_ramRoot_MTpre__Person_MTpre__Element, gen_ramRoot_MTpre__Man_MTpre__Person, gen_ramRoot_MTpre__Woman_MTpre__Person, gen_ramRoot_GenericNode_MT__Element, gen_ramRoot_MTpre__Classroom_MTpre__Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)