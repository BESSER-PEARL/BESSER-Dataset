





import java.util.List;
import java.util.ArrayList;

public class frontend_core_IfBranch  {






    private List<Statement> statements;




    private Expression expression;


    public frontend_core_IfBranch(
    ) {
        this.statements = new ArrayList<>();
    }

    public frontend_core_IfBranch(
        ArrayList<Statement> statements    ) {
        this.statements = statements;
    }


    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}