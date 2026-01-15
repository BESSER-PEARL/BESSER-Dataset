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
xtextTest_EmfTest = Class(name="xtextTest::EmfTest")
xtextTest_Input = Class(name="xtextTest::Input")
xtextTest_Tokens = Class(name="xtextTest::Tokens")
xtextTest_Element = Class(name="xtextTest::Element")
xtextTest_Generator = Class(name="xtextTest::Generator")
xtextTest_Model = Class(name="xtextTest::Model")
xtextTest_XtextTest = Class(name="xtextTest::XtextTest")
xtextTest_Import = Class(name="xtextTest::Import")
xtextTest_CodeCall = Class(name="xtextTest::CodeCall")
xtextTest_Before = Class(name="xtextTest::Before")
xtextTest_After = Class(name="xtextTest::After")
xtextTest_MyTokens = Class(name="xtextTest::MyTokens")
xtextTest_Inner = Class(name="xtextTest::Inner")
xtextTest_ReplacePatterns = Class(name="xtextTest::ReplacePatterns")

# xtextTest_EmfTest class attributes and methods
xtextTest_EmfTest_package: Property = Property(name="package", type=StringType)
xtextTest_EmfTest_mydefault: Property = Property(name="mydefault", type=StringType)
xtextTest_EmfTest_timeOut: Property = Property(name="timeOut", type=IntegerType)
xtextTest_EmfTest_file: Property = Property(name="file", type=StringType)
xtextTest_EmfTest.attributes={xtextTest_EmfTest_timeOut, xtextTest_EmfTest_mydefault, xtextTest_EmfTest_package, xtextTest_EmfTest_file}

# xtextTest_Input class attributes and methods
xtextTest_Input_text: Property = Property(name="text", type=StringType)
xtextTest_Input_file: Property = Property(name="file", type=StringType)
xtextTest_Input.attributes={xtextTest_Input_file, xtextTest_Input_text}

# xtextTest_Tokens class attributes and methods

# xtextTest_Element class attributes and methods
xtextTest_Element_importing: Property = Property(name="importing", type=StringType)
xtextTest_Element_name: Property = Property(name="name", type=StringType)
xtextTest_Element.attributes={xtextTest_Element_importing, xtextTest_Element_name}

# xtextTest_Generator class attributes and methods
xtextTest_Generator_output: Property = Property(name="output", type=StringType)
xtextTest_Generator_expected: Property = Property(name="expected", type=StringType)
xtextTest_Generator_isSameAsInputFile: Property = Property(name="isSameAsInputFile", type=BooleanType)
xtextTest_Generator_patternFile: Property = Property(name="patternFile", type=StringType)
xtextTest_Generator_exception: Property = Property(name="exception", type=StringType)
xtextTest_Generator.attributes={xtextTest_Generator_expected, xtextTest_Generator_output, xtextTest_Generator_exception, xtextTest_Generator_isSameAsInputFile, xtextTest_Generator_patternFile}

# xtextTest_Model class attributes and methods

# xtextTest_XtextTest class attributes and methods
xtextTest_XtextTest_package: Property = Property(name="package", type=StringType)
xtextTest_XtextTest_lang: Property = Property(name="lang", type=StringType)
xtextTest_XtextTest_imports: Property = Property(name="imports", type=StringType)
xtextTest_XtextTest_boolean: Property = Property(name="boolean", type=StringType)
xtextTest_XtextTest_timeOut: Property = Property(name="timeOut", type=IntegerType)
xtextTest_XtextTest.attributes={xtextTest_XtextTest_package, xtextTest_XtextTest_lang, xtextTest_XtextTest_boolean, xtextTest_XtextTest_imports, xtextTest_XtextTest_timeOut}

# xtextTest_Import class attributes and methods
xtextTest_Import_id: Property = Property(name="id", type=StringType)
xtextTest_Import_alias: Property = Property(name="alias", type=StringType)
xtextTest_Import.attributes={xtextTest_Import_alias, xtextTest_Import_id}

