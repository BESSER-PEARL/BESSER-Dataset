





import java.util.List;
import java.util.ArrayList;

public class stateMachineDsl_VarParName  {

    private String name;





    private stateMachineDsl_Parameter statemachinedsl_parameter;




    private stateMachineDsl_Variable statemachinedsl_variable;


    public stateMachineDsl_VarParName(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public stateMachineDsl_Parameter getStatemachinedsl_parameter() {
        return statemachinedsl_parameter;
    }

    public void setStatemachinedsl_parameter(stateMachineDsl_Parameter statemachinedsl_parameter) {
        this.statemachinedsl_parameter = statemachinedsl_parameter;
    }
    public stateMachineDsl_Variable getStatemachinedsl_variable() {
        return statemachinedsl_variable;
    }

    public void setStatemachinedsl_variable(stateMachineDsl_Variable statemachinedsl_variable) {
        this.statemachinedsl_variable = statemachinedsl_variable;
    }

}