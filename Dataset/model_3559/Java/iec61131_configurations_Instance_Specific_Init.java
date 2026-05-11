





import java.util.List;
import java.util.ArrayList;

public class iec61131_configurations_Instance_Specific_Init  {






    private Resource_Name resource_name;




    private Program_Name program_name;




    private List<Variable_Name> variable_names;


    public iec61131_configurations_Instance_Specific_Init(
    ) {
        this.variable_names = new ArrayList<>();
    }

    public iec61131_configurations_Instance_Specific_Init(
        ArrayList<Variable_Name> variable_names    ) {
        this.variable_names = variable_names;
    }


    public Resource_Name getResource_name() {
        return resource_name;
    }

    public void setResource_name(Resource_Name resource_name) {
        this.resource_name = resource_name;
    }
    public Program_Name getProgram_name() {
        return program_name;
    }

    public void setProgram_name(Program_Name program_name) {
        this.program_name = program_name;
    }
    public List<Variable_Name> getVariable_names() {
        return variable_names;
    }

    public void addVariable_name(Variable_name variable_name) {
        this.variable_names.add(variable_name);
    }

}