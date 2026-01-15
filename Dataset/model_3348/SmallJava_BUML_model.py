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
SJAccessLevel: Enumeration = Enumeration(
    name="SJAccessLevel",
    literals={
            EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="PROTECTED")
    }
)

# Classes
smallJava_SJProgram = Class(name="smallJava::SJProgram")
smallJava_SJImport = Class(name="smallJava::SJImport")
smallJava_SJClass = Class(name="smallJava::SJClass")
smallJava_SJMember = Class(name="smallJava::SJMember")
smallJava_SJIfBlock = Class(name="smallJava::SJIfBlock")
smallJava_SJBlock = Class(name="smallJava::SJBlock")
smallJava_SJSymbol = Class(name="smallJava::SJSymbol")
smallJava_SJAssignment = Class(name="smallJava::SJAssignment")
SJExpression = Class(name="SJExpression")
smallJava_SJMemberSelection = Class(name="smallJava::SJMemberSelection")
smallJava_SJField = Class(name="smallJava::SJField")
SJMember = Class(name="SJMember")
smallJava_SJMethod = Class(name="smallJava::SJMethod")
smallJava_SJParameter = Class(name="smallJava::SJParameter")
smallJava_SJMethodBody = Class(name="smallJava::SJMethodBody")
SJSymbol = Class(name="SJSymbol")
SJBlock = Class(name="SJBlock")
smallJava_SJStatement = Class(name="smallJava::SJStatement")
smallJava_SJReturn = Class(name="smallJava::SJReturn")
SJStatement = Class(name="SJStatement")
smallJava_SJExpression = Class(name="smallJava::SJExpression")
smallJava_SJVariableDeclaration = Class(name="smallJava::SJVariableDeclaration")
smallJava_SJIfStatement = Class(name="smallJava::SJIfStatement")
smallJava_SJStringConstant = Class(name="smallJava::SJStringConstant")
smallJava_SJIntConstant = Class(name="smallJava::SJIntConstant")
smallJava_SJBoolConstant = Class(name="smallJava::SJBoolConstant")
smallJava_SJThis = Class(name="smallJava::SJThis")
smallJava_SJSuper = Class(name="smallJava::SJSuper")
smallJava_SJNull = Class(name="smallJava::SJNull")
smallJava_SJSymbolRef = Class(name="smallJava::SJSymbolRef")
smallJava_SJNew = Class(name="smallJava::SJNew")

# smallJava_SJProgram class attributes and methods
smallJava_SJProgram_name: Property = Property(name="name", type=StringType)
smallJava_SJProgram.attributes={smallJava_SJProgram_name}

# smallJava_SJImport class attributes and methods
smallJava_SJImport_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
smallJava_SJImport.attributes={smallJava_SJImport_importedNamespace}

# smallJava_SJClass class attributes and methods
smallJava_SJClass_name: Property = Property(name="name", type=StringType)
smallJava_SJClass.attributes={smallJava_SJClass_name}

# smallJava_SJMember class attributes and methods
smallJava_SJMember_access: Property = Property(name="access", type=StringType)
smallJava_SJMember_name: Property = Property(name="name", type=StringType)
smallJava_SJMember.attributes={smallJava_SJMember_name, smallJava_SJMember_access}

# smallJava_SJIfBlock class attributes and methods

# smallJava_SJBlock class attributes and methods

# smallJava_SJSymbol class attributes and methods
smallJava_SJSymbol_name: Property = Property(name="name", type=StringType)
smallJava_SJSymbol.attributes={smallJava_SJSymbol_name}

# smallJava_SJAssignment class attributes and methods

# SJExpression class attributes and methods

# smallJava_SJMemberSelection class attributes and methods
smallJava_SJMemberSelection_methodinvocation: Property = Property(name="methodinvocation", type=BooleanType)
smallJava_SJMemberSelection.attributes={smallJava_SJMemberSelection_methodinvocation}

# smallJava_SJField class attributes and methods

# SJMember class attributes and methods

# smallJava_SJMethod class attributes and methods

# smallJava_SJParameter class attributes and methods

# smallJava_SJMethodBody class attributes and methods

# SJSymbol class attributes and methods

# SJBlock class attributes and methods

# smallJava_SJStatement class attributes and methods

# smallJava_SJReturn class attributes and methods

# SJStatement class attributes and methods

# smallJava_SJExpression class attributes and methods

# smallJava_SJVariableDeclaration class attributes and methods

# smallJava_SJIfStatement class attributes and methods

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

# smallJava_SJSuper class attributes and methods

# smallJava_SJNull class attributes and methods

# smallJava_SJSymbolRef class attributes and methods

