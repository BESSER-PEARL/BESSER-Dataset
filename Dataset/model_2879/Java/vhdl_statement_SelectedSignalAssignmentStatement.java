





import java.util.List;
import java.util.ArrayList;

public class vhdl_statement_SelectedSignalAssignmentStatement extends ConditionalSignalAssignmentStatement {






    private Expression expression;


    public vhdl_statement_SelectedSignalAssignmentStatement(
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