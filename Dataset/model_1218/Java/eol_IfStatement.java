





import java.util.List;
import java.util.ArrayList;

public class eol_IfStatement extends Statement {






    private eol_Expression eol_expression;




    private List<eol_ExpressionOrStatementBlock> eol_expressionorstatementblocks;




    private eol_ExpressionOrStatementBlock eol_expressionorstatementblock;




    private eol_ExpressionOrStatementBlock eol_expressionorstatementblock;


    public eol_IfStatement(
    ) {
        super(
        );
        this.eol_expressionorstatementblocks = new ArrayList<>();
    }

    public eol_IfStatement(
        ArrayList<eol_ExpressionOrStatementBlock> eol_expressionorstatementblocks    ) {
        this.eol_expressionorstatementblocks = eol_expressionorstatementblocks;
    }


    public eol_Expression getEol_expression() {
        return eol_expression;
    }

    public void setEol_expression(eol_Expression eol_expression) {
        this.eol_expression = eol_expression;
    }
    public List<eol_ExpressionOrStatementBlock> getEol_expressionorstatementblocks() {
        return eol_expressionorstatementblocks;
    }

    public void addEol_expressionorstatementblock(Eol_expressionorstatementblock eol_expressionorstatementblock) {
        this.eol_expressionorstatementblocks.add(eol_expressionorstatementblock);
    }
    public eol_ExpressionOrStatementBlock getEol_expressionorstatementblock() {
        return eol_expressionorstatementblock;
    }

    public void setEol_expressionorstatementblock(eol_ExpressionOrStatementBlock eol_expressionorstatementblock) {
        this.eol_expressionorstatementblock = eol_expressionorstatementblock;
    }
    public eol_ExpressionOrStatementBlock getEol_expressionorstatementblock() {
        return eol_expressionorstatementblock;
    }

    public void setEol_expressionorstatementblock(eol_ExpressionOrStatementBlock eol_expressionorstatementblock) {
        this.eol_expressionorstatementblock = eol_expressionorstatementblock;
    }

}