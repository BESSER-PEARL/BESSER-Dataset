





import java.util.List;
import java.util.ArrayList;

public class vhdl_expression_RelationalExpression extends BinaryExpression {

    private String operator;



    public vhdl_expression_RelationalExpression(
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