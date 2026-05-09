





import java.util.List;
import java.util.ArrayList;

public class stateMachineDsl_FunctionUse extends Expression {






    private stateMachineDsl_Function statemachinedsl_function;




    private List<stateMachineDsl_Expression> statemachinedsl_expressions;


    public stateMachineDsl_FunctionUse(
    ) {
        super(
        );
        this.statemachinedsl_expressions = new ArrayList<>();
    }

    public stateMachineDsl_FunctionUse(
        ArrayList<stateMachineDsl_Expression> statemachinedsl_expressions    ) {
        this.statemachinedsl_expressions = statemachinedsl_expressions;
    }


    public stateMachineDsl_Function getStatemachinedsl_function() {
        return statemachinedsl_function;
    }

    public void setStatemachinedsl_function(stateMachineDsl_Function statemachinedsl_function) {
        this.statemachinedsl_function = statemachinedsl_function;
    }
    public List<stateMachineDsl_Expression> getStatemachinedsl_expressions() {
        return statemachinedsl_expressions;
    }

    public void addStatemachinedsl_expression(Statemachinedsl_expression statemachinedsl_expression) {
        this.statemachinedsl_expressions.add(statemachinedsl_expression);
    }

}