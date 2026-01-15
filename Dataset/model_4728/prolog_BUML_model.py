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
prolog_Term = Class(name="prolog::Term", is_abstract=True)
Expression = Class(name="Expression")
prolog_CompoundTerm = Class(name="prolog::CompoundTerm")
Term = Class(name="Term")
prolog_Program = Class(name="prolog::Program")
prolog_Clause = Class(name="prolog::Clause", is_abstract=True)
prolog_Comment = Class(name="prolog::Comment")
Clause = Class(name="Clause")
prolog_directives_PredicateIndicator = Class(name="prolog::directives::PredicateIndicator")
prolog_directives_Dynamic = Class(name="prolog::directives::Dynamic")
Directive = Class(name="Directive")
prolog_directives_Discontiguous = Class(name="prolog::directives::Discontiguous")
prolog_AtomicNumber = Class(name="prolog::AtomicNumber")
prolog_AtomicQuotedString = Class(name="prolog::AtomicQuotedString")
prolog_List = Class(name="prolog::List")
prolog_Fact = Class(name="prolog::Fact")
prolog_Rule = Class(name="prolog::Rule")
prolog_ControlPredicate = Class(name="prolog::ControlPredicate", is_abstract=True)
prolog_True = Class(name="prolog::True")
ControlPredicate = Class(name="ControlPredicate")
prolog_False = Class(name="prolog::False")
prolog_Fail = Class(name="prolog::Fail")
prolog_Cut = Class(name="prolog::Cut")
prolog_directives_Directive = Class(name="prolog::directives::Directive", is_abstract=True)
PredicateIndicator = Class(name="PredicateIndicator")
prolog_expressions_StructuralEquivalenceNotProvable = Class(name="prolog::expressions::StructuralEquivalenceNotProvable")
prolog_expressions_NumberEqual = Class(name="prolog::expressions::NumberEqual")
prolog_expressions_LessOrEqual = Class(name="prolog::expressions::LessOrEqual")
prolog_expressions_Equivalence = Class(name="prolog::expressions::Equivalence")
prolog_expressions_NonEqualNumber = Class(name="prolog::expressions::NonEqualNumber")
prolog_expressions_GreaterThan = Class(name="prolog::expressions::GreaterThan")
prolog_directives_Multifile = Class(name="prolog::directives::Multifile")
prolog_directives_Public = Class(name="prolog::directives::Public")
prolog_directives_Volatile = Class(name="prolog::directives::Volatile")
prolog_directives_Table = Class(name="prolog::directives::Table")
prolog_expressions_Expression = Class(name="prolog::expressions::Expression", is_abstract=True)
prolog_expressions_UnaryExpression = Class(name="prolog::expressions::UnaryExpression", is_abstract=True)
prolog_expressions_BinaryExpression = Class(name="prolog::expressions::BinaryExpression", is_abstract=True)
prolog_expressions_LogicalOr = Class(name="prolog::expressions::LogicalOr")
BinaryExpression = Class(name="BinaryExpression")
prolog_expressions_Condition = Class(name="prolog::expressions::Condition", is_abstract=True)
prolog_expressions_SoftCut = Class(name="prolog::expressions::SoftCut")
prolog_expressions_LogicalAnd = Class(name="prolog::expressions::LogicalAnd")
prolog_expressions_NotProvable = Class(name="prolog::expressions::NotProvable")
UnaryExpression = Class(name="UnaryExpression")
prolog_expressions_LessThan = Class(name="prolog::expressions::LessThan")
prolog_expressions_Unification = Class(name="prolog::expressions::Unification")
prolog_expressions_Univ = Class(name="prolog::expressions::Univ")
prolog_expressions_StructuralEquivalence = Class(name="prolog::expressions::StructuralEquivalence")
prolog_expressions_PositiveNumber = Class(name="prolog::expressions::PositiveNumber")
prolog_expressions_NegativeNumber = Class(name="prolog::expressions::NegativeNumber")
prolog_expressions_BitwiseNegation = Class(name="prolog::expressions::BitwiseNegation")
prolog_expressions_GreaterOrEqual = Class(name="prolog::expressions::GreaterOrEqual")
prolog_expressions_StandardOrderBefore = Class(name="prolog::expressions::StandardOrderBefore")
prolog_expressions_EqualOrStandardOrderBefore = Class(name="prolog::expressions::EqualOrStandardOrderBefore")
prolog_expressions_StandardOrderAfter = Class(name="prolog::expressions::StandardOrderAfter")
prolog_expressions_EqualOrStandardOrderAfter = Class(name="prolog::expressions::EqualOrStandardOrderAfter")
prolog_expressions_NotUnifiable = Class(name="prolog::expressions::NotUnifiable")
prolog_expressions_Disequality = Class(name="prolog::expressions::Disequality")
prolog_expressions_As = Class(name="prolog::expressions::As")
prolog_expressions_Is = Class(name="prolog::expressions::Is")
prolog_expressions_ParticalUnification = Class(name="prolog::expressions::ParticalUnification")
prolog_expressions_SubDict = Class(name="prolog::expressions::SubDict")
prolog_expressions_ModuleCall = Class(name="prolog::expressions::ModuleCall")
prolog_expressions_Plus = Class(name="prolog::expressions::Plus")
prolog_expressions_Minus = Class(name="prolog::expressions::Minus")
prolog_expressions_BinaryAnd = Class(name="prolog::expressions::BinaryAnd")
prolog_expressions_BinaryOr = Class(name="prolog::expressions::BinaryOr")
prolog_expressions_Xor = Class(name="prolog::expressions::Xor")
prolog_expressions_Multiplication = Class(name="prolog::expressions::Multiplication")
prolog_expressions_Division = Class(name="prolog::expressions::Division")
prolog_expressions_IntegerDivision = Class(name="prolog::expressions::IntegerDivision")
prolog_expressions_Div = Class(name="prolog::expressions::Div")
prolog_expressions_Rdiv = Class(name="prolog::expressions::Rdiv")
prolog_expressions_BitwiseShiftLeft = Class(name="prolog::expressions::BitwiseShiftLeft")
prolog_expressions_Mod = Class(name="prolog::expressions::Mod")
prolog_expressions_Rem = Class(name="prolog::expressions::Rem")
prolog_expressions_Power = Class(name="prolog::expressions::Power")