# xtextTest_CodeCall class attributes and methods
xtextTest_CodeCall_myclass: Property = Property(name="myclass", type=StringType)
xtextTest_CodeCall_method: Property = Property(name="method", type=StringType)
xtextTest_CodeCall_params: Property = Property(name="params", type=StringType)
xtextTest_CodeCall.attributes={xtextTest_CodeCall_params, xtextTest_CodeCall_myclass, xtextTest_CodeCall_method}

# xtextTest_Before class attributes and methods

# xtextTest_After class attributes and methods

# xtextTest_MyTokens class attributes and methods
xtextTest_MyTokens_token: Property = Property(name="token", type=StringType)
xtextTest_MyTokens_string: Property = Property(name="string", type=StringType)
xtextTest_MyTokens_count: Property = Property(name="count", type=IntegerType)
xtextTest_MyTokens.attributes={xtextTest_MyTokens_string, xtextTest_MyTokens_count, xtextTest_MyTokens_token}

# xtextTest_Inner class attributes and methods
xtextTest_Inner_value: Property = Property(name="value", type=StringType)
xtextTest_Inner_assignAsData: Property = Property(name="assignAsData", type=StringType)
xtextTest_Inner_assignAsBool: Property = Property(name="assignAsBool", type=StringType)
xtextTest_Inner_isNull: Property = Property(name="isNull", type=BooleanType)
xtextTest_Inner_isNotNull: Property = Property(name="isNotNull", type=BooleanType)
xtextTest_Inner_isEmpty: Property = Property(name="isEmpty", type=BooleanType)
xtextTest_Inner_parameter: Property = Property(name="parameter", type=StringType)
xtextTest_Inner.attributes={xtextTest_Inner_value, xtextTest_Inner_isNull, xtextTest_Inner_isEmpty, xtextTest_Inner_assignAsData, xtextTest_Inner_parameter, xtextTest_Inner_assignAsBool, xtextTest_Inner_isNotNull}

# xtextTest_ReplacePatterns class attributes and methods
xtextTest_ReplacePatterns_regex: Property = Property(name="regex", type=StringType)
xtextTest_ReplacePatterns_replace: Property = Property(name="replace", type=StringType)
xtextTest_ReplacePatterns.attributes={xtextTest_ReplacePatterns_replace, xtextTest_ReplacePatterns_regex}

