





import java.util.List;
import java.util.ArrayList;

public class simpleExpressions_Comparison extends Expression {

    private String operator;



    public simpleExpressions_Comparison(
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