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
ramRoot_MTpos__Table = Class(name="ramRoot::MTpos::::Table")
MTpos__Element = Class(name="MTpos::::Element")
ramRoot_MTpos__Chair = Class(name="ramRoot::MTpos::::Chair")
ramRoot_MT__Element = Class(name="ramRoot::MT::::Element", is_abstract=True)
ramRoot_MTpos__Element = Class(name="ramRoot::MTpos::::Element", is_abstract=True)
MT__Element = Class(name="MT::::Element")
ramRoot_MTpre__Element = Class(name="ramRoot::MTpre::::Element", is_abstract=True)
ramRoot_GenericNode = Class(name="ramRoot::GenericNode")
ramRoot_MTpre__Waitress = Class(name="ramRoot::MTpre::::Waitress")
ramRoot_MTpre__Restaurant = Class(name="ramRoot::MTpre::::Restaurant")
ramRoot_MTpos__Restaurant = Class(name="ramRoot::MTpos::::Restaurant")
ramRoot_MTpos__Waitress = Class(name="ramRoot::MTpos::::Waitress")
ramRoot_MTpre__Table = Class(name="ramRoot::MTpre::::Table")
MTpre__Element = Class(name="MTpre::::Element")
ramRoot_MTpre__Chair = Class(name="ramRoot::MTpre::::Chair")

# ramRoot_MTpos__Table class attributes and methods
ramRoot_MTpos__Table_MTpos__id: Property = Property(name="MTpos__id", type=StringType)
ramRoot_MTpos__Table_MTpos__isReserved: Property = Property(name="MTpos__isReserved", type=StringType)
ramRoot_MTpos__Table.attributes={ramRoot_MTpos__Table_MTpos__isReserved, ramRoot_MTpos__Table_MTpos__id}

# MTpos__Element class attributes and methods

# ramRoot_MTpos__Chair class attributes and methods
ramRoot_MTpos__Chair_MTpos__order: Property = Property(name="MTpos__order", type=StringType)
ramRoot_MTpos__Chair.attributes={ramRoot_MTpos__Chair_MTpos__order}

# ramRoot_MT__Element class attributes and methods
ramRoot_MT__Element_MT__label: Property = Property(name="MT__label", type=StringType)
ramRoot_MT__Element_MT__isProcessed: Property = Property(name="MT__isProcessed", type=BooleanType)
ramRoot_MT__Element.attributes={ramRoot_MT__Element_MT__label, ramRoot_MT__Element_MT__isProcessed}

# ramRoot_MTpos__Element class attributes and methods

# MT__Element class attributes and methods

# ramRoot_MTpre__Element class attributes and methods
ramRoot_MTpre__Element_MT__matchSubtype: Property = Property(name="MT__matchSubtype", type=BooleanType)
ramRoot_MTpre__Element.attributes={ramRoot_MTpre__Element_MT__matchSubtype}

# ramRoot_GenericNode class attributes and methods

# ramRoot_MTpre__Waitress class attributes and methods
ramRoot_MTpre__Waitress_MTpre__name: Property = Property(name="MTpre__name", type=StringType)
ramRoot_MTpre__Waitress.attributes={ramRoot_MTpre__Waitress_MTpre__name}

# ramRoot_MTpre__Restaurant class attributes and methods

# ramRoot_MTpos__Restaurant class attributes and methods

# ramRoot_MTpos__Waitress class attributes and methods
ramRoot_MTpos__Waitress_MTpos__name: Property = Property(name="MTpos__name", type=StringType)
ramRoot_MTpos__Waitress.attributes={ramRoot_MTpos__Waitress_MTpos__name}

# ramRoot_MTpre__Table class attributes and methods
ramRoot_MTpre__Table_MTpre__id: Property = Property(name="MTpre__id", type=StringType)
ramRoot_MTpre__Table_MTpre__isReserved: Property = Property(name="MTpre__isReserved", type=StringType)
ramRoot_MTpre__Table.attributes={ramRoot_MTpre__Table_MTpre__isReserved, ramRoot_MTpre__Table_MTpre__id}

# MTpre__Element class attributes and methods

# ramRoot_MTpre__Chair class attributes and methods
ramRoot_MTpre__Chair_MTpre__order: Property = Property(name="MTpre__order", type=StringType)
ramRoot_MTpre__Chair.attributes={ramRoot_MTpre__Chair_MTpre__order}

