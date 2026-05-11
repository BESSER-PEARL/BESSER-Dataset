





import java.util.List;
import java.util.ArrayList;

public class expressions_NumericalMultiplyDivideExpression extends BinaryExpression {

    private String operator;



    public expressions_NumericalMultiplyDivideExpression(
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