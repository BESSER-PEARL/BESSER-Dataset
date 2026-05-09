





import java.util.List;
import java.util.ArrayList;

public class eol_ForStatement extends Statement {






    private eol_ExpressionOrStatementBlock eol_expressionorstatementblock;




    private eol_Expression eol_expression;


    public eol_ForStatement(
    ) {
        super(
        );
    }



    public eol_ExpressionOrStatementBlock getEol_expressionorstatementblock() {
        return eol_expressionorstatementblock;
    }

    public void setEol_expressionorstatementblock(eol_ExpressionOrStatementBlock eol_expressionorstatementblock) {
        this.eol_expressionorstatementblock = eol_expressionorstatementblock;
    }
    public eol_Expression getEol_expression() {
        return eol_expression;
    }

    public void setEol_expression(eol_Expression eol_expression) {
        this.eol_expression = eol_expression;
    }

}