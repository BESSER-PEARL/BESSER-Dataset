





import java.util.List;
import java.util.ArrayList;

public class eol_SwitchCaseExpressionStatement extends SwitchCaseStatement {






    private eol_Expression eol_expression;




    private eol_SwitchStatement eol_switchstatement;


    public eol_SwitchCaseExpressionStatement(
    ) {
        super(
        );
    }



    public eol_Expression getEol_expression() {
        return eol_expression;
    }

    public void setEol_expression(eol_Expression eol_expression) {
        this.eol_expression = eol_expression;
    }
    public eol_SwitchStatement getEol_switchstatement() {
        return eol_switchstatement;
    }

    public void setEol_switchstatement(eol_SwitchStatement eol_switchstatement) {
        this.eol_switchstatement = eol_switchstatement;
    }

}