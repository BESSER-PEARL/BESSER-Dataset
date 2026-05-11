





import java.util.List;
import java.util.ArrayList;

public class expression_StatementList extends Phrase {






    private expression_StatementList expression_statementlist;




    private expression_Statement expression_statement;


    public expression_StatementList(
    ) {
        super(
        );
    }



    public expression_StatementList getExpression_statementlist() {
        return expression_statementlist;
    }

    public void setExpression_statementlist(expression_StatementList expression_statementlist) {
        this.expression_statementlist = expression_statementlist;
    }
    public expression_Statement getExpression_statement() {
        return expression_statement;
    }

    public void setExpression_statement(expression_Statement expression_statement) {
        this.expression_statement = expression_statement;
    }

}