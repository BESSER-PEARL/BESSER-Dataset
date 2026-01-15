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
            EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Double")
    }
)

# Classes
testintentionsAssistance_Model = Class(name="testintentionsAssistance::Model")
testintentionsAssistance_DomainDeclaration = Class(name="testintentionsAssistance::DomainDeclaration")
AbstractElement = Class(name="AbstractElement")
testintentionsAssistance_Import = Class(name="testintentionsAssistance::Import")
testintentionsAssistance_Function = Class(name="testintentionsAssistance::Function")
testintentionsAssistance_OutVariable = Class(name="testintentionsAssistance::OutVariable")
testintentionsAssistance_Variable = Class(name="testintentionsAssistance::Variable")
testintentionsAssistance_Data = Class(name="testintentionsAssistance::Data")
testintentionsAssistance_Inst = Class(name="testintentionsAssistance::Inst")
testintentionsAssistance_AbstractElement = Class(name="testintentionsAssistance::AbstractElement")
testintentionsAssistance_TestIntention = Class(name="testintentionsAssistance::TestIntention")
testintentionsAssistance_Or = Class(name="testintentionsAssistance::Or")
Expression = Class(name="Expression")
testintentionsAssistance_And = Class(name="testintentionsAssistance::And")
testintentionsAssistance_Expression = Class(name="testintentionsAssistance::Expression")
testintentionsAssistance_Equality = Class(name="testintentionsAssistance::Equality")
testintentionsAssistance_Comparison = Class(name="testintentionsAssistance::Comparison")
testintentionsAssistance_Plus = Class(name="testintentionsAssistance::Plus")
testintentionsAssistance_Minus = Class(name="testintentionsAssistance::Minus")
testintentionsAssistance_MulOrDiv = Class(name="testintentionsAssistance::MulOrDiv")
testintentionsAssistance_Not = Class(name="testintentionsAssistance::Not")
testintentionsAssistance_INT = Class(name="testintentionsAssistance::INT")
testintentionsAssistance_STRING = Class(name="testintentionsAssistance::STRING")
testintentionsAssistance_Boolean = Class(name="testintentionsAssistance::Boolean")
testintentionsAssistance_Double = Class(name="testintentionsAssistance::Double")
testintentionsAssistance_VariableRef = Class(name="testintentionsAssistance::VariableRef")

# testintentionsAssistance_Model class attributes and methods

# testintentionsAssistance_DomainDeclaration class attributes and methods
testintentionsAssistance_DomainDeclaration_name: Property = Property(name="name", type=StringType)
testintentionsAssistance_DomainDeclaration.attributes={testintentionsAssistance_DomainDeclaration_name}

# AbstractElement class attributes and methods

# testintentionsAssistance_Import class attributes and methods
testintentionsAssistance_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
testintentionsAssistance_Import.attributes={testintentionsAssistance_Import_importedNamespace}

# testintentionsAssistance_Function class attributes and methods
testintentionsAssistance_Function_methode: Property = Property(name="methode", type=StringType)
testintentionsAssistance_Function.attributes={testintentionsAssistance_Function_methode}

# testintentionsAssistance_OutVariable class attributes and methods
testintentionsAssistance_OutVariable_name: Property = Property(name="name", type=StringType)
testintentionsAssistance_OutVariable_type: Property = Property(name="type", type=StringType)
testintentionsAssistance_OutVariable.attributes={testintentionsAssistance_OutVariable_type, testintentionsAssistance_OutVariable_name}

# testintentionsAssistance_Variable class attributes and methods
testintentionsAssistance_Variable_name: Property = Property(name="name", type=StringType)
testintentionsAssistance_Variable_type: Property = Property(name="type", type=StringType)
testintentionsAssistance_Variable.attributes={testintentionsAssistance_Variable_type, testintentionsAssistance_Variable_name}

# testintentionsAssistance_Data class attributes and methods

# testintentionsAssistance_Inst class attributes and methods

# testintentionsAssistance_AbstractElement class attributes and methods

