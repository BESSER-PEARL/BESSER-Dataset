





import java.util.List;
import java.util.ArrayList;

public class java_PrefixExpression extends Expression {

    private String operator;



    public java_PrefixExpression(
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