





import java.util.List;
import java.util.ArrayList;

public class ACG_ConditionalStat extends CompoundStat {






    private Expression expression;




    private List<Statement> statements;


    public ACG_ConditionalStat(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
    }

    public ACG_ConditionalStat(
        ArrayList<Statement> statements    ) {
        this.statements = statements;
    }


    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }
    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }

}