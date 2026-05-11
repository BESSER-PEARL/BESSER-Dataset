





import java.util.List;
import java.util.ArrayList;

public class iec61131_configurations_Symbolic_Path extends Access_Path {






    private Symbolic_Variable symbolic_variable;




    private List<Variable_Name> variable_names;




    private Program_Name program_name;


    public iec61131_configurations_Symbolic_Path(
    ) {
        super(
        );
        this.variable_names = new ArrayList<>();
    }

    public iec61131_configurations_Symbolic_Path(
        ArrayList<Variable_Name> variable_names    ) {
        this.variable_names = variable_names;
    }


    public Symbolic_Variable getSymbolic_variable() {
        return symbolic_variable;
    }

    public void setSymbolic_variable(Symbolic_Variable symbolic_variable) {
        this.symbolic_variable = symbolic_variable;
    }
    public List<Variable_Name> getVariable_names() {
        return variable_names;
    }

    public void addVariable_name(Variable_name variable_name) {
        this.variable_names.add(variable_name);
    }
    public Program_Name getProgram_name() {
        return program_name;
    }

    public void setProgram_name(Program_Name program_name) {
        this.program_name = program_name;
    }

}