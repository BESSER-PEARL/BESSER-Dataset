





import java.util.List;
import java.util.ArrayList;

public class thingml_FunctionCall  {






    private thingml_Function thingml_function;




    private List<thingml_Expression> thingml_expressions;


    public thingml_FunctionCall(
    ) {
        this.thingml_expressions = new ArrayList<>();
    }

    public thingml_FunctionCall(
        ArrayList<thingml_Expression> thingml_expressions    ) {
        this.thingml_expressions = thingml_expressions;
    }


    public thingml_Function getThingml_function() {
        return thingml_function;
    }

    public void setThingml_function(thingml_Function thingml_function) {
        this.thingml_function = thingml_function;
    }
    public List<thingml_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }

}