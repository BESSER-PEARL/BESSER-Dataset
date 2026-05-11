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
smallJava_SJProgram = Class(name="smallJava_SJProgram")
smallJava_SJParameter = Class(name="smallJava_SJParameter")
smallJava_SJBlock = Class(name="smallJava_SJBlock")
SJSymbol = Class(name="SJSymbol")
smallJava_SJStatement = Class(name="smallJava_SJStatement")
smallJava_SJClass = Class(name="smallJava_SJClass")
SJNamedElement = Class(name="SJNamedElement")
smallJava_SJMember = Class(name="smallJava_SJMember")
smallJava_SJField = Class(name="smallJava_SJField")
SJMember = Class(name="SJMember")
smallJava_SJMethod = Class(name="smallJava_SJMethod")
smallJava_SJNamedElement = Class(name="smallJava_SJNamedElement")
smallJava_SJVariableDeclaration = Class(name="smallJava_SJVariableDeclaration")
SJStatement = Class(name="SJStatement")
smallJava_SJExpression = Class(name="smallJava_SJExpression")
smallJava_SJReturn = Class(name="smallJava_SJReturn")
smallJava_SJIfStatement = Class(name="smallJava_SJIfStatement")
smallJava_SJSymbol = Class(name="smallJava_SJSymbol")
smallJava_SJAssignment = Class(name="smallJava_SJAssignment")
SJExpression = Class(name="SJExpression")
smallJava_SJMemberSelection = Class(name="smallJava_SJMemberSelection")
smallJava_SJStringConstant = Class(name="smallJava_SJStringConstant")
smallJava_SJIntConstant = Class(name="smallJava_SJIntConstant")
smallJava_SJBoolConstant = Class(name="smallJava_SJBoolConstant")
smallJava_SJThis = Class(name="smallJava_SJThis")
smallJava_SJNull = Class(name="smallJava_SJNull")
smallJava_SJSymbolRef = Class(name="smallJava_SJSymbolRef")
smallJava_SJNew = Class(name="smallJava_SJNew")

# smallJava_SJProgram class attributes and methods

# smallJava_SJParameter class attributes and methods

# smallJava_SJBlock class attributes and methods

# SJSymbol class attributes and methods

# smallJava_SJStatement class attributes and methods

# smallJava_SJClass class attributes and methods

# SJNamedElement class attributes and methods

# smallJava_SJMember class attributes and methods

# smallJava_SJField class attributes and methods

# SJMember class attributes and methods

# smallJava_SJMethod class attributes and methods

# smallJava_SJNamedElement class attributes and methods
smallJava_SJNamedElement_name: Property = Property(name="name", type=StringType)
smallJava_SJNamedElement.attributes={smallJava_SJNamedElement_name}

# smallJava_SJVariableDeclaration class attributes and methods

# SJStatement class attributes and methods

# smallJava_SJExpression class attributes and methods

# smallJava_SJReturn class attributes and methods

# smallJava_SJIfStatement class attributes and methods

# smallJava_SJSymbol class attributes and methods

# smallJava_SJAssignment class attributes and methods

# SJExpression class attributes and methods

# smallJava_SJMemberSelection class attributes and methods
smallJava_SJMemberSelection_methodinvocation: Property = Property(name="methodinvocation", type=BooleanType)
smallJava_SJMemberSelection.attributes={smallJava_SJMemberSelection_methodinvocation}

# smallJava_SJStringConstant class attributes and methods
smallJava_SJStringConstant_value: Property = Property(name="value", type=StringType)
smallJava_SJStringConstant.attributes={smallJava_SJStringConstant_value}

# smallJava_SJIntConstant class attributes and methods
smallJava_SJIntConstant_value: Property = Property(name="value", type=IntegerType)
smallJava_SJIntConstant.attributes={smallJava_SJIntConstant_value}

# smallJava_SJBoolConstant class attributes and methods
smallJava_SJBoolConstant_value: Property = Property(name="value", type=StringType)
smallJava_SJBoolConstant.attributes={smallJava_SJBoolConstant_value}

# smallJava_SJThis class attributes and methods

# smallJava_SJNull class attributes and methods

# smallJava_SJSymbolRef class attributes and methods