# testintentionsAssistance_TestIntention class attributes and methods
testintentionsAssistance_TestIntention_description: Property = Property(name="description", type=StringType)
testintentionsAssistance_TestIntention.attributes={testintentionsAssistance_TestIntention_description}

# testintentionsAssistance_Or class attributes and methods

# Expression class attributes and methods

# testintentionsAssistance_And class attributes and methods

# testintentionsAssistance_Expression class attributes and methods

# testintentionsAssistance_Equality class attributes and methods
testintentionsAssistance_Equality_op: Property = Property(name="op", type=StringType)
testintentionsAssistance_Equality.attributes={testintentionsAssistance_Equality_op}

# testintentionsAssistance_Comparison class attributes and methods
testintentionsAssistance_Comparison_op: Property = Property(name="op", type=StringType)
testintentionsAssistance_Comparison.attributes={testintentionsAssistance_Comparison_op}

# testintentionsAssistance_Plus class attributes and methods

# testintentionsAssistance_Minus class attributes and methods

# testintentionsAssistance_MulOrDiv class attributes and methods
testintentionsAssistance_MulOrDiv_op: Property = Property(name="op", type=StringType)
testintentionsAssistance_MulOrDiv.attributes={testintentionsAssistance_MulOrDiv_op}

# testintentionsAssistance_Not class attributes and methods

# testintentionsAssistance_INT class attributes and methods
testintentionsAssistance_INT_value: Property = Property(name="value", type=IntegerType)
testintentionsAssistance_INT.attributes={testintentionsAssistance_INT_value}

# testintentionsAssistance_STRING class attributes and methods
testintentionsAssistance_STRING_value: Property = Property(name="value", type=StringType)
testintentionsAssistance_STRING.attributes={testintentionsAssistance_STRING_value}

# testintentionsAssistance_Boolean class attributes and methods
testintentionsAssistance_Boolean_value: Property = Property(name="value", type=StringType)
testintentionsAssistance_Boolean.attributes={testintentionsAssistance_Boolean_value}

# testintentionsAssistance_Double class attributes and methods
testintentionsAssistance_Double_value: Property = Property(name="value", type=StringType)
testintentionsAssistance_Double.attributes={testintentionsAssistance_Double_value}

