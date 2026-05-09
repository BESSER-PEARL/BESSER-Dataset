





import java.util.List;
import java.util.ArrayList;

public class statements_WhileLoop extends StatementContainer, Statement {






    private Expression expression;


    public statements_WhileLoop(
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