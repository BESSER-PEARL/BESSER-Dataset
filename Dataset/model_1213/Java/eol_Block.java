





import java.util.List;
import java.util.ArrayList;

public class eol_Block extends EOLElement {






    private List<eol_Statement> eol_statements;




    private eol_OperationDefinition eol_operationdefinition;




    private eol_ExpressionOrStatementBlock eol_expressionorstatementblock;


    public eol_Block(
    ) {
        super(
        );
        this.eol_statements = new ArrayList<>();
    }

    public eol_Block(
        ArrayList<eol_Statement> eol_statements    ) {
        this.eol_statements = eol_statements;
    }


    public List<eol_Statement> getEol_statements() {
        return eol_statements;
    }

    public void addEol_statement(Eol_statement eol_statement) {
        this.eol_statements.add(eol_statement);
    }
    public eol_OperationDefinition getEol_operationdefinition() {
        return eol_operationdefinition;
    }

    public void setEol_operationdefinition(eol_OperationDefinition eol_operationdefinition) {
        this.eol_operationdefinition = eol_operationdefinition;
    }
    public eol_ExpressionOrStatementBlock getEol_expressionorstatementblock() {
        return eol_expressionorstatementblock;
    }

    public void setEol_expressionorstatementblock(eol_ExpressionOrStatementBlock eol_expressionorstatementblock) {
        this.eol_expressionorstatementblock = eol_expressionorstatementblock;
    }

}