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
terms_TermsDeclaration = Class(name="terms::TermsDeclaration", is_abstract=True)
terms_Declaration = Class(name="terms::Declaration")
terms_Type = Class(name="terms::Type")
terms_All = Class(name="terms::All")
terms_Empty = Class(name="terms::Empty")
terms_Partition = Class(name="terms::Partition")
Sort = Class(name="Sort")
terms_Term = Class(name="terms::Term", is_abstract=True)
terms_Operator = Class(name="terms::Operator", is_abstract=True)
terms_NamedOperator = Class(name="terms::NamedOperator")
terms_HLMarking = Class(name="terms::HLMarking")
terms_Condition = Class(name="terms::Condition")
terms_HLAnnotation = Class(name="terms::HLAnnotation")
terms_Sort = Class(name="terms::Sort", is_abstract=True)
terms_MultisetSort = Class(name="terms::MultisetSort")
terms_NamedSort = Class(name="terms::NamedSort")
terms_VariableDecl = Class(name="terms::VariableDecl")
terms_ProductSort = Class(name="terms::ProductSort")
TermsDeclaration = Class(name="TermsDeclaration")
terms_Variable = Class(name="terms::Variable")
terms_BuiltInSort = Class(name="terms::BuiltInSort", is_abstract=True)
terms_BuiltInConstant = Class(name="terms::BuiltInConstant", is_abstract=True)
Operator = Class(name="Operator")
terms_MultisetOperator = Class(name="terms::MultisetOperator", is_abstract=True)
terms_Tuple = Class(name="terms::Tuple")
terms_SortDecl = Class(name="terms::SortDecl", is_abstract=True)
terms_BuiltInOperator = Class(name="terms::BuiltInOperator", is_abstract=True)
SortDecl = Class(name="SortDecl")
terms_UserSort = Class(name="terms::UserSort")
terms_PartitionElement = Class(name="terms::PartitionElement")
Term = Class(name="Term")
terms_UserOperator = Class(name="terms::UserOperator")
terms_OperatorDecl = Class(name="terms::OperatorDecl", is_abstract=True)
OperatorDecl = Class(name="OperatorDecl")

# terms_Declarations class attributes and methods

# terms_TermsDeclaration class attributes and methods
terms_TermsDeclaration_id: Property = Property(name="id", type=StringType)
terms_TermsDeclaration_name: Property = Property(name="name", type=StringType)
terms_TermsDeclaration.attributes={terms_TermsDeclaration_id, terms_TermsDeclaration_name}

# terms_Declaration class attributes and methods

# terms_Type class attributes and methods

# terms_All class attributes and methods

# terms_Empty class attributes and methods

# terms_Partition class attributes and methods

# Sort class attributes and methods

# terms_Term class attributes and methods

# terms_Operator class attributes and methods

# terms_NamedOperator class attributes and methods

# terms_HLMarking class attributes and methods

# terms_Condition class attributes and methods

# terms_HLAnnotation class attributes and methods

# terms_Sort class attributes and methods

# terms_MultisetSort class attributes and methods

# terms_NamedSort class attributes and methods

# terms_VariableDecl class attributes and methods

# terms_ProductSort class attributes and methods

# TermsDeclaration class attributes and methods

# terms_Variable class attributes and methods

# terms_BuiltInSort class attributes and methods

# terms_BuiltInConstant class attributes and methods

# Operator class attributes and methods

# terms_MultisetOperator class attributes and methods

# terms_Tuple class attributes and methods

# terms_SortDecl class attributes and methods

# terms_BuiltInOperator class attributes and methods

# SortDecl class attributes and methods

# terms_UserSort class attributes and methods

# terms_PartitionElement class attributes and methods

# Term class attributes and methods

# terms_UserOperator class attributes and methods

# terms_OperatorDecl class attributes and methods

# OperatorDecl class attributes and methods

