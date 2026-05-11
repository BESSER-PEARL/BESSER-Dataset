





import java.util.List;
import java.util.ArrayList;

public class expressions_NumericalAddSubtractExpression extends BinaryExpression {

    private String operator;



    public expressions_NumericalAddSubtractExpression(
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