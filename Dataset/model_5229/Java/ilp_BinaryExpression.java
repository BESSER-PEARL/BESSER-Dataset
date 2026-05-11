





import java.util.List;
import java.util.ArrayList;

public class ilp_BinaryExpression extends Expression {

    private String operator;



    public ilp_BinaryExpression(
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