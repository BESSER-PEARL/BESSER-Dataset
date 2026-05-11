





import java.util.List;
import java.util.ArrayList;

public class thingml_VariableAssignment extends Action {






    private List<thingml_Expression> thingml_expressions;




    private thingml_Expression thingml_expression;




    private thingml_Variable thingml_variable;


    public thingml_VariableAssignment(
    ) {
        super(
        );
        this.thingml_expressions = new ArrayList<>();
    }

    public thingml_VariableAssignment(
        ArrayList<thingml_Expression> thingml_expressions    ) {
        this.thingml_expressions = thingml_expressions;
    }


    public List<thingml_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }
    public thingml_Expression getThingml_expression() {
        return thingml_expression;
    }

    public void setThingml_expression(thingml_Expression thingml_expression) {
        this.thingml_expression = thingml_expression;
    }
    public thingml_Variable getThingml_variable() {
        return thingml_variable;
    }

    public void setThingml_variable(thingml_Variable thingml_variable) {
        this.thingml_variable = thingml_variable;
    }

}