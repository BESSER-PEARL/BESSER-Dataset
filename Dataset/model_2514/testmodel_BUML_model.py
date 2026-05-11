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
C = Class(name="C")
D = Class(name="D")
test_ntas_A = Class(name="test_ntas_A")
test_ntas_Root = Class(name="test_ntas_Root")
A = Class(name="A")
B = Class(name="B")
test_ast_AbstractD = Class(name="test_ast_AbstractD", is_abstract=True)
test_ast_E = Class(name="test_ast_E")
test_ntas_B = Class(name="test_ntas_B")
test_ntas_C = Class(name="test_ntas_C")
test_ast_D = Class(name="test_ast_D")
AbstractD = Class(name="AbstractD")

# C class attributes and methods

# D class attributes and methods

# test_ntas_A class attributes and methods
test_ntas_A_name: Property = Property(name="name", type=StringType)
test_ntas_A.attributes={test_ntas_A_name}

# test_ntas_Root class attributes and methods

# A class attributes and methods

# B class attributes and methods

# test_ast_AbstractD class attributes and methods
test_ast_AbstractD_derivedString: Property = Property(name="derivedString", type=StringType)
test_ast_AbstractD.attributes={test_ast_AbstractD_derivedString}

# test_ast_E class attributes and methods
test_ast_E_derivedBool: Property = Property(name="derivedBool", type=BooleanType)
test_ast_E_lazyBool: Property = Property(name="lazyBool", type=BooleanType)
test_ast_E.attributes={test_ast_E_derivedBool, test_ast_E_lazyBool}

# test_ntas_B class attributes and methods

# test_ntas_C class attributes and methods
test_ntas_C_someTerminal: Property = Property(name="someTerminal", type=StringType)
test_ntas_C.attributes={test_ntas_C_someTerminal}

# test_ast_D class attributes and methods
test_ast_D_someBool: Property = Property(name="someBool", type=BooleanType)
test_ast_D_someOtherBool: Property = Property(name="someOtherBool", type=StringType)
test_ast_D_index: Property = Property(name="index", type=IntegerType)
test_ast_D_name: Property = Property(name="name", type=StringType)
test_ast_D_someQCollection: Property = Property(name="someQCollection", type=StringType)
test_ast_D_someCollection: Property = Property(name="someCollection", type=StringType)
test_ast_D_m_operationAttribute: Method = Method(name="operationAttribute", parameters={Parameter(name='test_param', type=StringType)}, type=StringType)
test_ast_D.attributes={test_ast_D_someQCollection, test_ast_D_index, test_ast_D_name, test_ast_D_someCollection, test_ast_D_someBool, test_ast_D_someOtherBool}
test_ast_D.methods={test_ast_D_m_operationAttribute}

# AbstractD class attributes and methods

# Relationships
containmentC3: BinaryAssociation = BinaryAssociation(
    name="containmentC3",
    ends={
        Property(name="C", type=test_ntas_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ntas_Root4", type=C, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containmentD5: BinaryAssociation = BinaryAssociation(
    name="containmentD5",
    ends={
        Property(name="D", type=test_ntas_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ntas_Root6", type=D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
myA7: BinaryAssociation = BinaryAssociation(
    name="myA7",
    ends={
        Property(name="A9", type=test_ntas_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ntas_Root8", type=A, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
derivedA0: BinaryAssociation = BinaryAssociation(
    name="derivedA0",
    ends={
        Property(name="A", type=test_ntas_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ntas_Root", type=A, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
derivedB1: BinaryAssociation = BinaryAssociation(
    name="derivedB1",
    ends={
        Property(name="B", type=test_ntas_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ntas_Root2", type=B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refToSomeA33: BinaryAssociation = BinaryAssociation(
    name="refToSomeA33",
    ends={
        Property(name="A34", type=test_ast_AbstractD, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ast_AbstractD", type=A, multiplicity=Multiplicity(1, 1))
    }
)
lowerD10: BinaryAssociation = BinaryAssociation(
    name="lowerD10",
    ends={
        Property(name="D11", type=test_ast_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ast_D", type=D, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
UpperC12: BinaryAssociation = BinaryAssociation(
    name="UpperC12",
    ends={
        Property(name="C14", type=test_ast_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ast_D13", type=C, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
multipleLowerD15: BinaryAssociation = BinaryAssociation(
    name="multipleLowerD15",
    ends={
        Property(name="D17", type=test_ast_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ast_D16", type=D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
MultipleUpperC18: BinaryAssociation = BinaryAssociation(
    name="MultipleUpperC18",
    ends={
        Property(name="C20", type=test_ast_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ast_D19", type=C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DerivedUpperD21: BinaryAssociation = BinaryAssociation(
    name="DerivedUpperD21",
    ends={
        Property(name="D23", type=test_ast_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ast_D22", type=D, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
DerivedMultipleUpperC24: BinaryAssociation = BinaryAssociation(
    name="DerivedMultipleUpperC24",
    ends={
        Property(name="C26", type=test_ast_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ast_D25", type=C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
UpperA27: BinaryAssociation = BinaryAssociation(
    name="UpperA27",
    ends={
        Property(name="A29", type=test_ast_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ast_D28", type=A, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
derivedMultipleLowerA30: BinaryAssociation = BinaryAssociation(
    name="derivedMultipleLowerA30",
    ends={
        Property(name="A32", type=test_ast_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ast_D31", type=A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_test_ast_E_D = Generalization(general=D, specific=test_ast_E)
gen_test_ast_D_AbstractD = Generalization(general=AbstractD, specific=test_ast_D)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={C, D, test_ntas_A, test_ntas_Root, A, B, test_ast_AbstractD, test_ast_E, test_ntas_B, test_ntas_C, test_ast_D, AbstractD},
    associations={containmentC3, containmentD5, myA7, derivedA0, derivedB1, refToSomeA33, lowerD10, UpperC12, multipleLowerD15, MultipleUpperC18, DerivedUpperD21, DerivedMultipleUpperC24, UpperA27, derivedMultipleLowerA30},
    generalizations={gen_test_ast_E_D, gen_test_ast_D_AbstractD},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)