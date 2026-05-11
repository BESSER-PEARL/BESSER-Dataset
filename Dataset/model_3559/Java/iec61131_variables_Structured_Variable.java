





import java.util.List;
import java.util.ArrayList;

public class iec61131_variables_Structured_Variable extends Multi_Element_Variable {






    private Variable_Name variable_name;




    private Symbolic_Variable symbolic_variable;


    public iec61131_variables_Structured_Variable(
    ) {
        super(
        );
    }



    public Variable_Name getVariable_name() {
        return variable_name;
    }

    public void setVariable_name(Variable_Name variable_name) {
        this.variable_name = variable_name;
    }
    public Symbolic_Variable getSymbolic_variable() {
        return symbolic_variable;
    }

    public void setSymbolic_variable(Symbolic_Variable symbolic_variable) {
        this.symbolic_variable = symbolic_variable;
    }

}