





import java.util.List;
import java.util.ArrayList;

public class logiclanguage_Term extends TermDescription {






    private logiclanguage_Iff logiclanguage_iff;




    private logiclanguage_QuantifiedExpression logiclanguage_quantifiedexpression;




    private logiclanguage_LessOrEqualThan logiclanguage_lessorequalthan;




    private logiclanguage_IfThenElse logiclanguage_ifthenelse;




    private logiclanguage_ConstantDefinition logiclanguage_constantdefinition;




    private logiclanguage_NumericOperation logiclanguage_numericoperation;




    private logiclanguage_NumericOperation logiclanguage_numericoperation;




    private logiclanguage_TransitiveClosure logiclanguage_transitiveclosure;




    private logiclanguage_MoreThan logiclanguage_morethan;




    private logiclanguage_InstanceOf logiclanguage_instanceof;




    private logiclanguage_Or logiclanguage_or;




    private logiclanguage_RelationDefinition logiclanguage_relationdefinition;




    private logiclanguage_IfThenElse logiclanguage_ifthenelse;




    private logiclanguage_Impl logiclanguage_impl;




    private logiclanguage_Not logiclanguage_not;




    private logiclanguage_Iff logiclanguage_iff;




    private logiclanguage_Assertion logiclanguage_assertion;




    private logiclanguage_LessOrEqualThan logiclanguage_lessorequalthan;




    private logiclanguage_MoreOrEqualThan logiclanguage_moreorequalthan;




    private logiclanguage_TransitiveClosure logiclanguage_transitiveclosure;




    private logiclanguage_And logiclanguage_and;




    private logiclanguage_Impl logiclanguage_impl;




    private logiclanguage_IfThenElse logiclanguage_ifthenelse;




    private logiclanguage_MoreOrEqualThan logiclanguage_moreorequalthan;




    private logiclanguage_MoreThan logiclanguage_morethan;




    private logiclanguage_FunctionDefinition logiclanguage_functiondefinition;


    public logiclanguage_Term(
    ) {
        super(
        );
    }



    public logiclanguage_Iff getLogiclanguage_iff() {
        return logiclanguage_iff;
    }

    public void setLogiclanguage_iff(logiclanguage_Iff logiclanguage_iff) {
        this.logiclanguage_iff = logiclanguage_iff;
    }
    public logiclanguage_QuantifiedExpression getLogiclanguage_quantifiedexpression() {
        return logiclanguage_quantifiedexpression;
    }

    public void setLogiclanguage_quantifiedexpression(logiclanguage_QuantifiedExpression logiclanguage_quantifiedexpression) {
        this.logiclanguage_quantifiedexpression = logiclanguage_quantifiedexpression;
    }
    public logiclanguage_LessOrEqualThan getLogiclanguage_lessorequalthan() {
        return logiclanguage_lessorequalthan;
    }

    public void setLogiclanguage_lessorequalthan(logiclanguage_LessOrEqualThan logiclanguage_lessorequalthan) {
        this.logiclanguage_lessorequalthan = logiclanguage_lessorequalthan;
    }
    public logiclanguage_IfThenElse getLogiclanguage_ifthenelse() {
        return logiclanguage_ifthenelse;
    }

    public void setLogiclanguage_ifthenelse(logiclanguage_IfThenElse logiclanguage_ifthenelse) {
        this.logiclanguage_ifthenelse = logiclanguage_ifthenelse;
    }
    public logiclanguage_ConstantDefinition getLogiclanguage_constantdefinition() {
        return logiclanguage_constantdefinition;
    }

    public void setLogiclanguage_constantdefinition(logiclanguage_ConstantDefinition logiclanguage_constantdefinition) {
        this.logiclanguage_constantdefinition = logiclanguage_constantdefinition;
    }
    public logiclanguage_NumericOperation getLogiclanguage_numericoperation() {
        return logiclanguage_numericoperation;
    }

    public void setLogiclanguage_numericoperation(logiclanguage_NumericOperation logiclanguage_numericoperation) {
        this.logiclanguage_numericoperation = logiclanguage_numericoperation;
    }
    public logiclanguage_NumericOperation getLogiclanguage_numericoperation() {
        return logiclanguage_numericoperation;
    }

    public void setLogiclanguage_numericoperation(logiclanguage_NumericOperation logiclanguage_numericoperation) {
        this.logiclanguage_numericoperation = logiclanguage_numericoperation;
    }
    public logiclanguage_TransitiveClosure getLogiclanguage_transitiveclosure() {
        return logiclanguage_transitiveclosure;
    }

    public void setLogiclanguage_transitiveclosure(logiclanguage_TransitiveClosure logiclanguage_transitiveclosure) {
        this.logiclanguage_transitiveclosure = logiclanguage_transitiveclosure;
    }
    public logiclanguage_MoreThan getLogiclanguage_morethan() {
        return logiclanguage_morethan;
    }

    public void setLogiclanguage_morethan(logiclanguage_MoreThan logiclanguage_morethan) {
        this.logiclanguage_morethan = logiclanguage_morethan;
    }
    public logiclanguage_InstanceOf getLogiclanguage_instanceof() {
        return logiclanguage_instanceof;
    }

