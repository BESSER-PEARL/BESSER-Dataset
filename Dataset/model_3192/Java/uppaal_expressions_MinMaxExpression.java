





import java.util.List;
import java.util.ArrayList;

public class uppaal_expressions_MinMaxExpression extends BinaryExpression {

    private String operator;



    public uppaal_expressions_MinMaxExpression(
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