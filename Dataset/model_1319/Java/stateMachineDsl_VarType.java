





import java.util.List;
import java.util.ArrayList;

public class stateMachineDsl_VarType  {

    private String vt;





    private stateMachineDsl_ParameterFunction statemachinedsl_parameterfunction;




    private stateMachineDsl_Parameter statemachinedsl_parameter;




    private stateMachineDsl_Variable statemachinedsl_variable;




    private stateMachineDsl_Function statemachinedsl_function;


    public stateMachineDsl_VarType(
        String vt    ) {
        this.vt = vt;
    }


    public String getVt() {
        return vt;
    }

    public void setVt(String vt) {
        this.vt = vt;
    }

    public stateMachineDsl_ParameterFunction getStatemachinedsl_parameterfunction() {
        return statemachinedsl_parameterfunction;
    }

    public void setStatemachinedsl_parameterfunction(stateMachineDsl_ParameterFunction statemachinedsl_parameterfunction) {
        this.statemachinedsl_parameterfunction = statemachinedsl_parameterfunction;
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
    public stateMachineDsl_Function getStatemachinedsl_function() {
        return statemachinedsl_function;
    }

    public void setStatemachinedsl_function(stateMachineDsl_Function statemachinedsl_function) {
        this.statemachinedsl_function = statemachinedsl_function;
    }

}