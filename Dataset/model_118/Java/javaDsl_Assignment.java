





import java.util.List;
import java.util.ArrayList;

public class javaDsl_Assignment extends AssignmentExpression, StatementExpression {

    private String operator;





    private javaDsl_AssignmentExpression javadsl_assignmentexpression;


    public javaDsl_Assignment(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public javaDsl_AssignmentExpression getJavadsl_assignmentexpression() {
        return javadsl_assignmentexpression;
    }

    public void setJavadsl_assignmentexpression(javaDsl_AssignmentExpression javadsl_assignmentexpression) {
        this.javadsl_assignmentexpression = javadsl_assignmentexpression;
    }

}