# prolog_Term class attributes and methods

# Expression class attributes and methods

# prolog_CompoundTerm class attributes and methods
prolog_CompoundTerm_value: Property = Property(name="value", type=StringType)
prolog_CompoundTerm.attributes={prolog_CompoundTerm_value}

# Term class attributes and methods

# prolog_Program class attributes and methods

# prolog_Clause class attributes and methods

# prolog_Comment class attributes and methods
prolog_Comment_value: Property = Property(name="value", type=StringType)
prolog_Comment.attributes={prolog_Comment_value}

# Clause class attributes and methods

# prolog_directives_PredicateIndicator class attributes and methods
prolog_directives_PredicateIndicator_name: Property = Property(name="name", type=StringType)
prolog_directives_PredicateIndicator_arity: Property = Property(name="arity", type=IntegerType)
prolog_directives_PredicateIndicator.attributes={prolog_directives_PredicateIndicator_arity, prolog_directives_PredicateIndicator_name}

# prolog_directives_Dynamic class attributes and methods

# Directive class attributes and methods

# prolog_directives_Discontiguous class attributes and methods

# prolog_AtomicNumber class attributes and methods
prolog_AtomicNumber_value: Property = Property(name="value", type=IntegerType)
prolog_AtomicNumber.attributes={prolog_AtomicNumber_value}

# prolog_AtomicQuotedString class attributes and methods
prolog_AtomicQuotedString_value: Property = Property(name="value", type=StringType)
prolog_AtomicQuotedString.attributes={prolog_AtomicQuotedString_value}

# prolog_List class attributes and methods

# prolog_Fact class attributes and methods

# prolog_Rule class attributes and methods

# prolog_ControlPredicate class attributes and methods

# prolog_True class attributes and methods

# ControlPredicate class attributes and methods

# prolog_False class attributes and methods

# prolog_Fail class attributes and methods

# prolog_Cut class attributes and methods

# prolog_directives_Directive class attributes and methods
prolog_directives_Directive_name: Property = Property(name="name", type=StringType)
prolog_directives_Directive.attributes={prolog_directives_Directive_name}

# PredicateIndicator class attributes and methods

# prolog_expressions_StructuralEquivalenceNotProvable class attributes and methods

# prolog_expressions_NumberEqual class attributes and methods

# prolog_expressions_LessOrEqual class attributes and methods

# prolog_expressions_Equivalence class attributes and methods

