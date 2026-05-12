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
Graph_Graph = Class(name="Graph_Graph")
Graph_ID1006 = Class(name="Graph_ID1006")
Graph_TBoolean = Class(name="Graph_TBoolean")
Graph_TFloat = Class(name="Graph_TFloat")
Graph_TDouble = Class(name="Graph_TDouble")
Graph_TString = Class(name="Graph_TString")
Graph_TChar = Class(name="Graph_TChar")
Graph_TByte = Class(name="Graph_TByte")
Graph_TShort = Class(name="Graph_TShort")
Graph_TInt = Class(name="Graph_TInt")
Graph_TLong = Class(name="Graph_TLong")

# Graph_Graph class attributes and methods
Graph_Graph_id: Property = Property(name="id", type=StringType)
Graph_Graph.attributes={Graph_Graph_id}

# Graph_ID1006 class attributes and methods
Graph_ID1006_id: Property = Property(name="id", type=StringType)
Graph_ID1006_name: Property = Property(name="name", type=StringType)
Graph_ID1006.attributes={Graph_ID1006_name, Graph_ID1006_id}

# Graph_TBoolean class attributes and methods
Graph_TBoolean_value: Property = Property(name="value", type=BooleanType)
Graph_TBoolean.attributes={Graph_TBoolean_value}

# Graph_TFloat class attributes and methods
Graph_TFloat_value: Property = Property(name="value", type=FloatType)
Graph_TFloat.attributes={Graph_TFloat_value}

# Graph_TDouble class attributes and methods
Graph_TDouble_value: Property = Property(name="value", type=FloatType)
Graph_TDouble.attributes={Graph_TDouble_value}

# Graph_TString class attributes and methods
Graph_TString_id: Property = Property(name="id", type=StringType)
Graph_TString_name: Property = Property(name="name", type=StringType)
Graph_TString.attributes={Graph_TString_id, Graph_TString_name}

# Graph_TChar class attributes and methods
Graph_TChar_value: Property = Property(name="value", type=StringType)
Graph_TChar.attributes={Graph_TChar_value}

# Graph_TByte class attributes and methods
Graph_TByte_value: Property = Property(name="value", type=StringType)
Graph_TByte.attributes={Graph_TByte_value}

# Graph_TShort class attributes and methods
Graph_TShort_value: Property = Property(name="value", type=StringType)
Graph_TShort.attributes={Graph_TShort_value}

# Graph_TInt class attributes and methods
Graph_TInt_value: Property = Property(name="value", type=IntegerType)
Graph_TInt.attributes={Graph_TInt_value}

# Graph_TLong class attributes and methods
Graph_TLong_value: Property = Property(name="value", type=StringType)
Graph_TLong.attributes={Graph_TLong_value}

# Relationships
id1006s0: BinaryAssociation = BinaryAssociation(
    name="id1006s0",
    ends={
        Property(name="Graph_ID1006", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Graph", type=Graph_ID1006, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tLongs11: BinaryAssociation = BinaryAssociation(
    name="tLongs11",
    ends={
        Property(name="Graph_Graph12", type=Graph_TLong, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Graph_TLong", type=Graph_Graph, multiplicity=Multiplicity(1, 1))
    }
)
tFloats13: BinaryAssociation = BinaryAssociation(
    name="tFloats13",
    ends={
        Property(name="Graph_TFloat", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Graph14", type=Graph_TFloat, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tDoubles15: BinaryAssociation = BinaryAssociation(
    name="tDoubles15",
    ends={
        Property(name="Graph_TDouble", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Graph16", type=Graph_TDouble, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tBooleans1: BinaryAssociation = BinaryAssociation(
    name="tBooleans1",
    ends={
        Property(name="Graph_TBoolean", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Graph2", type=Graph_TBoolean, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tChars3: BinaryAssociation = BinaryAssociation(
    name="tChars3",
    ends={
        Property(name="Graph_TChar", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Graph4", type=Graph_TChar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tBytes5: BinaryAssociation = BinaryAssociation(
    name="tBytes5",
    ends={
        Property(name="Graph_TByte", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Graph6", type=Graph_TByte, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tShorts7: BinaryAssociation = BinaryAssociation(
    name="tShorts7",
    ends={
        Property(name="Graph_TShort", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Graph8", type=Graph_TShort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tInts9: BinaryAssociation = BinaryAssociation(
    name="tInts9",
    ends={
        Property(name="Graph_TInt", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Graph10", type=Graph_TInt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tStrings17: BinaryAssociation = BinaryAssociation(
    name="tStrings17",
    ends={
        Property(name="Graph_TString", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Graph18", type=Graph_TString, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outID1008s19: BinaryAssociation = BinaryAssociation(
    name="outID1008s19",
    ends={
        Property(name="Graph_TString21", type=Graph_ID1006, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_ID100620", type=Graph_TString, multiplicity=Multiplicity(0, 9999))
    }
)


# OCL Constraints
maxElems: Constraint = Constraint(
    name="maxElems",
    context=Graph_ID1006,
    expression="context ID1006 inv: outID1008s->size() <= 1",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="Graph",
    types={Graph_Graph, Graph_ID1006, Graph_TBoolean, Graph_TFloat, Graph_TDouble, Graph_TString, Graph_TChar, Graph_TByte, Graph_TShort, Graph_TInt, Graph_TLong},
    associations={id1006s0, tLongs11, tFloats13, tDoubles15, tBooleans1, tChars3, tBytes5, tShorts7, tInts9, tStrings17, outID1008s19},
    constraints={maxElems},
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