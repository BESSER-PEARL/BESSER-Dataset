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
terms_Declarations = Class(name="terms::Declarations")
terms_Empty = Class(name="terms::Empty")
terms_Partition = Class(name="terms::Partition")
terms_HLPNList = Class(name="terms::HLPNList")
terms_EmptyList = Class(name="terms::EmptyList")
terms_MakeList = Class(name="terms::MakeList")
terms_TermsDeclaration = Class(name="terms::TermsDeclaration", is_abstract=True)
terms_Declaration = Class(name="terms::Declaration")
terms_Sort = Class(name="terms::Sort", is_abstract=True)
terms_MultisetSort = Class(name="terms::MultisetSort")
terms_NamedSort = Class(name="terms::NamedSort")
terms_VariableDecl = Class(name="terms::VariableDecl")
terms_ProductSort = Class(name="terms::ProductSort")
terms_Type = Class(name="terms::Type")
terms_All = Class(name="terms::All")
TermsDeclaration = Class(name="TermsDeclaration")
Sort = Class(name="Sort")
terms_Term = Class(name="terms::Term", is_abstract=True)
terms_Operator = Class(name="terms::Operator", is_abstract=True)
terms_NamedOperator = Class(name="terms::NamedOperator")
terms_HLMarking = Class(name="terms::HLMarking")
terms_Condition = Class(name="terms::Condition")
terms_HLAnnotation = Class(name="terms::HLAnnotation")
terms_PartitionElement = Class(name="terms::PartitionElement")
Term = Class(name="Term")
terms_BuiltInConstant = Class(name="terms::BuiltInConstant", is_abstract=True)
Operator = Class(name="Operator")
terms_MultisetOperator = Class(name="terms::MultisetOperator", is_abstract=True)
terms_Variable = Class(name="terms::Variable")
terms_BuiltInSort = Class(name="terms::BuiltInSort", is_abstract=True)
terms_UserOperator = Class(name="terms::UserOperator")
terms_Tuple = Class(name="terms::Tuple")
terms_SortDecl = Class(name="terms::SortDecl", is_abstract=True)
terms_BuiltInOperator = Class(name="terms::BuiltInOperator", is_abstract=True)
SortDecl = Class(name="SortDecl")
terms_UserSort = Class(name="terms::UserSort")
terms_OperatorDecl = Class(name="terms::OperatorDecl", is_abstract=True)
OperatorDecl = Class(name="OperatorDecl")

# terms_Declarations class attributes and methods

# terms_Empty class attributes and methods

# terms_Partition class attributes and methods

# terms_HLPNList class attributes and methods

# terms_EmptyList class attributes and methods

# terms_MakeList class attributes and methods

# terms_TermsDeclaration class attributes and methods
terms_TermsDeclaration_id: Property = Property(name="id", type=StringType)
terms_TermsDeclaration_name: Property = Property(name="name", type=StringType)
terms_TermsDeclaration.attributes={terms_TermsDeclaration_id, terms_TermsDeclaration_name}

# terms_Declaration class attributes and methods

# terms_Sort class attributes and methods

# terms_MultisetSort class attributes and methods

# terms_NamedSort class attributes and methods

# terms_VariableDecl class attributes and methods

# terms_ProductSort class attributes and methods

# terms_Type class attributes and methods

# terms_All class attributes and methods

# TermsDeclaration class attributes and methods

# Sort class attributes and methods

# terms_Term class attributes and methods

# terms_Operator class attributes and methods

# terms_NamedOperator class attributes and methods

# terms_HLMarking class attributes and methods

# terms_Condition class attributes and methods

# terms_HLAnnotation class attributes and methods

# terms_PartitionElement class attributes and methods

# Term class attributes and methods

# terms_BuiltInConstant class attributes and methods

# Operator class attributes and methods

# terms_MultisetOperator class attributes and methods

# terms_Variable class attributes and methods

# terms_BuiltInSort class attributes and methods

# terms_UserOperator class attributes and methods

# terms_Tuple class attributes and methods

# terms_SortDecl class attributes and methods

