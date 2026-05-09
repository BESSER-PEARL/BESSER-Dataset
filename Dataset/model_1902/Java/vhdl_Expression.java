





import java.util.List;
import java.util.ArrayList;

public class vhdl_Expression  {

    private String unary_operator;
    private String attribute;





    private vhdl_Expression vhdl_expression;




    private vhdl_Expression vhdl_expression;




    private vhdl_Expression vhdl_expression;




    private List<vhdl_Expression> vhdl_expressions;


    public vhdl_Expression(
        String unary_operator,        String attribute    ) {
        this.unary_operator = unary_operator;
        this.attribute = attribute;
        this.vhdl_expressions = new ArrayList<>();
    }

    public vhdl_Expression(
        String unary_operator,        String attribute        ArrayList<vhdl_Expression> vhdl_expressions    ) {
        this.unary_operator = unary_operator;
        this.attribute = attribute;
        this.vhdl_expressions = vhdl_expressions;
    }

    public String getUnary_operator() {
        return unary_operator;
    }

    public void setUnary_operator(String unary_operator) {
        this.unary_operator = unary_operator;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
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
    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }
    public List<vhdl_Expression> getVhdl_expressions() {
        return vhdl_expressions;
    }

    public void addVhdl_expression(Vhdl_expression vhdl_expression) {
        this.vhdl_expressions.add(vhdl_expression);
    }

}