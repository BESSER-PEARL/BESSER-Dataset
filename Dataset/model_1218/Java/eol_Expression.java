





import java.util.List;
import java.util.ArrayList;

public class eol_Expression extends EOLElement {

    private boolean inBrackets;





    private eol_ExpressionOrStatementBlock eol_expressionorstatementblock;




    private eol_ExpressionOrStatementBlock eol_expressionorstatementblock;


    public eol_Expression(
        boolean inBrackets    ) {
        super(
        );
        this.inBrackets = inBrackets;
    }


    public boolean getInbrackets() {
        return inBrackets;
    }

    public void setInbrackets(boolean inBrackets) {
        this.inBrackets = inBrackets;
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