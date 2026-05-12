





import java.util.List;
import java.util.ArrayList;

public class jPQL_MultiplicationExpression extends Expression {

    private String operator;



    public jPQL_MultiplicationExpression(
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