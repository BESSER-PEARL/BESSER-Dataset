





import java.util.List;
import java.util.ArrayList;

public class dom_FunctionCall extends Expression {

    private String function;





    private List<dom_Expression> dom_expressions;


    public dom_FunctionCall(
        String function    ) {
        super(
        );
        this.function = function;
        this.dom_expressions = new ArrayList<>();
    }

    public dom_FunctionCall(
        String function        ArrayList<dom_Expression> dom_expressions    ) {
        this.function = function;
        this.dom_expressions = dom_expressions;
    }

    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }

    public List<dom_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }

}