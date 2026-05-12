





import java.util.List;
import java.util.ArrayList;

public class jDOQL_AdditionExpression extends Expression {

    private String operator;



    public jDOQL_AdditionExpression(
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