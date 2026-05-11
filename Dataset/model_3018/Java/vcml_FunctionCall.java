





import java.util.List;
import java.util.ArrayList;

public class vcml_FunctionCall extends Expression {

    private String function;





    private vcml_Expression vcml_expression;


    public vcml_FunctionCall(
        String function    ) {
        super(
        );
        this.function = function;
    }


    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }

    public vcml_Expression getVcml_expression() {
        return vcml_expression;
    }

    public void setVcml_expression(vcml_Expression vcml_expression) {
        this.vcml_expression = vcml_expression;
    }

}