# Relationships
GenericLink0: BinaryAssociation = BinaryAssociation(
    name="GenericLink0",
    ends={
        Property(name="ramRoot_MT__Element", type=ramRoot_GenericNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_GenericNode", type=ramRoot_MT__Element, multiplicity=Multiplicity(0, 9999))
    }
)
chairs1: BinaryAssociation = BinaryAssociation(
    name="chairs1",
    ends={
        Property(name="ramRoot_MTpos__Chair", type=ramRoot_MTpos__Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpos__Table", type=ramRoot_MTpos__Chair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables5: BinaryAssociation = BinaryAssociation(
    name="tables5",
    ends={
        Property(name="ramRoot_MTpre__Table6", type=ramRoot_MTpre__Waitress, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpre__Waitress", type=ramRoot_MTpre__Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables7: BinaryAssociation = BinaryAssociation(
    name="tables7",
    ends={
        Property(name="ramRoot_MTpre__Table8", type=ramRoot_MTpre__Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpre__Restaurant", type=ramRoot_MTpre__Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
waitress9: BinaryAssociation = BinaryAssociation(
    name="waitress9",
    ends={
        Property(name="ramRoot_MTpre__Waitress11", type=ramRoot_MTpre__Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpre__Restaurant10", type=ramRoot_MTpre__Waitress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
waitress12: BinaryAssociation = BinaryAssociation(
    name="waitress12",
    ends={
        Property(name="ramRoot_MTpos__Waitress13", type=ramRoot_MTpos__Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpos__Restaurant", type=ramRoot_MTpos__Waitress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables2: BinaryAssociation = BinaryAssociation(
    name="tables2",
    ends={
        Property(name="ramRoot_MTpos__Table3", type=ramRoot_MTpos__Waitress, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpos__Waitress", type=ramRoot_MTpos__Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables14: BinaryAssociation = BinaryAssociation(
    name="tables14",
    ends={
        Property(name="ramRoot_MTpos__Table16", type=ramRoot_MTpos__Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpos__Restaurant15", type=ramRoot_MTpos__Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
chairs4: BinaryAssociation = BinaryAssociation(
    name="chairs4",
    ends={
        Property(name="ramRoot_MTpre__Chair", type=ramRoot_MTpre__Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ramRoot_MTpre__Table", type=ramRoot_MTpre__Chair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ramRoot_MTpos__Table_MTpos__Element = Generalization(general=MTpos__Element, specific=ramRoot_MTpos__Table)
gen_ramRoot_MTpos__Element_MT__Element = Generalization(general=MT__Element, specific=ramRoot_MTpos__Element)
gen_ramRoot_MTpre__Element_MT__Element = Generalization(general=MT__Element, specific=ramRoot_MTpre__Element)
gen_ramRoot_GenericNode_MT__Element = Generalization(general=MT__Element, specific=ramRoot_GenericNode)
gen_ramRoot_MTpre__Waitress_MTpre__Element = Generalization(general=MTpre__Element, specific=ramRoot_MTpre__Waitress)
gen_ramRoot_MTpre__Restaurant_MTpre__Element = Generalization(general=MTpre__Element, specific=ramRoot_MTpre__Restaurant)
gen_ramRoot_MTpos__Chair_MTpos__Element = Generalization(general=MTpos__Element, specific=ramRoot_MTpos__Chair)
gen_ramRoot_MTpos__Restaurant_MTpos__Element = Generalization(general=MTpos__Element, specific=ramRoot_MTpos__Restaurant)
gen_ramRoot_MTpos__Waitress_MTpos__Element = Generalization(general=MTpos__Element, specific=ramRoot_MTpos__Waitress)
gen_ramRoot_MTpre__Table_MTpre__Element = Generalization(general=MTpre__Element, specific=ramRoot_MTpre__Table)
gen_ramRoot_MTpre__Chair_MTpre__Element = Generalization(general=MTpre__Element, specific=ramRoot_MTpre__Chair)

# Domain Model
domain_model = DomainModel(
    name="ramRoot",
    types={ramRoot_MTpos__Table, MTpos__Element, ramRoot_MTpos__Chair, ramRoot_MT__Element, ramRoot_MTpos__Element, MT__Element, ramRoot_MTpre__Element, ramRoot_GenericNode, ramRoot_MTpre__Waitress, ramRoot_MTpre__Restaurant, ramRoot_MTpos__Restaurant, ramRoot_MTpos__Waitress, ramRoot_MTpre__Table, MTpre__Element, ramRoot_MTpre__Chair},
    associations={GenericLink0, chairs1, tables5, tables7, waitress9, waitress12, tables2, tables14, chairs4},
    generalizations={gen_ramRoot_MTpos__Table_MTpos__Element, gen_ramRoot_MTpos__Element_MT__Element, gen_ramRoot_MTpre__Element_MT__Element, gen_ramRoot_GenericNode_MT__Element, gen_ramRoot_MTpre__Waitress_MTpre__Element, gen_ramRoot_MTpre__Restaurant_MTpre__Element, gen_ramRoot_MTpos__Chair_MTpos__Element, gen_ramRoot_MTpos__Restaurant_MTpos__Element, gen_ramRoot_MTpos__Waitress_MTpos__Element, gen_ramRoot_MTpre__Table_MTpre__Element, gen_ramRoot_MTpre__Chair_MTpre__Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)