# Relationships
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
containerEmpty10: BinaryAssociation = BinaryAssociation(
    name="containerEmpty10",
    ends={
        Property(name="terms_Empty", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_Sort", type=terms_Empty, multiplicity=Multiplicity(0, 1))
    }
)
containerPartition11: BinaryAssociation = BinaryAssociation(
    name="containerPartition11",
    ends={
        Property(name="partitions.ecorePartition", type=terms_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="def", type=terms_Partition, multiplicity=Multiplicity(0, 1))
    }
)
basis12: BinaryAssociation = BinaryAssociation(
    name="basis12",
    ends={
        Property(name="Sort", type=terms_MultisetSort, multiplicity=Multiplicity(1, 1)),
        Property(name="multi", type=terms_Sort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sort13: BinaryAssociation = BinaryAssociation(
    name="sort13",
    ends={
        Property(name="terms_Sort14", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_Term", type=terms_Sort, multiplicity=Multiplicity(0, 1))
    }
)
containerOperator15: BinaryAssociation = BinaryAssociation(
    name="containerOperator15",
    ends={
        Property(name="Operator", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="subterm", type=terms_Operator, multiplicity=Multiplicity(0, 1))
    }
)
containerNamedOperator16: BinaryAssociation = BinaryAssociation(
    name="containerNamedOperator16",
    ends={
        Property(name="NamedOperator", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="def17", type=terms_NamedOperator, multiplicity=Multiplicity(0, 1))
    }
)
containerHLMarking18: BinaryAssociation = BinaryAssociation(
    name="containerHLMarking18",
    ends={
        Property(name="hlcorestructure.ecoreHLMarking", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="structure19", type=terms_HLMarking, multiplicity=Multiplicity(0, 1))
    }
)
containerCondition20: BinaryAssociation = BinaryAssociation(
    name="containerCondition20",
    ends={
        Property(name="hlcorestructure.ecoreCondition", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="structure21", type=terms_Condition, multiplicity=Multiplicity(0, 1))
    }
)
containerHLAnnotation22: BinaryAssociation = BinaryAssociation(
    name="containerHLAnnotation22",
    ends={
        Property(name="hlcorestructure.ecoreHLAnnotation", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="structure23", type=terms_HLAnnotation, multiplicity=Multiplicity(0, 1))
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
sort31: BinaryAssociation = BinaryAssociation(
    name="sort31",
    ends={
        Property(name="Sort32", type=terms_VariableDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="containerVariableDecl", type=terms_Sort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerNamedOperator33: BinaryAssociation = BinaryAssociation(
    name="containerNamedOperator33",
    ends={
        Property(name="NamedOperator34", type=terms_VariableDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=terms_NamedOperator, multiplicity=Multiplicity(0, 1))
    }
)
variableDecl35: BinaryAssociation = BinaryAssociation(
    name="variableDecl35",
    ends={
        Property(name="terms_VariableDecl", type=terms_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_Variable", type=terms_VariableDecl, multiplicity=Multiplicity(1, 1))
    }
)
elementSort36: BinaryAssociation = BinaryAssociation(
    name="elementSort36",
    ends={
        Property(name="Sort37", type=terms_ProductSort, multiplicity=Multiplicity(1, 1)),
        Property(name="containerProductSort", type=terms_Sort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sortdef38: BinaryAssociation = BinaryAssociation(
    name="sortdef38",
    ends={
        Property(name="Sort39", type=terms_NamedSort, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamedSort", type=terms_Sort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerPartitionElement24: BinaryAssociation = BinaryAssociation(
    name="containerPartitionElement24",
    ends={
        Property(name="partitions.ecorePartitionElement", type=terms_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="partitionelementconstants", type=terms_PartitionElement, multiplicity=Multiplicity(0, 1))
    }
)
subterm25: BinaryAssociation = BinaryAssociation(
    name="subterm25",
    ends={
        Property(name="Term", type=terms_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="containerOperator", type=terms_Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output26: BinaryAssociation = BinaryAssociation(
    name="output26",
    ends={
        Property(name="terms_Sort27", type=terms_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_Operator", type=terms_Sort, multiplicity=Multiplicity(0, 1))
    }
)
input28: BinaryAssociation = BinaryAssociation(
    name="input28",
    ends={
        Property(name="terms_Sort30", type=terms_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_Operator29", type=terms_Sort, multiplicity=Multiplicity(0, 9999))
    }
)
declaration46: BinaryAssociation = BinaryAssociation(
    name="declaration46",
    ends={
        Property(name="terms_OperatorDecl", type=terms_UserOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_UserOperator", type=terms_OperatorDecl, multiplicity=Multiplicity(1, 1))
    }
)
declaration40: BinaryAssociation = BinaryAssociation(
    name="declaration40",
    ends={
        Property(name="terms_SortDecl", type=terms_UserSort, multiplicity=Multiplicity(1, 1)),
        Property(name="terms_UserSort", type=terms_SortDecl, multiplicity=Multiplicity(1, 1))
    }
)
def41: BinaryAssociation = BinaryAssociation(
    name="def41",
    ends={
        Property(name="Term42", type=terms_NamedOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamedOperator", type=terms_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters43: BinaryAssociation = BinaryAssociation(
    name="parameters43",
    ends={
        Property(name="VariableDecl45", type=terms_NamedOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamedOperator44", type=terms_VariableDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_terms_MultisetSort_Sort = Generalization(general=Sort, specific=terms_MultisetSort)
gen_terms_VariableDecl_TermsDeclaration = Generalization(general=TermsDeclaration, specific=terms_VariableDecl)
gen_terms_Variable_Term = Generalization(general=Term, specific=terms_Variable)
gen_terms_BuiltInSort_Sort = Generalization(general=Sort, specific=terms_BuiltInSort)
gen_terms_ProductSort_Sort = Generalization(general=Sort, specific=terms_ProductSort)
gen_terms_BuiltInConstant_Operator = Generalization(general=Operator, specific=terms_BuiltInConstant)
gen_terms_MultisetOperator_Operator = Generalization(general=Operator, specific=terms_MultisetOperator)
gen_terms_Tuple_Operator = Generalization(general=Operator, specific=terms_Tuple)
gen_terms_SortDecl_TermsDeclaration = Generalization(general=TermsDeclaration, specific=terms_SortDecl)
gen_terms_BuiltInOperator_Operator = Generalization(general=Operator, specific=terms_BuiltInOperator)
gen_terms_NamedSort_SortDecl = Generalization(general=SortDecl, specific=terms_NamedSort)
gen_terms_UserSort_Sort = Generalization(general=Sort, specific=terms_UserSort)
gen_terms_Operator_Term = Generalization(general=Term, specific=terms_Operator)
gen_terms_UserOperator_Operator = Generalization(general=Operator, specific=terms_UserOperator)
gen_terms_OperatorDecl_TermsDeclaration = Generalization(general=TermsDeclaration, specific=terms_OperatorDecl)
gen_terms_NamedOperator_OperatorDecl = Generalization(general=OperatorDecl, specific=terms_NamedOperator)

# Domain Model
domain_model = DomainModel(
    name="terms",
    types={terms_Declarations, terms_TermsDeclaration, terms_Declaration, terms_Type, terms_All, terms_Empty, terms_Partition, Sort, terms_Term, terms_Operator, terms_NamedOperator, terms_HLMarking, terms_Condition, terms_HLAnnotation, terms_Sort, terms_MultisetSort, terms_NamedSort, terms_VariableDecl, terms_ProductSort, TermsDeclaration, terms_Variable, terms_BuiltInSort, terms_BuiltInConstant, Operator, terms_MultisetOperator, terms_Tuple, terms_SortDecl, terms_BuiltInOperator, SortDecl, terms_UserSort, terms_PartitionElement, Term, terms_UserOperator, terms_OperatorDecl, OperatorDecl},
    associations={declaration0, containerDeclaration1, containerType7, containerAll9, containerEmpty10, containerPartition11, basis12, sort13, containerOperator15, containerNamedOperator16, containerHLMarking18, containerCondition20, containerHLAnnotation22, containerDeclarations2, multi3, containerNamedSort4, containerVariableDecl5, containerProductSort6, sort31, containerNamedOperator33, variableDecl35, elementSort36, sortdef38, containerPartitionElement24, subterm25, output26, input28, declaration46, declaration40, def41, parameters43},
    generalizations={gen_terms_MultisetSort_Sort, gen_terms_VariableDecl_TermsDeclaration, gen_terms_Variable_Term, gen_terms_BuiltInSort_Sort, gen_terms_ProductSort_Sort, gen_terms_BuiltInConstant_Operator, gen_terms_MultisetOperator_Operator, gen_terms_Tuple_Operator, gen_terms_SortDecl_TermsDeclaration, gen_terms_BuiltInOperator_Operator, gen_terms_NamedSort_SortDecl, gen_terms_UserSort_Sort, gen_terms_Operator_Term, gen_terms_UserOperator_Operator, gen_terms_OperatorDecl_TermsDeclaration, gen_terms_NamedOperator_OperatorDecl},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)