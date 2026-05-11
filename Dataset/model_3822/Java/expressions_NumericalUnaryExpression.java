





import java.util.List;
import java.util.ArrayList;

public class expressions_NumericalUnaryExpression extends UnaryExpression {

    private String operator;



    public expressions_NumericalUnaryExpression(
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