# prolog_expressions_NonEqualNumber class attributes and methods

# prolog_expressions_GreaterThan class attributes and methods

# prolog_directives_Multifile class attributes and methods

# prolog_directives_Public class attributes and methods

# prolog_directives_Volatile class attributes and methods

# prolog_directives_Table class attributes and methods

# prolog_expressions_Expression class attributes and methods

# prolog_expressions_UnaryExpression class attributes and methods

# prolog_expressions_BinaryExpression class attributes and methods

# prolog_expressions_LogicalOr class attributes and methods

# BinaryExpression class attributes and methods

# prolog_expressions_Condition class attributes and methods

# prolog_expressions_SoftCut class attributes and methods

# prolog_expressions_LogicalAnd class attributes and methods

# prolog_expressions_NotProvable class attributes and methods

# UnaryExpression class attributes and methods

# prolog_expressions_LessThan class attributes and methods

# prolog_expressions_Unification class attributes and methods

# prolog_expressions_Univ class attributes and methods

# prolog_expressions_StructuralEquivalence class attributes and methods

# prolog_expressions_PositiveNumber class attributes and methods

# prolog_expressions_NegativeNumber class attributes and methods

# prolog_expressions_BitwiseNegation class attributes and methods

# prolog_expressions_GreaterOrEqual class attributes and methods

# prolog_expressions_StandardOrderBefore class attributes and methods

# prolog_expressions_EqualOrStandardOrderBefore class attributes and methods

# prolog_expressions_StandardOrderAfter class attributes and methods

# prolog_expressions_EqualOrStandardOrderAfter class attributes and methods

# prolog_expressions_NotUnifiable class attributes and methods

# prolog_expressions_Disequality class attributes and methods

# prolog_expressions_As class attributes and methods

# prolog_expressions_Is class attributes and methods

# prolog_expressions_ParticalUnification class attributes and methods

# prolog_expressions_SubDict class attributes and methods

# prolog_expressions_ModuleCall class attributes and methods

# prolog_expressions_Plus class attributes and methods

# prolog_expressions_Minus class attributes and methods

# prolog_expressions_BinaryAnd class attributes and methods

# prolog_expressions_BinaryOr class attributes and methods

# prolog_expressions_Xor class attributes and methods

# prolog_expressions_Multiplication class attributes and methods

# prolog_expressions_Division class attributes and methods

# prolog_expressions_IntegerDivision class attributes and methods

# prolog_expressions_Div class attributes and methods

# prolog_expressions_Rdiv class attributes and methods

# prolog_expressions_BitwiseShiftLeft class attributes and methods

# prolog_expressions_Mod class attributes and methods

# prolog_expressions_Rem class attributes and methods

# prolog_expressions_Power class attributes and methods

