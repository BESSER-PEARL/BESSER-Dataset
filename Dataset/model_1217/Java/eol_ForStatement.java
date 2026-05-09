





import java.util.List;
import java.util.ArrayList;

public class eol_ForStatement extends Statement {






    private eol_FormalParameterExpression eol_formalparameterexpression;




    private eol_Expression eol_expression;


    public eol_ForStatement(
    ) {
        super(
        );
    }



    public eol_FormalParameterExpression getEol_formalparameterexpression() {
        return eol_formalparameterexpression;
    }

    public void setEol_formalparameterexpression(eol_FormalParameterExpression eol_formalparameterexpression) {
        this.eol_formalparameterexpression = eol_formalparameterexpression;
    }
    public eol_Expression getEol_expression() {
        return eol_expression;
    }

    public void setEol_expression(eol_Expression eol_expression) {
        this.eol_expression = eol_expression;
    }

}