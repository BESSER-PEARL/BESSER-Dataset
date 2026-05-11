





import java.util.List;
import java.util.ArrayList;

public class vcml_BinaryExpression extends Expression {

    private String operator;





    private vcml_Expression vcml_expression;




    private vcml_Expression vcml_expression;


    public vcml_BinaryExpression(
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

    public vcml_Expression getVcml_expression() {
        return vcml_expression;
    }

    public void setVcml_expression(vcml_Expression vcml_expression) {
        this.vcml_expression = vcml_expression;
    }
    public vcml_Expression getVcml_expression() {
        return vcml_expression;
    }

    public void setVcml_expression(vcml_Expression vcml_expression) {
        this.vcml_expression = vcml_expression;
    }

}