# Relationships
clauses0: BinaryAssociation = BinaryAssociation(
    name="clauses0",
    ends={
        Property(name="prolog_Clause", type=prolog_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Program", type=prolog_Clause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predicates14: BinaryAssociation = BinaryAssociation(
    name="predicates14",
    ends={
        Property(name="PredicateIndicator", type=prolog_directives_Directive, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_directives_Directive", type=PredicateIndicator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments1: BinaryAssociation = BinaryAssociation(
    name="arguments1",
    ends={
        Property(name="Expression", type=prolog_CompoundTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_CompoundTerm", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
heads2: BinaryAssociation = BinaryAssociation(
    name="heads2",
    ends={
        Property(name="Expression3", type=prolog_List, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_List", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tails4: BinaryAssociation = BinaryAssociation(
    name="tails4",
    ends={
        Property(name="Expression6", type=prolog_List, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_List5", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
head7: BinaryAssociation = BinaryAssociation(
    name="head7",
    ends={
        Property(name="prolog_CompoundTerm8", type=prolog_Fact, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Fact", type=prolog_CompoundTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
head9: BinaryAssociation = BinaryAssociation(
    name="head9",
    ends={
        Property(name="prolog_CompoundTerm10", type=prolog_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Rule", type=prolog_CompoundTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body11: BinaryAssociation = BinaryAssociation(
    name="body11",
    ends={
        Property(name="Expression13", type=prolog_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Rule12", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predicate15: BinaryAssociation = BinaryAssociation(
    name="predicate15",
    ends={
        Property(name="PredicateIndicator16", type=prolog_directives_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_directives_Table", type=PredicateIndicator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr17: BinaryAssociation = BinaryAssociation(
    name="expr17",
    ends={
        Property(name="Expression18", type=prolog_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_expressions_UnaryExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left19: BinaryAssociation = BinaryAssociation(
    name="left19",
    ends={
        Property(name="Expression20", type=prolog_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_expressions_BinaryExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right21: BinaryAssociation = BinaryAssociation(
    name="right21",
    ends={
        Property(name="Expression23", type=prolog_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_expressions_BinaryExpression22", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_prolog_Term_Expression = Generalization(general=Expression, specific=prolog_Term)
gen_prolog_CompoundTerm_Clause = Generalization(general=Clause, specific=prolog_CompoundTerm)
gen_prolog_CompoundTerm_Term = Generalization(general=Term, specific=prolog_CompoundTerm)
gen_prolog_Comment_Clause = Generalization(general=Clause, specific=prolog_Comment)
gen_prolog_directives_Dynamic_Directive = Generalization(general=Directive, specific=prolog_directives_Dynamic)
gen_prolog_directives_Discontiguous_Directive = Generalization(general=Directive, specific=prolog_directives_Discontiguous)
gen_prolog_AtomicNumber_Term = Generalization(general=Term, specific=prolog_AtomicNumber)
gen_prolog_AtomicQuotedString_Term = Generalization(general=Term, specific=prolog_AtomicQuotedString)
gen_prolog_List_Term = Generalization(general=Term, specific=prolog_List)
gen_prolog_Fact_Clause = Generalization(general=Clause, specific=prolog_Fact)
gen_prolog_Rule_Clause = Generalization(general=Clause, specific=prolog_Rule)
gen_prolog_ControlPredicate_Term = Generalization(general=Term, specific=prolog_ControlPredicate)
gen_prolog_True_ControlPredicate = Generalization(general=ControlPredicate, specific=prolog_True)
gen_prolog_False_ControlPredicate = Generalization(general=ControlPredicate, specific=prolog_False)
gen_prolog_Fail_ControlPredicate = Generalization(general=ControlPredicate, specific=prolog_Fail)
gen_prolog_Cut_ControlPredicate = Generalization(general=ControlPredicate, specific=prolog_Cut)
gen_prolog_directives_Directive_Clause = Generalization(general=Clause, specific=prolog_directives_Directive)
gen_prolog_expressions_StructuralEquivalenceNotProvable_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_StructuralEquivalenceNotProvable)
gen_prolog_expressions_NumberEqual_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_NumberEqual)
gen_prolog_expressions_LessOrEqual_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_LessOrEqual)
gen_prolog_expressions_Equivalence_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Equivalence)
gen_prolog_expressions_NonEqualNumber_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_NonEqualNumber)
gen_prolog_expressions_GreaterThan_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_GreaterThan)
gen_prolog_directives_Multifile_Directive = Generalization(general=Directive, specific=prolog_directives_Multifile)
gen_prolog_directives_Public_Directive = Generalization(general=Directive, specific=prolog_directives_Public)
gen_prolog_directives_Volatile_Directive = Generalization(general=Directive, specific=prolog_directives_Volatile)
gen_prolog_directives_Table_Clause = Generalization(general=Clause, specific=prolog_directives_Table)
gen_prolog_expressions_UnaryExpression_Expression = Generalization(general=Expression, specific=prolog_expressions_UnaryExpression)
gen_prolog_expressions_BinaryExpression_Expression = Generalization(general=Expression, specific=prolog_expressions_BinaryExpression)
gen_prolog_expressions_LogicalOr_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_LogicalOr)
gen_prolog_expressions_Condition_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Condition)
gen_prolog_expressions_SoftCut_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_SoftCut)
gen_prolog_expressions_LogicalAnd_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_LogicalAnd)
gen_prolog_expressions_NotProvable_UnaryExpression = Generalization(general=UnaryExpression, specific=prolog_expressions_NotProvable)
gen_prolog_expressions_LessThan_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_LessThan)
gen_prolog_expressions_Unification_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Unification)
gen_prolog_expressions_Univ_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Univ)
gen_prolog_expressions_StructuralEquivalence_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_StructuralEquivalence)
gen_prolog_expressions_PositiveNumber_UnaryExpression = Generalization(general=UnaryExpression, specific=prolog_expressions_PositiveNumber)
gen_prolog_expressions_NegativeNumber_UnaryExpression = Generalization(general=UnaryExpression, specific=prolog_expressions_NegativeNumber)
gen_prolog_expressions_BitwiseNegation_UnaryExpression = Generalization(general=UnaryExpression, specific=prolog_expressions_BitwiseNegation)
gen_prolog_expressions_GreaterOrEqual_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_GreaterOrEqual)
gen_prolog_expressions_StandardOrderBefore_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_StandardOrderBefore)
gen_prolog_expressions_EqualOrStandardOrderBefore_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_EqualOrStandardOrderBefore)
gen_prolog_expressions_StandardOrderAfter_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_StandardOrderAfter)
gen_prolog_expressions_EqualOrStandardOrderAfter_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_EqualOrStandardOrderAfter)
gen_prolog_expressions_NotUnifiable_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_NotUnifiable)
gen_prolog_expressions_Disequality_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Disequality)
gen_prolog_expressions_As_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_As)
gen_prolog_expressions_Is_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Is)
gen_prolog_expressions_ParticalUnification_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_ParticalUnification)
gen_prolog_expressions_SubDict_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_SubDict)
gen_prolog_expressions_ModuleCall_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_ModuleCall)
gen_prolog_expressions_Plus_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Plus)
gen_prolog_expressions_Minus_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Minus)
gen_prolog_expressions_BinaryAnd_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_BinaryAnd)
gen_prolog_expressions_BinaryOr_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_BinaryOr)
gen_prolog_expressions_Xor_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Xor)
gen_prolog_expressions_Multiplication_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Multiplication)
gen_prolog_expressions_Division_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Division)
gen_prolog_expressions_IntegerDivision_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_IntegerDivision)
gen_prolog_expressions_Div_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Div)
gen_prolog_expressions_Rdiv_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Rdiv)
gen_prolog_expressions_BitwiseShiftLeft_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_BitwiseShiftLeft)
gen_prolog_expressions_Mod_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Mod)
gen_prolog_expressions_Rem_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Rem)
gen_prolog_expressions_Power_BinaryExpression = Generalization(general=BinaryExpression, specific=prolog_expressions_Power)