# testintentionsAssistance_VariableRef class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="testintentionsAssistance_DomainDeclaration", type=testintentionsAssistance_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Model", type=testintentionsAssistance_DomainDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="testintentionsAssistance_DomainDeclaration2", type=testintentionsAssistance_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="testintentionsAssistance_AbstractElement", type=testintentionsAssistance_DomainDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
out3: BinaryAssociation = BinaryAssociation(
    name="out3",
    ends={
        Property(name="testintentionsAssistance_OutVariable", type=testintentionsAssistance_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Function", type=testintentionsAssistance_OutVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg4: BinaryAssociation = BinaryAssociation(
    name="arg4",
    ends={
        Property(name="testintentionsAssistance_Variable", type=testintentionsAssistance_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Function5", type=testintentionsAssistance_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
arg16: BinaryAssociation = BinaryAssociation(
    name="arg16",
    ends={
        Property(name="testintentionsAssistance_Variable8", type=testintentionsAssistance_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Function7", type=testintentionsAssistance_Variable, multiplicity=Multiplicity(0, 1))
    }
)
inst9: BinaryAssociation = BinaryAssociation(
    name="inst9",
    ends={
        Property(name="testintentionsAssistance_Inst", type=testintentionsAssistance_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Data", type=testintentionsAssistance_Inst, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable10: BinaryAssociation = BinaryAssociation(
    name="variable10",
    ends={
        Property(name="testintentionsAssistance_Variable12", type=testintentionsAssistance_Inst, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Inst11", type=testintentionsAssistance_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression15: BinaryAssociation = BinaryAssociation(
    name="expression15",
    ends={
        Property(name="testintentionsAssistance_Expression16", type=testintentionsAssistance_TestIntention, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_TestIntention", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outvar17: BinaryAssociation = BinaryAssociation(
    name="outvar17",
    ends={
        Property(name="testintentionsAssistance_OutVariable19", type=testintentionsAssistance_TestIntention, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_TestIntention18", type=testintentionsAssistance_OutVariable, multiplicity=Multiplicity(0, 1))
    }
)
left20: BinaryAssociation = BinaryAssociation(
    name="left20",
    ends={
        Property(name="testintentionsAssistance_Expression21", type=testintentionsAssistance_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Or", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right22: BinaryAssociation = BinaryAssociation(
    name="right22",
    ends={
        Property(name="testintentionsAssistance_Expression24", type=testintentionsAssistance_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Or23", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valeur13: BinaryAssociation = BinaryAssociation(
    name="valeur13",
    ends={
        Property(name="testintentionsAssistance_Expression", type=testintentionsAssistance_Inst, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Inst14", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right27: BinaryAssociation = BinaryAssociation(
    name="right27",
    ends={
        Property(name="testintentionsAssistance_Expression29", type=testintentionsAssistance_And, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_And28", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left30: BinaryAssociation = BinaryAssociation(
    name="left30",
    ends={
        Property(name="testintentionsAssistance_Expression31", type=testintentionsAssistance_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Equality", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right32: BinaryAssociation = BinaryAssociation(
    name="right32",
    ends={
        Property(name="testintentionsAssistance_Expression34", type=testintentionsAssistance_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Equality33", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left35: BinaryAssociation = BinaryAssociation(
    name="left35",
    ends={
        Property(name="testintentionsAssistance_Expression36", type=testintentionsAssistance_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Comparison", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right37: BinaryAssociation = BinaryAssociation(
    name="right37",
    ends={
        Property(name="testintentionsAssistance_Expression39", type=testintentionsAssistance_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Comparison38", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left40: BinaryAssociation = BinaryAssociation(
    name="left40",
    ends={
        Property(name="testintentionsAssistance_Expression41", type=testintentionsAssistance_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Plus", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left25: BinaryAssociation = BinaryAssociation(
    name="left25",
    ends={
        Property(name="testintentionsAssistance_Expression26", type=testintentionsAssistance_And, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_And", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left45: BinaryAssociation = BinaryAssociation(
    name="left45",
    ends={
        Property(name="testintentionsAssistance_Expression46", type=testintentionsAssistance_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Minus", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right47: BinaryAssociation = BinaryAssociation(
    name="right47",
    ends={
        Property(name="testintentionsAssistance_Expression49", type=testintentionsAssistance_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Minus48", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left50: BinaryAssociation = BinaryAssociation(
    name="left50",
    ends={
        Property(name="testintentionsAssistance_Expression51", type=testintentionsAssistance_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_MulOrDiv", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right52: BinaryAssociation = BinaryAssociation(
    name="right52",
    ends={
        Property(name="testintentionsAssistance_Expression54", type=testintentionsAssistance_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_MulOrDiv53", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression55: BinaryAssociation = BinaryAssociation(
    name="expression55",
    ends={
        Property(name="testintentionsAssistance_Expression56", type=testintentionsAssistance_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Not", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right42: BinaryAssociation = BinaryAssociation(
    name="right42",
    ends={
        Property(name="testintentionsAssistance_Expression44", type=testintentionsAssistance_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_Plus43", type=testintentionsAssistance_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable57: BinaryAssociation = BinaryAssociation(
    name="variable57",
    ends={
        Property(name="testintentionsAssistance_Variable58", type=testintentionsAssistance_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="testintentionsAssistance_VariableRef", type=testintentionsAssistance_Variable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_testintentionsAssistance_DomainDeclaration_AbstractElement = Generalization(general=AbstractElement, specific=testintentionsAssistance_DomainDeclaration)
gen_testintentionsAssistance_Import_AbstractElement = Generalization(general=AbstractElement, specific=testintentionsAssistance_Import)
gen_testintentionsAssistance_Function_AbstractElement = Generalization(general=AbstractElement, specific=testintentionsAssistance_Function)
gen_testintentionsAssistance_Data_AbstractElement = Generalization(general=AbstractElement, specific=testintentionsAssistance_Data)
gen_testintentionsAssistance_TestIntention_AbstractElement = Generalization(general=AbstractElement, specific=testintentionsAssistance_TestIntention)
gen_testintentionsAssistance_Or_Expression = Generalization(general=Expression, specific=testintentionsAssistance_Or)
gen_testintentionsAssistance_And_Expression = Generalization(general=Expression, specific=testintentionsAssistance_And)
gen_testintentionsAssistance_Equality_Expression = Generalization(general=Expression, specific=testintentionsAssistance_Equality)
gen_testintentionsAssistance_Comparison_Expression = Generalization(general=Expression, specific=testintentionsAssistance_Comparison)
gen_testintentionsAssistance_Plus_Expression = Generalization(general=Expression, specific=testintentionsAssistance_Plus)
gen_testintentionsAssistance_Minus_Expression = Generalization(general=Expression, specific=testintentionsAssistance_Minus)
gen_testintentionsAssistance_MulOrDiv_Expression = Generalization(general=Expression, specific=testintentionsAssistance_MulOrDiv)
gen_testintentionsAssistance_Not_Expression = Generalization(general=Expression, specific=testintentionsAssistance_Not)
gen_testintentionsAssistance_INT_Expression = Generalization(general=Expression, specific=testintentionsAssistance_INT)
gen_testintentionsAssistance_STRING_Expression = Generalization(general=Expression, specific=testintentionsAssistance_STRING)
gen_testintentionsAssistance_Double_Expression = Generalization(general=Expression, specific=testintentionsAssistance_Double)
gen_testintentionsAssistance_VariableRef_Expression = Generalization(general=Expression, specific=testintentionsAssistance_VariableRef)
gen_testintentionsAssistance_Boolean_Expression = Generalization(general=Expression, specific=testintentionsAssistance_Boolean)

# Domain Model
domain_model = DomainModel(
    name="testintentionsAssistance",
    types={testintentionsAssistance_Model, testintentionsAssistance_DomainDeclaration, AbstractElement, testintentionsAssistance_Import, testintentionsAssistance_Function, testintentionsAssistance_OutVariable, testintentionsAssistance_Variable, testintentionsAssistance_Data, testintentionsAssistance_Inst, testintentionsAssistance_AbstractElement, testintentionsAssistance_TestIntention, testintentionsAssistance_Or, Expression, testintentionsAssistance_And, testintentionsAssistance_Expression, testintentionsAssistance_Equality, testintentionsAssistance_Comparison, testintentionsAssistance_Plus, testintentionsAssistance_Minus, testintentionsAssistance_MulOrDiv, testintentionsAssistance_Not, testintentionsAssistance_INT, testintentionsAssistance_STRING, testintentionsAssistance_Boolean, testintentionsAssistance_Double, testintentionsAssistance_VariableRef, Type},
    associations={elements0, elements1, out3, arg4, arg16, inst9, variable10, expression15, outvar17, left20, right22, valeur13, right27, left30, right32, left35, right37, left40, left25, left45, right47, left50, right52, expression55, right42, variable57},
    generalizations={gen_testintentionsAssistance_DomainDeclaration_AbstractElement, gen_testintentionsAssistance_Import_AbstractElement, gen_testintentionsAssistance_Function_AbstractElement, gen_testintentionsAssistance_Data_AbstractElement, gen_testintentionsAssistance_TestIntention_AbstractElement, gen_testintentionsAssistance_Or_Expression, gen_testintentionsAssistance_And_Expression, gen_testintentionsAssistance_Equality_Expression, gen_testintentionsAssistance_Comparison_Expression, gen_testintentionsAssistance_Plus_Expression, gen_testintentionsAssistance_Minus_Expression, gen_testintentionsAssistance_MulOrDiv_Expression, gen_testintentionsAssistance_Not_Expression, gen_testintentionsAssistance_INT_Expression, gen_testintentionsAssistance_STRING_Expression, gen_testintentionsAssistance_Double_Expression, gen_testintentionsAssistance_VariableRef_Expression, gen_testintentionsAssistance_Boolean_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)