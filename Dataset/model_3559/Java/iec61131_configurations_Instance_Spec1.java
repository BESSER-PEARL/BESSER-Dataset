





import java.util.List;
import java.util.ArrayList;

public class iec61131_configurations_Instance_Spec1 extends Instance_Specific_Init {






    private Variable_Name variable_name;




    private Located_Var_Spec_Init located_var_spec_init;




    private Location location;


    public iec61131_configurations_Instance_Spec1(
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
    public Located_Var_Spec_Init getLocated_var_spec_init() {
        return located_var_spec_init;
    }

    public void setLocated_var_spec_init(Located_Var_Spec_Init located_var_spec_init) {
        this.located_var_spec_init = located_var_spec_init;
    }
    public Location getLocation() {
        return location;
    }

    public void setLocation(Location location) {
        this.location = location;
    }

}