# Domain Model
domain_model = DomainModel(
    name="prolog",
    types={prolog_Term, Expression, prolog_CompoundTerm, Term, prolog_Program, prolog_Clause, prolog_Comment, Clause, prolog_directives_PredicateIndicator, prolog_directives_Dynamic, Directive, prolog_directives_Discontiguous, prolog_AtomicNumber, prolog_AtomicQuotedString, prolog_List, prolog_Fact, prolog_Rule, prolog_ControlPredicate, prolog_True, ControlPredicate, prolog_False, prolog_Fail, prolog_Cut, prolog_directives_Directive, PredicateIndicator, prolog_expressions_StructuralEquivalenceNotProvable, prolog_expressions_NumberEqual, prolog_expressions_LessOrEqual, prolog_expressions_Equivalence, prolog_expressions_NonEqualNumber, prolog_expressions_GreaterThan, prolog_directives_Multifile, prolog_directives_Public, prolog_directives_Volatile, prolog_directives_Table, prolog_expressions_Expression, prolog_expressions_UnaryExpression, prolog_expressions_BinaryExpression, prolog_expressions_LogicalOr, BinaryExpression, prolog_expressions_Condition, prolog_expressions_SoftCut, prolog_expressions_LogicalAnd, prolog_expressions_NotProvable, UnaryExpression, prolog_expressions_LessThan, prolog_expressions_Unification, prolog_expressions_Univ, prolog_expressions_StructuralEquivalence, prolog_expressions_PositiveNumber, prolog_expressions_NegativeNumber, prolog_expressions_BitwiseNegation, prolog_expressions_GreaterOrEqual, prolog_expressions_StandardOrderBefore, prolog_expressions_EqualOrStandardOrderBefore, prolog_expressions_StandardOrderAfter, prolog_expressions_EqualOrStandardOrderAfter, prolog_expressions_NotUnifiable, prolog_expressions_Disequality, prolog_expressions_As, prolog_expressions_Is, prolog_expressions_ParticalUnification, prolog_expressions_SubDict, prolog_expressions_ModuleCall, prolog_expressions_Plus, prolog_expressions_Minus, prolog_expressions_BinaryAnd, prolog_expressions_BinaryOr, prolog_expressions_Xor, prolog_expressions_Multiplication, prolog_expressions_Division, prolog_expressions_IntegerDivision, prolog_expressions_Div, prolog_expressions_Rdiv, prolog_expressions_BitwiseShiftLeft, prolog_expressions_Mod, prolog_expressions_Rem, prolog_expressions_Power},
    associations={clauses0, predicates14, arguments1, heads2, tails4, head7, head9, body11, predicate15, expr17, left19, right21},
    generalizations={gen_prolog_Term_Expression, gen_prolog_CompoundTerm_Clause, gen_prolog_CompoundTerm_Term, gen_prolog_Comment_Clause, gen_prolog_directives_Dynamic_Directive, gen_prolog_directives_Discontiguous_Directive, gen_prolog_AtomicNumber_Term, gen_prolog_AtomicQuotedString_Term, gen_prolog_List_Term, gen_prolog_Fact_Clause, gen_prolog_Rule_Clause, gen_prolog_ControlPredicate_Term, gen_prolog_True_ControlPredicate, gen_prolog_False_ControlPredicate, gen_prolog_Fail_ControlPredicate, gen_prolog_Cut_ControlPredicate, gen_prolog_directives_Directive_Clause, gen_prolog_expressions_StructuralEquivalenceNotProvable_BinaryExpression, gen_prolog_expressions_NumberEqual_BinaryExpression, gen_prolog_expressions_LessOrEqual_BinaryExpression, gen_prolog_expressions_Equivalence_BinaryExpression, gen_prolog_expressions_NonEqualNumber_BinaryExpression, gen_prolog_expressions_GreaterThan_BinaryExpression, gen_prolog_directives_Multifile_Directive, gen_prolog_directives_Public_Directive, gen_prolog_directives_Volatile_Directive, gen_prolog_directives_Table_Clause, gen_prolog_expressions_UnaryExpression_Expression, gen_prolog_expressions_BinaryExpression_Expression, gen_prolog_expressions_LogicalOr_BinaryExpression, gen_prolog_expressions_Condition_BinaryExpression, gen_prolog_expressions_SoftCut_BinaryExpression, gen_prolog_expressions_LogicalAnd_BinaryExpression, gen_prolog_expressions_NotProvable_UnaryExpression, gen_prolog_expressions_LessThan_BinaryExpression, gen_prolog_expressions_Unification_BinaryExpression, gen_prolog_expressions_Univ_BinaryExpression, gen_prolog_expressions_StructuralEquivalence_BinaryExpression, gen_prolog_expressions_PositiveNumber_UnaryExpression, gen_prolog_expressions_NegativeNumber_UnaryExpression, gen_prolog_expressions_BitwiseNegation_UnaryExpression, gen_prolog_expressions_GreaterOrEqual_BinaryExpression, gen_prolog_expressions_StandardOrderBefore_BinaryExpression, gen_prolog_expressions_EqualOrStandardOrderBefore_BinaryExpression, gen_prolog_expressions_StandardOrderAfter_BinaryExpression, gen_prolog_expressions_EqualOrStandardOrderAfter_BinaryExpression, gen_prolog_expressions_NotUnifiable_BinaryExpression, gen_prolog_expressions_Disequality_BinaryExpression, gen_prolog_expressions_As_BinaryExpression, gen_prolog_expressions_Is_BinaryExpression, gen_prolog_expressions_ParticalUnification_BinaryExpression, gen_prolog_expressions_SubDict_BinaryExpression, gen_prolog_expressions_ModuleCall_BinaryExpression, gen_prolog_expressions_Plus_BinaryExpression, gen_prolog_expressions_Minus_BinaryExpression, gen_prolog_expressions_BinaryAnd_BinaryExpression, gen_prolog_expressions_BinaryOr_BinaryExpression, gen_prolog_expressions_Xor_BinaryExpression, gen_prolog_expressions_Multiplication_BinaryExpression, gen_prolog_expressions_Division_BinaryExpression, gen_prolog_expressions_IntegerDivision_BinaryExpression, gen_prolog_expressions_Div_BinaryExpression, gen_prolog_expressions_Rdiv_BinaryExpression, gen_prolog_expressions_BitwiseShiftLeft_BinaryExpression, gen_prolog_expressions_Mod_BinaryExpression, gen_prolog_expressions_Rem_BinaryExpression, gen_prolog_expressions_Power_BinaryExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)