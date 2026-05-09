





import java.util.List;
import java.util.ArrayList;

public class javaMM_PostfixExpression extends Expression {

    private String operator;



    public javaMM_PostfixExpression(
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