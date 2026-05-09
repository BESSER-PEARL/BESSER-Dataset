





import java.util.List;
import java.util.ArrayList;

public class vhdl_SliceExpression extends Expression {






    private List<vhdl_Expression> vhdl_expressions;




    private vhdl_Expression vhdl_expression;


    public vhdl_SliceExpression(
    ) {
        super(
        );
        this.vhdl_expressions = new ArrayList<>();
    }

    public vhdl_SliceExpression(
        ArrayList<vhdl_Expression> vhdl_expressions    ) {
        this.vhdl_expressions = vhdl_expressions;
    }


    public List<vhdl_Expression> getVhdl_expressions() {
        return vhdl_expressions;
    }

    public void addVhdl_expression(Vhdl_expression vhdl_expression) {
        this.vhdl_expressions.add(vhdl_expression);
    }
    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }

}