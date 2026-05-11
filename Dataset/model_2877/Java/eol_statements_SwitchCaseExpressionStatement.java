





import java.util.List;
import java.util.ArrayList;

public class eol_statements_SwitchCaseExpressionStatement extends SwitchCaseStatement {






    private eol_statements_Expression eol_statements_expression;




    private eol_statements_SwitchStatement eol_statements_switchstatement;


    public eol_statements_SwitchCaseExpressionStatement(
    ) {
        super(
        );
    }



    public eol_statements_Expression getEol_statements_expression() {
        return eol_statements_expression;
    }

    public void setEol_statements_expression(eol_statements_Expression eol_statements_expression) {
        this.eol_statements_expression = eol_statements_expression;
    }
    public eol_statements_SwitchStatement getEol_statements_switchstatement() {
        return eol_statements_switchstatement;
    }

    public void setEol_statements_switchstatement(eol_statements_SwitchStatement eol_statements_switchstatement) {
        this.eol_statements_switchstatement = eol_statements_switchstatement;
    }

}