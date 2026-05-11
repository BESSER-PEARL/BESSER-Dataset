





import java.util.List;
import java.util.ArrayList;

public class mt_expressions_Operator extends Expression {

    private String operator;



    public mt_expressions_Operator(
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