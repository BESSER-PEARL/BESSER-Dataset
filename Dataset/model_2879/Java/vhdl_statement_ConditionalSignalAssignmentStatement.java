





import java.util.List;
import java.util.ArrayList;

public class vhdl_statement_ConditionalSignalAssignmentStatement extends SignalAssignmentStatement {






    private List<Expression> expressions;


    public vhdl_statement_ConditionalSignalAssignmentStatement(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public vhdl_statement_ConditionalSignalAssignmentStatement(
        ArrayList<Expression> expressions    ) {
        this.expressions = expressions;
    }


    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}