# smallJava_SJNew class attributes and methods

# Relationships
params9: BinaryAssociation = BinaryAssociation(
    name="params9",
    ends={
        Property(name="smallJava_SJParameter", type=smallJava_SJMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJMethod", type=smallJava_SJParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body10: BinaryAssociation = BinaryAssociation(
    name="body10",
    ends={
        Property(name="smallJava_SJBlock", type=smallJava_SJMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJMethod11", type=smallJava_SJBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="smallJava_SJClass", type=smallJava_SJProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJProgram", type=smallJava_SJClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclass2: BinaryAssociation = BinaryAssociation(
    name="superclass2",
    ends={
        Property(name="smallJava_SJClass3", type=smallJava_SJClass, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJClass1", type=smallJava_SJClass, multiplicity=Multiplicity(0, 1))
    }
)
members4: BinaryAssociation = BinaryAssociation(
    name="members4",
    ends={
        Property(name="smallJava_SJMember", type=smallJava_SJClass, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJClass5", type=smallJava_SJMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="smallJava_SJClass8", type=smallJava_SJMember, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJMember7", type=smallJava_SJClass, multiplicity=Multiplicity(0, 1))
    }
)
statements12: BinaryAssociation = BinaryAssociation(
    name="statements12",
    ends={
        Property(name="smallJava_SJStatement", type=smallJava_SJBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJBlock13", type=smallJava_SJStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression14: BinaryAssociation = BinaryAssociation(
    name="expression14",
    ends={
        Property(name="smallJava_SJExpression", type=smallJava_SJVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJVariableDeclaration", type=smallJava_SJExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression15: BinaryAssociation = BinaryAssociation(
    name="expression15",
    ends={
        Property(name="smallJava_SJExpression16", type=smallJava_SJReturn, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJReturn", type=smallJava_SJExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression17: BinaryAssociation = BinaryAssociation(
    name="expression17",
    ends={
        Property(name="smallJava_SJExpression18", type=smallJava_SJIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJIfStatement", type=smallJava_SJExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBlock19: BinaryAssociation = BinaryAssociation(
    name="thenBlock19",
    ends={
        Property(name="smallJava_SJBlock21", type=smallJava_SJIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJIfStatement20", type=smallJava_SJBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock22: BinaryAssociation = BinaryAssociation(
    name="elseBlock22",
    ends={
        Property(name="smallJava_SJBlock24", type=smallJava_SJIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJIfStatement23", type=smallJava_SJBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="smallJava_SJClass26", type=smallJava_SJSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJSymbol", type=smallJava_SJClass, multiplicity=Multiplicity(0, 1))
    }
)
left27: BinaryAssociation = BinaryAssociation(
    name="left27",
    ends={
        Property(name="smallJava_SJExpression28", type=smallJava_SJAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJAssignment", type=smallJava_SJExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right29: BinaryAssociation = BinaryAssociation(
    name="right29",
    ends={
        Property(name="smallJava_SJExpression31", type=smallJava_SJAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJAssignment30", type=smallJava_SJExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver32: BinaryAssociation = BinaryAssociation(
    name="receiver32",
    ends={
        Property(name="smallJava_SJExpression33", type=smallJava_SJMemberSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJMemberSelection", type=smallJava_SJExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member34: BinaryAssociation = BinaryAssociation(
    name="member34",
    ends={
        Property(name="smallJava_SJMember36", type=smallJava_SJMemberSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJMemberSelection35", type=smallJava_SJMember, multiplicity=Multiplicity(0, 1))
    }
)
args37: BinaryAssociation = BinaryAssociation(
    name="args37",
    ends={
        Property(name="smallJava_SJExpression39", type=smallJava_SJMemberSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJMemberSelection38", type=smallJava_SJExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
symbol40: BinaryAssociation = BinaryAssociation(
    name="symbol40",
    ends={
        Property(name="smallJava_SJSymbol41", type=smallJava_SJSymbolRef, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJSymbolRef", type=smallJava_SJSymbol, multiplicity=Multiplicity(0, 1))
    }
)
type42: BinaryAssociation = BinaryAssociation(
    name="type42",
    ends={
        Property(name="smallJava_SJClass43", type=smallJava_SJNew, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJNew", type=smallJava_SJClass, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_smallJava_SJParameter_SJSymbol = Generalization(general=SJSymbol, specific=smallJava_SJParameter)
gen_smallJava_SJClass_SJNamedElement = Generalization(general=SJNamedElement, specific=smallJava_SJClass)
gen_smallJava_SJMember_SJNamedElement = Generalization(general=SJNamedElement, specific=smallJava_SJMember)
gen_smallJava_SJField_SJMember = Generalization(general=SJMember, specific=smallJava_SJField)
gen_smallJava_SJMethod_SJMember = Generalization(general=SJMember, specific=smallJava_SJMethod)
gen_smallJava_SJExpression_SJStatement = Generalization(general=SJStatement, specific=smallJava_SJExpression)
gen_smallJava_SJVariableDeclaration_SJStatement = Generalization(general=SJStatement, specific=smallJava_SJVariableDeclaration)
gen_smallJava_SJVariableDeclaration_SJSymbol = Generalization(general=SJSymbol, specific=smallJava_SJVariableDeclaration)
gen_smallJava_SJReturn_SJStatement = Generalization(general=SJStatement, specific=smallJava_SJReturn)
gen_smallJava_SJIfStatement_SJStatement = Generalization(general=SJStatement, specific=smallJava_SJIfStatement)
gen_smallJava_SJSymbol_SJNamedElement = Generalization(general=SJNamedElement, specific=smallJava_SJSymbol)
gen_smallJava_SJAssignment_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJAssignment)
gen_smallJava_SJMemberSelection_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJMemberSelection)
gen_smallJava_SJStringConstant_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJStringConstant)
gen_smallJava_SJIntConstant_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJIntConstant)
gen_smallJava_SJBoolConstant_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJBoolConstant)
gen_smallJava_SJThis_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJThis)
gen_smallJava_SJNull_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJNull)
gen_smallJava_SJSymbolRef_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJSymbolRef)
gen_smallJava_SJNew_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJNew)

# Domain Model
domain_model = DomainModel(
    name="smallJava",
    types={smallJava_SJProgram, smallJava_SJParameter, smallJava_SJBlock, SJSymbol, smallJava_SJStatement, smallJava_SJClass, SJNamedElement, smallJava_SJMember, smallJava_SJField, SJMember, smallJava_SJMethod, smallJava_SJNamedElement, smallJava_SJVariableDeclaration, SJStatement, smallJava_SJExpression, smallJava_SJReturn, smallJava_SJIfStatement, smallJava_SJSymbol, smallJava_SJAssignment, SJExpression, smallJava_SJMemberSelection, smallJava_SJStringConstant, smallJava_SJIntConstant, smallJava_SJBoolConstant, smallJava_SJThis, smallJava_SJNull, smallJava_SJSymbolRef, smallJava_SJNew},
    associations={params9, body10, classes0, superclass2, members4, type6, statements12, expression14, expression15, expression17, thenBlock19, elseBlock22, type25, left27, right29, receiver32, member34, args37, symbol40, type42},
    generalizations={gen_smallJava_SJParameter_SJSymbol, gen_smallJava_SJClass_SJNamedElement, gen_smallJava_SJMember_SJNamedElement, gen_smallJava_SJField_SJMember, gen_smallJava_SJMethod_SJMember, gen_smallJava_SJExpression_SJStatement, gen_smallJava_SJVariableDeclaration_SJStatement, gen_smallJava_SJVariableDeclaration_SJSymbol, gen_smallJava_SJReturn_SJStatement, gen_smallJava_SJIfStatement_SJStatement, gen_smallJava_SJSymbol_SJNamedElement, gen_smallJava_SJAssignment_SJExpression, gen_smallJava_SJMemberSelection_SJExpression, gen_smallJava_SJStringConstant_SJExpression, gen_smallJava_SJIntConstant_SJExpression, gen_smallJava_SJBoolConstant_SJExpression, gen_smallJava_SJThis_SJExpression, gen_smallJava_SJNull_SJExpression, gen_smallJava_SJSymbolRef_SJExpression, gen_smallJava_SJNew_SJExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)