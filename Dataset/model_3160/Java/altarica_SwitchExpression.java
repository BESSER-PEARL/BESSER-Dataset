





import java.util.List;
import java.util.ArrayList;

public class altarica_SwitchExpression extends Expression {






    private altarica_Expression altarica_expression;




    private List<altarica_CaseExpression> altarica_caseexpressions;


    public altarica_SwitchExpression(
    ) {
        super(
        );
        this.altarica_caseexpressions = new ArrayList<>();
    }

    public altarica_SwitchExpression(
        ArrayList<altarica_CaseExpression> altarica_caseexpressions    ) {
        this.altarica_caseexpressions = altarica_caseexpressions;
    }


    public altarica_Expression getAltarica_expression() {
        return altarica_expression;
    }

    public void setAltarica_expression(altarica_Expression altarica_expression) {
        this.altarica_expression = altarica_expression;
    }
    public List<altarica_CaseExpression> getAltarica_caseexpressions() {
        return altarica_caseexpressions;
    }

    public void addAltarica_caseexpression(Altarica_caseexpression altarica_caseexpression) {
        this.altarica_caseexpressions.add(altarica_caseexpression);
    }

}