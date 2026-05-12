





import java.util.List;
import java.util.ArrayList;

public class sparql_ExpressionFilterExpression extends Expression {

    private String operator;



    public sparql_ExpressionFilterExpression(
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