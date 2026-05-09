





import java.util.List;
import java.util.ArrayList;

public class vhdl_RangeExpression extends Expression {

    private String operator;
    private String direction;





    private vhdl_Expression vhdl_expression;




    private vhdl_Expression vhdl_expression;


    public vhdl_RangeExpression(
        String operator,        String direction    ) {
        super(
        );
        this.operator = operator;
        this.direction = direction;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }
    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }

}