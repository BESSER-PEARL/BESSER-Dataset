





import java.util.List;
import java.util.ArrayList;

public class c_sharp_expressions_StatementExpressionList extends ForInitializer {






    private List<StatementExpression> statementexpressions;


    public c_sharp_expressions_StatementExpressionList(
    ) {
        super(
        );
        this.statementexpressions = new ArrayList<>();
    }

    public c_sharp_expressions_StatementExpressionList(
        ArrayList<StatementExpression> statementexpressions    ) {
        this.statementexpressions = statementexpressions;
    }


    public List<StatementExpression> getStatementexpressions() {
        return statementexpressions;
    }

    public void addStatementexpression(Statementexpression statementexpression) {
        this.statementexpressions.add(statementexpression);
    }

}