





import java.util.List;
import java.util.ArrayList;

public class vhdl_statement_SequentialSignalAssignmentStatement extends SignalAssignmentStatement {






    private Expression expression;


    public vhdl_statement_SequentialSignalAssignmentStatement(
    ) {
        super(
        );
    }



    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}