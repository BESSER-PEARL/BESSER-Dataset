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
ElementType: Enumeration = Enumeration(
    name="ElementType",
    literals={
            EnumerationLiteral(name="Type1"),
			EnumerationLiteral(name="Type2")
    }
)

# Classes
testModel_Node = Class(name="testModel::Node")
testModel_ContainedLeaf = Class(name="testModel::ContainedLeaf")
testModel_multiRefLeaf = Class(name="testModel::multiRefLeaf")
testModel_Leafs = Class(name="testModel::Leafs", is_abstract=True)
testModel_referedLeaf = Class(name="testModel::referedLeaf")
testModel_upperBoundLeaf = Class(name="testModel::upperBoundLeaf")
Leafs = Class(name="Leafs")

# testModel_Node class attributes and methods
testModel_Node_name: Property = Property(name="name", type=StringType)
testModel_Node_bigdeci: Property = Property(name="bigdeci", type=StringType)
testModel_Node_bigint: Property = Property(name="bigint", type=StringType)
testModel_Node_bool: Property = Property(name="bool", type=BooleanType)
testModel_Node_Boolean: Property = Property(name="Boolean", type=StringType)
testModel_Node_byte: Property = Property(name="byte", type=StringType)
testModel_Node.attributes={testModel_Node_bigint, testModel_Node_bool, testModel_Node_byte, testModel_Node_Boolean, testModel_Node_name, testModel_Node_bigdeci}

# testModel_ContainedLeaf class attributes and methods
testModel_ContainedLeaf_name: Property = Property(name="name", type=StringType)
testModel_ContainedLeaf_byteArray: Property = Property(name="byteArray", type=StringType)
testModel_ContainedLeaf_byteObject: Property = Property(name="byteObject", type=StringType)
testModel_ContainedLeaf_char: Property = Property(name="char", type=StringType)
testModel_ContainedLeaf_Character: Property = Property(name="Character", type=StringType)
testModel_ContainedLeaf_date: Property = Property(name="date", type=DateType)
testModel_ContainedLeaf_double: Property = Property(name="double", type=FloatType)
testModel_ContainedLeaf_DoubleObj: Property = Property(name="DoubleObj", type=StringType)
testModel_ContainedLeaf_float: Property = Property(name="float", type=FloatType)
testModel_ContainedLeaf_elementType: Property = Property(name="elementType", type=StringType)
testModel_ContainedLeaf.attributes={testModel_ContainedLeaf_DoubleObj, testModel_ContainedLeaf_float, testModel_ContainedLeaf_byteObject, testModel_ContainedLeaf_Character, testModel_ContainedLeaf_name, testModel_ContainedLeaf_byteArray, testModel_ContainedLeaf_elementType, testModel_ContainedLeaf_double, testModel_ContainedLeaf_char, testModel_ContainedLeaf_date}

# testModel_multiRefLeaf class attributes and methods
testModel_multiRefLeaf_name: Property = Property(name="name", type=StringType)
testModel_multiRefLeaf.attributes={testModel_multiRefLeaf_name}

# testModel_Leafs class attributes and methods

# testModel_referedLeaf class attributes and methods
testModel_referedLeaf_name: Property = Property(name="name", type=StringType)
testModel_referedLeaf_notChangeable: Property = Property(name="notChangeable", type=StringType)
testModel_referedLeaf_Float: Property = Property(name="Float", type=StringType)
testModel_referedLeaf_int: Property = Property(name="int", type=IntegerType)
testModel_referedLeaf_Integer: Property = Property(name="Integer", type=StringType)
testModel_referedLeaf_long: Property = Property(name="long", type=StringType)
testModel_referedLeaf_LongObj: Property = Property(name="LongObj", type=StringType)
testModel_referedLeaf_short: Property = Property(name="short", type=StringType)
testModel_referedLeaf_ShortObj: Property = Property(name="ShortObj", type=StringType)
testModel_referedLeaf.attributes={testModel_referedLeaf_long, testModel_referedLeaf_Integer, testModel_referedLeaf_Float, testModel_referedLeaf_notChangeable, testModel_referedLeaf_short, testModel_referedLeaf_name, testModel_referedLeaf_LongObj, testModel_referedLeaf_int, testModel_referedLeaf_ShortObj}

# testModel_upperBoundLeaf class attributes and methods
testModel_upperBoundLeaf_name: Property = Property(name="name", type=StringType)
testModel_upperBoundLeaf.attributes={testModel_upperBoundLeaf_name}

# Leafs class attributes and methods

# Relationships
subNode1: BinaryAssociation = BinaryAssociation(
    name="subNode1",
    ends={
        Property(name="testModel_Node", type=testModel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_Node0", type=testModel_Node, multiplicity=Multiplicity(0, 9999))
    }
)
contains2: BinaryAssociation = BinaryAssociation(
    name="contains2",
    ends={
        Property(name="testModel_ContainedLeaf", type=testModel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_Node3", type=testModel_ContainedLeaf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiRef8: BinaryAssociation = BinaryAssociation(
    name="multiRef8",
    ends={
        Property(name="testModel_multiRefLeaf", type=testModel_referedLeaf, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_referedLeaf9", type=testModel_multiRefLeaf, multiplicity=Multiplicity(0, 9999))
    }
)
ref4: BinaryAssociation = BinaryAssociation(
    name="ref4",
    ends={
        Property(name="testModel_referedLeaf", type=testModel_ContainedLeaf, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_ContainedLeaf5", type=testModel_referedLeaf, multiplicity=Multiplicity(0, 9999))
    }
)
upperBound6: BinaryAssociation = BinaryAssociation(
    name="upperBound6",
    ends={
        Property(name="testModel_upperBoundLeaf", type=testModel_ContainedLeaf, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_ContainedLeaf7", type=testModel_upperBoundLeaf, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)

# Generalizations
gen_testModel_multiRefLeaf_Leafs = Generalization(general=Leafs, specific=testModel_multiRefLeaf)
gen_testModel_upperBoundLeaf_Leafs = Generalization(general=Leafs, specific=testModel_upperBoundLeaf)
gen_testModel_referedLeaf_Leafs = Generalization(general=Leafs, specific=testModel_referedLeaf)

# Domain Model
domain_model = DomainModel(
    name="testModel",
    types={testModel_Node, testModel_ContainedLeaf, testModel_multiRefLeaf, testModel_Leafs, testModel_referedLeaf, testModel_upperBoundLeaf, Leafs, ElementType},
    associations={subNode1, contains2, multiRef8, ref4, upperBound6},
    generalizations={gen_testModel_multiRefLeaf_Leafs, gen_testModel_upperBoundLeaf_Leafs, gen_testModel_referedLeaf_Leafs},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)