    public void setLogiclanguage_instanceof(logiclanguage_InstanceOf logiclanguage_instanceof) {
        this.logiclanguage_instanceof = logiclanguage_instanceof;
    }
    public logiclanguage_Or getLogiclanguage_or() {
        return logiclanguage_or;
    }

    public void setLogiclanguage_or(logiclanguage_Or logiclanguage_or) {
        this.logiclanguage_or = logiclanguage_or;
    }
    public logiclanguage_RelationDefinition getLogiclanguage_relationdefinition() {
        return logiclanguage_relationdefinition;
    }

    public void setLogiclanguage_relationdefinition(logiclanguage_RelationDefinition logiclanguage_relationdefinition) {
        this.logiclanguage_relationdefinition = logiclanguage_relationdefinition;
    }
    public logiclanguage_IfThenElse getLogiclanguage_ifthenelse() {
        return logiclanguage_ifthenelse;
    }

    public void setLogiclanguage_ifthenelse(logiclanguage_IfThenElse logiclanguage_ifthenelse) {
        this.logiclanguage_ifthenelse = logiclanguage_ifthenelse;
    }
    public logiclanguage_Impl getLogiclanguage_impl() {
        return logiclanguage_impl;
    }

    public void setLogiclanguage_impl(logiclanguage_Impl logiclanguage_impl) {
        this.logiclanguage_impl = logiclanguage_impl;
    }
    public logiclanguage_Not getLogiclanguage_not() {
        return logiclanguage_not;
    }

    public void setLogiclanguage_not(logiclanguage_Not logiclanguage_not) {
        this.logiclanguage_not = logiclanguage_not;
    }
    public logiclanguage_Iff getLogiclanguage_iff() {
        return logiclanguage_iff;
    }

    public void setLogiclanguage_iff(logiclanguage_Iff logiclanguage_iff) {
        this.logiclanguage_iff = logiclanguage_iff;
    }
    public logiclanguage_Assertion getLogiclanguage_assertion() {
        return logiclanguage_assertion;
    }

    public void setLogiclanguage_assertion(logiclanguage_Assertion logiclanguage_assertion) {
        this.logiclanguage_assertion = logiclanguage_assertion;
    }
    public logiclanguage_LessOrEqualThan getLogiclanguage_lessorequalthan() {
        return logiclanguage_lessorequalthan;
    }

    public void setLogiclanguage_lessorequalthan(logiclanguage_LessOrEqualThan logiclanguage_lessorequalthan) {
        this.logiclanguage_lessorequalthan = logiclanguage_lessorequalthan;
    }
    public logiclanguage_MoreOrEqualThan getLogiclanguage_moreorequalthan() {
        return logiclanguage_moreorequalthan;
    }

    public void setLogiclanguage_moreorequalthan(logiclanguage_MoreOrEqualThan logiclanguage_moreorequalthan) {
        this.logiclanguage_moreorequalthan = logiclanguage_moreorequalthan;
    }
    public logiclanguage_TransitiveClosure getLogiclanguage_transitiveclosure() {
        return logiclanguage_transitiveclosure;
    }

    public void setLogiclanguage_transitiveclosure(logiclanguage_TransitiveClosure logiclanguage_transitiveclosure) {
        this.logiclanguage_transitiveclosure = logiclanguage_transitiveclosure;
    }
    public logiclanguage_And getLogiclanguage_and() {
        return logiclanguage_and;
    }

    public void setLogiclanguage_and(logiclanguage_And logiclanguage_and) {
        this.logiclanguage_and = logiclanguage_and;
    }
    public logiclanguage_Impl getLogiclanguage_impl() {
        return logiclanguage_impl;
    }

    public void setLogiclanguage_impl(logiclanguage_Impl logiclanguage_impl) {
        this.logiclanguage_impl = logiclanguage_impl;
    }
    public logiclanguage_IfThenElse getLogiclanguage_ifthenelse() {
        return logiclanguage_ifthenelse;
    }

    public void setLogiclanguage_ifthenelse(logiclanguage_IfThenElse logiclanguage_ifthenelse) {
        this.logiclanguage_ifthenelse = logiclanguage_ifthenelse;
    }
    public logiclanguage_MoreOrEqualThan getLogiclanguage_moreorequalthan() {
        return logiclanguage_moreorequalthan;
    }

    public void setLogiclanguage_moreorequalthan(logiclanguage_MoreOrEqualThan logiclanguage_moreorequalthan) {
        this.logiclanguage_moreorequalthan = logiclanguage_moreorequalthan;
    }
    public logiclanguage_MoreThan getLogiclanguage_morethan() {
        return logiclanguage_morethan;
    }

    public void setLogiclanguage_morethan(logiclanguage_MoreThan logiclanguage_morethan) {
        this.logiclanguage_morethan = logiclanguage_morethan;
    }
    public logiclanguage_FunctionDefinition getLogiclanguage_functiondefinition() {
        return logiclanguage_functiondefinition;
    }

    public void setLogiclanguage_functiondefinition(logiclanguage_FunctionDefinition logiclanguage_functiondefinition) {
        this.logiclanguage_functiondefinition = logiclanguage_functiondefinition;
    }

}