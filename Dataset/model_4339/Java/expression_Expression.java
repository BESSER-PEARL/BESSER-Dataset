





import java.util.List;
import java.util.ArrayList;

public class expression_Expression extends ExpressionRest, Phrase {






    private expression_AssignmentStatement expression_assignmentstatement;




    private expression_Expression expression_expression;


    public expression_Expression(
    ) {
        super(
        );
    }



    public expression_AssignmentStatement getExpression_assignmentstatement() {
        return expression_assignmentstatement;
    }

    public void setExpression_assignmentstatement(expression_AssignmentStatement expression_assignmentstatement) {
        this.expression_assignmentstatement = expression_assignmentstatement;
    }
    public expression_Expression getExpression_expression() {
        return expression_expression;
    }

    public void setExpression_expression(expression_Expression expression_expression) {
        this.expression_expression = expression_expression;
    }

}