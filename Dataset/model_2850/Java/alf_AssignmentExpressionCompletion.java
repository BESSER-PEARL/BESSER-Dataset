





import java.util.List;
import java.util.ArrayList;

public class alf_AssignmentExpressionCompletion extends ExpressionCompletion {

    private String operator;



    public alf_AssignmentExpressionCompletion(
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


}