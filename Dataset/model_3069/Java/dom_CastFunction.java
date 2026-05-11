





import java.util.List;
import java.util.ArrayList;

public class dom_CastFunction extends Expression {

    private String name;
    private String function;





    private dom_Expression dom_expression;


    public dom_CastFunction(
        String name,        String function    ) {
        super(
        );
        this.name = name;
        this.function = function;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }

    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}