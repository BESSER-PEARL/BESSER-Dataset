





import java.util.List;
import java.util.ArrayList;

public class optGrammar_Assignment extends Expression {

    private String assignmentOp;





    private optGrammar_Expression optgrammar_expression;




    private optGrammar_Expression optgrammar_expression;


    public optGrammar_Assignment(
        String assignmentOp    ) {
        super(
        );
        this.assignmentOp = assignmentOp;
    }


    public String getAssignmentop() {
        return assignmentOp;
    }

    public void setAssignmentop(String assignmentOp) {
        this.assignmentOp = assignmentOp;
    }

    public optGrammar_Expression getOptgrammar_expression() {
        return optgrammar_expression;
    }

    public void setOptgrammar_expression(optGrammar_Expression optgrammar_expression) {
        this.optgrammar_expression = optgrammar_expression;
    }
    public optGrammar_Expression getOptgrammar_expression() {
        return optgrammar_expression;
    }

    public void setOptgrammar_expression(optGrammar_Expression optgrammar_expression) {
        this.optgrammar_expression = optgrammar_expression;
    }

}