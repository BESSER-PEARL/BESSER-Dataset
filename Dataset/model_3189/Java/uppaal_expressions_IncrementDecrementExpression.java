





import java.util.List;
import java.util.ArrayList;

public class uppaal_expressions_IncrementDecrementExpression extends Expression {

    private String operator;



    public uppaal_expressions_IncrementDecrementExpression(
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