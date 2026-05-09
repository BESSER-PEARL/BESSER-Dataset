





import java.util.List;
import java.util.ArrayList;

public class stateMachineDsl_ProcedureUse  {






    private stateMachineDsl_Procedure statemachinedsl_procedure;




    private List<stateMachineDsl_Expression> statemachinedsl_expressions;


    public stateMachineDsl_ProcedureUse(
    ) {
        this.statemachinedsl_expressions = new ArrayList<>();
    }

    public stateMachineDsl_ProcedureUse(
        ArrayList<stateMachineDsl_Expression> statemachinedsl_expressions    ) {
        this.statemachinedsl_expressions = statemachinedsl_expressions;
    }


    public stateMachineDsl_Procedure getStatemachinedsl_procedure() {
        return statemachinedsl_procedure;
    }

    public void setStatemachinedsl_procedure(stateMachineDsl_Procedure statemachinedsl_procedure) {
        this.statemachinedsl_procedure = statemachinedsl_procedure;
    }
    public List<stateMachineDsl_Expression> getStatemachinedsl_expressions() {
        return statemachinedsl_expressions;
    }

    public void addStatemachinedsl_expression(Statemachinedsl_expression statemachinedsl_expression) {
        this.statemachinedsl_expressions.add(statemachinedsl_expression);
    }

}