





import java.util.List;
import java.util.ArrayList;

public class thingML_VariableAssignment extends Action {






    private thingML_Variable thingml_variable;




    private List<thingML_Expression> thingml_expressions;




    private thingML_Expression thingml_expression;


    public thingML_VariableAssignment(
    ) {
        super(
        );
        this.thingml_expressions = new ArrayList<>();
    }

    public thingML_VariableAssignment(
        ArrayList<thingML_Expression> thingml_expressions    ) {
        this.thingml_expressions = thingml_expressions;
    }


    public thingML_Variable getThingml_variable() {
        return thingml_variable;
    }

    public void setThingml_variable(thingML_Variable thingml_variable) {
        this.thingml_variable = thingml_variable;
    }
    public List<thingML_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }
    public thingML_Expression getThingml_expression() {
        return thingml_expression;
    }

    public void setThingml_expression(thingML_Expression thingml_expression) {
        this.thingml_expression = thingml_expression;
    }

}