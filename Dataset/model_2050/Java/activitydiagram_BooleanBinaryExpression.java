





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_BooleanBinaryExpression extends BooleanExpression {

    private String operator;



    public activitydiagram_BooleanBinaryExpression(
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