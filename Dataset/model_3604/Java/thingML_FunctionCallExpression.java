





import java.util.List;
import java.util.ArrayList;

public class thingML_FunctionCallExpression extends Expression {






    private thingML_Function thingml_function;




    private List<thingML_Expression> thingml_expressions;


    public thingML_FunctionCallExpression(
    ) {
        super(
        );
        this.thingml_expressions = new ArrayList<>();
    }

    public thingML_FunctionCallExpression(
        ArrayList<thingML_Expression> thingml_expressions    ) {
        this.thingml_expressions = thingml_expressions;
    }


    public thingML_Function getThingml_function() {
        return thingml_function;
    }

    public void setThingml_function(thingML_Function thingml_function) {
        this.thingml_function = thingml_function;
    }
    public List<thingML_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }

}