# smallJava_SJNew class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="smallJava_SJImport", type=smallJava_SJProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJProgram", type=smallJava_SJImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes1: BinaryAssociation = BinaryAssociation(
    name="classes1",
    ends={
        Property(name="smallJava_SJClass", type=smallJava_SJProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJProgram2", type=smallJava_SJClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclass4: BinaryAssociation = BinaryAssociation(
    name="superclass4",
    ends={
        Property(name="smallJava_SJClass5", type=smallJava_SJClass, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJClass3", type=smallJava_SJClass, multiplicity=Multiplicity(0, 1))
    }
)
members6: BinaryAssociation = BinaryAssociation(
    name="members6",
    ends={
        Property(name="smallJava_SJMember", type=smallJava_SJClass, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJClass7", type=smallJava_SJMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="smallJava_SJClass10", type=smallJava_SJMember, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJMember9", type=smallJava_SJClass, multiplicity=Multiplicity(0, 1))
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
        Property(name="smallJava_SJIfBlock", type=smallJava_SJIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJIfStatement20", type=smallJava_SJIfBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock21: BinaryAssociation = BinaryAssociation(
    name="elseBlock21",
    ends={
        Property(name="smallJava_SJIfBlock23", type=smallJava_SJIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJIfStatement22", type=smallJava_SJIfBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements24: BinaryAssociation = BinaryAssociation(
    name="statements24",
    ends={
        Property(name="smallJava_SJStatement", type=smallJava_SJBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJBlock", type=smallJava_SJStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
params11: BinaryAssociation = BinaryAssociation(
    name="params11",
    ends={
        Property(name="smallJava_SJParameter", type=smallJava_SJMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJMethod", type=smallJava_SJParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body12: BinaryAssociation = BinaryAssociation(
    name="body12",
    ends={
        Property(name="smallJava_SJMethodBody", type=smallJava_SJMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJMethod13", type=smallJava_SJMethodBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression14: BinaryAssociation = BinaryAssociation(
    name="expression14",
    ends={
        Property(name="smallJava_SJExpression", type=smallJava_SJReturn, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJReturn", type=smallJava_SJExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression15: BinaryAssociation = BinaryAssociation(
    name="expression15",
    ends={
        Property(name="smallJava_SJExpression16", type=smallJava_SJVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="smallJava_SJVariableDeclaration", type=smallJava_SJExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
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
gen_smallJava_SJIfBlock_SJBlock = Generalization(general=SJBlock, specific=smallJava_SJIfBlock)
gen_smallJava_SJExpression_SJStatement = Generalization(general=SJStatement, specific=smallJava_SJExpression)
gen_smallJava_SJAssignment_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJAssignment)
gen_smallJava_SJMemberSelection_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJMemberSelection)
gen_smallJava_SJField_SJMember = Generalization(general=SJMember, specific=smallJava_SJField)
gen_smallJava_SJMethod_SJMember = Generalization(general=SJMember, specific=smallJava_SJMethod)
gen_smallJava_SJParameter_SJSymbol = Generalization(general=SJSymbol, specific=smallJava_SJParameter)
gen_smallJava_SJMethodBody_SJBlock = Generalization(general=SJBlock, specific=smallJava_SJMethodBody)
gen_smallJava_SJReturn_SJStatement = Generalization(general=SJStatement, specific=smallJava_SJReturn)
gen_smallJava_SJVariableDeclaration_SJStatement = Generalization(general=SJStatement, specific=smallJava_SJVariableDeclaration)
gen_smallJava_SJVariableDeclaration_SJSymbol = Generalization(general=SJSymbol, specific=smallJava_SJVariableDeclaration)
gen_smallJava_SJIfStatement_SJStatement = Generalization(general=SJStatement, specific=smallJava_SJIfStatement)
gen_smallJava_SJStringConstant_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJStringConstant)
gen_smallJava_SJIntConstant_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJIntConstant)
gen_smallJava_SJBoolConstant_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJBoolConstant)
gen_smallJava_SJThis_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJThis)
gen_smallJava_SJSuper_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJSuper)
gen_smallJava_SJNull_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJNull)
gen_smallJava_SJSymbolRef_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJSymbolRef)
gen_smallJava_SJNew_SJExpression = Generalization(general=SJExpression, specific=smallJava_SJNew)

# Domain Model
domain_model = DomainModel(
    name="smallJava",
    types={smallJava_SJProgram, smallJava_SJImport, smallJava_SJClass, smallJava_SJMember, smallJava_SJIfBlock, smallJava_SJBlock, smallJava_SJSymbol, smallJava_SJAssignment, SJExpression, smallJava_SJMemberSelection, smallJava_SJField, SJMember, smallJava_SJMethod, smallJava_SJParameter, smallJava_SJMethodBody, SJSymbol, SJBlock, smallJava_SJStatement, smallJava_SJReturn, SJStatement, smallJava_SJExpression, smallJava_SJVariableDeclaration, smallJava_SJIfStatement, smallJava_SJStringConstant, smallJava_SJIntConstant, smallJava_SJBoolConstant, smallJava_SJThis, smallJava_SJSuper, smallJava_SJNull, smallJava_SJSymbolRef, smallJava_SJNew, SJAccessLevel},
    associations={imports0, classes1, superclass4, members6, type8, expression17, thenBlock19, elseBlock21, statements24, type25, left27, right29, receiver32, params11, body12, expression14, expression15, member34, args37, symbol40, type42},
    generalizations={gen_smallJava_SJIfBlock_SJBlock, gen_smallJava_SJExpression_SJStatement, gen_smallJava_SJAssignment_SJExpression, gen_smallJava_SJMemberSelection_SJExpression, gen_smallJava_SJField_SJMember, gen_smallJava_SJMethod_SJMember, gen_smallJava_SJParameter_SJSymbol, gen_smallJava_SJMethodBody_SJBlock, gen_smallJava_SJReturn_SJStatement, gen_smallJava_SJVariableDeclaration_SJStatement, gen_smallJava_SJVariableDeclaration_SJSymbol, gen_smallJava_SJIfStatement_SJStatement, gen_smallJava_SJStringConstant_SJExpression, gen_smallJava_SJIntConstant_SJExpression, gen_smallJava_SJBoolConstant_SJExpression, gen_smallJava_SJThis_SJExpression, gen_smallJava_SJSuper_SJExpression, gen_smallJava_SJNull_SJExpression, gen_smallJava_SJSymbolRef_SJExpression, gen_smallJava_SJNew_SJExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)