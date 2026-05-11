





import java.util.List;
import java.util.ArrayList;

public class vhdl_expression_AddingExpression extends BinaryExpression {

    private String operator;



    public vhdl_expression_AddingExpression(
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