# terms_BuiltInOperator class attributes and methods

# SortDecl class attributes and methods

# terms_UserSort class attributes and methods

# terms_OperatorDecl class attributes and methods

# OperatorDecl class attributes and methods

# Relationships
containerEmpty10: BinaryAssociation = BinaryAssociation(
    name="containerEmpty10",
    ends={
        Property(name="multisets.ecoreEmpty", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="refsort11", type=terms_Empty, multiplicity=Multiplicity(0, 1))
    }
)
containerPartition12: BinaryAssociation = BinaryAssociation(
    name="containerPartition12",
    ends={
        Property(name="partitions.ecorePartition", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="def", type=terms_Partition, multiplicity=Multiplicity(0, 1))
    }
)
containerList13: BinaryAssociation = BinaryAssociation(
    name="containerList13",
    ends={
        Property(name="lists.ecoreHLPNList", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="basis14", type=terms_HLPNList, multiplicity=Multiplicity(0, 1))
    }
)
containerEmptyList15: BinaryAssociation = BinaryAssociation(
    name="containerEmptyList15",
    ends={
        Property(name="lists.ecoreEmptyList", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="refsort16", type=terms_EmptyList, multiplicity=Multiplicity(0, 1))
    }
)
containerMakeList17: BinaryAssociation = BinaryAssociation(
    name="containerMakeList17",
    ends={
        Property(name="lists.ecoreMakeList", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="refsort18", type=terms_MakeList, multiplicity=Multiplicity(0, 1))
    }
)
declaration0: BinaryAssociation = BinaryAssociation(
    name="declaration0",
    ends={
        Property(name="TermsDeclaration", type=terms_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="containerDeclarations", type=terms_TermsDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerDeclaration1: BinaryAssociation = BinaryAssociation(
    name="containerDeclaration1",
    ends={
        Property(name="hlcorestructure.ecoreDeclaration", type=terms_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="structure", type=terms_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
containerDeclarations2: BinaryAssociation = BinaryAssociation(
    name="containerDeclarations2",
    ends={
        Property(name="Declarations", type=terms_TermsDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaration", type=terms_Declarations, multiplicity=Multiplicity(0, 1))
    }
)
multi3: BinaryAssociation = BinaryAssociation(
    name="multi3",
    ends={
        Property(name="MultisetSort", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="basis", type=terms_MultisetSort, multiplicity=Multiplicity(0, 1))
    }
)
containerNamedSort4: BinaryAssociation = BinaryAssociation(
    name="containerNamedSort4",
    ends={
        Property(name="NamedSort", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="sortdef", type=terms_NamedSort, multiplicity=Multiplicity(0, 1))
    }
)
containerVariableDecl5: BinaryAssociation = BinaryAssociation(
    name="containerVariableDecl5",
    ends={
        Property(name="VariableDecl", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="sort", type=terms_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
containerProductSort6: BinaryAssociation = BinaryAssociation(
    name="containerProductSort6",
    ends={
        Property(name="ProductSort", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="elementSort", type=terms_ProductSort, multiplicity=Multiplicity(0, 1))
    }
)
containerType7: BinaryAssociation = BinaryAssociation(
    name="containerType7",
    ends={
        Property(name="hlcorestructure.ecoreType", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="structure8", type=terms_Type, multiplicity=Multiplicity(0, 1))
    }
)
containerAll9: BinaryAssociation = BinaryAssociation(
    name="containerAll9",
    ends={
        Property(name="multisets.ecoreAll", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="refsort", type=terms_All, multiplicity=Multiplicity(0, 1))
    }
)
output32: BinaryAssociation = BinaryAssociation(
    name="output32",
    ends={
        Property(name="terms_Sort33", type=terms_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_Operator", type=terms_Sort, multiplicity=Multiplicity(0, 1))
    }
)
input34: BinaryAssociation = BinaryAssociation(
    name="input34",
    ends={
        Property(name="terms_Sort36", type=terms_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_Operator35", type=terms_Sort, multiplicity=Multiplicity(0, 9999))
    }
)
sort37: BinaryAssociation = BinaryAssociation(
    name="sort37",
    ends={
        Property(name="Sort38", type=terms_VariableDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="containerVariableDecl", type=terms_Sort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
basis19: BinaryAssociation = BinaryAssociation(
    name="basis19",
    ends={
        Property(name="Sort", type=terms_MultisetSort, multiplicity=Multiplicity(1, 1)),
        Property(name="multi", type=terms_Sort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sort20: BinaryAssociation = BinaryAssociation(
    name="sort20",
    ends={
        Property(name="terms_Sort", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_Term", type=terms_Sort, multiplicity=Multiplicity(0, 1))
    }
)
containerOperator21: BinaryAssociation = BinaryAssociation(
    name="containerOperator21",
    ends={
        Property(name="Operator", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="subterm", type=terms_Operator, multiplicity=Multiplicity(0, 1))
    }
)
containerNamedOperator22: BinaryAssociation = BinaryAssociation(
    name="containerNamedOperator22",
    ends={
        Property(name="NamedOperator", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="def23", type=terms_NamedOperator, multiplicity=Multiplicity(0, 1))
    }
)
containerHLMarking24: BinaryAssociation = BinaryAssociation(
    name="containerHLMarking24",
    ends={
        Property(name="hlcorestructure.ecoreHLMarking", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="structure25", type=terms_HLMarking, multiplicity=Multiplicity(0, 1))
    }
)
containerCondition26: BinaryAssociation = BinaryAssociation(
    name="containerCondition26",
    ends={
        Property(name="hlcorestructure.ecoreCondition", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="structure27", type=terms_Condition, multiplicity=Multiplicity(0, 1))
    }
)
containerHLAnnotation28: BinaryAssociation = BinaryAssociation(
    name="containerHLAnnotation28",
    ends={
        Property(name="hlcorestructure.ecoreHLAnnotation", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="structure29", type=terms_HLAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
containerPartitionElement30: BinaryAssociation = BinaryAssociation(
    name="containerPartitionElement30",
    ends={
        Property(name="partitions.ecorePartitionElement", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="partitionelementconstants", type=terms_PartitionElement, multiplicity=Multiplicity(0, 1))
    }
)
subterm31: BinaryAssociation = BinaryAssociation(
    name="subterm31",
    ends={
        Property(name="Term", type=terms_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="containerOperator", type=terms_Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementSort42: BinaryAssociation = BinaryAssociation(
    name="elementSort42",
    ends={
        Property(name="Sort43", type=terms_ProductSort, multiplicity=Multiplicity(1, 1)),
        Property(name="containerProductSort", type=terms_Sort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerNamedOperator39: BinaryAssociation = BinaryAssociation(
    name="containerNamedOperator39",
    ends={
        Property(name="NamedOperator40", type=terms_VariableDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=terms_NamedOperator, multiplicity=Multiplicity(0, 1))
    }
)
variableDecl41: BinaryAssociation = BinaryAssociation(
    name="variableDecl41",
    ends={
        Property(name="terms_VariableDecl", type=terms_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_Variable", type=terms_VariableDecl, multiplicity=Multiplicity(1, 1))
    }
)
parameters49: BinaryAssociation = BinaryAssociation(
    name="parameters49",
    ends={
        Property(name="VariableDecl51", type=terms_NamedOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamedOperator50", type=terms_VariableDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sortdef44: BinaryAssociation = BinaryAssociation(
    name="sortdef44",
    ends={
        Property(name="Sort45", type=terms_NamedSort, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamedSort", type=terms_Sort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration46: BinaryAssociation = BinaryAssociation(
    name="declaration46",
    ends={
        Property(name="terms_SortDecl", type=terms_UserSort, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_UserSort", type=terms_SortDecl, multiplicity=Multiplicity(1, 1))
    }
)
def47: BinaryAssociation = BinaryAssociation(
    name="def47",
    ends={
        Property(name="Term48", type=terms_NamedOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamedOperator", type=terms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration52: BinaryAssociation = BinaryAssociation(
    name="declaration52",
    ends={
        Property(name="terms_OperatorDecl", type=terms_UserOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_UserOperator", type=terms_OperatorDecl, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_terms_VariableDecl_TermsDeclaration = Generalization(general=TermsDeclaration, specific=terms_VariableDecl)
gen_terms_MultisetSort_Sort = Generalization(general=Sort, specific=terms_MultisetSort)
gen_terms_Operator_Term = Generalization(general=Term, specific=terms_Operator)
gen_terms_ProductSort_Sort = Generalization(general=Sort, specific=terms_ProductSort)
gen_terms_BuiltInConstant_Operator = Generalization(general=Operator, specific=terms_BuiltInConstant)
gen_terms_MultisetOperator_Operator = Generalization(general=Operator, specific=terms_MultisetOperator)
gen_terms_Variable_Term = Generalization(general=Term, specific=terms_Variable)
gen_terms_BuiltInSort_Sort = Generalization(general=Sort, specific=terms_BuiltInSort)
gen_terms_UserOperator_Operator = Generalization(general=Operator, specific=terms_UserOperator)
gen_terms_Tuple_Operator = Generalization(general=Operator, specific=terms_Tuple)
gen_terms_SortDecl_TermsDeclaration = Generalization(general=TermsDeclaration, specific=terms_SortDecl)
gen_terms_BuiltInOperator_Operator = Generalization(general=Operator, specific=terms_BuiltInOperator)
gen_terms_NamedSort_SortDecl = Generalization(general=SortDecl, specific=terms_NamedSort)
gen_terms_UserSort_Sort = Generalization(general=Sort, specific=terms_UserSort)
gen_terms_OperatorDecl_TermsDeclaration = Generalization(general=TermsDeclaration, specific=terms_OperatorDecl)
gen_terms_NamedOperator_OperatorDecl = Generalization(general=OperatorDecl, specific=terms_NamedOperator)

# Domain Model
domain_model = DomainModel(
    name="terms",
    types={terms_Declarations, terms_Empty, terms_Partition, terms_HLPNList, terms_EmptyList, terms_MakeList, terms_TermsDeclaration, terms_Declaration, terms_Sort, terms_MultisetSort, terms_NamedSort, terms_VariableDecl, terms_ProductSort, terms_Type, terms_All, TermsDeclaration, Sort, terms_Term, terms_Operator, terms_NamedOperator, terms_HLMarking, terms_Condition, terms_HLAnnotation, terms_PartitionElement, Term, terms_BuiltInConstant, Operator, terms_MultisetOperator, terms_Variable, terms_BuiltInSort, terms_UserOperator, terms_Tuple, terms_SortDecl, terms_BuiltInOperator, SortDecl, terms_UserSort, terms_OperatorDecl, OperatorDecl},
    associations={containerEmpty10, containerPartition12, containerList13, containerEmptyList15, containerMakeList17, declaration0, containerDeclaration1, containerDeclarations2, multi3, containerNamedSort4, containerVariableDecl5, containerProductSort6, containerType7, containerAll9, output32, input34, sort37, basis19, sort20, containerOperator21, containerNamedOperator22, containerHLMarking24, containerCondition26, containerHLAnnotation28, containerPartitionElement30, subterm31, elementSort42, containerNamedOperator39, variableDecl41, parameters49, sortdef44, declaration46, def47, declaration52},
    generalizations={gen_terms_VariableDecl_TermsDeclaration, gen_terms_MultisetSort_Sort, gen_terms_Operator_Term, gen_terms_ProductSort_Sort, gen_terms_BuiltInConstant_Operator, gen_terms_MultisetOperator_Operator, gen_terms_Variable_Term, gen_terms_BuiltInSort_Sort, gen_terms_UserOperator_Operator, gen_terms_Tuple_Operator, gen_terms_SortDecl_TermsDeclaration, gen_terms_BuiltInOperator_Operator, gen_terms_NamedSort_SortDecl, gen_terms_UserSort_Sort, gen_terms_OperatorDecl_TermsDeclaration, gen_terms_NamedOperator_OperatorDecl},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)