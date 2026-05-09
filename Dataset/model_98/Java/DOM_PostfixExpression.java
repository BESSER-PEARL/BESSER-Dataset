





import java.util.List;
import java.util.ArrayList;

public class DOM_PostfixExpression extends Expression {

    private String operator;



    public DOM_PostfixExpression(
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