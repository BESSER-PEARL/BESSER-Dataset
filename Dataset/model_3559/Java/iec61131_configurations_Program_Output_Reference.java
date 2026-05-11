





import java.util.List;
import java.util.ArrayList;

public class iec61131_configurations_Program_Output_Reference extends Data_Source {






    private Program_Name program_name;




    private Symbolic_Variable symbolic_variable;


    public iec61131_configurations_Program_Output_Reference(
    ) {
        super(
        );
    }



    public Program_Name getProgram_name() {
        return program_name;
    }

    public void setProgram_name(Program_Name program_name) {
        this.program_name = program_name;
    }
    public Symbolic_Variable getSymbolic_variable() {
        return symbolic_variable;
    }

    public void setSymbolic_variable(Symbolic_Variable symbolic_variable) {
        this.symbolic_variable = symbolic_variable;
    }

}