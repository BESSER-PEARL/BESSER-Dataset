





import java.util.List;
import java.util.ArrayList;

public class sml_BinaryOperationExpression extends Expression {

    private String operator;



    public sml_BinaryOperationExpression(
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