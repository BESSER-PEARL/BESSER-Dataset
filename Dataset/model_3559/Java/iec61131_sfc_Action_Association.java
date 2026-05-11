





import java.util.List;
import java.util.ArrayList;

public class iec61131_sfc_Action_Association  {






    private List<Variable_Name> variable_names;




    private Action_Name action_name;


    public iec61131_sfc_Action_Association(
    ) {
        this.variable_names = new ArrayList<>();
    }

    public iec61131_sfc_Action_Association(
        ArrayList<Variable_Name> variable_names    ) {
        this.variable_names = variable_names;
    }


    public List<Variable_Name> getVariable_names() {
        return variable_names;
    }

    public void addVariable_name(Variable_name variable_name) {
        this.variable_names.add(variable_name);
    }
    public Action_Name getAction_name() {
        return action_name;
    }

    public void setAction_name(Action_Name action_name) {
        this.action_name = action_name;
    }

}