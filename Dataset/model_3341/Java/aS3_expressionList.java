





import java.util.List;
import java.util.ArrayList;

public class aS3_expressionList extends ExpressionStatement, forInClauseTail, brackets {






    private List<aS3_assignmentExpression> as3_assignmentexpressions;


    public aS3_expressionList(
    ) {
        super(
        );
        this.as3_assignmentexpressions = new ArrayList<>();
    }

    public aS3_expressionList(
        ArrayList<aS3_assignmentExpression> as3_assignmentexpressions    ) {
        this.as3_assignmentexpressions = as3_assignmentexpressions;
    }


    public List<aS3_assignmentExpression> getAs3_assignmentexpressions() {
        return as3_assignmentexpressions;
    }

    public void addAs3_assignmentexpression(As3_assignmentexpression as3_assignmentexpression) {
        this.as3_assignmentexpressions.add(as3_assignmentexpression);
    }

}