# Relationships
emfTest1: BinaryAssociation = BinaryAssociation(
    name="emfTest1",
    ends={
        Property(name="xtextTest_EmfTest", type=xtextTest_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_Model2", type=xtextTest_EmfTest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
input3: BinaryAssociation = BinaryAssociation(
    name="input3",
    ends={
        Property(name="xtextTest_Input", type=xtextTest_XtextTest, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_XtextTest4", type=xtextTest_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tokens5: BinaryAssociation = BinaryAssociation(
    name="tokens5",
    ends={
        Property(name="xtextTest_Tokens", type=xtextTest_XtextTest, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_XtextTest6", type=xtextTest_Tokens, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
root7: BinaryAssociation = BinaryAssociation(
    name="root7",
    ends={
        Property(name="xtextTest_Element", type=xtextTest_XtextTest, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_XtextTest8", type=xtextTest_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xtextTest0: BinaryAssociation = BinaryAssociation(
    name="xtextTest0",
    ends={
        Property(name="xtextTest_XtextTest", type=xtextTest_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_Model", type=xtextTest_XtextTest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after13: BinaryAssociation = BinaryAssociation(
    name="after13",
    ends={
        Property(name="xtextTest_XtextTest14", type=xtextTest_After, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="xtextTest_After", type=xtextTest_XtextTest, multiplicity=Multiplicity(1, 1))
    }
)
myimport15: BinaryAssociation = BinaryAssociation(
    name="myimport15",
    ends={
        Property(name="xtextTest_Import", type=xtextTest_EmfTest, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_EmfTest16", type=xtextTest_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
codeCall17: BinaryAssociation = BinaryAssociation(
    name="codeCall17",
    ends={
        Property(name="xtextTest_CodeCall", type=xtextTest_EmfTest, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_EmfTest18", type=xtextTest_CodeCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optionCall19: BinaryAssociation = BinaryAssociation(
    name="optionCall19",
    ends={
        Property(name="xtextTest_CodeCall21", type=xtextTest_EmfTest, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_EmfTest20", type=xtextTest_CodeCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paramCall22: BinaryAssociation = BinaryAssociation(
    name="paramCall22",
    ends={
        Property(name="xtextTest_CodeCall24", type=xtextTest_EmfTest, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_EmfTest23", type=xtextTest_CodeCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output9: BinaryAssociation = BinaryAssociation(
    name="output9",
    ends={
        Property(name="xtextTest_Generator", type=xtextTest_XtextTest, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_XtextTest10", type=xtextTest_Generator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
before11: BinaryAssociation = BinaryAssociation(
    name="before11",
    ends={
        Property(name="xtextTest_Before", type=xtextTest_XtextTest, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_XtextTest12", type=xtextTest_Before, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tokens34: BinaryAssociation = BinaryAssociation(
    name="tokens34",
    ends={
        Property(name="xtextTest_MyTokens", type=xtextTest_Tokens, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_Tokens35", type=xtextTest_MyTokens, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root25: BinaryAssociation = BinaryAssociation(
    name="root25",
    ends={
        Property(name="xtextTest_Element27", type=xtextTest_EmfTest, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_EmfTest26", type=xtextTest_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
before28: BinaryAssociation = BinaryAssociation(
    name="before28",
    ends={
        Property(name="xtextTest_Before30", type=xtextTest_EmfTest, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_EmfTest29", type=xtextTest_Before, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after31: BinaryAssociation = BinaryAssociation(
    name="after31",
    ends={
        Property(name="xtextTest_After33", type=xtextTest_EmfTest, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_EmfTest32", type=xtextTest_After, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignList41: BinaryAssociation = BinaryAssociation(
    name="assignList41",
    ends={
        Property(name="xtextTest_Element43", type=xtextTest_Inner, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_Inner42", type=xtextTest_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replacePatterns44: BinaryAssociation = BinaryAssociation(
    name="replacePatterns44",
    ends={
        Property(name="xtextTest_ReplacePatterns", type=xtextTest_Generator, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_Generator45", type=xtextTest_ReplacePatterns, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inner36: BinaryAssociation = BinaryAssociation(
    name="inner36",
    ends={
        Property(name="xtextTest_Inner", type=xtextTest_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_Element37", type=xtextTest_Inner, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assign38: BinaryAssociation = BinaryAssociation(
    name="assign38",
    ends={
        Property(name="xtextTest_Element40", type=xtextTest_Inner, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_Inner39", type=xtextTest_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
codeCall49: BinaryAssociation = BinaryAssociation(
    name="codeCall49",
    ends={
        Property(name="xtextTest_CodeCall51", type=xtextTest_After, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_After50", type=xtextTest_CodeCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
codeCall46: BinaryAssociation = BinaryAssociation(
    name="codeCall46",
    ends={
        Property(name="xtextTest_CodeCall48", type=xtextTest_Before, multiplicity=Multiplicity(1, 1)),
        Property(name="xtextTest_Before47", type=xtextTest_CodeCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="xtextTest",
    types={xtextTest_EmfTest, xtextTest_Input, xtextTest_Tokens, xtextTest_Element, xtextTest_Generator, xtextTest_Model, xtextTest_XtextTest, xtextTest_Import, xtextTest_CodeCall, xtextTest_Before, xtextTest_After, xtextTest_MyTokens, xtextTest_Inner, xtextTest_ReplacePatterns},
    associations={emfTest1, input3, tokens5, root7, xtextTest0, after13, myimport15, codeCall17, optionCall19, paramCall22, output9, before11, tokens34, root25, before28, after31, assignList41, replacePatterns44, inner36, assign38, codeCall49, codeCall46},
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