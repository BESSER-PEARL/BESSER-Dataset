





import java.util.List;
import java.util.ArrayList;

public class eol_Block extends EOLElement {






    private eol_ExpressionOrStatementBlock eol_expressionorstatementblock;




    private eol_OperationDefinition eol_operationdefinition;


    public eol_Block(
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
    public eol_OperationDefinition getEol_operationdefinition() {
        return eol_operationdefinition;
    }

    public void setEol_operationdefinition(eol_OperationDefinition eol_operationdefinition) {
        this.eol_operationdefinition = eol_operationdefinition;
    }

}