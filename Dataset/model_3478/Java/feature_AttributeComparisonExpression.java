





import java.util.List;
import java.util.ArrayList;

public class feature_AttributeComparisonExpression extends AtomicExpression {

    private String operator;



    public feature_AttributeComparisonExpression(
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