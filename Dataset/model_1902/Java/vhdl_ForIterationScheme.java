





import java.util.List;
import java.util.ArrayList;

public class vhdl_ForIterationScheme extends IterationScheme {

    private String variable;





    private vhdl_Expression vhdl_expression;


    public vhdl_ForIterationScheme(
        String variable    ) {
        super(
        );
        this.variable = variable;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }

    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }

}