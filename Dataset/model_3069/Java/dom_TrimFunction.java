





import java.util.List;
import java.util.ArrayList;

public class dom_TrimFunction extends Expression {

    private String function;
    private String mode;





    private dom_Expression dom_expression;


    public dom_TrimFunction(
        String function,        String mode    ) {
        super(
        );
        this.function = function;
        this.mode = mode;
    }


    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}